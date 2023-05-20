import subprocess


class GitCommandError(Exception):
    """
    Exception thrown by a GitCommand.
    """

    pass


class GitCommand(object):
    """
    Wrapper around a Git command.

    Instantiate with a command name and an optional args list.
    These can later be modified with set_command() and set_args().

    Execute the command with run()

    If successful the results can be read as string lists with
    - stdout()
    - stderr()
    In case of an error a verbose GitCommandError is raised.
    """

    def __init__(self, command: str, args: list = []):
        """
        Initialize the GitCommand.

        Args:
            command a string ('git' will implicitly be prepended)
            args: a string list with remaining command arguments.
                  Defaults to an empty list
        """

        self.set_command(command)
        self.set_args(args)
        self._stdout = None
        self._stderr = None
        self._completed = False

    def run(self):
        """
        Execute the configured Git command.

        In case of success the results can be retrieved as string lists
        with self.stdout() and self.stderr(), otherwise a GitCommandError
        is raised.

        Args:

        Returns:
            The process's return code.
                Note: usually the result will be used through the methods.
        """

        args = ["git"]
        args.append(self._command)
        args.extend(self._args)
        p = subprocess.run(
            args,
            # encoding='utf8', # Uncomment after dropping support for python 3.5
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        try:
            p.check_returncode()
        except subprocess.CalledProcessError:
            msg = ["GitCommand error:"]
            msg.append('Command "%s" failed' % " ".join(args))
            msg.append("Return code: %s" % p.returncode)
            msg.append("Output:")
            msg.append(p.stdout.decode("utf-8"))
            msg.append("Error messages:")
            msg.append(p.stderr.decode("utf-8"))
            raise GitCommandError("\n".join(msg))

        self._stdout = p.stdout.decode("utf-8").strip("'\n").split("\n")
        self._stderr = p.stderr.decode("utf-8").strip("'\n").split("\n")

        self._completed = True
        return int(str(p.returncode))

    def set_args(self, args: list):
        """
        Change the command arguments.

        Args:
            args: list of process arguments
        """
        self._args = args

    def set_command(self, command: str):
        """
        Change the Git command.

        Args:
            command: string with the git-NNN command name.
        """
        self._command = command

    def stderr(self):
        """
        Return the stderr output of the command as a string list.

        Args:

        Returns:
            string list
        """
        if not self._completed:
            raise GitCommandError("Trying to read from uncompleted GitCommand")
        return self._stderr

    def stdout(self):
        """
        Return the stdout output of the command as a string list.

        Args:

        Returns:
            string list
        """
        if not self._completed:
            raise GitCommandError("Trying to read from uncompleted GitCommand")
        return self._stdout
