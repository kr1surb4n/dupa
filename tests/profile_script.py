"""
MAGIC IPYTHON FUNCTIONS FOR PROFILING

IPython has the following magic commands for profiling:

    %time: Shows how long a one or more lines of code take to run.

    %timeit: Like %time but gives an average from multiple runs.
    Option -n can be used to specify the number of runs. Depending
    on how long the program takes, the number of runs is limited
    automatically. This is unlike the timeit module.

    %prun: Shows time taken by each function.

    %lprun: Shows time taken line by line.
    Functions to profile can be specified with -f option.

    %mprun: Shows how much memory is used.

    %memit: Like %mprun but gives an average from multiple
    runs, which can be specified with -r option.

Commands %time and %timeit are available by default. Commands %lprun,
%mprun and %memit are available via modules line-profiler, memory-profiler
and psutil. But to use them within IPython as magic commands, mapping
must be done via IPython extension files. Or use the %load_ext magic command.

When timing multiple lines of code, use %%timeit instead of %timeit.
This is available for %prun as well.

"""
from click.testing import CliRunner
from dupa.cli import main as ClickApp

sample_input = "Value 1\nValue 2\n".encode()

# test the happy path
runner = CliRunner()
result = runner.invoke(
    ClickApp, ['tests/test.txt.tpl', '/tmp/test.out'], input=sample_input)
