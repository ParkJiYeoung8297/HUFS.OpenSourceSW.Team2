class ColorCombination:
    """
    class for represent color combination
    """
    def __init__(self, top: str, bottom: str):
        """
        constructor
        :param top: color of top
        :param bottom: color of bottom
        """
        self.top = top
        self.bottom = bottom

    def getTop(self):
        return self.top

    def getBottom(self):
        return self.bottom

    def __eq__(self,other): ##다른 인스턴스 값가 같은지 비교
        return self.top==other.top and self.bottom == other.bottom
# Example: ColorCombination("WHITE", "SKYBLUE") -> top == "WHITE", bottom == "SKYBLUE"
# TODO: Implement getter


"""
LIGHTBLUE= 연청 DARKBLUE = 진청
data reference
        https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=kkulkkuls&logNo=221587846538
        https://m.blog.naver.com/ktaitai1/221936224085
"""
combinations = [
    ColorCombination("WHITE", "DARKBLUE"),
    ColorCombination("WHITE", "LIGHTBLUE"),
    ColorCombination("WHITE", "BEIGE"),
    ColorCombination("WHITE", "KHAKI"),
    ColorCombination("WHITE", "CHARCOAL"),
    ColorCombination("WHITE", "BLACK"),
    ColorCombination("NAVY", "DARKBLUE"),
    ColorCombination("NAVY", "LIGHTBLUE"),
    ColorCombination("NAVY", "BEIGE"),
    ColorCombination("NAVY", "KHAKI"),
    ColorCombination("NAVY", "CHARCOAL"),
    ColorCombination("NAVY", "BLACK"),
    ColorCombination("PINK", "DARKBLUE"),
    ColorCombination("PINK", "LIGHTBLUE"),
    ColorCombination("PINK", "BEIGE"),
    ColorCombination("PINK", "KHAKI"),
    ColorCombination("PINK", "CHARCOAL"),
    ColorCombination("PINK", "BLACK"),
    ColorCombination("YELLOW", "DARKBLUE"),
    ColorCombination("YELLOW", "LIGHTBLUE"),
    ColorCombination("YELLOW", "BEIGE"),
    ColorCombination("YELLOW", "KHAKI"),
    ColorCombination("YELLOW", "CHARCOAL"),
    ColorCombination("YELLOW", "BLACK"),
    ColorCombination("BLUE", "DARKBLUE"),
    ColorCombination("BLUE", "LIGHTBLUE"),
    ColorCombination("BLUE", "BEIGE"),
    ColorCombination("BLUE", "KHAKI"),
    ColorCombination("BLUE", "CHARCOAL"),
    ColorCombination("BLUE", "BLACK"),
    ColorCombination("GREEN", "DARKBLUE"),
    ColorCombination("GREEN", "LIGHTBLUE"),
    ColorCombination("GREEN", "BEIGE"),
    ColorCombination("GREEN", "KHAKI"),
    ColorCombination("GREEN", "CHARCOAL"),
    ColorCombination("GREEN", "BLACK"),
    ColorCombination("RED", "BLACK"),
    ColorCombination("RED", "DARKBLUE"),
    ColorCombination("MAROON", "KHAKI"),
    ColorCombination("PURPLE", "KHAKI"),
    ColorCombination("TEAL", "KHAKI"),
    ColorCombination("GRAY", "KHAKI"),
    ColorCombination("MAROON", "BLACK"),
    ColorCombination("LIGHTORANGE", "BLACK"),
    ColorCombination("PURPLE", "BLACK"),
    ColorCombination("LIGHTPINK", "BLACK"),
    ColorCombination("LIGHTGRAY", "BLACK"),
    ColorCombination("LIGHTYELLOW", "BLACK"),
    ColorCombination("TURQUOISEGREEN", "BLACK"),
    ColorCombination("NAVYBLUE", "CRAEM"),
    ColorCombination("MAROON", "CRAEM"),
    ColorCombination("PINK", "CRAEM"),
    ColorCombination("SEAGREEN", "CRAEM"),
    ColorCombination("BLACK", "CRAEM"),
    ColorCombination("SPRINGBLOOM", "GRAY"),
    ColorCombination("PURPLE", "GRAY"),
    ColorCombination("AQUA", "GRAY"),
    ColorCombination("LIGHTPINK", "GRAY"),
    ColorCombination("CHERRY", "GRAY"),
    ColorCombination("BLUE", "GRAY"),
    ColorCombination("GREEN", "GRAY"),
    ColorCombination("RED", "GRAY"),
    ColorCombination("BLACK", "GRAY"),
    ColorCombination("WHITE", "GRAY"),
    ColorCombination("YELLOW", "NAVY"),
    ColorCombination("PEACH", "NAVY"),
    ColorCombination("PINK", "NAVY"),
    ColorCombination("LIGHTGREEN", "NAVY"),
    ColorCombination("PURPLE", "NAVY"),
    ColorCombination("ROYALBLUE", "NAVY"),
    ColorCombination("BROWN", "NAVY"),
    ColorCombination("MAGENTA", "NAVY"),
    ColorCombination("AQUA", "NAVY"),
    ColorCombination("CREAM", "NAVY"),
    ColorCombination("KHAKI", "NAVY"),
    ColorCombination("GRAY", "NAVY"),
    ColorCombination("MAROON", "NAVY"),
    ColorCombination("RUSTORANGE", "NAVY"),
    ColorCombination("CRIMSON", "NAVY"),
    ColorCombination("SUNNYYELLOW", "NAVY"),
    ColorCombination("WHITE", "NAVY"),
    ColorCombination("RED", "NAVY"),
    ColorCombination("BLACK", "NAVY"),
]
def checkLetters():
    for com in combinations:
        com.top = com.top.replace(" ","").upper()
        com.bottom = com.bottom.replace(" ","").upper()

