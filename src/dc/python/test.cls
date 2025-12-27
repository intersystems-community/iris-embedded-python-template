Class dc.python.test
{

ClassMethod HelloWorld() As %Status
{
  Set sc = $$$OK
  Set b = ##class(%SYS.Python).Import("builtins")
  Do b.print("Hello world")
  Return sc
}

ClassMethod Today() As %Status
{
  Set sc = $$$OK
  Set dt = ##class(%SYS.Python).Import("datetime")
  write dt.date.today().isoformat()
  Return sc
}

ClassMethod Hello() As %Status
{
  Set sc = $$$OK
  Set sm = ##class(%SYS.Python).Import("sample")
  write sm.hello()
  Return sc
}

/// Titanic
ClassMethod TitanicMeanAge() As %Status
{
    Set sc = $$$OK
    set tt=##class(%SYS.Python).Import("sample")
    set path=##class(%File).NormalizeDirectory("lib", ##class(%File).GetDirectory($zu(86)))_"data/iris-python-template/titanic.csv"
    write "mean age="_tt.meanage(path)
    Return sc
}

ClassMethod DivideByZero() As %Status
{
    Set sc = $$$OK
    set tt=##class(%SYS.Python).Import("sample")
    try {
    write "divide by zero="_tt.dividezero(1)
    #dim ex as %Exception.PythonException
    } catch ex  {
        do ex.Log()
        write "Caught exception: ", ex.DisplayString(), !
    }
    Return sc
}

ClassMethod DivideByZeroPython() [ Language = python ]
{
    import sample
    import traceback
    import iris
    try:
        print("divide by zero=" + str(sample.dividezero(1)))
    except ZeroDivisionError as e:
        errobj=iris.cls("%Exception.General")._New(str(e),42)
        stack_trace_list = traceback.format_tb(e.__traceback__)
        if stack_trace_list:
            last_instruction_line = stack_trace_list[-1].strip()
            errobj.Location = last_instruction_line
        errobj.Log()
        print("Caught exception: " +str(e))
}

ClassMethod DivideByZeroPython2() [ Language = python ]
{
    import sample
    import traceback
    import iris
    import os
    try:
        print("divide by zero=" + str(sample.dividezero(1)))
    except ZeroDivisionError as e:
        tb = e.__traceback__
        last_frame = traceback.extract_tb(tb)[-1]

        # 2. Extract specific parts
        error_name = f"<{type(e).__name__.upper()}>" # e.g., <NAMEERROR>
        line_no = last_frame.lineno               # e.g., 6
        func_name = last_frame.name               # e.g., <module> or my_func
        filename = os.path.basename(last_frame.filename).replace('.py', '')

        iris_error = f"{func_name}+{line_no}^{filename}"
        errobj=iris.cls("%Exception.General")._New(error_name,2603,iris_error)
        errobj.Log()
        print("Caught exception: " +str(e))
}

ClassMethod DivideByZeroPythonWithInCls() [ Language = python ]
{
    import traceback
    import iris

    class MathOperations:
        def divide_numbers(self):
            try:
                print(1/0)
            except Exception as e:
                tb = e.__traceback__
                stack = traceback.extract_tb(tb)[-1]

                error_name = f"<{type(e).__name__.upper()}>"
                cls_name = self.__class__.__name__
                func_name = stack[2]
                line_no = stack[1]
                # create IRIS format error string
                iris_error = f"{func_name}+{line_no}^{cls_name}"
                python_exception= 2603
                errobj=iris.cls("%Exception.General")._New(error_name, python_exception, iris_error)
                a=errobj.Log()
                print("Caught exception: " + str(e))

    obj = MathOperations()
    obj.divide_numbers()
}

/// Pass the python exception to IRIS class to store the error in error log
ClassMethod PYExecCaptureInIRIS() [ Language = python ]
{
    import traceback
    import iris

    class MathOperations:
        def divide_numbers(self):
            try:
                print(1/0)
            except Exception as e:
                status = iris.cls(__name__).ConvertPyExceToIRISFormat(e)

    obj = MathOperations()
    obj.divide_numbers()
}
ClassMethod PYFuncExecCaptureInIRIS() [ Language = python ]
{
    import traceback
    import iris

    def divide_numbers():
        try:
            print(1/0)
        except Exception as e:
            status = iris.cls(__name__).ConvertPyExceToIRISFormat(e)

    divide_numbers()
}
/// Convert Python Exception to IRIS Exception Format and log it
ClassMethod ConvertPyExceToIRISFormat(pyException)
{
	Set pyBuiltins = ##class(%SYS.Python).Builtins()
	Set ex = pyBuiltins.type(pyException)
	Set error = $Property(ex, "__name__")
	Set error = "<"_$ZCVT(error,"U")_">"

	Set traceback = ##class(%SYS.Python).Import("traceback")

	Set tb = $Property(pyException, "__traceback__")
	Set frames = $Method(traceback,"extract_tb",tb)
	Set lastFrame = $Method(frames,"__getitem__",-1)

	Set file= $Property(lastFrame,"filename")
	set line= $Property(lastFrame,"lineno")
	set function= $Property(lastFrame,"name")
	Set code = $Property(lastFrame,"line")

	Set msg = function_"+"_line_"^"_file

	Set generalExcep = ##class(%Exception.General).%New(error,2603,msg)
	Do generalExcep.Log()
}

}
