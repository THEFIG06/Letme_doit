import config, os, platform, subprocess
from utils.get_path_prompt import GetPath
from utils.prompt_shared_key_bindings import prompt_shared_key_bindings
from prompt_toolkit.application import run_in_terminal
from prompt_toolkit.key_binding import KeyBindings, merge_key_bindings
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.filters import Condition
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.shortcuts import confirm


class SystemCommandPrompt:

    def __init__(self):
        self.divider = "--------------------"
        self.getPath = GetPath(
            cancel_entry="",
            promptIndicatorColor=config.terminalPromptIndicatorColor2,
            promptEntryColor=config.terminalCommandEntryColor2,
            subHeadingColor=config.terminalHeadingTextColor,
            itemColor=config.terminalResourceLinkColor,
        )
        self.promptStyle = Style.from_dict({
            # User input (default text).
            "": config.terminalCommandEntryColor2,
            # Prompt.
            "indicator": config.terminalPromptIndicatorColor2,
        })
        system_command_history = os.path.join(config.myHandAIFolder, "history", "commands")
        self.terminal_system_command_session = PromptSession(history=FileHistory(system_command_history))
        self.openCommand = config.open

    def getToolBar(self):
        return " [ctrl+q] cancel [ctrl+l] list content [ctrl+p] add path "

    def getSystemCommands(self):
        try:
            options = subprocess.Popen("bash -c 'compgen -ac | sort'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, *_ = options.communicate()
            options = stdout.decode("utf-8").split("\n")
            options = [option for option in options if option and not option in ("{", "}", ".", "!", ":")]
            return options
        except:
            return []

    def run(self, allowPathChanges=False):
        self.runSystemCommandPrompt = True
        # initial message
        print("You are now using system command prompt!")
        print(f"To go back, either press 'ctrl+q' or run '{config.exit_entry}'.")
        # keep current path in case users change directory
        appPath = os.getcwd()

        this_key_bindings = KeyBindings()

        @this_key_bindings.add("c-q")
        def _(event):
            event.app.current_buffer.text = config.exit_entry
            event.app.current_buffer.validate_and_handle()

        @this_key_bindings.add("c-l")
        def _(_):
            print("")
            print(self.divider)
            run_in_terminal(lambda: self.getPath.displayDirectoryContent())

        @this_key_bindings.add("c-p")
        def _(event):
            self.addPath = True
            buffer = event.app.current_buffer
            self.systemCommandPromptEntry = buffer.text
            self.systemCommandPromptPosition = buffer.cursor_position
            buffer.validate_and_handle()

        this_key_bindings = merge_key_bindings([
            this_key_bindings,
            prompt_shared_key_bindings,
        ])

        userInput = ""
        self.addPath = False
        self.systemCommandPromptEntry = ""
        self.systemCommandPromptPosition = 0
        if config.suggestSystemCommand:
            systemCommands = self.getSystemCommands()
        while self.runSystemCommandPrompt and not userInput == config.exit_entry:
            try:
                indicator = "{0} {1} ".format(os.path.basename(os.getcwd()), "%")
                inputIndicator = [("class:indicator", indicator)]
                dirIndicator = "\\" if platform.system() == "Windows" else "/"
                if config.suggestSystemCommand:
                    completer = WordCompleter(sorted(set(systemCommands + [f"{i}{dirIndicator}" if os.path.isdir(i) else i for i in os.listdir()])))
                else:
                    completer = WordCompleter(sorted([f"{i}{dirIndicator}" if os.path.isdir(i) else i for i in os.listdir()]))
                auto_suggestion=AutoSuggestFromHistory()
                userInput = self.terminal_system_command_session.prompt(inputIndicator, swap_light_and_dark_colors=Condition(lambda: not config.terminalResourceLinkColor.startswith("ansibright")), style=self.promptStyle, key_bindings=this_key_bindings, auto_suggest=auto_suggestion, completer=completer, bottom_toolbar=self.getToolBar(), default=self.systemCommandPromptEntry).strip()
                if self.addPath:
                    self.addPath = False
                    prefix = self.systemCommandPromptEntry[:self.systemCommandPromptPosition]
                    suffix = self.systemCommandPromptEntry[self.systemCommandPromptPosition:]
                    message = f"{prefix}[add a path here]{suffix}"
                    userInput = self.getPath.getPath(message=message, bottom_toolbar=self.getToolBar(), promptIndicator=">>> ", empty_to_cancel=True)
                    self.systemCommandPromptEntry = f"{prefix}{userInput}{suffix}"
                elif userInput and not userInput == config.exit_entry:
                    self.systemCommandPromptEntry = ""
                    self.systemCommandPromptPosition = 0
                    if userInput.strip() == "cd":
                        userInput = "cd ~"
                    userInput = userInput.replace("~", os.path.expanduser("~"))
                    # execute or open file if input is a valid file
                    if os.path.isfile(userInput):
                        # execute file
                        stdout, stderr = subprocess.Popen(userInput, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
                        if stdout:
                            print(stdout.decode("utf-8"))
                        # try to open it if it was not executed
                        if stderr:
                            try:
                                os.system(f'{self.openCommand} "{userInput}"')
                            except:
                                print(traceback.format_exc())
                    # open directory if input is a valid directory
                    elif os.path.isdir(userInput):
                        os.system(f"{self.openCommand} {userInput}")
                    # run as command
                    else:
                        os.system(userInput)
                        # check if directory is changed
                        cmdList = []
                        userInput = userInput.split(";")
                        for i in userInput:
                            subList = i.split("&")
                            cmdList += subList
                        cmdList = [i.strip() for i in cmdList if i and i.strip().startswith("cd ")]
                        if cmdList:
                            lastDir = cmdList[-1][3:]
                            if os.path.isdir(lastDir):
                                os.chdir(lastDir)
                else:
                    self.systemCommandPromptEntry = ""
                    self.systemCommandPromptPosition = 0
            except:
                pass
        if not allowPathChanges:
            os.chdir(appPath)