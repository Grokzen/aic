
 * All logging messages must be done to warning level or higher. Info logging level should not be used becuase it can interfere with output parsing. A regular run should be possible to pipe to a file.
 * There are no argument if you want to output it to a file. Use regular stdout redirections on unix platforms.
 * If `--pretty` is NOT used then the output will be squashed to a oneline and always be on the very last text row. Running `aic | tail -n 1` should always be possible to run.
 * In case of any kind of exception in the run, error code 1 will be returned and the exception will be outputed last in the run. No data will be outputed in this case.
 