"""
BTcalc – BattleTech Trefferkalkulator
Android-App (Kivy)
"""
import random

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import SpinnerOption

# ── Spieldaten ─────────────────────────────────────────────────────────────

MISSILE_TABLE = {
    "SRM2":  {2:1,  3:1,  4:1,  5:1,  6:1,  7:1,  8:2,  9:2,  10:2,  11:2,  12:2},
    "SRM4":  {2:1,  3:2,  4:2,  5:2,  6:2,  7:3,  8:3,  9:3,  10:4,  11:4,  12:4},
    "SRM6":  {2:2,  3:2,  4:3,  5:3,  6:4,  7:4,  8:4,  9:5,  10:5,  11:6,  12:6},
    "STREAKSRM2":  {2:2,  3:2,  4:2,  5:2,  6:2,  7:2,  8:2,  9:2,  10:2,  11:2,  12:2},
    "STREAKSRM4":  {2:4,  3:4,  4:4,  5:4,  6:4,  7:4,  8:4,  9:4,  10:4,  11:4,  12:4},
    "STREAKSRM6":  {2:6,  3:6,  4:6,  5:6,  6:6,  7:6,  8:6,  9:6,  10:6,  11:6,  12:6},
    "LRM5":  {2:1,  3:2,  4:2,  5:3,  6:3,  7:3,  8:3,  9:4,  10:4,  11:5,  12:5},
    "LRM10": {2:3,  3:3,  4:4,  5:6,  6:6,  7:6,  8:6,  9:8,  10:8,  11:10, 12:10},
    "LRM15": {2:5,  3:5,  4:6,  5:9,  6:9,  7:9,  8:9,  9:12, 10:12, 11:15, 12:15},
    "LRM20": {2:6,  3:6,  4:9,  5:12, 6:12, 7:12, 8:12, 9:16, 10:16, 11:20, 12:20},
    "CSRM2":  {2:1,  3:1,  4:1,  5:1,  6:1,  7:1,  8:2,  9:2,  10:2,  11:2,  12:2},
    "CSRM4":  {2:1,  3:2,  4:2,  5:2,  6:2,  7:3,  8:3,  9:3,  10:4,  11:4,  12:4},
    "CSRM6":  {2:2,  3:2,  4:3,  5:3,  6:4,  7:4,  8:4,  9:5,  10:5,  11:6,  12:6},
    "CSTREAKSRM2":  {2:2,  3:2,  4:2,  5:2,  6:2,  7:2,  8:2,  9:2,  10:2,  11:2,  12:2},
    "CSTREAKSRM4":  {2:4,  3:4,  4:4,  5:4,  6:4,  7:4,  8:4,  9:4,  10:4,  11:4,  12:4},
    "CSTREAKSRM6":  {2:6,  3:6,  4:6,  5:6,  6:6,  7:6,  8:6,  9:6,  10:6,  11:6,  12:6},
    "CLRM5":  {2:1,  3:2,  4:2,  5:3,  6:3,  7:3,  8:3,  9:4,  10:4,  11:5,  12:5},
    "CLRM10": {2:3,  3:3,  4:4,  5:6,  6:6,  7:6,  8:6,  9:8,  10:8,  11:10, 12:10},
    "CLRM15": {2:5,  3:5,  4:6,  5:9,  6:9,  7:9,  8:9,  9:12, 10:12, 11:15, 12:15},
    "CLRM20": {2:6,  3:6,  4:9,  5:12, 6:12, 7:12, 8:12, 9:16, 10:16, 11:20, 12:20},
}

