from collections import namedtuple

LineError = namedtuple(
    "Error",
    [
        "line_section_index",
        "section_name",
        "predicate",
        "line_index",
        "error"
    ]
)

PathData = namedtuple(
    "PathData",
    [
        "name",
        "suffix",
    ]
)

Line = namedtuple(
    "Line",
    [
        "section_index", 
        "section", 
        "sub_section", 
        "sub_sub_section", 
        "predicate", 
    ]
)

FIXED_SECTION_NAME_MAP = {
    "0100000": "START DELIMITER",
    # "0800100": " MIDDLE JOKER",
    "5000100": "END DELIMITER",
}

FIXED_REQUIRED_SECTIONS_AT_LEAST_ONCE = [
    "0100000",
    "0100100",
    "0100200",
    "0100300",
    "0100400",
    "0100500",
    "0100600",
    "0100700",
    "0100800",
    "0100900",
    "0101000",
    "0101200",

    "0200000",
    "0200100",
    "0200200",
    "0200300",
    "0200400",
    "0200500",
    "0200600",

    # "0300100",
    # "0300110",
    # "0300150",

    "5000100",
]

MOBILE_SECTION_NAME_MAP = {
    "100000": "START DELIMITER",
    # "0800100": " MIDDLE JOKER",
    "999999": "END DELIMITER",
}

MOBILE_REQUIRED_SECTIONS_AT_LEAST_ONCE = [
    "100000",
    "100001",
    "100002",
    "100003",
    "100004",
    "100005",
    "100006",
    "100007",
    "100008",
    "100009",
    "100010",
    "100011",
    "100012",
    "100013",
    "100014",
    "100015",
    "100016",
    
    "100100",
    "100101",
    "100102",
    "100103",
    "100104",
    "100105",
    "100106",
    "100107",
    
    "100200",
    "100201",
    "100202",
    "100203",
    "100204",
    "100205",
    "100206",
    "100207",
    "100208",
    "100209",
    
    "100300",
    "100301",
    "100302",
    "100303",
    "100304",
    "100305",
    "100306",
    "100307",
    "100308",
    "100309",
    "100310",
    "100311",
    "100312",
    "100313",
    
    "100400",
    "100401",
    "100402",
    "100403",
    "100404",
    "100405",
    "100406",
    "100407",
    "100408",
    "100409",
    "100410",
    "100430",
    
    "100500",
    "100501",
    "100502",
    "100503",
    
    "100600",
    "100602",
    "100603",
    "100604",
    
    "200000",
    "200003",
    "200004",
    
    "200100",
    
    "200200",
    
    "200300",
    
    "200400",
    
    "200500",
    
    "200600",
    
    "300000",
    
    "400000",

    "900000",
    
    "999999"
]


def code_to_textual(codes):
    return codes
    # return [f"{section_code}: {SECTION_NAME_MAP[section_code]}" for section_code in codes]



class Bill:

    def __init__(self, start_line):
        self.errors = []
        self.processed_lines = []
        self.start_line = start_line
        self.end_line = -1
        
        self.first_0800100_encountered = False

    @property
    def missing_sections(self):
        missing_sections = set(self.REQUIRED_SECTIONS_AT_LEAST_ONCE) - set(self.processed_lines)
        return missing_sections

    
    @property
    def has_errors(self):
        text_errors = True if len(self.errors) > 0 else False
        section_errors = True if len(self.missing_sections) > 0 else False
        return text_errors, section_errors


class FixedBill(Bill):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.REQUIRED_SECTIONS_AT_LEAST_ONCE = FIXED_REQUIRED_SECTIONS_AT_LEAST_ONCE
        self.SECTION_NAME_MAP = FIXED_SECTION_NAME_MAP

class MobileBill(Bill):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.REQUIRED_SECTIONS_AT_LEAST_ONCE = MOBILE_REQUIRED_SECTIONS_AT_LEAST_ONCE
        self.SECTION_NAME_MAP = MOBILE_SECTION_NAME_MAP