#비교방법1 - top 비교 -> bottom 비교
def isRepeated():
    n=0
    for c in combinations[1:]:
        if combinations[n].top == c.top: #top먼저 비교 -> 같으면 하의도 같으면 T, 다르면 F
            re = combinations[n].bottom == c.bottom
            if re is True:
                print(combinations[n],c)
            return not re #return false

        n+=1
    
def checkReapeted():
    if isRepeated() == False:
        print("there is a repeated data")
    else: print("complete data")

checkLetters()
checkReapeted()

#비교2 __eq__메서드 이용
def compareData():
    n=0
    for c in combinations[1:]:
        if c.__eq__(combinations[n]):
            print(c.top ,c.bottom, combinations[n].top,combinations[n].bottom)
            print("same data occur!")
            break
        n+=1
compareData()
#두 개다 동일한 결과 나오는 것 확인

# ColorfulOnes_MatchTip={maincolor:[outfit pairings with]}
ColorfulOnes_MatchTip={ 
    "PINK":["LIGHTBLUE",'NAVY','GRAY','WHITE','BLACK'],
    "RED":["LIGHTBLUE",'NAVY','GRAY','WHITE','BLACK'],
    "ORAGE":["LIGHTBLUE",'NAVY','GREEN','WHITE','BLACK'],
    'BEIGE':["NAVY",'PURPLE','BROWN','WHITE','BLACK'],
    'YELLOW':["GREEN",'NAVY','WHITE','BLACK'],
    'GREEN':["ORANGE","PURPLE","WHITE","BLACK"],
    'LIGHTBLUE':["PINK",'RED','ORANGE','WHITE','BLACK'],
    'DARKBLUE':["PINK",'RED','YELLOW','GRAY','WHITE','BLACK'],
    'PURPLE':["ORANGE",'GRAY','GREEN','WHITE','BLACK'],
    'BROWN':['BEIGE','WHITE','BLACK'],
    'GREY':["PINK",'RED','NAVY','PURPLE']
}
"""
list for store color combination 
"""
# TODO: Add Color Combination Data


color_code_map = {
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255),
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0)
}
"""
dictionary for store RGB color code
"""
# TODO: Add Color Code Map


def get_combi(where: str, color: str) -> str:
    """
    get color combination from combinations
    :param where: location. value is "TOP" or "BOTTOM"
    :param color: color of cloth
    :return: where="TOP" will return color of bottom. where="BOTTOM" will return color of top.
    """
    pass
# Example: get_combi("TOP", "WHITE") will return "SKYBLUE"
# TODO: Implement Function: Get "ColorCombination" Instance from "combinations" List


def get_color_code(color) -> tuple:
    """
    get color code
    :param color: color name (dictionary key of color_code_map)
    :return: tuple for color code
    """
    return color_code_map[color]
# Example: get_color_code("RED") will return (255, 0, 0)
# TODO: Implement Function: Get color code from color_code_map
#print(get_color_code("RED")) #test get_color_code_map