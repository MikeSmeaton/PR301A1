import os
import cmd
import rlcompleter

class Console(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "=>> "
        self.intro = "welcome to the Console!"  # Defaults to None

# Command Definitions #
    def do_hist(self, args):
        """Print a list of commands that have been entered"""
        print (self._hist)

    def do_exit(self, args):
        """Exists from console"""
        return -1


# Command definitions to support Cmd object functionality #
    def do_EOF(self, args):
        """Exit on system end of file character"""

    def do_shell(self, args):
        """Pass command to a system shell when line begins with '!' """
        os.system(args)

    def do_help(self, args):
        """ Get help on commands
            'help' or '?' with no arguments prints a list of commands
                for which help is available
            'help <command> or '? <command>' gives help on <command>
        """
        # The only reason to define this method is for the
        # help text in the doc string
        cmd.Cmd.do_help(self, args)

    # Override methods in Cmd object #
    def preloopo(self):
        """Initialization before prompting user
            for commands.
            Despite the claims in the Cmd documentation,
            Cmd.preloop() is not a stub.
        """
        cmd.Cmd.preloop(self)  # sets up command completion
        self._hist = []        # no history yet
        self._locals = []      # Initialize execution namespace for user

    def postloop(self):
        """ Take care of any unfinished business
            Despite the claims in the Cmd documentation,
            Cmd.postloop() is not a stub.
        """
        cmd.Cmd.postloop(self)  # clean up command completion
        print("Exiting...")

    def precmd(self, line):
        """ This method is called after the line has been input but before
            it has been interpreted. if you want to modify the input line
            before execution (for example, variable substitution)
            do it here.
        """
        self._hist += [line.strip()]
        return line

    def postcmd(self, stop, line):
        """ If you want to stop the console, return something that evaluates to true.
            If you want to do some post command processing, do it here.
        """
        return stop

    def emptyline(self):
        """ Do nothing on empty input line """
        pass

    def default(self, line):
        """ Called on an input line when the command prefix is not recognized.
            In that case we execute thea line as Python code.
        """
        try:
            exec(line) in self._locals, self._globals

        except Exception as e:
            print (e.__class__, ":", e)

if __name__ == '__main__':
    console = Console()
    console.cmdloop()
