import psutil
import platform

__author__ = 'Sungho Park'


def ps():
    """
    Display process list. Processes which you do not have permission are not displayed.
    """
    for p in psutil.process_iter():
        try:
            pid = p.pid
            name = p.name()
            cmdline = p.cmdline()
        except psutil.AccessDenied:
            continue

        print("%5d %10s %s" % (pid, name, cmdline))


def kill(pid):
    """
    Kill process specified by pid paramter

    :param pid: Process ID to kill
    """
    p = psutil.Process(pid)

    try:
        p.kill()
    except Exception:
        pass


def killall(name, params=None):
    """
        Kill process specified by parameters.
        If you input name only, the same name processes are killed.
        If you input params too, this function checks the string is in the process command line and kills it.
        params are list or str separated by ','.

            >>> util.killall("emulator-x86")
            >>> util.killall("java", "main.jar,string.jar")

        :type name: Process name to kill
        :type params: Filter string for Process command line. ex)params="main.jar,string.jar,/lib/usr.so"
        """

    if platform.system() == "Windows":
        name += ".exe"

    for ps in psutil.process_iter():
        cmdline = ""
        try:
            if ps.name() != name:
                continue

            if params:
                cmdline = ps.cmdline()
        except psutil.AccessDenied:
            continue

        ps_found = True

        if params:  # If you want to compare command line
            check_list = []
            if params is list:
                check_list = params
            elif params is str:
                check_list = str.split(",")
            else:
                check_list.append(str(params))

            # Compare command line's parameters
            for item in check_list:
                ps_found = False

                for param in cmdline:
                    if param.find(item):
                        ps_found = True
                        break

                if ps_found is False:  # Process is not found.
                    break

        if ps_found:
            try:
                ps.kill()
            except Exception:
                pass
