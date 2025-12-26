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
    import iris
    try:
        print("divide by zero=" + str(sample.dividezero(1)))
    except ZeroDivisionError as e:
        errobj=iris.cls("%Exception.General")._New(str(e),42)
        a=errobj.Log()
        print("Caught exception: " + str(e))
}

}
