
from grongier.pex import BusinessOperation

import iris

import os
import datetime

from message import PostMessage

class FileOperation(BusinessOperation):
    """
    This operation receive a PostMessage and write down in the right company
    .txt all the important information and the time of the operation
    """
    def on_init(self):
        if hasattr(self,'path'):
            os.chdir(self.path)

    def on_post_message(self, request: PostMessage):
        """
        This method is called when a PostMessage is received.
        """
        
        ts = title = author = url = text = ""

        if (request.post is not None):
            title = request.post.title
            author = request.post.author
            url = request.post.url
            text = request.post.selftext
            ts = datetime.datetime.fromtimestamp(request.post.created_utc).__str__()

        line = ts+" : "+title+" : "+author+" : "+url
        filename = request.found+".txt"


        self.put_line(filename, line)
        self.put_line(filename, "")
        self.put_line(filename, text)
        self.put_line(filename, " * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")

        return 

    def put_line(self,filename,string):
        try:
            with open(filename, "a",encoding="utf-8") as outfile:
                outfile.write(string)
        except Exception as e:
            raise e

class FileOperationWithIrisAdapter(BusinessOperation):
    """
    This operation receive a PostMessage and write down in the right company
    .txt all the important information and the time of the operation using the iris
    adapter EnsLib.File.OutboundAdapter
    """
    def get_adapter_type():
        """
        Name of the registred Adapter
        """
        return "EnsLib.File.OutboundAdapter"

    def on_message(self, request):

        ts = title = author = url = text = ""

        if (request.post != ""):
            title = request.post.title
            author = request.post.author
            url = request.post.url
            text = request.post.selftext
            ts = iris.cls("%Library.PosixTime").LogicalToOdbc(iris.cls("%Library.PosixTime").UnixTimeToLogical(request.post.created_utc))

        line = ts+" : "+title+" : "+author+" : "+url
        filename = request.found+".txt" 
        
        self.Adapter.PutLine(filename, line)
        self.Adapter.PutLine(filename, "")
        self.Adapter.PutLine(filename, text)
        self.Adapter.PutLine(filename, " * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")

        return
