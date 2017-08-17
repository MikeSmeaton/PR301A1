from Cmd2 import Cmd


class REPL(Cmd):

    def __init__(self):
        Cmd.__init__(self)


if __name__ == '__main__':
    app = REPL()
    app.cmdloop()