WEAPONS = {
    "SRM2":      {"dmg": "x2",  "heat": 2,  "missile": True},
    "SRM4":      {"dmg": "x2",  "heat": 3,  "missile": True},
    "SRM6":      {"dmg": "x2",  "heat": 4,  "missile": True},
    "STREAKSRM2":      {"dmg": "x2",  "heat": 2,  "missile": True},
    "STREAKSRM4":      {"dmg": "x2",  "heat": 3,  "missile": True},
    "STREAKSRM6":      {"dmg": "x2",  "heat": 4,  "missile": True},
    "LRM5":      {"dmg": "x1",  "heat": 2,  "missile": True},
    "LRM10":     {"dmg": "x1",  "heat": 4,  "missile": True},
    "LRM15":     {"dmg": "x1",  "heat": 5,  "missile": True},
    "LRM20":     {"dmg": "x1",  "heat": 6,  "missile": True},
    "SLASER":    {"dmg": "x3",  "heat": 1,  "missile": False},
    "MLASER":    {"dmg": "x5",  "heat": 3,  "missile": False},
    "LLASER":    {"dmg": "x8",  "heat": 8,  "missile": False},
    "ERSLASER":  {"dmg": "x3",  "heat": 2,  "missile": False},
    "ERMLASER":  {"dmg": "x5",  "heat": 5,  "missile": False},
    "ERLLASER":  {"dmg": "x8",  "heat": 12, "missile": False},
    "PPC":       {"dmg": "x10", "heat": 10, "missile": False},
    "ERPPC":     {"dmg": "x10", "heat": 15, "missile": False},
    "AC2":       {"dmg": "x2",  "heat": 1,  "missile": False},
    "AC5":       {"dmg": "x5",  "heat": 1,  "missile": False},
    "AC10":      {"dmg": "x10", "heat": 3,  "missile": False},
    "AC20":      {"dmg": "x20", "heat": 7,  "missile": False},
    "ULTRAAC2":  {"dmg": "x2",  "heat": 1,  "missile": False},
    "ULTRAAC5":  {"dmg": "x5",  "heat": 1,  "missile": False},
    "ULTRAAC10": {"dmg": "x10", "heat": 4,  "missile": False},
    "ULTRAAC20": {"dmg": "x20", "heat": 8,  "missile": False},
    "GAUS":      {"dmg": "x15", "heat": 1,  "missile": False},
    "MGUN":      {"dmg": "x2",  "heat": 0,  "missile": False},
}

WEAPONS_CLAN = {
    "CSRM2":      {"dmg": "x2",  "heat": 2,  "missile": True},
    "CSRM4":      {"dmg": "x2",  "heat": 3,  "missile": True},
    "CSRM6":      {"dmg": "x2",  "heat": 4,  "missile": True},
    "CSTREAKSRM2":      {"dmg": "x2",  "heat": 2,  "missile": True},
    "CSTREAKSRM4":      {"dmg": "x2",  "heat": 3,  "missile": True},
    "CSTREAKSRM6":      {"dmg": "x2",  "heat": 4,  "missile": True},
    "CLRM5":      {"dmg": "x1",  "heat": 2,  "missile": True},
    "CLRM10":     {"dmg": "x1",  "heat": 4,  "missile": True},
    "CLRM15":     {"dmg": "x1",  "heat": 5,  "missile": True},
    "CLRM20":     {"dmg": "x1",  "heat": 6,  "missile": True},
    "CERSLASER":  {"dmg": "x5",  "heat": 2,  "missile": False},
    "CERMLASER":  {"dmg": "x7",  "heat": 5,  "missile": False},
    "CERLLASER":  {"dmg": "x10",  "heat": 12, "missile": False},
    "CERPPC":     {"dmg": "x15", "heat": 15, "missile": False},
    "CULTRAAC2":  {"dmg": "x2",  "heat": 1,  "missile": False},
    "CULTRAAC5":  {"dmg": "x5",  "heat": 1,  "missile": False},
    "CULTRAAC10": {"dmg": "x10", "heat": 3,  "missile": False},
    "CULTRAAC20": {"dmg": "x20", "heat": 7,  "missile": False},
    "CGAUS":      {"dmg": "x15", "heat": 1,  "missile": False},
    "CMGUN":      {"dmg": "x2",  "heat": 0,  "missile": False},
}

ZONE_VORNE  = {2:"ct_crit",3:"ra", 4:"ra", 5:"rl", 6:"rt",
               7:"ct",     8:"lt", 9:"ll",10:"la",11:"la",12:"hd"}
ZONE_LINKS  = {2:"lt_crit",3:"ll", 4:"la", 5:"la", 6:"ll",
               7:"lt",     8:"ct", 9:"rt",10:"ra",11:"rl",12:"hd"}
