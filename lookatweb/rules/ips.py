from .consts import *

# Rules to match IP addresses
IP_RULES = [
    {'type' : RULETYPE_REGEXP, 'text' : '194.85.61.78',
        'entities' : [
            {'name' : 'web:parking/nicruexpired'},
        ]
    },
    {'type' : RULETYPE_REGEXP, 'text' : '194.190.139.249',
        'entities' : [
            {'name' : 'web:parking/nicruexpired'},
        ]
    },


    {'type' : RULETYPE_REGEXP, 'text' : '212.227.34.3',
        'entities' : [
            {'name' : 'web:parking/sedo'},
        ]
    },

]
