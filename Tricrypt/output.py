# Tricrypt formats
# This file defines various formats
# that Tricrypt can output in.

formats = {
'plain': {
        'header': "{service} [{sec} secs] [{digits} digits]\n--------------------\n",
        'linepre': "",
        'linepost': "\n",
        'shapeformat': "{shape}{num} ",
        'footer': ""
        },
        
'xml':  {
        'header': "<code service=\"{service}\" validfor={sec} length={digits}>\n",
        'linepre': "\t<line>\n",
        'linepost': "\t</line>\n",
        'shapeformat': "\t\t<{shape}>{num}</{shape}>\n",
        'footer': "</code>"
        },
        
'html': {
        'header': "<section class=\"Tricrypt\">",
        'linepre': "",
        'linepost': "\n",
        'shapeformat': "<span class=\"tricryptShape {shape}\">{num}</span>",
        'footer': "</section>"
        },
        
# you can add custom formats here
}