ZONE_RECHTS = {2:"rt_crit",3:"rl", 4:"ra", 5:"ra", 6:"rl",
               7:"rt",     8:"ct", 9:"lt",10:"la",11:"ll",12:"hd"}
ZONES = {"vorne": ZONE_VORNE, "rechts": ZONE_RECHTS, "links": ZONE_LINKS}

CRIT_LABELS = {
    "ct_crit": "Center Torso Krit.",
    "lt_crit": "Linker Torso Krit.",
    "rt_crit": "Rechter Torso Krit.",
}

WEAPON_LIST = list(WEAPONS.keys())

# ── Spiellogik ─────────────────────────────────────────────────────────────

def _roll2d10():
    return random.randint(1, 10) + random.randint(1, 10)

def _roll2d6():
    return random.randint(1, 6) + random.randint(1, 6)

def calc_hits(count, threshold):
    return sum(1 for _ in range(count) if _roll2d10() >= threshold)

def calc_missiles(hits, weapon):
    table = MISSILE_TABLE[weapon]
    return sum(table[_roll2d6()] for _ in range(hits))

def calc_locations(count, zone):
    table = ZONES[zone]
    result = {}
    for _ in range(count):
        loc = table[_roll2d6()]
        result[loc] = result.get(loc, 0) + 1
    return result

# ── KV Layout ──────────────────────────────────────────────────────────────

