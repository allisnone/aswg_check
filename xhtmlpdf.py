#from xhtml2pdf import pisa             # import python module
from xhtml2pdf import pisa
# Define your data
#sourceHtml = "<myhtml><body><p>To PDF or not to PDF</p></body></myhtml>"
#outputFilename = "test.pdf"

# Utility function
def convertHtmlToPdf(sourceHtml, outputFilename):
    # open output file for writing (truncated binary)
    resultFile = open(outputFilename, "w+b")

    # convert HTML to PDF
    pisaStatus = pisa.CreatePDF(
            sourceHtml,                # the HTML to convert
            dest=resultFile,
            encoding='utf-8')           # file handle to recieve result

    # close output file
    resultFile.close()                 # close output file

    # return True on success and False on errors
    return pisaStatus.err

# Main program
"""
if __name__ == "__main__":
    pisa.showLogging()
    convertHtmlToPdf(sourceHtml, outputFilename)
"""