Class dc.python.PersistentClass Extends %Persistent
{

/// Description
Property Test As %VarString;

ClassMethod CreateRecord(propValue As %VarString = "TestString", ByRef id As %Integer) As %Status
{
    set sc=$$$OK
    set obj=..%New()
    set obj.Test=propValue
    set sc=obj.%Save()
    set id=obj.%Id()
    return sc
}

ClassMethod CreateRecordPython(propValue As %VarString, ByRef id As %Integer) [ Language = python ]
{
    import iris
    obj=iris.cls(__name__)._New()
    obj.Test=propValue
    sc=obj._Save()
    id=obj._Id()
    return sc
}

/// opens the record by id and reads its property
ClassMethod PrintProperty(id As %Integer) As %Status
{
    Set sc = $$$OK
    set obj=..%OpenId(id,,.sc)
    if $ISOBJECT(obj) write obj.Test
    Return sc
}

ClassMethod PrintPropertyPython(id As %Integer) [ Language = python ]
{
    import iris
    obj=iris.cls(__name__)._OpenId(id)
    print(obj.Test)
}

Storage Default
{
<Data name="PersistentClassDefaultData">
<Value name="1">
<Value>%%CLASSNAME</Value>
</Value>
<Value name="2">
<Value>Test</Value>
</Value>
</Data>
<DataLocation>^dc.Package4C8F.PersistentC1A93D</DataLocation>
<DefaultData>PersistentClassDefaultData</DefaultData>
<IdLocation>^dc.Package4C8F.PersistentC1A93D</IdLocation>
<IndexLocation>^dc.Package4C8F.PersistentC1A93I</IndexLocation>
<StreamLocation>^dc.Package4C8F.PersistentC1A93S</StreamLocation>
<Type>%Storage.Persistent</Type>
}

}