KV = """
#:import dp kivy.metrics.dp

# Dark spinner option for the dropdown list
<DarkSpinnerOption>:
    background_normal: ''
    background_color: 0.059, 0.129, 0.243, 1
    color: 1, 1, 1, 1
    font_size: dp(17)
    height: dp(52)
    size_hint_y: None

# Flat button with rounded corners – base class
<FlatBtn@Button>:
    bg_color: 0.059, 0.204, 0.376, 1
    background_normal: ''
    background_down: ''
    background_color: 0, 0, 0, 0
    color: 1, 1, 1, 1
    bold: True
    font_size: dp(15)
    canvas.before:
        Color:
            rgba: self.bg_color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(8), dp(8), dp(8), dp(8)]

# Red variant for the fire button and active zone button
<RedBtn@FlatBtn>:
    bg_color: 0.914, 0.271, 0.376, 1

# Stepper +/- buttons
<StepBtn@FlatBtn>:
    bg_color: 0.118, 0.118, 0.235, 1
    font_size: dp(24)
    bold: True

# ── Main layout ────────────────────────────────────────────────────────────
<MainWidget>:
    orientation: 'vertical'
    canvas.before:
        Color:
            rgba: 0.102, 0.102, 0.176, 1
        Rectangle:
            pos: self.pos
            size: self.size

    # Header bar
    BoxLayout:
        size_hint_y: None
        height: dp(58)
        padding: [dp(16), dp(8)]
        canvas.before:
            Color:
                rgba: 0.059, 0.059, 0.118, 1
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: 'BTCalc'
            font_size: dp(26)
            bold: True
            color: 0.914, 0.271, 0.376, 1
            size_hint_x: 0.38
            halign: 'left'
            valign: 'middle'
            text_size: self.size
        Label:
            text: 'BattleTech Kalkulator'
            font_size: dp(13)
            color: 0.533, 0.533, 0.627, 1
            size_hint_x: 0.62
            halign: 'right'
            valign: 'middle'
            text_size: self.size

    # Scrollable content
    ScrollView:
        do_scroll_x: False
        BoxLayout:
            orientation: 'vertical'
            padding: dp(12)
            spacing: dp(10)
            size_hint_y: None
            height: self.minimum_height

            # ── Input card ─────────────────────────────────────────────
            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                padding: dp(14)
                spacing: dp(10)
                canvas.before:
                    Color:
                        rgba: 0.086, 0.129, 0.243, 1
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [dp(12), dp(12), dp(12), dp(12)]

                Label:
                    text: 'KAMPFPARAMETER'
                    font_size: dp(11)
                    color: 0.533, 0.533, 0.627, 1
                    size_hint_y: None
                    height: dp(22)
                    halign: 'left'
                    text_size: self.size

                # IS / CLAN Fraktion
                BoxLayout:
                    size_hint_y: None
                    height: dp(52)
                    spacing: dp(8)
                    Label:
                        text: 'Fraktion'
                        color: 0.8, 0.8, 0.9, 1
                        font_size: dp(15)
                        size_hint_x: 0.30
                        halign: 'left'
                        text_size: self.size
                        valign: 'middle'
                    FlatBtn:
                        id: btn_is
                        text: 'IS'
                        bg_color: 0.914, 0.271, 0.376, 1
                        on_press: root.set_faction('is')
                    FlatBtn:
                        id: btn_clan
                        text: 'CLAN'
                        bg_color: 0.059, 0.204, 0.376, 1
                        on_press: root.set_faction('clan')

                # Waffe
                BoxLayout:
                    size_hint_y: None
                    height: dp(52)
                    spacing: dp(8)
                    Label:
                        text: 'Waffe'
                        color: 0.8, 0.8, 0.9, 1
                        font_size: dp(15)
                        size_hint_x: 0.30
                        halign: 'left'
                        text_size: self.size
                        valign: 'middle'
                    Spinner:
                        id: weapon_spinner
                        text: 'SRM2'
                        values: ['SRM2','SRM4','SRM6','STREAKSRM2','STREAKSRM4','STREAKSRM6','LRM5','LRM10','LRM15','LRM20','SLASER','MLASER','LLASER','ERSLASER','ERMLASER','ERLLASER','PPC','ERPPC','AC2','AC5','AC10','AC20','ULTRAAC2','ULTRAAC5','ULTRAAC10','ULTRAAC20','GAUS','MGUN']
                        option_cls: app.DarkSpinnerOption
                        background_normal: ''
                        background_color: 0.082, 0.258, 0.478, 1
                        color: 1, 1, 1, 1
                        font_size: dp(16)
                        size_hint_x: 0.70

                # Anzahl Waffen
                BoxLayout:
                    size_hint_y: None
                    height: dp(52)
                    spacing: dp(8)
                    Label:
                        text: 'Anzahl'
                        color: 0.8, 0.8, 0.9, 1
                        font_size: dp(15)
                        size_hint_x: 0.30
                        halign: 'left'
                        text_size: self.size
                        valign: 'middle'
                    StepBtn:
                        text: '-'
                        size_hint_x: 0.18
                        on_press: root.dec_count()
                    Label:
                        id: count_label
                        text: '1'
                        font_size: dp(22)
                        bold: True
                        color: 1, 1, 1, 1
                        size_hint_x: 0.22
                        halign: 'center'
                        text_size: self.size
                        valign: 'middle'
                    StepBtn:
                        text: '+'
                        size_hint_x: 0.18
                        on_press: root.inc_count()

                # Trefferwert
                BoxLayout:
                    size_hint_y: None
                    height: dp(52)
                    spacing: dp(8)
                    Label:
                        text: 'Trefferwert'
                        color: 0.8, 0.8, 0.9, 1
                        font_size: dp(15)
                        size_hint_x: 0.30
                        halign: 'left'
                        text_size: self.size
                        valign: 'middle'
                    StepBtn:
                        text: '-'
                        size_hint_x: 0.18
                        on_press: root.dec_treffw()
                    Label:
                        id: treffw_label
                        text: '8'
                        font_size: dp(22)
                        bold: True
                        color: 1, 1, 1, 1
                        size_hint_x: 0.22
                        halign: 'center'
                        text_size: self.size
                        valign: 'middle'
                    StepBtn:
                        text: '+'
                        size_hint_x: 0.18
                        on_press: root.inc_treffw()

                # Trefferzone
                BoxLayout:
                    size_hint_y: None
                    height: dp(52)
                    spacing: dp(6)
                    Label:
                        text: 'Zone'
                        color: 0.8, 0.8, 0.9, 1
                        font_size: dp(15)
                        size_hint_x: 0.22
                        halign: 'left'
                        text_size: self.size
                        valign: 'middle'
                    FlatBtn:
                        id: btn_vorne
                        text: 'Vorne'
                        bg_color: 0.914, 0.271, 0.376, 1
                        on_press: root.set_zone('vorne')
                    FlatBtn:
                        id: btn_rechts
                        text: 'Rechts'
                        bg_color: 0.059, 0.204, 0.376, 1
                        on_press: root.set_zone('rechts')
                    FlatBtn:
                        id: btn_links
                        text: 'Links'
                        bg_color: 0.059, 0.204, 0.376, 1
                        on_press: root.set_zone('links')

            # ── Fire button ────────────────────────────────────────────
            RedBtn:
                id: fire_btn
                text: 'FEUER FREI!'
                size_hint_y: None
                height: dp(68)
                font_size: dp(22)
                on_press: root.fire()

            # ── Results card ───────────────────────────────────────────
            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                padding: dp(14)
                spacing: dp(4)
                canvas.before:
                    Color:
                        rgba: 0.086, 0.129, 0.243, 1
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [dp(12), dp(12), dp(12), dp(12)]

                Label:
                    text: 'TREFFERERGEBNIS'
                    font_size: dp(11)
                    color: 0.533, 0.533, 0.627, 1
                    size_hint_y: None
                    height: dp(22)
                    halign: 'left'
                    text_size: self.size

                # Divider
                BoxLayout:
                    size_hint_y: None
                    height: dp(1)
                    canvas.before:
                        Color:
                            rgba: 0.2, 0.2, 0.35, 1
                        Rectangle:
                            pos: self.pos
                            size: self.size

                # Kopf
                BoxLayout:
                    size_hint_y: None
                    height: dp(44)
                    Label:
                        text: 'Kopf'
                        color: 0.7, 0.7, 0.8, 1
                        font_size: dp(15)
                        size_hint_x: 0.55
                        halign: 'left'
                        text_size: self.size
                        valign: 'middle'
                    Label:
                        id: res_hd
                        text: '-'
                        color: 0.914, 0.271, 0.376, 1
                        font_size: dp(17)
                        bold: True
                        size_hint_x: 0.45
                        halign: 'right'
                        text_size: self.size
                        valign: 'middle'

                # Linker Arm
                BoxLayout:
                    size_hint_y: None
                    height: dp(44)
                    Label:
                        text: 'Linker Arm'
                        color: 0.7, 0.7, 0.8, 1
                        font_size: dp(15)
                        size_hint_x: 0.55
                        halign: 'left'
                        text_size: self.size
                        valign: 'middle'
                    Label:
                        id: res_la
                        text: '-'
                        color: 0.957, 0.635, 0.380, 1
                        font_size: dp(17)
                        bold: True
                        size_hint_x: 0.45
                        halign: 'right'
                        text_size: self.size
                        valign: 'middle'

                # Rechter Arm
                BoxLayout:
                    size_hint_y: None
                    height: dp(44)
                    Label:
                        text: 'Rechter Arm'
                        color: 0.7, 0.7, 0.8, 1
                        font_size: dp(15)
                        size_hint_x: 0.55
                        halign: 'left'
                        text_size: self.size
                        valign: 'middle'
                    Label:
                        id: res_ra
                        text: '-'
                        color: 0.957, 0.635, 0.380, 1
                        font_size: dp(17)
                        bold: True
                        size_hint_x: 0.45
                        halign: 'right'
                        text_size: self.size
                        valign: 'middle'

                # Linker Torso
                BoxLayout:
                    size_hint_y: None
                    height: dp(44)
                    Label:
                        text: 'Linker Torso'
                        color: 0.7, 0.7, 0.8, 1
                        font_size: dp(15)
                        size_hint_x: 0.55
                        halign: 'left'
                        text_size: self.size
                        valign: 'middle'
                    Label:
                        id: res_lt
                        text: '-'
                        color: 0.957, 0.635, 0.380, 1
                        font_size: dp(17)
                        bold: True
                        size_hint_x: 0.45
                        halign: 'right'
                        text_size: self.size
                        valign: 'middle'

                # Rechter Torso
                BoxLayout:
                    size_hint_y: None
                    height: dp(44)
                    Label:
                        text: 'Rechter Torso'
                        color: 0.7, 0.7, 0.8, 1
                        font_size: dp(15)
                        size_hint_x: 0.55
                        halign: 'left'
                        text_size: self.size
                        valign: 'middle'
                    Label:
                        id: res_rt
                        text: '-'
                        color: 0.957, 0.635, 0.380, 1
                        font_size: dp(17)
                        bold: True
                        size_hint_x: 0.45
                        halign: 'right'
                        text_size: self.size
                        valign: 'middle'

                # Center Torso
                BoxLayout:
                    size_hint_y: None
                    height: dp(44)
                    Label:
                        text: 'Center Torso'
                        color: 0.7, 0.7, 0.8, 1
                        font_size: dp(15)
                        size_hint_x: 0.55
                        halign: 'left'
                        text_size: self.size
                        valign: 'middle'
                    Label:
                        id: res_ct
                        text: '-'
                        color: 0.957, 0.635, 0.380, 1
                        font_size: dp(17)
                        bold: True
                        size_hint_x: 0.45
                        halign: 'right'
                        text_size: self.size
                        valign: 'middle'

                # Torso Kritisch (label changes based on zone)
                BoxLayout:
                    size_hint_y: None
                    height: dp(44)
                    Label:
                        id: lbl_crit_name
                        text: 'CT Kritisch'
                        color: 0.914, 0.271, 0.376, 1
                        font_size: dp(15)
                        bold: True
                        size_hint_x: 0.55
                        halign: 'left'
                        text_size: self.size
                        valign: 'middle'
                    Label:
                        id: res_crit
                        text: '-'
                        color: 0.914, 0.271, 0.376, 1
                        font_size: dp(17)
                        bold: True
                        size_hint_x: 0.45
                        halign: 'right'
                        text_size: self.size
                        valign: 'middle'

                # Linkes Bein
                BoxLayout:
                    size_hint_y: None
                    height: dp(44)
                    Label:
                        text: 'Linkes Bein'
                        color: 0.7, 0.7, 0.8, 1
                        font_size: dp(15)
                        size_hint_x: 0.55
                        halign: 'left'
                        text_size: self.size
                        valign: 'middle'
                    Label:
                        id: res_ll
                        text: '-'
                        color: 0.957, 0.635, 0.380, 1
                        font_size: dp(17)
                        bold: True
                        size_hint_x: 0.45
                        halign: 'right'
                        text_size: self.size
                        valign: 'middle'

                # Rechtes Bein
                BoxLayout:
                    size_hint_y: None
                    height: dp(44)
                    Label:
                        text: 'Rechtes Bein'
                        color: 0.7, 0.7, 0.8, 1
                        font_size: dp(15)
                        size_hint_x: 0.55
                        halign: 'left'
                        text_size: self.size
                        valign: 'middle'
                    Label:
                        id: res_rl
                        text: '-'
                        color: 0.957, 0.635, 0.380, 1
                        font_size: dp(17)
                        bold: True
                        size_hint_x: 0.45
                        halign: 'right'
                        text_size: self.size
                        valign: 'middle'

                # Divider before heat
                BoxLayout:
                    size_hint_y: None
                    height: dp(1)
                    canvas.before:
                        Color:
                            rgba: 0.2, 0.2, 0.35, 1
                        Rectangle:
                            pos: self.pos
                            size: self.size

                # Generierte Hitze
                BoxLayout:
                    size_hint_y: None
                    height: dp(50)
                    Label:
                        text: 'Generierte Hitze'
                        color: 1.0, 0.55, 0.2, 1
                        font_size: dp(15)
                        bold: True
                        size_hint_x: 0.55
                        halign: 'left'
                        text_size: self.size
                        valign: 'middle'
                    Label:
                        id: res_hitze
                        text: '-'
                        color: 1.0, 0.55, 0.2, 1
                        font_size: dp(19)
                        bold: True
                        size_hint_x: 0.45
                        halign: 'right'
                        text_size: self.size
                        valign: 'middle'

            # Bottom padding
            Widget:
                size_hint_y: None
                height: dp(16)
"""

