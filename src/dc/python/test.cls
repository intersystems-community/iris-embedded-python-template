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

}
