Class dc.Demo.ObjectScript Extends %RegisteredObject
{

/// Demo of pure ObjectScript Code
/// Invoke with: do ##class(Demo.ObjectScript).Test() in the terminal
ClassMethod Test() As %Integer
{
    set a=42 
    write "It works!",!
    return a
}

}