Builder.load_string(KV)

# ── Klassen ────────────────────────────────────────────────────────────────

class DarkSpinnerOption(SpinnerOption):
    """Dark-themed option row for the weapon spinner dropdown."""
    pass


class MainWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._count   = 1
        self._treffw  = 8
        self._zone    = 'vorne'
        self._faction = 'is'

    # Stepper callbacks
    def inc_count(self):
        self._count = min(self._count + 1, 20)
        self.ids.count_label.text = str(self._count)

    def dec_count(self):
        self._count = max(self._count - 1, 1)
        self.ids.count_label.text = str(self._count)

    def inc_treffw(self):
        self._treffw = min(self._treffw + 1, 20)
        self.ids.treffw_label.text = str(self._treffw)

    def dec_treffw(self):
        self._treffw = max(self._treffw - 1, 2)
        self.ids.treffw_label.text = str(self._treffw)

    # Faction toggle
    def set_faction(self, faction):
        self._faction = faction
        active   = (0.914, 0.271, 0.376, 1)
        inactive = (0.059, 0.204, 0.376, 1)
        self.ids.btn_is.bg_color   = active   if faction == 'is'   else inactive
        self.ids.btn_clan.bg_color = active   if faction == 'clan' else inactive
        new_values = list(WEAPONS.keys()) if faction == 'is' else list(WEAPONS_CLAN.keys())
        self.ids.weapon_spinner.values = new_values
        self.ids.weapon_spinner.text   = new_values[0]

    # Zone toggle
    def set_zone(self, zone):
        self._zone = zone
        active   = (0.914, 0.271, 0.376, 1)
        inactive = (0.059, 0.204, 0.376, 1)
        self.ids.btn_vorne.bg_color  = active   if zone == 'vorne'  else inactive
        self.ids.btn_rechts.bg_color = active   if zone == 'rechts' else inactive
        self.ids.btn_links.bg_color  = active   if zone == 'links'  else inactive
        # Update crit label immediately
        possible_crit = ZONES[zone][2]
        self.ids.lbl_crit_name.text = CRIT_LABELS[possible_crit]

    # Re-enable fire button after grey-out
    def _re_enable_fire_btn(self, dt):
        btn = self.ids.fire_btn
        btn.disabled  = False
        btn.bg_color  = (0.914, 0.271, 0.376, 1)

    # Main calculation
    def fire(self):
        # Visual feedback: grey out button for 3 s
        btn = self.ids.fire_btn
        btn.disabled = True
        btn.bg_color = (0.3, 0.3, 0.3, 1)
        Clock.schedule_once(self._re_enable_fire_btn, 3)

        # Haptic feedback: vibrate 0.2 s
        try:
            from plyer import vibrator
            vibrator.vibrate(0.2)
        except Exception:
            pass

        weapon = self.ids.weapon_spinner.text
        weapons_table = WEAPONS if self._faction == 'is' else WEAPONS_CLAN
        w = weapons_table[weapon]

        # 1. Hits (2d10 >= Trefferwert)
        hits = calc_hits(self._count, self._treffw)

        # 2. For missile weapons: roll missile count per hit
        if w["missile"] and hits > 0:
            effective_hits = calc_missiles(hits, weapon)
        else:
            effective_hits = hits

        # 3. Hit locations (2d6 per effective hit)
        locs = calc_locations(effective_hits, self._zone) if effective_hits > 0 else {}

        # 4. Generated heat
        heat = self._count * w["heat"]

        # 5. Crit label for this zone
        possible_crit = ZONES[self._zone][2]
        self.ids.lbl_crit_name.text = CRIT_LABELS[possible_crit]

        # 6. Format helper
        dmg = w["dmg"]

        def fmt(key):
            n = locs.get(key, 0)
            return f"{n}  {dmg}" if n > 0 else "-"

        # 7. Update all result labels
        self.ids.res_hd.text    = fmt("hd")
        self.ids.res_la.text    = fmt("la")
        self.ids.res_ra.text    = fmt("ra")
        self.ids.res_lt.text    = fmt("lt")
        self.ids.res_rt.text    = fmt("rt")
        self.ids.res_ct.text    = fmt("ct")
        self.ids.res_crit.text  = fmt(possible_crit)
        self.ids.res_ll.text    = fmt("ll")
        self.ids.res_rl.text    = fmt("rl")
        self.ids.res_hitze.text = str(heat)


class BTCalcApp(App):
    title = 'BTcalc'

    @property
    def DarkSpinnerOption(self):
        return DarkSpinnerOption

    def build(self):
        return MainWidget()


if __name__ == '__main__':
    BTCalcApp().run()
