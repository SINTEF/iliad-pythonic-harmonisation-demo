"""This module contains functions for the units in QUDT."""

from rdflib import URIRef
from constants import QUDT_UNIT


def get_qudt_unit_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram (http://qudt.org/vocab/unit/KiloGM)"""
    return QUDT_UNIT["KILOGM"]


def get_qudt_unit_reciprocal_mole() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Mole (http://qudt.org/vocab/unit/PER-MOL)"""
    return QUDT_UNIT["PER-MOL"]


def get_qudt_unit_joule_per_tesla() -> URIRef:
    """Returns the URI for QUDT unit: Joule per Tesla (http://qudt.org/vocab/unit/J-PER-T)"""
    return QUDT_UNIT["J-PER-T"]


def get_qudt_unit_metre() -> URIRef:
    """Returns the URI for QUDT unit: Metre (http://qudt.org/vocab/unit/M)"""
    return QUDT_UNIT["M"]


def get_qudt_unit_joule_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Joule per Kelvin (http://qudt.org/vocab/unit/J-PER-K)"""
    return QUDT_UNIT["J-PER-K"]


def get_qudt_unit_henry_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Henry per Metre (http://qudt.org/vocab/unit/H-PER-M)"""
    return QUDT_UNIT["H-PER-M"]


def get_qudt_unit_ampere_square_metre_per_joule_second() -> URIRef:
    """Returns the URI for QUDT unit: Ampere Square Metre per Joule Second (http://qudt.org/vocab/unit/A-M2-PER-J-SEC)"""
    return QUDT_UNIT["A-M2-PER-J-SEC"]


def get_qudt_unit_coulomb_per_mole() -> URIRef:
    """Returns the URI for QUDT unit: Coulomb per Mole (http://qudt.org/vocab/unit/C-PER-MOL)"""
    return QUDT_UNIT["C-PER-MOL"]


def get_qudt_unit_unitless() -> URIRef:
    """Returns the URI for QUDT unit: Unitless (http://qudt.org/vocab/unit/UNITLESS)"""
    return QUDT_UNIT["UNITLESS"]


def get_qudt_unit_newton_square_metre_per_square_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Newton Square Metre per Square Kilogram (http://qudt.org/vocab/unit/N-M2-PER-KiloGM2)"""
    return QUDT_UNIT["N-M2-PER-KILOGM2"]


def get_qudt_unit_reciprocal_weber() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Weber (http://qudt.org/vocab/unit/PER-WB)"""
    return QUDT_UNIT["PER-WB"]


def get_qudt_unit_joule_per_mole_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Joule per Mole Kelvin (http://qudt.org/vocab/unit/J-PER-MOL-K)"""
    return QUDT_UNIT["J-PER-MOL-K"]


def get_qudt_unit_farad_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Farad per Metre (http://qudt.org/vocab/unit/FARAD-PER-M)"""
    return QUDT_UNIT["FARAD-PER-M"]


def get_qudt_unit_joule_second() -> URIRef:
    """Returns the URI for QUDT unit: Joule Second (http://qudt.org/vocab/unit/J-SEC)"""
    return QUDT_UNIT["J-SEC"]


def get_qudt_unit_reciprocal_metre() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Metre (http://qudt.org/vocab/unit/PER-M)"""
    return QUDT_UNIT["PER-M"]


def get_qudt_unit_joule() -> URIRef:
    """Returns the URI for QUDT unit: Joule (http://qudt.org/vocab/unit/J)"""
    return QUDT_UNIT["J"]


def get_qudt_unit_mega_electron_volt() -> URIRef:
    """Returns the URI for QUDT unit: Mega Electron Volt (http://qudt.org/vocab/unit/MegaEV)"""
    return QUDT_UNIT["MEGAEV"]


def get_qudt_unit_unified_atomic_mass_unit() -> URIRef:
    """Returns the URI for QUDT unit: Unified Atomic Mass Unit (http://qudt.org/vocab/unit/U)"""
    return QUDT_UNIT["U"]


def get_qudt_unit_kilogram_per_mole() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Mole (http://qudt.org/vocab/unit/KiloGM-PER-MOL)"""
    return QUDT_UNIT["KILOGM-PER-MOL"]


def get_qudt_unit_electron_volt() -> URIRef:
    """Returns the URI for QUDT unit: Electron Volt (http://qudt.org/vocab/unit/EV)"""
    return QUDT_UNIT["EV"]


def get_qudt_unit_hartree() -> URIRef:
    """Returns the URI for QUDT unit: Hartree (http://qudt.org/vocab/unit/E_h)"""
    return QUDT_UNIT["E_H"]


def get_qudt_unit_hertz() -> URIRef:
    """Returns the URI for QUDT unit: Hertz (http://qudt.org/vocab/unit/HZ)"""
    return QUDT_UNIT["HZ"]


def get_qudt_unit_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Kelvin (http://qudt.org/vocab/unit/K)"""
    return QUDT_UNIT["K"]


def get_qudt_unit_cubic_coulomb_metre_per_square_joule() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Coulomb Metre per Square Joule (http://qudt.org/vocab/unit/C3-M-PER-J2)"""
    return QUDT_UNIT["C3-M-PER-J2"]


def get_qudt_unit_quartic_coulomb_quartic_metre_per_cubic_joule() -> URIRef:
    """Returns the URI for QUDT unit: Quartic Coulomb Quartic Metre per Cubic Joule (http://qudt.org/vocab/unit/C4-M4-PER-J3)"""
    return QUDT_UNIT["C4-M4-PER-J3"]


def get_qudt_unit_coulomb() -> URIRef:
    """Returns the URI for QUDT unit: Coulomb (http://qudt.org/vocab/unit/C)"""
    return QUDT_UNIT["C"]


def get_qudt_unit_coulomb_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Coulomb per Cubic Metre (http://qudt.org/vocab/unit/C-PER-M3)"""
    return QUDT_UNIT["C-PER-M3"]


def get_qudt_unit_ampere() -> URIRef:
    """Returns the URI for QUDT unit: Ampere (http://qudt.org/vocab/unit/A)"""
    return QUDT_UNIT["A"]


def get_qudt_unit_coulomb_metre() -> URIRef:
    """Returns the URI for QUDT unit: Coulomb Metre (http://qudt.org/vocab/unit/C-M)"""
    return QUDT_UNIT["C-M"]


def get_qudt_unit_volt_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Volt per Metre (http://qudt.org/vocab/unit/V-PER-M)"""
    return QUDT_UNIT["V-PER-M"]


def get_qudt_unit_volt_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Volt per Square Metre (http://qudt.org/vocab/unit/V-PER-M2)"""
    return QUDT_UNIT["V-PER-M2"]


def get_qudt_unit_square_coulomb_square_metre_per_joule() -> URIRef:
    """Returns the URI for QUDT unit: Square Coulomb Square Metre per Joule (http://qudt.org/vocab/unit/C2-M2-PER-J)"""
    return QUDT_UNIT["C2-M2-PER-J"]


def get_qudt_unit_volt() -> URIRef:
    """Returns the URI for QUDT unit: Volt (http://qudt.org/vocab/unit/V)"""
    return QUDT_UNIT["V"]


def get_qudt_unit_coulomb_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Coulomb Square Metre (http://qudt.org/vocab/unit/C-M2)"""
    return QUDT_UNIT["C-M2"]


def get_qudt_unit_newton() -> URIRef:
    """Returns the URI for QUDT unit: Newton (http://qudt.org/vocab/unit/N)"""
    return QUDT_UNIT["N"]


def get_qudt_unit_tesla() -> URIRef:
    """Returns the URI for QUDT unit: Tesla (http://qudt.org/vocab/unit/T)"""
    return QUDT_UNIT["T"]


def get_qudt_unit_joule_per_square_tesla() -> URIRef:
    """Returns the URI for QUDT unit: Joule per Square Tesla (http://qudt.org/vocab/unit/J-PER-T2)"""
    return QUDT_UNIT["J-PER-T2"]


def get_qudt_unit_kilogram_metre_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram Metre per Second (http://qudt.org/vocab/unit/KiloGM-M-PER-SEC)"""
    return QUDT_UNIT["KILOGM-M-PER-SEC"]


def get_qudt_unit_second() -> URIRef:
    """Returns the URI for QUDT unit: Second (http://qudt.org/vocab/unit/SEC)"""
    return QUDT_UNIT["SEC"]


def get_qudt_unit_metre_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Metre per Second (http://qudt.org/vocab/unit/M-PER-SEC)"""
    return QUDT_UNIT["M-PER-SEC"]


def get_qudt_unit_electron_volt_per_tesla() -> URIRef:
    """Returns the URI for QUDT unit: Electron Volt per Tesla (http://qudt.org/vocab/unit/EV-PER-T)"""
    return QUDT_UNIT["EV-PER-T"]


def get_qudt_unit_hertz_per_tesla() -> URIRef:
    """Returns the URI for QUDT unit: Hertz per Tesla (http://qudt.org/vocab/unit/HZ-PER-T)"""
    return QUDT_UNIT["HZ-PER-T"]


def get_qudt_unit_reciprocal_tesla_metre() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Tesla Metre (http://qudt.org/vocab/unit/PER-T-M)"""
    return QUDT_UNIT["PER-T-M"]


def get_qudt_unit_kelvin_per_tesla() -> URIRef:
    """Returns the URI for QUDT unit: Kelvin per Tesla (http://qudt.org/vocab/unit/K-PER-T)"""
    return QUDT_UNIT["K-PER-T"]


def get_qudt_unit_electron_volt_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Electron Volt per Kelvin (http://qudt.org/vocab/unit/EV-PER-K)"""
    return QUDT_UNIT["EV-PER-K"]


def get_qudt_unit_hertz_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Hertz per Kelvin (http://qudt.org/vocab/unit/HZ-PER-K)"""
    return QUDT_UNIT["HZ-PER-K"]


def get_qudt_unit_reciprocal_metre_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Metre Kelvin (http://qudt.org/vocab/unit/PER-M-K)"""
    return QUDT_UNIT["PER-M-K"]


def get_qudt_unit_ohm() -> URIRef:
    """Returns the URI for QUDT unit: Ohm (http://qudt.org/vocab/unit/OHM)"""
    return QUDT_UNIT["OHM"]


def get_qudt_unit_siemens() -> URIRef:
    """Returns the URI for QUDT unit: Siemens (http://qudt.org/vocab/unit/S)"""
    return QUDT_UNIT["S"]


def get_qudt_unit_hertz_per_volt() -> URIRef:
    """Returns the URI for QUDT unit: Hertz per Volt (http://qudt.org/vocab/unit/HZ-PER-V)"""
    return QUDT_UNIT["HZ-PER-V"]


def get_qudt_unit_coulomb_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Coulomb per Kilogram (http://qudt.org/vocab/unit/C-PER-KiloGM)"""
    return QUDT_UNIT["C-PER-KILOGM"]


def get_qudt_unit_reciprocal_tesla_second() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Tesla Second (http://qudt.org/vocab/unit/PER-T-SEC)"""
    return QUDT_UNIT["PER-T-SEC"]


def get_qudt_unit_megahertz_per_tesla() -> URIRef:
    """Returns the URI for QUDT unit: Megahertz per Tesla (http://qudt.org/vocab/unit/MegaHZ-PER-T)"""
    return QUDT_UNIT["MEGAHZ-PER-T"]


def get_qudt_unit_ampere_per_joule() -> URIRef:
    """Returns the URI for QUDT unit: Ampere per Joule (http://qudt.org/vocab/unit/A-PER-J)"""
    return QUDT_UNIT["A-PER-J"]


def get_qudt_unit_reciprocal_square_giga_electron_volt() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Square Giga Electron Volt (http://qudt.org/vocab/unit/PER-GigaEV2)"""
    return QUDT_UNIT["PER-GIGAEV2"]


def get_qudt_unit_watt_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Watt Square Metre (http://qudt.org/vocab/unit/W-M2)"""
    return QUDT_UNIT["W-M2"]


def get_qudt_unit_watt_square_metre_per_steradian() -> URIRef:
    """Returns the URI for QUDT unit: Watt Square Metre per Steradian (http://qudt.org/vocab/unit/W-M2-PER-SR)"""
    return QUDT_UNIT["W-M2-PER-SR"]


def get_qudt_unit_reciprocal_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Cubic Metre (http://qudt.org/vocab/unit/PER-M3)"""
    return QUDT_UNIT["PER-M3"]


def get_qudt_unit_weber() -> URIRef:
    """Returns the URI for QUDT unit: Weber (http://qudt.org/vocab/unit/WB)"""
    return QUDT_UNIT["WB"]


def get_qudt_unit_joule_second_per_mole() -> URIRef:
    """Returns the URI for QUDT unit: Joule Second per Mole (http://qudt.org/vocab/unit/J-SEC-PER-MOL)"""
    return QUDT_UNIT["J-SEC-PER-MOL"]


def get_qudt_unit_joule_metre_per_mole() -> URIRef:
    """Returns the URI for QUDT unit: Joule Metre per Mole (http://qudt.org/vocab/unit/J-M-PER-MOL)"""
    return QUDT_UNIT["J-M-PER-MOL"]


def get_qudt_unit_cubic_metre_per_mole() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Metre per Mole (http://qudt.org/vocab/unit/M3-PER-MOL)"""
    return QUDT_UNIT["M3-PER-MOL"]


def get_qudt_unit_electron_volt_second() -> URIRef:
    """Returns the URI for QUDT unit: Electron Volt Second (http://qudt.org/vocab/unit/EV-SEC)"""
    return QUDT_UNIT["EV-SEC"]


def get_qudt_unit_mega_electron_volt_per_speed_of_light() -> URIRef:
    """Returns the URI for QUDT unit: Mega Electron Volt per Speed of Light (http://qudt.org/vocab/unit/MegaEV-PER-SpeedOfLight)"""
    return QUDT_UNIT["MEGAEV-PER-SPEEDOFLIGHT"]


def get_qudt_unit_cubic_metre_per_kilogram_square_second() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Metre per Kilogram Square Second (http://qudt.org/vocab/unit/M3-PER-KiloGM-SEC2)"""
    return QUDT_UNIT["M3-PER-KILOGM-SEC2"]


def get_qudt_unit_reciprocal_square_planck_mass() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Square Planck Mass (http://qudt.org/vocab/unit/PER-PlanckMass2)"""
    return QUDT_UNIT["PER-PLANCKMASS2"]


def get_qudt_unit_mega_electron_volt_femtometre() -> URIRef:
    """Returns the URI for QUDT unit: Mega Electron Volt Femtometre (http://qudt.org/vocab/unit/MegaEV-FemtoM)"""
    return QUDT_UNIT["MEGAEV-FEMTOM"]


def get_qudt_unit_giga_electron_volt() -> URIRef:
    """Returns the URI for QUDT unit: Giga Electron Volt (http://qudt.org/vocab/unit/GigaEV)"""
    return QUDT_UNIT["GIGAEV"]


def get_qudt_unit_square_metre_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre per Second (http://qudt.org/vocab/unit/M2-PER-SEC)"""
    return QUDT_UNIT["M2-PER-SEC"]


def get_qudt_unit_metre_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Metre Kelvin (http://qudt.org/vocab/unit/M-K)"""
    return QUDT_UNIT["M-K"]


def get_qudt_unit_international_mile_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: International Mile per Hour (http://qudt.org/vocab/unit/MI-PER-HR)"""
    return QUDT_UNIT["MI-PER-HR"]


def get_qudt_unit_metre_per_square_second() -> URIRef:
    """Returns the URI for QUDT unit: Metre per Square Second (http://qudt.org/vocab/unit/M-PER-SEC2)"""
    return QUDT_UNIT["M-PER-SEC2"]


def get_qudt_unit_pascal() -> URIRef:
    """Returns the URI for QUDT unit: Pascal (http://qudt.org/vocab/unit/PA)"""
    return QUDT_UNIT["PA"]


def get_qudt_unit_watt_per_square_metre_quartic_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Watt per Square Metre Quartic Kelvin (http://qudt.org/vocab/unit/W-PER-M2-K4)"""
    return QUDT_UNIT["W-PER-M2-K4"]


def get_qudt_unit_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre (http://qudt.org/vocab/unit/M2)"""
    return QUDT_UNIT["M2"]


def get_qudt_unit_united_arab_emirates_dirham() -> URIRef:
    """Returns the URI for QUDT unit: United Arab Emirates Dirham (http://qudt.org/vocab/unit/CCY_AED)"""
    return QUDT_UNIT["CCY_AED"]


def get_qudt_unit_afghani() -> URIRef:
    """Returns the URI for QUDT unit: Afghani (http://qudt.org/vocab/unit/CCY_AFN)"""
    return QUDT_UNIT["CCY_AFN"]


def get_qudt_unit_lek() -> URIRef:
    """Returns the URI for QUDT unit: Lek (http://qudt.org/vocab/unit/CCY_ALL)"""
    return QUDT_UNIT["CCY_ALL"]


def get_qudt_unit_armenian_dram() -> URIRef:
    """Returns the URI for QUDT unit: Armenian Dram (http://qudt.org/vocab/unit/CCY_AMD)"""
    return QUDT_UNIT["CCY_AMD"]


def get_qudt_unit_netherlands_antillian_guilder() -> URIRef:
    """Returns the URI for QUDT unit: Netherlands Antillian Guilder (http://qudt.org/vocab/unit/CCY_ANG)"""
    return QUDT_UNIT["CCY_ANG"]


def get_qudt_unit_kwanza() -> URIRef:
    """Returns the URI for QUDT unit: Kwanza (http://qudt.org/vocab/unit/CCY_AOA)"""
    return QUDT_UNIT["CCY_AOA"]


def get_qudt_unit_argentine_peso() -> URIRef:
    """Returns the URI for QUDT unit: Argentine Peso (http://qudt.org/vocab/unit/CCY_ARS)"""
    return QUDT_UNIT["CCY_ARS"]


def get_qudt_unit_australian_dollar() -> URIRef:
    """Returns the URI for QUDT unit: Australian Dollar (http://qudt.org/vocab/unit/CCY_AUD)"""
    return QUDT_UNIT["CCY_AUD"]


def get_qudt_unit_aruban_guilder() -> URIRef:
    """Returns the URI for QUDT unit: Aruban Guilder (http://qudt.org/vocab/unit/CCY_AWG)"""
    return QUDT_UNIT["CCY_AWG"]


def get_qudt_unit_azerbaijanian_manat() -> URIRef:
    """Returns the URI for QUDT unit: Azerbaijanian Manat (http://qudt.org/vocab/unit/CCY_AZN)"""
    return QUDT_UNIT["CCY_AZN"]


def get_qudt_unit_convertible_marks() -> URIRef:
    """Returns the URI for QUDT unit: Convertible Marks (http://qudt.org/vocab/unit/CCY_BAM)"""
    return QUDT_UNIT["CCY_BAM"]


def get_qudt_unit_barbados_dollar() -> URIRef:
    """Returns the URI for QUDT unit: Barbados Dollar (http://qudt.org/vocab/unit/CCY_BBD)"""
    return QUDT_UNIT["CCY_BBD"]


def get_qudt_unit_bangladeshi_taka() -> URIRef:
    """Returns the URI for QUDT unit: Bangladeshi Taka (http://qudt.org/vocab/unit/CCY_BDT)"""
    return QUDT_UNIT["CCY_BDT"]


def get_qudt_unit_bulgarian_lev() -> URIRef:
    """Returns the URI for QUDT unit: Bulgarian Lev (http://qudt.org/vocab/unit/CCY_BGN)"""
    return QUDT_UNIT["CCY_BGN"]


def get_qudt_unit_bahraini_dinar() -> URIRef:
    """Returns the URI for QUDT unit: Bahraini Dinar (http://qudt.org/vocab/unit/CCY_BHD)"""
    return QUDT_UNIT["CCY_BHD"]


def get_qudt_unit_burundian_franc() -> URIRef:
    """Returns the URI for QUDT unit: Burundian Franc (http://qudt.org/vocab/unit/CCY_BIF)"""
    return QUDT_UNIT["CCY_BIF"]


def get_qudt_unit_bermuda_dollar() -> URIRef:
    """Returns the URI for QUDT unit: Bermuda Dollar (http://qudt.org/vocab/unit/CCY_BMD)"""
    return QUDT_UNIT["CCY_BMD"]


def get_qudt_unit_brunei_dollar() -> URIRef:
    """Returns the URI for QUDT unit: Brunei Dollar (http://qudt.org/vocab/unit/CCY_BND)"""
    return QUDT_UNIT["CCY_BND"]


def get_qudt_unit_boliviano() -> URIRef:
    """Returns the URI for QUDT unit: Boliviano (http://qudt.org/vocab/unit/CCY_BOB)"""
    return QUDT_UNIT["CCY_BOB"]


def get_qudt_unit_bolivian_mvdol_funds_code() -> URIRef:
    """Returns the URI for QUDT unit: Bolivian Mvdol (funds Code) (http://qudt.org/vocab/unit/CCY_BOV)"""
    return QUDT_UNIT["CCY_BOV"]


def get_qudt_unit_brazilian_real() -> URIRef:
    """Returns the URI for QUDT unit: Brazilian Real (http://qudt.org/vocab/unit/CCY_BRL)"""
    return QUDT_UNIT["CCY_BRL"]


def get_qudt_unit_bahamian_dollar() -> URIRef:
    """Returns the URI for QUDT unit: Bahamian Dollar (http://qudt.org/vocab/unit/CCY_BSD)"""
    return QUDT_UNIT["CCY_BSD"]


def get_qudt_unit_ngultrum() -> URIRef:
    """Returns the URI for QUDT unit: Ngultrum (http://qudt.org/vocab/unit/CCY_BTN)"""
    return QUDT_UNIT["CCY_BTN"]


def get_qudt_unit_pula() -> URIRef:
    """Returns the URI for QUDT unit: Pula (http://qudt.org/vocab/unit/CCY_BWP)"""
    return QUDT_UNIT["CCY_BWP"]


def get_qudt_unit_belarussian_ruble() -> URIRef:
    """Returns the URI for QUDT unit: Belarussian Ruble (http://qudt.org/vocab/unit/CCY_BYN)"""
    return QUDT_UNIT["CCY_BYN"]


def get_qudt_unit_belize_dollar() -> URIRef:
    """Returns the URI for QUDT unit: Belize Dollar (http://qudt.org/vocab/unit/CCY_BZD)"""
    return QUDT_UNIT["CCY_BZD"]


def get_qudt_unit_canadian_dollar() -> URIRef:
    """Returns the URI for QUDT unit: Canadian Dollar (http://qudt.org/vocab/unit/CCY_CAD)"""
    return QUDT_UNIT["CCY_CAD"]


def get_qudt_unit_franc_congolais() -> URIRef:
    """Returns the URI for QUDT unit: Franc Congolais (http://qudt.org/vocab/unit/CCY_CDF)"""
    return QUDT_UNIT["CCY_CDF"]


def get_qudt_unit_wir_euro_complementary_currency() -> URIRef:
    """Returns the URI for QUDT unit: Wir Euro (complementary Currency) (http://qudt.org/vocab/unit/CCY_CHE)"""
    return QUDT_UNIT["CCY_CHE"]


def get_qudt_unit_swiss_franc() -> URIRef:
    """Returns the URI for QUDT unit: Swiss Franc (http://qudt.org/vocab/unit/CCY_CHF)"""
    return QUDT_UNIT["CCY_CHF"]


def get_qudt_unit_wir_franc_complementary_currency() -> URIRef:
    """Returns the URI for QUDT unit: Wir Franc (complementary Currency) (http://qudt.org/vocab/unit/CCY_CHW)"""
    return QUDT_UNIT["CCY_CHW"]


def get_qudt_unit_unidades_de_formento_funds_code() -> URIRef:
    """Returns the URI for QUDT unit: Unidades De Formento (funds Code) (http://qudt.org/vocab/unit/CCY_CLF)"""
    return QUDT_UNIT["CCY_CLF"]


def get_qudt_unit_chilean_peso() -> URIRef:
    """Returns the URI for QUDT unit: Chilean Peso (http://qudt.org/vocab/unit/CCY_CLP)"""
    return QUDT_UNIT["CCY_CLP"]


def get_qudt_unit_yuan_renminbi() -> URIRef:
    """Returns the URI for QUDT unit: Yuan Renminbi (http://qudt.org/vocab/unit/CCY_CNY)"""
    return QUDT_UNIT["CCY_CNY"]


def get_qudt_unit_colombian_peso() -> URIRef:
    """Returns the URI for QUDT unit: Colombian Peso (http://qudt.org/vocab/unit/CCY_COP)"""
    return QUDT_UNIT["CCY_COP"]


def get_qudt_unit_unidad_de_valor_real() -> URIRef:
    """Returns the URI for QUDT unit: Unidad De Valor Real (http://qudt.org/vocab/unit/CCY_COU)"""
    return QUDT_UNIT["CCY_COU"]


def get_qudt_unit_costa_rican_colon() -> URIRef:
    """Returns the URI for QUDT unit: Costa Rican Colon (http://qudt.org/vocab/unit/CCY_CRC)"""
    return QUDT_UNIT["CCY_CRC"]


def get_qudt_unit_cuban_peso() -> URIRef:
    """Returns the URI for QUDT unit: Cuban Peso (http://qudt.org/vocab/unit/CCY_CUP)"""
    return QUDT_UNIT["CCY_CUP"]


def get_qudt_unit_cape_verde_escudo() -> URIRef:
    """Returns the URI for QUDT unit: Cape Verde Escudo (http://qudt.org/vocab/unit/CCY_CVE)"""
    return QUDT_UNIT["CCY_CVE"]


def get_qudt_unit_cyprus_pound() -> URIRef:
    """Returns the URI for QUDT unit: Cyprus Pound (http://qudt.org/vocab/unit/CCY_CYP)"""
    return QUDT_UNIT["CCY_CYP"]


def get_qudt_unit_czech_koruna() -> URIRef:
    """Returns the URI for QUDT unit: Czech Koruna (http://qudt.org/vocab/unit/CCY_CZK)"""
    return QUDT_UNIT["CCY_CZK"]


def get_qudt_unit_djibouti_franc() -> URIRef:
    """Returns the URI for QUDT unit: Djibouti Franc (http://qudt.org/vocab/unit/CCY_DJF)"""
    return QUDT_UNIT["CCY_DJF"]


def get_qudt_unit_danish_krone() -> URIRef:
    """Returns the URI for QUDT unit: Danish Krone (http://qudt.org/vocab/unit/CCY_DKK)"""
    return QUDT_UNIT["CCY_DKK"]


def get_qudt_unit_dominican_peso() -> URIRef:
    """Returns the URI for QUDT unit: Dominican Peso (http://qudt.org/vocab/unit/CCY_DOP)"""
    return QUDT_UNIT["CCY_DOP"]


def get_qudt_unit_algerian_dinar() -> URIRef:
    """Returns the URI for QUDT unit: Algerian Dinar (http://qudt.org/vocab/unit/CCY_DZD)"""
    return QUDT_UNIT["CCY_DZD"]


def get_qudt_unit_kroon() -> URIRef:
    """Returns the URI for QUDT unit: Kroon (http://qudt.org/vocab/unit/CCY_EEK)"""
    return QUDT_UNIT["CCY_EEK"]


def get_qudt_unit_egyptian_pound() -> URIRef:
    """Returns the URI for QUDT unit: Egyptian Pound (http://qudt.org/vocab/unit/CCY_EGP)"""
    return QUDT_UNIT["CCY_EGP"]


def get_qudt_unit_nakfa() -> URIRef:
    """Returns the URI for QUDT unit: Nakfa (http://qudt.org/vocab/unit/CCY_ERN)"""
    return QUDT_UNIT["CCY_ERN"]


def get_qudt_unit_ethiopian_birr() -> URIRef:
    """Returns the URI for QUDT unit: Ethiopian Birr (http://qudt.org/vocab/unit/CCY_ETB)"""
    return QUDT_UNIT["CCY_ETB"]


def get_qudt_unit_euro() -> URIRef:
    """Returns the URI for QUDT unit: Euro (http://qudt.org/vocab/unit/CCY_EUR)"""
    return QUDT_UNIT["CCY_EUR"]


def get_qudt_unit_fiji_dollar() -> URIRef:
    """Returns the URI for QUDT unit: Fiji Dollar (http://qudt.org/vocab/unit/CCY_FJD)"""
    return QUDT_UNIT["CCY_FJD"]


def get_qudt_unit_falkland_islands_pound() -> URIRef:
    """Returns the URI for QUDT unit: Falkland Islands Pound (http://qudt.org/vocab/unit/CCY_FKP)"""
    return QUDT_UNIT["CCY_FKP"]


def get_qudt_unit_pound_sterling() -> URIRef:
    """Returns the URI for QUDT unit: Pound Sterling (http://qudt.org/vocab/unit/CCY_GBP)"""
    return QUDT_UNIT["CCY_GBP"]


def get_qudt_unit_lari() -> URIRef:
    """Returns the URI for QUDT unit: Lari (http://qudt.org/vocab/unit/CCY_GEL)"""
    return QUDT_UNIT["CCY_GEL"]


def get_qudt_unit_cedi() -> URIRef:
    """Returns the URI for QUDT unit: Cedi (http://qudt.org/vocab/unit/CCY_GHS)"""
    return QUDT_UNIT["CCY_GHS"]


def get_qudt_unit_gibraltar_pound() -> URIRef:
    """Returns the URI for QUDT unit: Gibraltar Pound (http://qudt.org/vocab/unit/CCY_GIP)"""
    return QUDT_UNIT["CCY_GIP"]


def get_qudt_unit_dalasi() -> URIRef:
    """Returns the URI for QUDT unit: Dalasi (http://qudt.org/vocab/unit/CCY_GMD)"""
    return QUDT_UNIT["CCY_GMD"]


def get_qudt_unit_guinea_franc() -> URIRef:
    """Returns the URI for QUDT unit: Guinea Franc (http://qudt.org/vocab/unit/CCY_GNF)"""
    return QUDT_UNIT["CCY_GNF"]


def get_qudt_unit_quetzal() -> URIRef:
    """Returns the URI for QUDT unit: Quetzal (http://qudt.org/vocab/unit/CCY_GTQ)"""
    return QUDT_UNIT["CCY_GTQ"]


def get_qudt_unit_guyana_dollar() -> URIRef:
    """Returns the URI for QUDT unit: Guyana Dollar (http://qudt.org/vocab/unit/CCY_GYD)"""
    return QUDT_UNIT["CCY_GYD"]


def get_qudt_unit_hong_kong_dollar() -> URIRef:
    """Returns the URI for QUDT unit: Hong Kong Dollar (http://qudt.org/vocab/unit/CCY_HKD)"""
    return QUDT_UNIT["CCY_HKD"]


def get_qudt_unit_lempira() -> URIRef:
    """Returns the URI for QUDT unit: Lempira (http://qudt.org/vocab/unit/CCY_HNL)"""
    return QUDT_UNIT["CCY_HNL"]


def get_qudt_unit_croatian_kuna() -> URIRef:
    """Returns the URI for QUDT unit: Croatian Kuna (http://qudt.org/vocab/unit/CCY_HRK)"""
    return QUDT_UNIT["CCY_HRK"]


def get_qudt_unit_haiti_gourde() -> URIRef:
    """Returns the URI for QUDT unit: Haiti Gourde (http://qudt.org/vocab/unit/CCY_HTG)"""
    return QUDT_UNIT["CCY_HTG"]


def get_qudt_unit_forint() -> URIRef:
    """Returns the URI for QUDT unit: Forint (http://qudt.org/vocab/unit/CCY_HUF)"""
    return QUDT_UNIT["CCY_HUF"]


def get_qudt_unit_rupiah() -> URIRef:
    """Returns the URI for QUDT unit: Rupiah (http://qudt.org/vocab/unit/CCY_IDR)"""
    return QUDT_UNIT["CCY_IDR"]


def get_qudt_unit_new_israeli_shekel() -> URIRef:
    """Returns the URI for QUDT unit: New Israeli Shekel (http://qudt.org/vocab/unit/CCY_ILS)"""
    return QUDT_UNIT["CCY_ILS"]


def get_qudt_unit_indian_rupee() -> URIRef:
    """Returns the URI for QUDT unit: Indian Rupee (http://qudt.org/vocab/unit/CCY_INR)"""
    return QUDT_UNIT["CCY_INR"]


def get_qudt_unit_iraqi_dinar() -> URIRef:
    """Returns the URI for QUDT unit: Iraqi Dinar (http://qudt.org/vocab/unit/CCY_IQD)"""
    return QUDT_UNIT["CCY_IQD"]


def get_qudt_unit_iranian_rial() -> URIRef:
    """Returns the URI for QUDT unit: Iranian Rial (http://qudt.org/vocab/unit/CCY_IRR)"""
    return QUDT_UNIT["CCY_IRR"]


def get_qudt_unit_iceland_krona() -> URIRef:
    """Returns the URI for QUDT unit: Iceland Krona (http://qudt.org/vocab/unit/CCY_ISK)"""
    return QUDT_UNIT["CCY_ISK"]


def get_qudt_unit_jamaican_dollar() -> URIRef:
    """Returns the URI for QUDT unit: Jamaican Dollar (http://qudt.org/vocab/unit/CCY_JMD)"""
    return QUDT_UNIT["CCY_JMD"]


def get_qudt_unit_jordanian_dinar() -> URIRef:
    """Returns the URI for QUDT unit: Jordanian Dinar (http://qudt.org/vocab/unit/CCY_JOD)"""
    return QUDT_UNIT["CCY_JOD"]


def get_qudt_unit_japanese_yen() -> URIRef:
    """Returns the URI for QUDT unit: Japanese Yen (http://qudt.org/vocab/unit/CCY_JPY)"""
    return QUDT_UNIT["CCY_JPY"]


def get_qudt_unit_kenyan_shilling() -> URIRef:
    """Returns the URI for QUDT unit: Kenyan Shilling (http://qudt.org/vocab/unit/CCY_KES)"""
    return QUDT_UNIT["CCY_KES"]


def get_qudt_unit_som() -> URIRef:
    """Returns the URI for QUDT unit: Som (http://qudt.org/vocab/unit/CCY_KGS)"""
    return QUDT_UNIT["CCY_KGS"]


def get_qudt_unit_riel() -> URIRef:
    """Returns the URI for QUDT unit: Riel (http://qudt.org/vocab/unit/CCY_KHR)"""
    return QUDT_UNIT["CCY_KHR"]


def get_qudt_unit_comoro_franc() -> URIRef:
    """Returns the URI for QUDT unit: Comoro Franc (http://qudt.org/vocab/unit/CCY_KMF)"""
    return QUDT_UNIT["CCY_KMF"]


def get_qudt_unit_north_korean_won() -> URIRef:
    """Returns the URI for QUDT unit: North Korean Won (http://qudt.org/vocab/unit/CCY_KPW)"""
    return QUDT_UNIT["CCY_KPW"]


def get_qudt_unit_south_korean_won() -> URIRef:
    """Returns the URI for QUDT unit: South Korean Won (http://qudt.org/vocab/unit/CCY_KRW)"""
    return QUDT_UNIT["CCY_KRW"]


def get_qudt_unit_kuwaiti_dinar() -> URIRef:
    """Returns the URI for QUDT unit: Kuwaiti Dinar (http://qudt.org/vocab/unit/CCY_KWD)"""
    return QUDT_UNIT["CCY_KWD"]


def get_qudt_unit_cayman_islands_dollar() -> URIRef:
    """Returns the URI for QUDT unit: Cayman Islands Dollar (http://qudt.org/vocab/unit/CCY_KYD)"""
    return QUDT_UNIT["CCY_KYD"]


def get_qudt_unit_tenge() -> URIRef:
    """Returns the URI for QUDT unit: Tenge (http://qudt.org/vocab/unit/CCY_KZT)"""
    return QUDT_UNIT["CCY_KZT"]


def get_qudt_unit_lao_kip() -> URIRef:
    """Returns the URI for QUDT unit: Lao Kip (http://qudt.org/vocab/unit/CCY_LAK)"""
    return QUDT_UNIT["CCY_LAK"]


def get_qudt_unit_lebanese_pound() -> URIRef:
    """Returns the URI for QUDT unit: Lebanese Pound (http://qudt.org/vocab/unit/CCY_LBP)"""
    return QUDT_UNIT["CCY_LBP"]


def get_qudt_unit_sri_lanka_rupee() -> URIRef:
    """Returns the URI for QUDT unit: Sri Lanka Rupee (http://qudt.org/vocab/unit/CCY_LKR)"""
    return QUDT_UNIT["CCY_LKR"]


def get_qudt_unit_liberian_dollar() -> URIRef:
    """Returns the URI for QUDT unit: Liberian Dollar (http://qudt.org/vocab/unit/CCY_LRD)"""
    return QUDT_UNIT["CCY_LRD"]


def get_qudt_unit_loti() -> URIRef:
    """Returns the URI for QUDT unit: Loti (http://qudt.org/vocab/unit/CCY_LSL)"""
    return QUDT_UNIT["CCY_LSL"]


def get_qudt_unit_lithuanian_litas() -> URIRef:
    """Returns the URI for QUDT unit: Lithuanian Litas (http://qudt.org/vocab/unit/CCY_LTL)"""
    return QUDT_UNIT["CCY_LTL"]


def get_qudt_unit_latvian_lats() -> URIRef:
    """Returns the URI for QUDT unit: Latvian Lats (http://qudt.org/vocab/unit/CCY_LVL)"""
    return QUDT_UNIT["CCY_LVL"]


def get_qudt_unit_libyan_dinar() -> URIRef:
    """Returns the URI for QUDT unit: Libyan Dinar (http://qudt.org/vocab/unit/CCY_LYD)"""
    return QUDT_UNIT["CCY_LYD"]


def get_qudt_unit_moroccan_dirham() -> URIRef:
    """Returns the URI for QUDT unit: Moroccan Dirham (http://qudt.org/vocab/unit/CCY_MAD)"""
    return QUDT_UNIT["CCY_MAD"]


def get_qudt_unit_moldovan_leu() -> URIRef:
    """Returns the URI for QUDT unit: Moldovan Leu (http://qudt.org/vocab/unit/CCY_MDL)"""
    return QUDT_UNIT["CCY_MDL"]


def get_qudt_unit_malagasy_ariary() -> URIRef:
    """Returns the URI for QUDT unit: Malagasy Ariary (http://qudt.org/vocab/unit/CCY_MGA)"""
    return QUDT_UNIT["CCY_MGA"]


def get_qudt_unit_denar() -> URIRef:
    """Returns the URI for QUDT unit: Denar (http://qudt.org/vocab/unit/CCY_MKD)"""
    return QUDT_UNIT["CCY_MKD"]


def get_qudt_unit_kyat() -> URIRef:
    """Returns the URI for QUDT unit: Kyat (http://qudt.org/vocab/unit/CCY_MMK)"""
    return QUDT_UNIT["CCY_MMK"]


def get_qudt_unit_mongolian_tugrik() -> URIRef:
    """Returns the URI for QUDT unit: Mongolian Tugrik (http://qudt.org/vocab/unit/CCY_MNT)"""
    return QUDT_UNIT["CCY_MNT"]


def get_qudt_unit_pataca() -> URIRef:
    """Returns the URI for QUDT unit: Pataca (http://qudt.org/vocab/unit/CCY_MOP)"""
    return QUDT_UNIT["CCY_MOP"]


def get_qudt_unit_ouguiya() -> URIRef:
    """Returns the URI for QUDT unit: Ouguiya (http://qudt.org/vocab/unit/CCY_MRU)"""
    return QUDT_UNIT["CCY_MRU"]


def get_qudt_unit_maltese_lira() -> URIRef:
    """Returns the URI for QUDT unit: Maltese Lira (http://qudt.org/vocab/unit/CCY_MTL)"""
    return QUDT_UNIT["CCY_MTL"]


def get_qudt_unit_mauritius_rupee() -> URIRef:
    """Returns the URI for QUDT unit: Mauritius Rupee (http://qudt.org/vocab/unit/CCY_MUR)"""
    return QUDT_UNIT["CCY_MUR"]


def get_qudt_unit_rufiyaa() -> URIRef:
    """Returns the URI for QUDT unit: Rufiyaa (http://qudt.org/vocab/unit/CCY_MVR)"""
    return QUDT_UNIT["CCY_MVR"]


def get_qudt_unit_malawi_kwacha() -> URIRef:
    """Returns the URI for QUDT unit: Malawi Kwacha (http://qudt.org/vocab/unit/CCY_MWK)"""
    return QUDT_UNIT["CCY_MWK"]


def get_qudt_unit_mexican_peso() -> URIRef:
    """Returns the URI for QUDT unit: Mexican Peso (http://qudt.org/vocab/unit/CCY_MXN)"""
    return QUDT_UNIT["CCY_MXN"]


def get_qudt_unit_mexican_unidad_de_inversion_udi_funds_code() -> URIRef:
    """Returns the URI for QUDT unit: Mexican Unidad De Inversion (udi) (funds Code) (http://qudt.org/vocab/unit/CCY_MXV)"""
    return QUDT_UNIT["CCY_MXV"]


def get_qudt_unit_malaysian_ringgit() -> URIRef:
    """Returns the URI for QUDT unit: Malaysian Ringgit (http://qudt.org/vocab/unit/CCY_MYR)"""
    return QUDT_UNIT["CCY_MYR"]


def get_qudt_unit_metical() -> URIRef:
    """Returns the URI for QUDT unit: Metical (http://qudt.org/vocab/unit/CCY_MZN)"""
    return QUDT_UNIT["CCY_MZN"]


def get_qudt_unit_namibian_dollar() -> URIRef:
    """Returns the URI for QUDT unit: Namibian Dollar (http://qudt.org/vocab/unit/CCY_NAD)"""
    return QUDT_UNIT["CCY_NAD"]


def get_qudt_unit_naira() -> URIRef:
    """Returns the URI for QUDT unit: Naira (http://qudt.org/vocab/unit/CCY_NGN)"""
    return QUDT_UNIT["CCY_NGN"]


def get_qudt_unit_cordoba_oro() -> URIRef:
    """Returns the URI for QUDT unit: Cordoba Oro (http://qudt.org/vocab/unit/CCY_NIO)"""
    return QUDT_UNIT["CCY_NIO"]


def get_qudt_unit_norwegian_krone() -> URIRef:
    """Returns the URI for QUDT unit: Norwegian Krone (http://qudt.org/vocab/unit/CCY_NOK)"""
    return QUDT_UNIT["CCY_NOK"]


def get_qudt_unit_nepalese_rupee() -> URIRef:
    """Returns the URI for QUDT unit: Nepalese Rupee (http://qudt.org/vocab/unit/CCY_NPR)"""
    return QUDT_UNIT["CCY_NPR"]


def get_qudt_unit_new_zealand_dollar() -> URIRef:
    """Returns the URI for QUDT unit: New Zealand Dollar (http://qudt.org/vocab/unit/CCY_NZD)"""
    return QUDT_UNIT["CCY_NZD"]


def get_qudt_unit_rial_omani() -> URIRef:
    """Returns the URI for QUDT unit: Rial Omani (http://qudt.org/vocab/unit/CCY_OMR)"""
    return QUDT_UNIT["CCY_OMR"]


def get_qudt_unit_balboa() -> URIRef:
    """Returns the URI for QUDT unit: Balboa (http://qudt.org/vocab/unit/CCY_PAB)"""
    return QUDT_UNIT["CCY_PAB"]


def get_qudt_unit_nuevo_sol() -> URIRef:
    """Returns the URI for QUDT unit: Nuevo Sol (http://qudt.org/vocab/unit/CCY_PEN)"""
    return QUDT_UNIT["CCY_PEN"]


def get_qudt_unit_kina() -> URIRef:
    """Returns the URI for QUDT unit: Kina (http://qudt.org/vocab/unit/CCY_PGK)"""
    return QUDT_UNIT["CCY_PGK"]


def get_qudt_unit_philippine_peso() -> URIRef:
    """Returns the URI for QUDT unit: Philippine Peso (http://qudt.org/vocab/unit/CCY_PHP)"""
    return QUDT_UNIT["CCY_PHP"]


def get_qudt_unit_pakistan_rupee() -> URIRef:
    """Returns the URI for QUDT unit: Pakistan Rupee (http://qudt.org/vocab/unit/CCY_PKR)"""
    return QUDT_UNIT["CCY_PKR"]


def get_qudt_unit_zloty() -> URIRef:
    """Returns the URI for QUDT unit: Zloty (http://qudt.org/vocab/unit/CCY_PLN)"""
    return QUDT_UNIT["CCY_PLN"]


def get_qudt_unit_guarani() -> URIRef:
    """Returns the URI for QUDT unit: Guarani (http://qudt.org/vocab/unit/CCY_PYG)"""
    return QUDT_UNIT["CCY_PYG"]


def get_qudt_unit_qatari_rial() -> URIRef:
    """Returns the URI for QUDT unit: Qatari Rial (http://qudt.org/vocab/unit/CCY_QAR)"""
    return QUDT_UNIT["CCY_QAR"]


def get_qudt_unit_romanian_new_leu() -> URIRef:
    """Returns the URI for QUDT unit: Romanian New Leu (http://qudt.org/vocab/unit/CCY_RON)"""
    return QUDT_UNIT["CCY_RON"]


def get_qudt_unit_serbian_dinar() -> URIRef:
    """Returns the URI for QUDT unit: Serbian Dinar (http://qudt.org/vocab/unit/CCY_RSD)"""
    return QUDT_UNIT["CCY_RSD"]


def get_qudt_unit_russian_ruble() -> URIRef:
    """Returns the URI for QUDT unit: Russian Ruble (http://qudt.org/vocab/unit/CCY_RUB)"""
    return QUDT_UNIT["CCY_RUB"]


def get_qudt_unit_rwanda_franc() -> URIRef:
    """Returns the URI for QUDT unit: Rwanda Franc (http://qudt.org/vocab/unit/CCY_RWF)"""
    return QUDT_UNIT["CCY_RWF"]


def get_qudt_unit_saudi_riyal() -> URIRef:
    """Returns the URI for QUDT unit: Saudi Riyal (http://qudt.org/vocab/unit/CCY_SAR)"""
    return QUDT_UNIT["CCY_SAR"]


def get_qudt_unit_solomon_islands_dollar() -> URIRef:
    """Returns the URI for QUDT unit: Solomon Islands Dollar (http://qudt.org/vocab/unit/CCY_SBD)"""
    return QUDT_UNIT["CCY_SBD"]


def get_qudt_unit_seychelles_rupee() -> URIRef:
    """Returns the URI for QUDT unit: Seychelles Rupee (http://qudt.org/vocab/unit/CCY_SCR)"""
    return QUDT_UNIT["CCY_SCR"]


def get_qudt_unit_sudanese_pound() -> URIRef:
    """Returns the URI for QUDT unit: Sudanese Pound (http://qudt.org/vocab/unit/CCY_SDG)"""
    return QUDT_UNIT["CCY_SDG"]


def get_qudt_unit_swedish_krona() -> URIRef:
    """Returns the URI for QUDT unit: Swedish Krona (http://qudt.org/vocab/unit/CCY_SEK)"""
    return QUDT_UNIT["CCY_SEK"]


def get_qudt_unit_singapore_dollar() -> URIRef:
    """Returns the URI for QUDT unit: Singapore Dollar (http://qudt.org/vocab/unit/CCY_SGD)"""
    return QUDT_UNIT["CCY_SGD"]


def get_qudt_unit_saint_helena_pound() -> URIRef:
    """Returns the URI for QUDT unit: Saint Helena Pound (http://qudt.org/vocab/unit/CCY_SHP)"""
    return QUDT_UNIT["CCY_SHP"]


def get_qudt_unit_slovak_koruna() -> URIRef:
    """Returns the URI for QUDT unit: Slovak Koruna (http://qudt.org/vocab/unit/CCY_SKK)"""
    return QUDT_UNIT["CCY_SKK"]


def get_qudt_unit_leone() -> URIRef:
    """Returns the URI for QUDT unit: Leone (http://qudt.org/vocab/unit/CCY_SLE)"""
    return QUDT_UNIT["CCY_SLE"]


def get_qudt_unit_somali_shilling() -> URIRef:
    """Returns the URI for QUDT unit: Somali Shilling (http://qudt.org/vocab/unit/CCY_SOS)"""
    return QUDT_UNIT["CCY_SOS"]


def get_qudt_unit_surinam_dollar() -> URIRef:
    """Returns the URI for QUDT unit: Surinam Dollar (http://qudt.org/vocab/unit/CCY_SRD)"""
    return QUDT_UNIT["CCY_SRD"]


def get_qudt_unit_dobra() -> URIRef:
    """Returns the URI for QUDT unit: Dobra (http://qudt.org/vocab/unit/CCY_STN)"""
    return QUDT_UNIT["CCY_STN"]


def get_qudt_unit_syrian_pound() -> URIRef:
    """Returns the URI for QUDT unit: Syrian Pound (http://qudt.org/vocab/unit/CCY_SYP)"""
    return QUDT_UNIT["CCY_SYP"]


def get_qudt_unit_lilangeni() -> URIRef:
    """Returns the URI for QUDT unit: Lilangeni (http://qudt.org/vocab/unit/CCY_SZL)"""
    return QUDT_UNIT["CCY_SZL"]


def get_qudt_unit_baht() -> URIRef:
    """Returns the URI for QUDT unit: Baht (http://qudt.org/vocab/unit/CCY_THB)"""
    return QUDT_UNIT["CCY_THB"]


def get_qudt_unit_somoni() -> URIRef:
    """Returns the URI for QUDT unit: Somoni (http://qudt.org/vocab/unit/CCY_TJS)"""
    return QUDT_UNIT["CCY_TJS"]


def get_qudt_unit_manat() -> URIRef:
    """Returns the URI for QUDT unit: Manat (http://qudt.org/vocab/unit/CCY_TMT)"""
    return QUDT_UNIT["CCY_TMT"]


def get_qudt_unit_tunisian_dinar() -> URIRef:
    """Returns the URI for QUDT unit: Tunisian Dinar (http://qudt.org/vocab/unit/CCY_TND)"""
    return QUDT_UNIT["CCY_TND"]


def get_qudt_unit_pa_anga() -> URIRef:
    """Returns the URI for QUDT unit: Pa'anga (http://qudt.org/vocab/unit/CCY_TOP)"""
    return QUDT_UNIT["CCY_TOP"]


def get_qudt_unit_new_turkish_lira() -> URIRef:
    """Returns the URI for QUDT unit: New Turkish Lira (http://qudt.org/vocab/unit/CCY_TRY)"""
    return QUDT_UNIT["CCY_TRY"]


def get_qudt_unit_trinidad_and_tobago_dollar() -> URIRef:
    """Returns the URI for QUDT unit: Trinidad and Tobago Dollar (http://qudt.org/vocab/unit/CCY_TTD)"""
    return QUDT_UNIT["CCY_TTD"]


def get_qudt_unit_new_taiwan_dollar() -> URIRef:
    """Returns the URI for QUDT unit: New Taiwan Dollar (http://qudt.org/vocab/unit/CCY_TWD)"""
    return QUDT_UNIT["CCY_TWD"]


def get_qudt_unit_tanzanian_shilling() -> URIRef:
    """Returns the URI for QUDT unit: Tanzanian Shilling (http://qudt.org/vocab/unit/CCY_TZS)"""
    return QUDT_UNIT["CCY_TZS"]


def get_qudt_unit_hryvnia() -> URIRef:
    """Returns the URI for QUDT unit: Hryvnia (http://qudt.org/vocab/unit/CCY_UAH)"""
    return QUDT_UNIT["CCY_UAH"]


def get_qudt_unit_uganda_shilling() -> URIRef:
    """Returns the URI for QUDT unit: Uganda Shilling (http://qudt.org/vocab/unit/CCY_UGX)"""
    return QUDT_UNIT["CCY_UGX"]


def get_qudt_unit_us_dollar() -> URIRef:
    """Returns the URI for QUDT unit: Us Dollar (http://qudt.org/vocab/unit/CCY_USD)"""
    return QUDT_UNIT["CCY_USD"]


def get_qudt_unit_united_states_dollar_next_day_funds_code() -> URIRef:
    """Returns the URI for QUDT unit: United States Dollar (next Day) (funds Code) (http://qudt.org/vocab/unit/CCY_USN)"""
    return QUDT_UNIT["CCY_USN"]


def get_qudt_unit_united_states_dollar_same_day_funds_code() -> URIRef:
    """Returns the URI for QUDT unit: United States Dollar (same Day) (funds Code) (http://qudt.org/vocab/unit/CCY_USS)"""
    return QUDT_UNIT["CCY_USS"]


def get_qudt_unit_peso_uruguayo() -> URIRef:
    """Returns the URI for QUDT unit: Peso Uruguayo (http://qudt.org/vocab/unit/CCY_UYU)"""
    return QUDT_UNIT["CCY_UYU"]


def get_qudt_unit_uzbekistan_som() -> URIRef:
    """Returns the URI for QUDT unit: Uzbekistan Som (http://qudt.org/vocab/unit/CCY_UZS)"""
    return QUDT_UNIT["CCY_UZS"]


def get_qudt_unit_venezuelan_bolvar() -> URIRef:
    """Returns the URI for QUDT unit: Venezuelan Bolvar (http://qudt.org/vocab/unit/CCY_VES)"""
    return QUDT_UNIT["CCY_VES"]


def get_qudt_unit_vietnamese_ng() -> URIRef:
    """Returns the URI for QUDT unit: Vietnamese ??ng (http://qudt.org/vocab/unit/CCY_VND)"""
    return QUDT_UNIT["CCY_VND"]


def get_qudt_unit_vatu() -> URIRef:
    """Returns the URI for QUDT unit: Vatu (http://qudt.org/vocab/unit/CCY_VUV)"""
    return QUDT_UNIT["CCY_VUV"]


def get_qudt_unit_samoan_tala() -> URIRef:
    """Returns the URI for QUDT unit: Samoan Tala (http://qudt.org/vocab/unit/CCY_WST)"""
    return QUDT_UNIT["CCY_WST"]


def get_qudt_unit_cfa_franc_beac() -> URIRef:
    """Returns the URI for QUDT unit: Cfa Franc Beac (http://qudt.org/vocab/unit/CCY_XAF)"""
    return QUDT_UNIT["CCY_XAF"]


def get_qudt_unit_silver_one_troy_ounce() -> URIRef:
    """Returns the URI for QUDT unit: Silver (one Troy Ounce) (http://qudt.org/vocab/unit/CCY_XAG)"""
    return QUDT_UNIT["CCY_XAG"]


def get_qudt_unit_gold_one_troy_ounce() -> URIRef:
    """Returns the URI for QUDT unit: Gold (one Troy Ounce) (http://qudt.org/vocab/unit/CCY_XAU)"""
    return QUDT_UNIT["CCY_XAU"]


def get_qudt_unit_european_composite_unit_eurco_bonds_market_unit() -> URIRef:
    """Returns the URI for QUDT unit: European Composite Unit (eurco) (bonds Market Unit) (http://qudt.org/vocab/unit/CCY_XBA)"""
    return QUDT_UNIT["CCY_XBA"]


def get_qudt_unit_european_monetary_unit_e_m_u_6_bonds_market_unit() -> URIRef:
    """Returns the URI for QUDT unit: European Monetary Unit (e.m.u.-6) (bonds Market Unit) (http://qudt.org/vocab/unit/CCY_XBB)"""
    return QUDT_UNIT["CCY_XBB"]


def get_qudt_unit_european_unit_of_account_9_e_u_a_9_bonds_market_unit() -> URIRef:
    """Returns the URI for QUDT unit: European Unit of Account 9 (e.u.a.-9) (bonds Market Unit) (http://qudt.org/vocab/unit/CCY_XBC)"""
    return QUDT_UNIT["CCY_XBC"]


def get_qudt_unit_european_unit_of_account_17_e_u_a_17_bonds_market_unit() -> URIRef:
    """Returns the URI for QUDT unit: European Unit of Account 17 (e.u.a.-17) (bonds Market Unit) (http://qudt.org/vocab/unit/CCY_XBD)"""
    return QUDT_UNIT["CCY_XBD"]


def get_qudt_unit_east_caribbean_dollar() -> URIRef:
    """Returns the URI for QUDT unit: East Caribbean Dollar (http://qudt.org/vocab/unit/CCY_XCD)"""
    return QUDT_UNIT["CCY_XCD"]


def get_qudt_unit_special_drawing_rights() -> URIRef:
    """Returns the URI for QUDT unit: Special Drawing Rights (http://qudt.org/vocab/unit/CCY_XDR)"""
    return QUDT_UNIT["CCY_XDR"]


def get_qudt_unit_gold_franc_special_settlement_currency() -> URIRef:
    """Returns the URI for QUDT unit: Gold Franc (special Settlement Currency) (http://qudt.org/vocab/unit/CCY_XFO)"""
    return QUDT_UNIT["CCY_XFO"]


def get_qudt_unit_uic_franc_special_settlement_currency() -> URIRef:
    """Returns the URI for QUDT unit: Uic Franc (special Settlement Currency) (http://qudt.org/vocab/unit/CCY_XFU)"""
    return QUDT_UNIT["CCY_XFU"]


def get_qudt_unit_cfa_franc_bceao() -> URIRef:
    """Returns the URI for QUDT unit: Cfa Franc Bceao (http://qudt.org/vocab/unit/CCY_XOF)"""
    return QUDT_UNIT["CCY_XOF"]


def get_qudt_unit_palladium_one_troy_ounce() -> URIRef:
    """Returns the URI for QUDT unit: Palladium (one Troy Ounce) (http://qudt.org/vocab/unit/CCY_XPD)"""
    return QUDT_UNIT["CCY_XPD"]


def get_qudt_unit_cfp_franc() -> URIRef:
    """Returns the URI for QUDT unit: Cfp Franc (http://qudt.org/vocab/unit/CCY_XPF)"""
    return QUDT_UNIT["CCY_XPF"]


def get_qudt_unit_platinum_one_troy_ounce() -> URIRef:
    """Returns the URI for QUDT unit: Platinum (one Troy Ounce) (http://qudt.org/vocab/unit/CCY_XPT)"""
    return QUDT_UNIT["CCY_XPT"]


def get_qudt_unit_yemeni_rial() -> URIRef:
    """Returns the URI for QUDT unit: Yemeni Rial (http://qudt.org/vocab/unit/CCY_YER)"""
    return QUDT_UNIT["CCY_YER"]


def get_qudt_unit_south_african_rand() -> URIRef:
    """Returns the URI for QUDT unit: South African Rand (http://qudt.org/vocab/unit/CCY_ZAR)"""
    return QUDT_UNIT["CCY_ZAR"]


def get_qudt_unit_zambian_kwacha() -> URIRef:
    """Returns the URI for QUDT unit: Zambian Kwacha (http://qudt.org/vocab/unit/CCY_ZMW)"""
    return QUDT_UNIT["CCY_ZMW"]


def get_qudt_unit_zimbabwe_dollar() -> URIRef:
    """Returns the URI for QUDT unit: Zimbabwe Dollar (http://qudt.org/vocab/unit/CCY_ZWL)"""
    return QUDT_UNIT["CCY_ZWL"]


def get_qudt_unit_degree_api() -> URIRef:
    """Returns the URI for QUDT unit: Degree Api (http://qudt.org/vocab/unit/DEGREE_API)"""
    return QUDT_UNIT["DEGREE_API"]


def get_qudt_unit_becquerel_second_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Becquerel Second per Cubic Metre (http://qudt.org/vocab/unit/BQ-SEC-PER-M3)"""
    return QUDT_UNIT["BQ-SEC-PER-M3"]


def get_qudt_unit_degree_balling() -> URIRef:
    """Returns the URI for QUDT unit: Degree Balling (http://qudt.org/vocab/unit/DEGREE_BALLING)"""
    return QUDT_UNIT["DEGREE_BALLING"]


def get_qudt_unit_degree_baume_origin_scale() -> URIRef:
    """Returns the URI for QUDT unit: Degree Baume (origin Scale) (http://qudt.org/vocab/unit/DEGREE_BAUME)"""
    return QUDT_UNIT["DEGREE_BAUME"]


def get_qudt_unit_degree_baume_us_heavy() -> URIRef:
    """Returns the URI for QUDT unit: Degree Baume (us Heavy) (http://qudt.org/vocab/unit/DEGREE_BAUME_US_HEAVY)"""
    return QUDT_UNIT["DEGREE_BAUME_US_HEAVY"]


def get_qudt_unit_degree_baume_us_light() -> URIRef:
    """Returns the URI for QUDT unit: Degree Baume (us Light) (http://qudt.org/vocab/unit/DEGREE_BAUME_US_LIGHT)"""
    return QUDT_UNIT["DEGREE_BAUME_US_LIGHT"]


def get_qudt_unit_degree_brix() -> URIRef:
    """Returns the URI for QUDT unit: Degree Brix (http://qudt.org/vocab/unit/DEGREE_BRIX)"""
    return QUDT_UNIT["DEGREE_BRIX"]


def get_qudt_unit_degree_oechsle() -> URIRef:
    """Returns the URI for QUDT unit: Degree Oechsle (http://qudt.org/vocab/unit/DEGREE_OECHSLE)"""
    return QUDT_UNIT["DEGREE_OECHSLE"]


def get_qudt_unit_degree_plato() -> URIRef:
    """Returns the URI for QUDT unit: Degree Plato (http://qudt.org/vocab/unit/DEGREE_PLATO)"""
    return QUDT_UNIT["DEGREE_PLATO"]


def get_qudt_unit_degree_twaddell() -> URIRef:
    """Returns the URI for QUDT unit: Degree Twaddell (http://qudt.org/vocab/unit/DEGREE_TWADDELL)"""
    return QUDT_UNIT["DEGREE_TWADDELL"]


def get_qudt_unit_femtogram_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: Femtogram per Litre (http://qudt.org/vocab/unit/FemtoGM-PER-L)"""
    return QUDT_UNIT["FEMTOGM-PER-L"]


def get_qudt_unit_gram_per_cubic_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Cubic Centimetre (http://qudt.org/vocab/unit/GM-PER-CentiM3)"""
    return QUDT_UNIT["GM-PER-CENTIM3"]


def get_qudt_unit_gram_per_decilitre() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Decilitre (http://qudt.org/vocab/unit/GM-PER-DeciL)"""
    return QUDT_UNIT["GM-PER-DECIL"]


def get_qudt_unit_gram_per_cubic_decimetre() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Cubic Decimetre (http://qudt.org/vocab/unit/GM-PER-DeciM3)"""
    return QUDT_UNIT["GM-PER-DECIM3"]


def get_qudt_unit_gram_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Litre (http://qudt.org/vocab/unit/GM-PER-L)"""
    return QUDT_UNIT["GM-PER-L"]


def get_qudt_unit_gram_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Cubic Metre (http://qudt.org/vocab/unit/GM-PER-M3)"""
    return QUDT_UNIT["GM-PER-M3"]


def get_qudt_unit_gram_per_millilitre() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Millilitre (http://qudt.org/vocab/unit/GM-PER-MilliL)"""
    return QUDT_UNIT["GM-PER-MILLIL"]


def get_qudt_unit_grain_per_imperial_gallon() -> URIRef:
    """Returns the URI for QUDT unit: Grain per Imperial Gallon (http://qudt.org/vocab/unit/GRAIN-PER-GAL_IMP)"""
    return QUDT_UNIT["GRAIN-PER-GAL_IMP"]


def get_qudt_unit_grain_per_us_gallon() -> URIRef:
    """Returns the URI for QUDT unit: Grain per Us Gallon (http://qudt.org/vocab/unit/GRAIN-PER-GAL_US)"""
    return QUDT_UNIT["GRAIN-PER-GAL_US"]


def get_qudt_unit_grain_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Grain per Cubic Metre (http://qudt.org/vocab/unit/GRAIN-PER-M3)"""
    return QUDT_UNIT["GRAIN-PER-M3"]


def get_qudt_unit_kilogram_per_cubic_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Cubic Centimetre (http://qudt.org/vocab/unit/KiloGM-PER-CentiM3)"""
    return QUDT_UNIT["KILOGM-PER-CENTIM3"]


def get_qudt_unit_kilogram_per_cubic_decimetre() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Cubic Decimetre (http://qudt.org/vocab/unit/KiloGM-PER-DeciM3)"""
    return QUDT_UNIT["KILOGM-PER-DECIM3"]


def get_qudt_unit_kilogram_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Litre (http://qudt.org/vocab/unit/KiloGM-PER-L)"""
    return QUDT_UNIT["KILOGM-PER-L"]


def get_qudt_unit_kilogram_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Cubic Metre (http://qudt.org/vocab/unit/KiloGM-PER-M3)"""
    return QUDT_UNIT["KILOGM-PER-M3"]


def get_qudt_unit_pound_mass_per_cubic_foot() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Cubic Foot (http://qudt.org/vocab/unit/LB-PER-FT3)"""
    return QUDT_UNIT["LB-PER-FT3"]


def get_qudt_unit_pound_mass_per_imperial_gallon() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Imperial Gallon (http://qudt.org/vocab/unit/LB-PER-GAL_IMP)"""
    return QUDT_UNIT["LB-PER-GAL_IMP"]


def get_qudt_unit_pound_mass_per_gallon_uk() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Gallon (UK) (http://qudt.org/vocab/unit/LB-PER-GAL_UK)"""
    return QUDT_UNIT["LB-PER-GAL_UK"]


def get_qudt_unit_pound_mass_per_us_gallon() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Us Gallon (http://qudt.org/vocab/unit/LB-PER-GAL_US)"""
    return QUDT_UNIT["LB-PER-GAL_US"]


def get_qudt_unit_pound_mass_per_cubic_inch() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Cubic Inch (http://qudt.org/vocab/unit/LB-PER-IN3)"""
    return QUDT_UNIT["LB-PER-IN3"]


def get_qudt_unit_pound_mass_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Cubic Metre (http://qudt.org/vocab/unit/LB-PER-M3)"""
    return QUDT_UNIT["LB-PER-M3"]


def get_qudt_unit_pound_mass_per_cubic_yard() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Cubic Yard (http://qudt.org/vocab/unit/LB-PER-YD3)"""
    return QUDT_UNIT["LB-PER-YD3"]


def get_qudt_unit_megagram_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Megagram per Cubic Metre (http://qudt.org/vocab/unit/MegaGM-PER-M3)"""
    return QUDT_UNIT["MEGAGM-PER-M3"]


def get_qudt_unit_microgram_per_decilitre() -> URIRef:
    """Returns the URI for QUDT unit: Microgram per Decilitre (http://qudt.org/vocab/unit/MicroGM-PER-DeciL)"""
    return QUDT_UNIT["MICROGM-PER-DECIL"]


def get_qudt_unit_microgram_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: Microgram per Litre (http://qudt.org/vocab/unit/MicroGM-PER-L)"""
    return QUDT_UNIT["MICROGM-PER-L"]


def get_qudt_unit_microgram_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Microgram per Cubic Metre (http://qudt.org/vocab/unit/MicroGM-PER-M3)"""
    return QUDT_UNIT["MICROGM-PER-M3"]


def get_qudt_unit_microgram_per_millilitre() -> URIRef:
    """Returns the URI for QUDT unit: Microgram per Millilitre (http://qudt.org/vocab/unit/MicroGM-PER-MilliL)"""
    return QUDT_UNIT["MICROGM-PER-MILLIL"]


def get_qudt_unit_milligram_per_decilitre() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Decilitre (http://qudt.org/vocab/unit/MilliGM-PER-DeciL)"""
    return QUDT_UNIT["MILLIGM-PER-DECIL"]


def get_qudt_unit_milligram_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Litre (http://qudt.org/vocab/unit/MilliGM-PER-L)"""
    return QUDT_UNIT["MILLIGM-PER-L"]


def get_qudt_unit_milligram_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Cubic Metre (http://qudt.org/vocab/unit/MilliGM-PER-M3)"""
    return QUDT_UNIT["MILLIGM-PER-M3"]


def get_qudt_unit_milligram_per_millilitre() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Millilitre (http://qudt.org/vocab/unit/MilliGM-PER-MilliL)"""
    return QUDT_UNIT["MILLIGM-PER-MILLIL"]


def get_qudt_unit_nanogram_per_decilitre() -> URIRef:
    """Returns the URI for QUDT unit: Nanogram per Decilitre (http://qudt.org/vocab/unit/NanoGM-PER-DeciL)"""
    return QUDT_UNIT["NANOGM-PER-DECIL"]


def get_qudt_unit_nanogram_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: Nanogram per Litre (http://qudt.org/vocab/unit/NanoGM-PER-L)"""
    return QUDT_UNIT["NANOGM-PER-L"]


def get_qudt_unit_nanogram_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Nanogram per Cubic Metre (http://qudt.org/vocab/unit/NanoGM-PER-M3)"""
    return QUDT_UNIT["NANOGM-PER-M3"]


def get_qudt_unit_nanogram_per_microlitre() -> URIRef:
    """Returns the URI for QUDT unit: Nanogram per Microlitre (http://qudt.org/vocab/unit/NanoGM-PER-MicroL)"""
    return QUDT_UNIT["NANOGM-PER-MICROL"]


def get_qudt_unit_nanogram_per_millilitre() -> URIRef:
    """Returns the URI for QUDT unit: Nanogram per Millilitre (http://qudt.org/vocab/unit/NanoGM-PER-MilliL)"""
    return QUDT_UNIT["NANOGM-PER-MILLIL"]


def get_qudt_unit_ounce_mass_per_imperial_gallon() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass per Imperial Gallon (http://qudt.org/vocab/unit/OZ-PER-GAL_IMP)"""
    return QUDT_UNIT["OZ-PER-GAL_IMP"]


def get_qudt_unit_ounce_mass_per_gallon_uk() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass per Gallon (UK) (http://qudt.org/vocab/unit/OZ-PER-GAL_UK)"""
    return QUDT_UNIT["OZ-PER-GAL_UK"]


def get_qudt_unit_ounce_mass_per_us_gallon() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass per Us Gallon (http://qudt.org/vocab/unit/OZ-PER-GAL_US)"""
    return QUDT_UNIT["OZ-PER-GAL_US"]


def get_qudt_unit_ounce_mass_per_cubic_inch() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass per Cubic Inch (http://qudt.org/vocab/unit/OZ-PER-IN3)"""
    return QUDT_UNIT["OZ-PER-IN3"]


def get_qudt_unit_ounce_mass_per_cubic_yard() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass per Cubic Yard (http://qudt.org/vocab/unit/OZ-PER-YD3)"""
    return QUDT_UNIT["OZ-PER-YD3"]


def get_qudt_unit_picogram_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: Picogram per Litre (http://qudt.org/vocab/unit/PicoGM-PER-L)"""
    return QUDT_UNIT["PICOGM-PER-L"]


def get_qudt_unit_picogram_per_millilitre() -> URIRef:
    """Returns the URI for QUDT unit: Picogram per Millilitre (http://qudt.org/vocab/unit/PicoGM-PER-MilliL)"""
    return QUDT_UNIT["PICOGM-PER-MILLIL"]


def get_qudt_unit_planck_density() -> URIRef:
    """Returns the URI for QUDT unit: Planck Density (http://qudt.org/vocab/unit/PlanckDensity)"""
    return QUDT_UNIT["PLANCKDENSITY"]


def get_qudt_unit_slug_per_cubic_foot() -> URIRef:
    """Returns the URI for QUDT unit: Slug per Cubic Foot (http://qudt.org/vocab/unit/SLUG-PER-FT3)"""
    return QUDT_UNIT["SLUG-PER-FT3"]


def get_qudt_unit_tonne_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Tonne per Cubic Metre (http://qudt.org/vocab/unit/TONNE-PER-M3)"""
    return QUDT_UNIT["TONNE-PER-M3"]


def get_qudt_unit_long_ton_per_cubic_yard() -> URIRef:
    """Returns the URI for QUDT unit: Long Ton per Cubic Yard (http://qudt.org/vocab/unit/TON_LONG-PER-YD3)"""
    return QUDT_UNIT["TON_LONG-PER-YD3"]


def get_qudt_unit_metric_ton_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Metric Ton per Cubic Metre (http://qudt.org/vocab/unit/TON_Metric-PER-M3)"""
    return QUDT_UNIT["TON_METRIC-PER-M3"]


def get_qudt_unit_short_ton_per_cubic_yard() -> URIRef:
    """Returns the URI for QUDT unit: Short Ton per Cubic Yard (http://qudt.org/vocab/unit/TON_SHORT-PER-YD3)"""
    return QUDT_UNIT["TON_SHORT-PER-YD3"]


def get_qudt_unit_ton_uk_per_cubic_yard() -> URIRef:
    """Returns the URI for QUDT unit: Ton (UK) per Cubic Yard (http://qudt.org/vocab/unit/TON_UK-PER-YD3)"""
    return QUDT_UNIT["TON_UK-PER-YD3"]


def get_qudt_unit_ton_us_per_cubic_yard() -> URIRef:
    """Returns the URI for QUDT unit: Ton (US) per Cubic Yard (http://qudt.org/vocab/unit/TON_US-PER-YD3)"""
    return QUDT_UNIT["TON_US-PER-YD3"]


def get_qudt_unit_angstrom() -> URIRef:
    """Returns the URI for QUDT unit: Angstrom (http://qudt.org/vocab/unit/ANGSTROM)"""
    return QUDT_UNIT["ANGSTROM"]


def get_qudt_unit_astronomical_unit() -> URIRef:
    """Returns the URI for QUDT unit: Astronomical-unit (http://qudt.org/vocab/unit/AU)"""
    return QUDT_UNIT["AU"]


def get_qudt_unit_british_thermal_unit_international_definition_per_pound_force() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) per Pound Force (http://qudt.org/vocab/unit/BTU_IT-PER-LB_F)"""
    return QUDT_UNIT["BTU_IT-PER-LB_F"]


def get_qudt_unit_chain() -> URIRef:
    """Returns the URI for QUDT unit: Chain (http://qudt.org/vocab/unit/CH)"""
    return QUDT_UNIT["CH"]


def get_qudt_unit_chain_based_on_u_s_survey_foot() -> URIRef:
    """Returns the URI for QUDT unit: Chain (based on U.s. Survey Foot) (http://qudt.org/vocab/unit/CHAIN_US)"""
    return QUDT_UNIT["CHAIN_US"]


def get_qudt_unit_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Centimetre (http://qudt.org/vocab/unit/CentiM)"""
    return QUDT_UNIT["CENTIM"]


def get_qudt_unit_decametre() -> URIRef:
    """Returns the URI for QUDT unit: Decametre (http://qudt.org/vocab/unit/DecaM)"""
    return QUDT_UNIT["DECAM"]


def get_qudt_unit_decimetre() -> URIRef:
    """Returns the URI for QUDT unit: Decimetre (http://qudt.org/vocab/unit/DeciM)"""
    return QUDT_UNIT["DECIM"]


def get_qudt_unit_fathom() -> URIRef:
    """Returns the URI for QUDT unit: Fathom (http://qudt.org/vocab/unit/FATH)"""
    return QUDT_UNIT["FATH"]


def get_qudt_unit_fermi() -> URIRef:
    """Returns the URI for QUDT unit: Fermi (http://qudt.org/vocab/unit/FM)"""
    return QUDT_UNIT["FM"]


def get_qudt_unit_foot() -> URIRef:
    """Returns the URI for QUDT unit: Foot (http://qudt.org/vocab/unit/FT)"""
    return QUDT_UNIT["FT"]


def get_qudt_unit_us_survey_foot() -> URIRef:
    """Returns the URI for QUDT unit: Us Survey Foot (http://qudt.org/vocab/unit/FT_US)"""
    return QUDT_UNIT["FT_US"]


def get_qudt_unit_furlong() -> URIRef:
    """Returns the URI for QUDT unit: Furlong (http://qudt.org/vocab/unit/FUR)"""
    return QUDT_UNIT["FUR"]


def get_qudt_unit_femtometre() -> URIRef:
    """Returns the URI for QUDT unit: Femtometre (http://qudt.org/vocab/unit/FemtoM)"""
    return QUDT_UNIT["FEMTOM"]


def get_qudt_unit_french_gauge() -> URIRef:
    """Returns the URI for QUDT unit: French Gauge (http://qudt.org/vocab/unit/GAUGE_FR)"""
    return QUDT_UNIT["GAUGE_FR"]


def get_qudt_unit_charrière_gauge() -> URIRef:
    """Returns the URI for QUDT unit: Charrière Gauge (http://qudt.org/vocab/unit/GA_Charriere)"""
    return QUDT_UNIT["GA_CHARRIERE"]


def get_qudt_unit_hectometre() -> URIRef:
    """Returns the URI for QUDT unit: Hectometre (http://qudt.org/vocab/unit/HectoM)"""
    return QUDT_UNIT["HECTOM"]


def get_qudt_unit_inch() -> URIRef:
    """Returns the URI for QUDT unit: Inch (http://qudt.org/vocab/unit/IN)"""
    return QUDT_UNIT["IN"]


def get_qudt_unit_kilometre() -> URIRef:
    """Returns the URI for QUDT unit: Kilometre (http://qudt.org/vocab/unit/KiloM)"""
    return QUDT_UNIT["KILOM"]


def get_qudt_unit_light_year() -> URIRef:
    """Returns the URI for QUDT unit: Light Year (http://qudt.org/vocab/unit/LY)"""
    return QUDT_UNIT["LY"]


def get_qudt_unit_international_mile() -> URIRef:
    """Returns the URI for QUDT unit: International Mile (http://qudt.org/vocab/unit/MI)"""
    return QUDT_UNIT["MI"]


def get_qudt_unit_nautical_mile() -> URIRef:
    """Returns the URI for QUDT unit: Nautical Mile (http://qudt.org/vocab/unit/MI_N)"""
    return QUDT_UNIT["MI_N"]


def get_qudt_unit_imperial_mile() -> URIRef:
    """Returns the URI for QUDT unit: Imperial Mile (http://qudt.org/vocab/unit/MI_UK)"""
    return QUDT_UNIT["MI_UK"]


def get_qudt_unit_us_survey_mile() -> URIRef:
    """Returns the URI for QUDT unit: Us Survey Mile (http://qudt.org/vocab/unit/MI_US)"""
    return QUDT_UNIT["MI_US"]


def get_qudt_unit_microinch() -> URIRef:
    """Returns the URI for QUDT unit: Microinch (http://qudt.org/vocab/unit/MicroIN)"""
    return QUDT_UNIT["MICROIN"]


def get_qudt_unit_micrometre() -> URIRef:
    """Returns the URI for QUDT unit: Micrometre (http://qudt.org/vocab/unit/MicroM)"""
    return QUDT_UNIT["MICROM"]


def get_qudt_unit_mil_length() -> URIRef:
    """Returns the URI for QUDT unit: Mil Length (http://qudt.org/vocab/unit/MilLength)"""
    return QUDT_UNIT["MILLENGTH"]


def get_qudt_unit_milliinch() -> URIRef:
    """Returns the URI for QUDT unit: Milliinch (http://qudt.org/vocab/unit/MilliIN)"""
    return QUDT_UNIT["MILLIIN"]


def get_qudt_unit_millimetre() -> URIRef:
    """Returns the URI for QUDT unit: Millimetre (http://qudt.org/vocab/unit/MilliM)"""
    return QUDT_UNIT["MILLIM"]


def get_qudt_unit_nanometre() -> URIRef:
    """Returns the URI for QUDT unit: Nanometre (http://qudt.org/vocab/unit/NanoM)"""
    return QUDT_UNIT["NANOM"]


def get_qudt_unit_parsec() -> URIRef:
    """Returns the URI for QUDT unit: Parsec (http://qudt.org/vocab/unit/PARSEC)"""
    return QUDT_UNIT["PARSEC"]


def get_qudt_unit_pica() -> URIRef:
    """Returns the URI for QUDT unit: Pica (http://qudt.org/vocab/unit/PCA)"""
    return QUDT_UNIT["PCA"]


def get_qudt_unit_point() -> URIRef:
    """Returns the URI for QUDT unit: Point (http://qudt.org/vocab/unit/PT)"""
    return QUDT_UNIT["PT"]


def get_qudt_unit_picometre() -> URIRef:
    """Returns the URI for QUDT unit: Picometre (http://qudt.org/vocab/unit/PicoM)"""
    return QUDT_UNIT["PICOM"]


def get_qudt_unit_planck_length() -> URIRef:
    """Returns the URI for QUDT unit: Planck Length (http://qudt.org/vocab/unit/PlanckLength)"""
    return QUDT_UNIT["PLANCKLENGTH"]


def get_qudt_unit_rod() -> URIRef:
    """Returns the URI for QUDT unit: Rod (http://qudt.org/vocab/unit/ROD)"""
    return QUDT_UNIT["ROD"]


def get_qudt_unit_yard() -> URIRef:
    """Returns the URI for QUDT unit: Yard (http://qudt.org/vocab/unit/YD)"""
    return QUDT_UNIT["YD"]


def get_qudt_unit_centigray() -> URIRef:
    """Returns the URI for QUDT unit: Centigray (http://qudt.org/vocab/unit/CentiGRAY)"""
    return QUDT_UNIT["CENTIGRAY"]


def get_qudt_unit_gray() -> URIRef:
    """Returns the URI for QUDT unit: Gray (http://qudt.org/vocab/unit/GRAY)"""
    return QUDT_UNIT["GRAY"]


def get_qudt_unit_kilogray() -> URIRef:
    """Returns the URI for QUDT unit: Kilogray (http://qudt.org/vocab/unit/KiloGRAY)"""
    return QUDT_UNIT["KILOGRAY"]


def get_qudt_unit_megagray() -> URIRef:
    """Returns the URI for QUDT unit: Megagray (http://qudt.org/vocab/unit/MegaGRAY)"""
    return QUDT_UNIT["MEGAGRAY"]


def get_qudt_unit_microgray() -> URIRef:
    """Returns the URI for QUDT unit: Microgray (http://qudt.org/vocab/unit/MicroGRAY)"""
    return QUDT_UNIT["MICROGRAY"]


def get_qudt_unit_milligray() -> URIRef:
    """Returns the URI for QUDT unit: Milligray (http://qudt.org/vocab/unit/MilliGRAY)"""
    return QUDT_UNIT["MILLIGRAY"]


def get_qudt_unit_millirad() -> URIRef:
    """Returns the URI for QUDT unit: Millirad (http://qudt.org/vocab/unit/MilliRAD_R)"""
    return QUDT_UNIT["MILLIRAD_R"]


def get_qudt_unit_nanogray() -> URIRef:
    """Returns the URI for QUDT unit: Nanogray (http://qudt.org/vocab/unit/NanoGRAY)"""
    return QUDT_UNIT["NANOGRAY"]


def get_qudt_unit_rad() -> URIRef:
    """Returns the URI for QUDT unit: Rad (http://qudt.org/vocab/unit/RAD_R)"""
    return QUDT_UNIT["RAD_R"]


def get_qudt_unit_erg_per_gram_second() -> URIRef:
    """Returns the URI for QUDT unit: Erg per Gram Second (http://qudt.org/vocab/unit/ERG-PER-GM-SEC)"""
    return QUDT_UNIT["ERG-PER-GM-SEC"]


def get_qudt_unit_gray_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Gray per Hour (http://qudt.org/vocab/unit/GRAY-PER-HR)"""
    return QUDT_UNIT["GRAY-PER-HR"]


def get_qudt_unit_gray_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Gray per Minute (http://qudt.org/vocab/unit/GRAY-PER-MIN)"""
    return QUDT_UNIT["GRAY-PER-MIN"]


def get_qudt_unit_gray_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Gray per Second (http://qudt.org/vocab/unit/GRAY-PER-SEC)"""
    return QUDT_UNIT["GRAY-PER-SEC"]


def get_qudt_unit_microgray_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Microgray per Hour (http://qudt.org/vocab/unit/MicroGRAY-PER-HR)"""
    return QUDT_UNIT["MICROGRAY-PER-HR"]


def get_qudt_unit_microgray_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Microgray per Minute (http://qudt.org/vocab/unit/MicroGRAY-PER-MIN)"""
    return QUDT_UNIT["MICROGRAY-PER-MIN"]


def get_qudt_unit_microgray_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Microgray per Second (http://qudt.org/vocab/unit/MicroGRAY-PER-SEC)"""
    return QUDT_UNIT["MICROGRAY-PER-SEC"]


def get_qudt_unit_microsievert_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Microsievert per Hour (http://qudt.org/vocab/unit/MicroSV-PER-HR)"""
    return QUDT_UNIT["MICROSV-PER-HR"]


def get_qudt_unit_microsievert_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Microsievert per Minute (http://qudt.org/vocab/unit/MicroSV-PER-MIN)"""
    return QUDT_UNIT["MICROSV-PER-MIN"]


def get_qudt_unit_microsievert_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Microsievert per Second (http://qudt.org/vocab/unit/MicroSV-PER-SEC)"""
    return QUDT_UNIT["MICROSV-PER-SEC"]


def get_qudt_unit_milligray_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Milligray per Hour (http://qudt.org/vocab/unit/MilliGRAY-PER-HR)"""
    return QUDT_UNIT["MILLIGRAY-PER-HR"]


def get_qudt_unit_milligray_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Milligray per Minute (http://qudt.org/vocab/unit/MilliGRAY-PER-MIN)"""
    return QUDT_UNIT["MILLIGRAY-PER-MIN"]


def get_qudt_unit_milligray_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Milligray per Second (http://qudt.org/vocab/unit/MilliGRAY-PER-SEC)"""
    return QUDT_UNIT["MILLIGRAY-PER-SEC"]


def get_qudt_unit_millirad_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Millirad per Hour (http://qudt.org/vocab/unit/MilliRAD_R-PER-HR)"""
    return QUDT_UNIT["MILLIRAD_R-PER-HR"]


def get_qudt_unit_millisievert_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Millisievert per Hour (http://qudt.org/vocab/unit/MilliSV-PER-HR)"""
    return QUDT_UNIT["MILLISV-PER-HR"]


def get_qudt_unit_millisievert_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Millisievert per Minute (http://qudt.org/vocab/unit/MilliSV-PER-MIN)"""
    return QUDT_UNIT["MILLISV-PER-MIN"]


def get_qudt_unit_millisievert_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Millisievert per Second (http://qudt.org/vocab/unit/MilliSV-PER-SEC)"""
    return QUDT_UNIT["MILLISV-PER-SEC"]


def get_qudt_unit_milliwatt_per_milligram() -> URIRef:
    """Returns the URI for QUDT unit: Milliwatt per Milligram (http://qudt.org/vocab/unit/MilliW-PER-MilliGM)"""
    return QUDT_UNIT["MILLIW-PER-MILLIGM"]


def get_qudt_unit_nanogray_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Nanogray per Hour (http://qudt.org/vocab/unit/NanoGRAY-PER-HR)"""
    return QUDT_UNIT["NANOGRAY-PER-HR"]


def get_qudt_unit_nanogray_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Nanogray per Minute (http://qudt.org/vocab/unit/NanoGRAY-PER-MIN)"""
    return QUDT_UNIT["NANOGRAY-PER-MIN"]


def get_qudt_unit_nanogray_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Nanogray per Second (http://qudt.org/vocab/unit/NanoGRAY-PER-SEC)"""
    return QUDT_UNIT["NANOGRAY-PER-SEC"]


def get_qudt_unit_nanosievert_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Nanosievert per Hour (http://qudt.org/vocab/unit/NanoSV-PER-HR)"""
    return QUDT_UNIT["NANOSV-PER-HR"]


def get_qudt_unit_nanosievert_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Nanosievert per Minute (http://qudt.org/vocab/unit/NanoSV-PER-MIN)"""
    return QUDT_UNIT["NANOSV-PER-MIN"]


def get_qudt_unit_nanosievert_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Nanosievert per Second (http://qudt.org/vocab/unit/NanoSV-PER-SEC)"""
    return QUDT_UNIT["NANOSV-PER-SEC"]


def get_qudt_unit_rem_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Rem per Second (http://qudt.org/vocab/unit/REM-PER-SEC)"""
    return QUDT_UNIT["REM-PER-SEC"]


def get_qudt_unit_sievert_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Sievert per Hour (http://qudt.org/vocab/unit/SV-PER-HR)"""
    return QUDT_UNIT["SV-PER-HR"]


def get_qudt_unit_sievert_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Sievert per Minute (http://qudt.org/vocab/unit/SV-PER-MIN)"""
    return QUDT_UNIT["SV-PER-MIN"]


def get_qudt_unit_sievert_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Sievert per Second (http://qudt.org/vocab/unit/SV-PER-SEC)"""
    return QUDT_UNIT["SV-PER-SEC"]


def get_qudt_unit_watt_per_gram() -> URIRef:
    """Returns the URI for QUDT unit: Watt per Gram (http://qudt.org/vocab/unit/W-PER-GM)"""
    return QUDT_UNIT["W-PER-GM"]


def get_qudt_unit_watt_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Watt per Kilogram (http://qudt.org/vocab/unit/W-PER-KiloGM)"""
    return QUDT_UNIT["W-PER-KILOGM"]


def get_qudt_unit_centimetre_per_square_second() -> URIRef:
    """Returns the URI for QUDT unit: Centimetre per Square Second (http://qudt.org/vocab/unit/CentiM-PER-SEC2)"""
    return QUDT_UNIT["CENTIM-PER-SEC2"]


def get_qudt_unit_foot_per_square_second() -> URIRef:
    """Returns the URI for QUDT unit: Foot per Square Second (http://qudt.org/vocab/unit/FT-PER-SEC2)"""
    return QUDT_UNIT["FT-PER-SEC2"]


def get_qudt_unit_gravity() -> URIRef:
    """Returns the URI for QUDT unit: Gravity (http://qudt.org/vocab/unit/G)"""
    return QUDT_UNIT["G"]


def get_qudt_unit_galileo() -> URIRef:
    """Returns the URI for QUDT unit: Galileo (http://qudt.org/vocab/unit/GALILEO)"""
    return QUDT_UNIT["GALILEO"]


def get_qudt_unit_inch_per_square_second() -> URIRef:
    """Returns the URI for QUDT unit: Inch per Square Second (http://qudt.org/vocab/unit/IN-PER-SEC2)"""
    return QUDT_UNIT["IN-PER-SEC2"]


def get_qudt_unit_knot_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Knot per Second (http://qudt.org/vocab/unit/KN-PER-SEC)"""
    return QUDT_UNIT["KN-PER-SEC"]


def get_qudt_unit_kilometre_per_square_second() -> URIRef:
    """Returns the URI for QUDT unit: Kilometre per Square Second (http://qudt.org/vocab/unit/KiloM-PER-SEC2)"""
    return QUDT_UNIT["KILOM-PER-SEC2"]


def get_qudt_unit_kilopascal_square_metre_per_gram() -> URIRef:
    """Returns the URI for QUDT unit: Kilopascal Square Metre per Gram (http://qudt.org/vocab/unit/KiloPA-M2-PER-GM)"""
    return QUDT_UNIT["KILOPA-M2-PER-GM"]


def get_qudt_unit_us_survey_mile_per_square_second() -> URIRef:
    """Returns the URI for QUDT unit: Us Survey Mile per Square Second (http://qudt.org/vocab/unit/MI_US-PER-SEC2)"""
    return QUDT_UNIT["MI_US-PER-SEC2"]


def get_qudt_unit_microgravity() -> URIRef:
    """Returns the URI for QUDT unit: Microgravity (http://qudt.org/vocab/unit/MicroG)"""
    return QUDT_UNIT["MICROG"]


def get_qudt_unit_microgalileo() -> URIRef:
    """Returns the URI for QUDT unit: Microgalileo (http://qudt.org/vocab/unit/MicroGALILEO)"""
    return QUDT_UNIT["MICROGALILEO"]


def get_qudt_unit_micrometre_per_square_second() -> URIRef:
    """Returns the URI for QUDT unit: Micrometre per Square Second (http://qudt.org/vocab/unit/MicroM-PER-SEC2)"""
    return QUDT_UNIT["MICROM-PER-SEC2"]


def get_qudt_unit_milligravity() -> URIRef:
    """Returns the URI for QUDT unit: Milligravity (http://qudt.org/vocab/unit/MilliG)"""
    return QUDT_UNIT["MILLIG"]


def get_qudt_unit_milligalileo() -> URIRef:
    """Returns the URI for QUDT unit: Milligalileo (http://qudt.org/vocab/unit/MilliGALILEO)"""
    return QUDT_UNIT["MILLIGALILEO"]


def get_qudt_unit_millimetre_per_square_second() -> URIRef:
    """Returns the URI for QUDT unit: Millimetre per Square Second (http://qudt.org/vocab/unit/MilliM-PER-SEC2)"""
    return QUDT_UNIT["MILLIM-PER-SEC2"]


def get_qudt_unit_yard_per_square_second() -> URIRef:
    """Returns the URI for QUDT unit: Yard per Square Second (http://qudt.org/vocab/unit/YD-PER-SEC2)"""
    return QUDT_UNIT["YD-PER-SEC2"]


def get_qudt_unit_number_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: Number per Litre (http://qudt.org/vocab/unit/NUM-PER-L)"""
    return QUDT_UNIT["NUM-PER-L"]


def get_qudt_unit_number_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Number per Cubic Metre (http://qudt.org/vocab/unit/NUM-PER-M3)"""
    return QUDT_UNIT["NUM-PER-M3"]


def get_qudt_unit_number_per_microlitre() -> URIRef:
    """Returns the URI for QUDT unit: Number per Microlitre (http://qudt.org/vocab/unit/NUM-PER-MicroL)"""
    return QUDT_UNIT["NUM-PER-MICROL"]


def get_qudt_unit_number_per_millilitre() -> URIRef:
    """Returns the URI for QUDT unit: Number per Millilitre (http://qudt.org/vocab/unit/NUM-PER-MilliL)"""
    return QUDT_UNIT["NUM-PER-MILLIL"]


def get_qudt_unit_number_per_cubic_millimetre() -> URIRef:
    """Returns the URI for QUDT unit: Number per Cubic Millimetre (http://qudt.org/vocab/unit/NUM-PER-MilliM3)"""
    return QUDT_UNIT["NUM-PER-MILLIM3"]


def get_qudt_unit_number_per_nanolitre() -> URIRef:
    """Returns the URI for QUDT unit: Number per Nanolitre (http://qudt.org/vocab/unit/NUM-PER-NanoL)"""
    return QUDT_UNIT["NUM-PER-NANOL"]


def get_qudt_unit_number_per_picolitre() -> URIRef:
    """Returns the URI for QUDT unit: Number per Picolitre (http://qudt.org/vocab/unit/NUM-PER-PicoL)"""
    return QUDT_UNIT["NUM-PER-PICOL"]


def get_qudt_unit_attojoule() -> URIRef:
    """Returns the URI for QUDT unit: Attojoule (http://qudt.org/vocab/unit/AttoJ)"""
    return QUDT_UNIT["ATTOJ"]


def get_qudt_unit_british_thermal_unit_international_definition() -> URIRef:
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) (http://qudt.org/vocab/unit/BTU_IT)"""
    return QUDT_UNIT["BTU_IT"]


def get_qudt_unit_british_thermal_unit_thermochemical_definition() -> URIRef:
    """Returns the URI for QUDT unit: British Thermal Unit (thermochemical Definition) (http://qudt.org/vocab/unit/BTU_TH)"""
    return QUDT_UNIT["BTU_TH"]


def get_qudt_unit_international_table_calorie() -> URIRef:
    """Returns the URI for QUDT unit: International Table Calorie (http://qudt.org/vocab/unit/CAL_IT)"""
    return QUDT_UNIT["CAL_IT"]


def get_qudt_unit_thermochemical_calorie() -> URIRef:
    """Returns the URI for QUDT unit: Thermochemical Calorie (http://qudt.org/vocab/unit/CAL_TH)"""
    return QUDT_UNIT["CAL_TH"]


def get_qudt_unit_erg() -> URIRef:
    """Returns the URI for QUDT unit: Erg (http://qudt.org/vocab/unit/ERG)"""
    return QUDT_UNIT["ERG"]


def get_qudt_unit_exajoule() -> URIRef:
    """Returns the URI for QUDT unit: Exajoule (http://qudt.org/vocab/unit/ExaJ)"""
    return QUDT_UNIT["EXAJ"]


def get_qudt_unit_foot_pound_force() -> URIRef:
    """Returns the URI for QUDT unit: Foot Pound Force (http://qudt.org/vocab/unit/FT-LB_F)"""
    return QUDT_UNIT["FT-LB_F"]


def get_qudt_unit_foot_poundal() -> URIRef:
    """Returns the URI for QUDT unit: Foot Poundal (http://qudt.org/vocab/unit/FT-PDL)"""
    return QUDT_UNIT["FT-PDL"]


def get_qudt_unit_femtojoule() -> URIRef:
    """Returns the URI for QUDT unit: Femtojoule (http://qudt.org/vocab/unit/FemtoJ)"""
    return QUDT_UNIT["FEMTOJ"]


def get_qudt_unit_gigajoule() -> URIRef:
    """Returns the URI for QUDT unit: Gigajoule (http://qudt.org/vocab/unit/GigaJ)"""
    return QUDT_UNIT["GIGAJ"]


def get_qudt_unit_gigawatt_hour() -> URIRef:
    """Returns the URI for QUDT unit: Gigawatt Hour (http://qudt.org/vocab/unit/GigaW-HR)"""
    return QUDT_UNIT["GIGAW-HR"]


def get_qudt_unit_kilo_british_thermal_unit_international_definition() -> URIRef:
    """Returns the URI for QUDT unit: Kilo British Thermal Unit (international Definition) (http://qudt.org/vocab/unit/KiloBTU_IT)"""
    return QUDT_UNIT["KILOBTU_IT"]


def get_qudt_unit_kilo_british_thermal_unit_thermochemical_definition() -> URIRef:
    """Returns the URI for QUDT unit: Kilo British Thermal Unit (thermochemical Definition) (http://qudt.org/vocab/unit/KiloBTU_TH)"""
    return QUDT_UNIT["KILOBTU_TH"]


def get_qudt_unit_kilocalorie() -> URIRef:
    """Returns the URI for QUDT unit: Kilocalorie (http://qudt.org/vocab/unit/KiloCAL)"""
    return QUDT_UNIT["KILOCAL"]


def get_qudt_unit_kilo_electron_volt() -> URIRef:
    """Returns the URI for QUDT unit: Kilo Electron Volt (http://qudt.org/vocab/unit/KiloEV)"""
    return QUDT_UNIT["KILOEV"]


def get_qudt_unit_kilojoule() -> URIRef:
    """Returns the URI for QUDT unit: Kilojoule (http://qudt.org/vocab/unit/KiloJ)"""
    return QUDT_UNIT["KILOJ"]


def get_qudt_unit_kilo_volt_ampere_hour() -> URIRef:
    """Returns the URI for QUDT unit: Kilo Volt Ampere Hour (http://qudt.org/vocab/unit/KiloVA-HR)"""
    return QUDT_UNIT["KILOVA-HR"]


def get_qudt_unit_kilo_volt_ampere_reactive_hour() -> URIRef:
    """Returns the URI for QUDT unit: Kilo Volt Ampere Reactive Hour (http://qudt.org/vocab/unit/KiloVAR-HR)"""
    return QUDT_UNIT["KILOVAR-HR"]


def get_qudt_unit_kilowatt_hour() -> URIRef:
    """Returns the URI for QUDT unit: Kilowatt Hour (http://qudt.org/vocab/unit/KiloW-HR)"""
    return QUDT_UNIT["KILOW-HR"]


def get_qudt_unit_mega_british_thermal_unit_international_definition() -> URIRef:
    """Returns the URI for QUDT unit: Mega British Thermal Unit (international Definition) (http://qudt.org/vocab/unit/MegaBTU_IT)"""
    return QUDT_UNIT["MEGABTU_IT"]


def get_qudt_unit_megajoule() -> URIRef:
    """Returns the URI for QUDT unit: Megajoule (http://qudt.org/vocab/unit/MegaJ)"""
    return QUDT_UNIT["MEGAJ"]


def get_qudt_unit_mega_ton_of_oil_equivalent() -> URIRef:
    """Returns the URI for QUDT unit: Mega Ton of Oil Equivalent (http://qudt.org/vocab/unit/MegaTOE)"""
    return QUDT_UNIT["MEGATOE"]


def get_qudt_unit_mega_volt_ampere_hour() -> URIRef:
    """Returns the URI for QUDT unit: Mega Volt Ampere Hour (http://qudt.org/vocab/unit/MegaVA-HR)"""
    return QUDT_UNIT["MEGAVA-HR"]


def get_qudt_unit_mega_volt_ampere_reactive_hour() -> URIRef:
    """Returns the URI for QUDT unit: Mega Volt Ampere Reactive Hour (http://qudt.org/vocab/unit/MegaVAR-HR)"""
    return QUDT_UNIT["MEGAVAR-HR"]


def get_qudt_unit_megawatt_hour() -> URIRef:
    """Returns the URI for QUDT unit: Megawatt Hour (http://qudt.org/vocab/unit/MegaW-HR)"""
    return QUDT_UNIT["MEGAW-HR"]


def get_qudt_unit_microjoule() -> URIRef:
    """Returns the URI for QUDT unit: Microjoule (http://qudt.org/vocab/unit/MicroJ)"""
    return QUDT_UNIT["MICROJ"]


def get_qudt_unit_millijoule() -> URIRef:
    """Returns the URI for QUDT unit: Millijoule (http://qudt.org/vocab/unit/MilliJ)"""
    return QUDT_UNIT["MILLIJ"]


def get_qudt_unit_nanojoule() -> URIRef:
    """Returns the URI for QUDT unit: Nanojoule (http://qudt.org/vocab/unit/NanoJ)"""
    return QUDT_UNIT["NANOJ"]


def get_qudt_unit_petajoule() -> URIRef:
    """Returns the URI for QUDT unit: Petajoule (http://qudt.org/vocab/unit/PetaJ)"""
    return QUDT_UNIT["PETAJ"]


def get_qudt_unit_picojoule() -> URIRef:
    """Returns the URI for QUDT unit: Picojoule (http://qudt.org/vocab/unit/PicoJ)"""
    return QUDT_UNIT["PICOJ"]


def get_qudt_unit_planck_energy() -> URIRef:
    """Returns the URI for QUDT unit: Planck Energy (http://qudt.org/vocab/unit/PlanckEnergy)"""
    return QUDT_UNIT["PLANCKENERGY"]


def get_qudt_unit_quad() -> URIRef:
    """Returns the URI for QUDT unit: Quad (http://qudt.org/vocab/unit/QUAD)"""
    return QUDT_UNIT["QUAD"]


def get_qudt_unit_therm_ec() -> URIRef:
    """Returns the URI for QUDT unit: Therm (ec) (http://qudt.org/vocab/unit/THERM_EC)"""
    return QUDT_UNIT["THERM_EC"]


def get_qudt_unit_therm_u_s() -> URIRef:
    """Returns the URI for QUDT unit: Therm (u.s.) (http://qudt.org/vocab/unit/THERM_US)"""
    return QUDT_UNIT["THERM_US"]


def get_qudt_unit_thm_eec() -> URIRef:
    """Returns the URI for QUDT unit: Thm_eec (http://qudt.org/vocab/unit/THM_EEC)"""
    return QUDT_UNIT["THM_EEC"]


def get_qudt_unit_therm_us() -> URIRef:
    """Returns the URI for QUDT unit: Therm Us (http://qudt.org/vocab/unit/THM_US)"""
    return QUDT_UNIT["THM_US"]


def get_qudt_unit_ton_of_oil_equivalent() -> URIRef:
    """Returns the URI for QUDT unit: Ton of Oil Equivalent (http://qudt.org/vocab/unit/TOE)"""
    return QUDT_UNIT["TOE"]


def get_qudt_unit_terajoule() -> URIRef:
    """Returns the URI for QUDT unit: Terajoule (http://qudt.org/vocab/unit/TeraJ)"""
    return QUDT_UNIT["TERAJ"]


def get_qudt_unit_terawatt_hour() -> URIRef:
    """Returns the URI for QUDT unit: Terawatt Hour (http://qudt.org/vocab/unit/TeraW-HR)"""
    return QUDT_UNIT["TERAW-HR"]


def get_qudt_unit_ton_energy() -> URIRef:
    """Returns the URI for QUDT unit: Ton Energy (http://qudt.org/vocab/unit/TonEnergy)"""
    return QUDT_UNIT["TONENERGY"]


def get_qudt_unit_volt_ampere_hour() -> URIRef:
    """Returns the URI for QUDT unit: Volt Ampere Hour (http://qudt.org/vocab/unit/VA-HR)"""
    return QUDT_UNIT["VA-HR"]


def get_qudt_unit_volt_ampere_reactive_hour() -> URIRef:
    """Returns the URI for QUDT unit: Volt Ampere Reactive Hour (http://qudt.org/vocab/unit/VAR-HR)"""
    return QUDT_UNIT["VAR-HR"]


def get_qudt_unit_watt_hour() -> URIRef:
    """Returns the URI for QUDT unit: Watt Hour (http://qudt.org/vocab/unit/W-HR)"""
    return QUDT_UNIT["W-HR"]


def get_qudt_unit_watt_second() -> URIRef:
    """Returns the URI for QUDT unit: Watt Second (http://qudt.org/vocab/unit/W-SEC)"""
    return QUDT_UNIT["W-SEC"]


def get_qudt_unit_acidity() -> URIRef:
    """Returns the URI for QUDT unit: Acidity (http://qudt.org/vocab/unit/PH)"""
    return QUDT_UNIT["PH"]


def get_qudt_unit_pascal_second_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Pascal Second per Metre (http://qudt.org/vocab/unit/PA-SEC-PER-M)"""
    return QUDT_UNIT["PA-SEC-PER-M"]


def get_qudt_unit_attojoule_second() -> URIRef:
    """Returns the URI for QUDT unit: Attojoule Second (http://qudt.org/vocab/unit/AttoJ-SEC)"""
    return QUDT_UNIT["ATTOJ-SEC"]


def get_qudt_unit_attosecond() -> URIRef:
    """Returns the URI for QUDT unit: Attosecond (http://qudt.org/vocab/unit/AttoSEC)"""
    return QUDT_UNIT["ATTOSEC"]


def get_qudt_unit_centipoise_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Centipoise per Bar (http://qudt.org/vocab/unit/CentiPOISE-PER-BAR)"""
    return QUDT_UNIT["CENTIPOISE-PER-BAR"]


def get_qudt_unit_day() -> URIRef:
    """Returns the URI for QUDT unit: Day (http://qudt.org/vocab/unit/DAY)"""
    return QUDT_UNIT["DAY"]


def get_qudt_unit_sidereal_day() -> URIRef:
    """Returns the URI for QUDT unit: Sidereal Day (http://qudt.org/vocab/unit/DAY_Sidereal)"""
    return QUDT_UNIT["DAY_SIDEREAL"]


def get_qudt_unit_decisecond() -> URIRef:
    """Returns the URI for QUDT unit: Decisecond (http://qudt.org/vocab/unit/DeciSEC)"""
    return QUDT_UNIT["DECISEC"]


def get_qudt_unit_femtosecond() -> URIRef:
    """Returns the URI for QUDT unit: Femtosecond (http://qudt.org/vocab/unit/FemtoSEC)"""
    return QUDT_UNIT["FEMTOSEC"]


def get_qudt_unit_henry_per_kiloohm() -> URIRef:
    """Returns the URI for QUDT unit: Henry per Kiloohm (http://qudt.org/vocab/unit/H-PER-KiloOHM)"""
    return QUDT_UNIT["H-PER-KILOOHM"]


def get_qudt_unit_henry_per_ohm() -> URIRef:
    """Returns the URI for QUDT unit: Henry per Ohm (http://qudt.org/vocab/unit/H-PER-OHM)"""
    return QUDT_UNIT["H-PER-OHM"]


def get_qudt_unit_hour() -> URIRef:
    """Returns the URI for QUDT unit: Hour (http://qudt.org/vocab/unit/HR)"""
    return QUDT_UNIT["HR"]


def get_qudt_unit_sidereal_hour() -> URIRef:
    """Returns the URI for QUDT unit: Sidereal Hour (http://qudt.org/vocab/unit/HR_Sidereal)"""
    return QUDT_UNIT["HR_SIDEREAL"]


def get_qudt_unit_kilosecond() -> URIRef:
    """Returns the URI for QUDT unit: Kilosecond (http://qudt.org/vocab/unit/KiloSEC)"""
    return QUDT_UNIT["KILOSEC"]


def get_qudt_unit_kiloyear() -> URIRef:
    """Returns the URI for QUDT unit: Kiloyear (http://qudt.org/vocab/unit/KiloYR)"""
    return QUDT_UNIT["KILOYR"]


def get_qudt_unit_minute() -> URIRef:
    """Returns the URI for QUDT unit: Minute (http://qudt.org/vocab/unit/MIN)"""
    return QUDT_UNIT["MIN"]


def get_qudt_unit_sidereal_minute() -> URIRef:
    """Returns the URI for QUDT unit: Sidereal Minute (http://qudt.org/vocab/unit/MIN_Sidereal)"""
    return QUDT_UNIT["MIN_SIDEREAL"]


def get_qudt_unit_month() -> URIRef:
    """Returns the URI for QUDT unit: Month (http://qudt.org/vocab/unit/MO)"""
    return QUDT_UNIT["MO"]


def get_qudt_unit_mean_gregorian_month() -> URIRef:
    """Returns the URI for QUDT unit: Mean Gregorian Month (http://qudt.org/vocab/unit/MO_MeanGREGORIAN)"""
    return QUDT_UNIT["MO_MEANGREGORIAN"]


def get_qudt_unit_mean_julian_month() -> URIRef:
    """Returns the URI for QUDT unit: Mean Julian Month (http://qudt.org/vocab/unit/MO_MeanJulian)"""
    return QUDT_UNIT["MO_MEANJULIAN"]


def get_qudt_unit_synodic_month() -> URIRef:
    """Returns the URI for QUDT unit: Synodic Month (http://qudt.org/vocab/unit/MO_Synodic)"""
    return QUDT_UNIT["MO_SYNODIC"]


def get_qudt_unit_megasecond() -> URIRef:
    """Returns the URI for QUDT unit: Megasecond (http://qudt.org/vocab/unit/MegaSEC)"""
    return QUDT_UNIT["MEGASEC"]


def get_qudt_unit_megayear() -> URIRef:
    """Returns the URI for QUDT unit: Megayear (http://qudt.org/vocab/unit/MegaYR)"""
    return QUDT_UNIT["MEGAYR"]


def get_qudt_unit_microhenry_per_kiloohm() -> URIRef:
    """Returns the URI for QUDT unit: Microhenry per Kiloohm (http://qudt.org/vocab/unit/MicroH-PER-KiloOHM)"""
    return QUDT_UNIT["MICROH-PER-KILOOHM"]


def get_qudt_unit_microhenry_per_ohm() -> URIRef:
    """Returns the URI for QUDT unit: Microhenry per Ohm (http://qudt.org/vocab/unit/MicroH-PER-OHM)"""
    return QUDT_UNIT["MICROH-PER-OHM"]


def get_qudt_unit_microsecond() -> URIRef:
    """Returns the URI for QUDT unit: Microsecond (http://qudt.org/vocab/unit/MicroSEC)"""
    return QUDT_UNIT["MICROSEC"]


def get_qudt_unit_millihenry_per_kiloohm() -> URIRef:
    """Returns the URI for QUDT unit: Millihenry per Kiloohm (http://qudt.org/vocab/unit/MilliH-PER-KiloOHM)"""
    return QUDT_UNIT["MILLIH-PER-KILOOHM"]


def get_qudt_unit_millihenry_per_ohm() -> URIRef:
    """Returns the URI for QUDT unit: Millihenry per Ohm (http://qudt.org/vocab/unit/MilliH-PER-OHM)"""
    return QUDT_UNIT["MILLIH-PER-OHM"]


def get_qudt_unit_millipascal_second_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Millipascal Second per Bar (http://qudt.org/vocab/unit/MilliPA-SEC-PER-BAR)"""
    return QUDT_UNIT["MILLIPA-SEC-PER-BAR"]


def get_qudt_unit_millisecond() -> URIRef:
    """Returns the URI for QUDT unit: Millisecond (http://qudt.org/vocab/unit/MilliSEC)"""
    return QUDT_UNIT["MILLISEC"]


def get_qudt_unit_nanosecond() -> URIRef:
    """Returns the URI for QUDT unit: Nanosecond (http://qudt.org/vocab/unit/NanoSEC)"""
    return QUDT_UNIT["NANOSEC"]


def get_qudt_unit_pascal_second_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Pascal Second per Bar (http://qudt.org/vocab/unit/PA-SEC-PER-BAR)"""
    return QUDT_UNIT["PA-SEC-PER-BAR"]


def get_qudt_unit_poise_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Poise per Bar (http://qudt.org/vocab/unit/POISE-PER-BAR)"""
    return QUDT_UNIT["POISE-PER-BAR"]


def get_qudt_unit_poise_per_pascal() -> URIRef:
    """Returns the URI for QUDT unit: Poise per Pascal (http://qudt.org/vocab/unit/POISE-PER-PA)"""
    return QUDT_UNIT["POISE-PER-PA"]


def get_qudt_unit_picosecond() -> URIRef:
    """Returns the URI for QUDT unit: Picosecond (http://qudt.org/vocab/unit/PicoSEC)"""
    return QUDT_UNIT["PICOSEC"]


def get_qudt_unit_planck_time() -> URIRef:
    """Returns the URI for QUDT unit: Planck Time (http://qudt.org/vocab/unit/PlanckTime)"""
    return QUDT_UNIT["PLANCKTIME"]


def get_qudt_unit_shake() -> URIRef:
    """Returns the URI for QUDT unit: Shake (http://qudt.org/vocab/unit/SH)"""
    return QUDT_UNIT["SH"]


def get_qudt_unit_week() -> URIRef:
    """Returns the URI for QUDT unit: Week (http://qudt.org/vocab/unit/WK)"""
    return QUDT_UNIT["WK"]


def get_qudt_unit_year() -> URIRef:
    """Returns the URI for QUDT unit: Year (http://qudt.org/vocab/unit/YR)"""
    return QUDT_UNIT["YR"]


def get_qudt_unit_common_year() -> URIRef:
    """Returns the URI for QUDT unit: Common Year (http://qudt.org/vocab/unit/YR_Common)"""
    return QUDT_UNIT["YR_COMMON"]


def get_qudt_unit_metrology_year() -> URIRef:
    """Returns the URI for QUDT unit: Metrology Year (http://qudt.org/vocab/unit/YR_Metrology)"""
    return QUDT_UNIT["YR_METROLOGY"]


def get_qudt_unit_sidereal_year() -> URIRef:
    """Returns the URI for QUDT unit: Sidereal Year (http://qudt.org/vocab/unit/YR_Sidereal)"""
    return QUDT_UNIT["YR_SIDEREAL"]


def get_qudt_unit_tropical_year() -> URIRef:
    """Returns the URI for QUDT unit: Tropical Year (http://qudt.org/vocab/unit/YR_TROPICAL)"""
    return QUDT_UNIT["YR_TROPICAL"]


def get_qudt_unit_exawatt() -> URIRef:
    """Returns the URI for QUDT unit: Exawatt (http://qudt.org/vocab/unit/ExaW)"""
    return QUDT_UNIT["EXAW"]


def get_qudt_unit_gigawatt() -> URIRef:
    """Returns the URI for QUDT unit: Gigawatt (http://qudt.org/vocab/unit/GigaW)"""
    return QUDT_UNIT["GIGAW"]


def get_qudt_unit_kilowatt() -> URIRef:
    """Returns the URI for QUDT unit: Kilowatt (http://qudt.org/vocab/unit/KiloW)"""
    return QUDT_UNIT["KILOW"]


def get_qudt_unit_megawatt() -> URIRef:
    """Returns the URI for QUDT unit: Megawatt (http://qudt.org/vocab/unit/MegaW)"""
    return QUDT_UNIT["MEGAW"]


def get_qudt_unit_microwatt() -> URIRef:
    """Returns the URI for QUDT unit: Microwatt (http://qudt.org/vocab/unit/MicroW)"""
    return QUDT_UNIT["MICROW"]


def get_qudt_unit_milliwatt() -> URIRef:
    """Returns the URI for QUDT unit: Milliwatt (http://qudt.org/vocab/unit/MilliW)"""
    return QUDT_UNIT["MILLIW"]


def get_qudt_unit_nanowatt() -> URIRef:
    """Returns the URI for QUDT unit: Nanowatt (http://qudt.org/vocab/unit/NanoW)"""
    return QUDT_UNIT["NANOW"]


def get_qudt_unit_petawatt() -> URIRef:
    """Returns the URI for QUDT unit: Petawatt (http://qudt.org/vocab/unit/PetaW)"""
    return QUDT_UNIT["PETAW"]


def get_qudt_unit_picowatt() -> URIRef:
    """Returns the URI for QUDT unit: Picowatt (http://qudt.org/vocab/unit/PicoW)"""
    return QUDT_UNIT["PICOW"]


def get_qudt_unit_terajoule_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Terajoule per Second (http://qudt.org/vocab/unit/TeraJ-PER-SEC)"""
    return QUDT_UNIT["TERAJ-PER-SEC"]


def get_qudt_unit_terawatt() -> URIRef:
    """Returns the URI for QUDT unit: Terawatt (http://qudt.org/vocab/unit/TeraW)"""
    return QUDT_UNIT["TERAW"]


def get_qudt_unit_watt() -> URIRef:
    """Returns the URI for QUDT unit: Watt (http://qudt.org/vocab/unit/W)"""
    return QUDT_UNIT["W"]


def get_qudt_unit_becquerel() -> URIRef:
    """Returns the URI for QUDT unit: Becquerel (http://qudt.org/vocab/unit/BQ)"""
    return QUDT_UNIT["BQ"]


def get_qudt_unit_curie() -> URIRef:
    """Returns the URI for QUDT unit: Curie (http://qudt.org/vocab/unit/CI)"""
    return QUDT_UNIT["CI"]


def get_qudt_unit_gigabecquerel() -> URIRef:
    """Returns the URI for QUDT unit: Gigabecquerel (http://qudt.org/vocab/unit/GigaBQ)"""
    return QUDT_UNIT["GIGABQ"]


def get_qudt_unit_kilobecquerel() -> URIRef:
    """Returns the URI for QUDT unit: Kilobecquerel (http://qudt.org/vocab/unit/KiloBQ)"""
    return QUDT_UNIT["KILOBQ"]


def get_qudt_unit_kilocurie() -> URIRef:
    """Returns the URI for QUDT unit: Kilocurie (http://qudt.org/vocab/unit/KiloCI)"""
    return QUDT_UNIT["KILOCI"]


def get_qudt_unit_megabecquerel() -> URIRef:
    """Returns the URI for QUDT unit: Megabecquerel (http://qudt.org/vocab/unit/MegaBQ)"""
    return QUDT_UNIT["MEGABQ"]


def get_qudt_unit_microbecquerel() -> URIRef:
    """Returns the URI for QUDT unit: Microbecquerel (http://qudt.org/vocab/unit/MicroBQ)"""
    return QUDT_UNIT["MICROBQ"]


def get_qudt_unit_microcurie() -> URIRef:
    """Returns the URI for QUDT unit: Microcurie (http://qudt.org/vocab/unit/MicroCI)"""
    return QUDT_UNIT["MICROCI"]


def get_qudt_unit_millibecquerel() -> URIRef:
    """Returns the URI for QUDT unit: Millibecquerel (http://qudt.org/vocab/unit/MilliBQ)"""
    return QUDT_UNIT["MILLIBQ"]


def get_qudt_unit_millicurie() -> URIRef:
    """Returns the URI for QUDT unit: Millicurie (http://qudt.org/vocab/unit/MilliCI)"""
    return QUDT_UNIT["MILLICI"]


def get_qudt_unit_nanobecquerel() -> URIRef:
    """Returns the URI for QUDT unit: Nanobecquerel (http://qudt.org/vocab/unit/NanoBQ)"""
    return QUDT_UNIT["NANOBQ"]


def get_qudt_unit_petabecquerel() -> URIRef:
    """Returns the URI for QUDT unit: Petabecquerel (http://qudt.org/vocab/unit/PetaBQ)"""
    return QUDT_UNIT["PETABQ"]


def get_qudt_unit_terabecquerel() -> URIRef:
    """Returns the URI for QUDT unit: Terabecquerel (http://qudt.org/vocab/unit/TeraBQ)"""
    return QUDT_UNIT["TERABQ"]


def get_qudt_unit_becquerel_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: Becquerel per Litre (http://qudt.org/vocab/unit/BQ-PER-L)"""
    return QUDT_UNIT["BQ-PER-L"]


def get_qudt_unit_becquerel_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Becquerel per Cubic Metre (http://qudt.org/vocab/unit/BQ-PER-M3)"""
    return QUDT_UNIT["BQ-PER-M3"]


def get_qudt_unit_microbecquerel_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: Microbecquerel per Litre (http://qudt.org/vocab/unit/MicroBQ-PER-L)"""
    return QUDT_UNIT["MICROBQ-PER-L"]


def get_qudt_unit_millibecquerel_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: Millibecquerel per Litre (http://qudt.org/vocab/unit/MilliBQ-PER-L)"""
    return QUDT_UNIT["MILLIBQ-PER-L"]


def get_qudt_unit_nanobecquerel_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: Nanobecquerel per Litre (http://qudt.org/vocab/unit/NanoBQ-PER-L)"""
    return QUDT_UNIT["NANOBQ-PER-L"]


def get_qudt_unit_becquerel_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Becquerel per Kilogram (http://qudt.org/vocab/unit/BQ-PER-KiloGM)"""
    return QUDT_UNIT["BQ-PER-KILOGM"]


def get_qudt_unit_curie_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Curie per Kilogram (http://qudt.org/vocab/unit/CI-PER-KiloGM)"""
    return QUDT_UNIT["CI-PER-KILOGM"]


def get_qudt_unit_kilobecquerel_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Kilobecquerel per Kilogram (http://qudt.org/vocab/unit/KiloBQ-PER-KiloGM)"""
    return QUDT_UNIT["KILOBQ-PER-KILOGM"]


def get_qudt_unit_megabecquerel_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Megabecquerel per Kilogram (http://qudt.org/vocab/unit/MegaBQ-PER-KiloGM)"""
    return QUDT_UNIT["MEGABQ-PER-KILOGM"]


def get_qudt_unit_decisiemens() -> URIRef:
    """Returns the URI for QUDT unit: Decisiemens (http://qudt.org/vocab/unit/DeciS)"""
    return QUDT_UNIT["DECIS"]


def get_qudt_unit_kilosiemens() -> URIRef:
    """Returns the URI for QUDT unit: Kilosiemens (http://qudt.org/vocab/unit/KiloS)"""
    return QUDT_UNIT["KILOS"]


def get_qudt_unit_mho() -> URIRef:
    """Returns the URI for QUDT unit: Mho (http://qudt.org/vocab/unit/MHO)"""
    return QUDT_UNIT["MHO"]


def get_qudt_unit_megasiemens() -> URIRef:
    """Returns the URI for QUDT unit: Megasiemens (http://qudt.org/vocab/unit/MegaS)"""
    return QUDT_UNIT["MEGAS"]


def get_qudt_unit_micromho() -> URIRef:
    """Returns the URI for QUDT unit: Micromho (http://qudt.org/vocab/unit/MicroMHO)"""
    return QUDT_UNIT["MICROMHO"]


def get_qudt_unit_microsiemens() -> URIRef:
    """Returns the URI for QUDT unit: Microsiemens (http://qudt.org/vocab/unit/MicroS)"""
    return QUDT_UNIT["MICROS"]


def get_qudt_unit_millisiemens() -> URIRef:
    """Returns the URI for QUDT unit: Millisiemens (http://qudt.org/vocab/unit/MilliS)"""
    return QUDT_UNIT["MILLIS"]


def get_qudt_unit_nanosiemens() -> URIRef:
    """Returns the URI for QUDT unit: Nanosiemens (http://qudt.org/vocab/unit/NanoS)"""
    return QUDT_UNIT["NANOS"]


def get_qudt_unit_picosiemens() -> URIRef:
    """Returns the URI for QUDT unit: Picosiemens (http://qudt.org/vocab/unit/PicoS)"""
    return QUDT_UNIT["PICOS"]


def get_qudt_unit_standard_atmosphere() -> URIRef:
    """Returns the URI for QUDT unit: Standard Atmosphere (http://qudt.org/vocab/unit/ATM)"""
    return QUDT_UNIT["ATM"]


def get_qudt_unit_technical_atmosphere() -> URIRef:
    """Returns the URI for QUDT unit: Technical Atmosphere (http://qudt.org/vocab/unit/ATM_T)"""
    return QUDT_UNIT["ATM_T"]


def get_qudt_unit_bar() -> URIRef:
    """Returns the URI for QUDT unit: Bar (http://qudt.org/vocab/unit/BAR)"""
    return QUDT_UNIT["BAR"]


def get_qudt_unit_barad() -> URIRef:
    """Returns the URI for QUDT unit: Barad (http://qudt.org/vocab/unit/BARAD)"""
    return QUDT_UNIT["BARAD"]


def get_qudt_unit_barye() -> URIRef:
    """Returns the URI for QUDT unit: Barye (http://qudt.org/vocab/unit/BARYE)"""
    return QUDT_UNIT["BARYE"]


def get_qudt_unit_bar_absolute() -> URIRef:
    """Returns the URI for QUDT unit: Bar Absolute (http://qudt.org/vocab/unit/BAR_A)"""
    return QUDT_UNIT["BAR_A"]


def get_qudt_unit_centibar() -> URIRef:
    """Returns the URI for QUDT unit: Centibar (http://qudt.org/vocab/unit/CentiBAR)"""
    return QUDT_UNIT["CENTIBAR"]


def get_qudt_unit_conventional_centimetre_of_water() -> URIRef:
    """Returns the URI for QUDT unit: Conventional Centimetre of Water (http://qudt.org/vocab/unit/CentiM_H2O)"""
    return QUDT_UNIT["CENTIM_H2O"]


def get_qudt_unit_centimetre_of_water_4_c() -> URIRef:
    """Returns the URI for QUDT unit: Centimetre of Water (4 °C) (http://qudt.org/vocab/unit/CentiM_H2O_4DEG_C)"""
    return QUDT_UNIT["CENTIM_H2O_4DEG_C"]


def get_qudt_unit_centimetre_of_mercury() -> URIRef:
    """Returns the URI for QUDT unit: Centimetre of Mercury (http://qudt.org/vocab/unit/CentiM_HG)"""
    return QUDT_UNIT["CENTIM_HG"]


def get_qudt_unit_centimetre_of_mercury_0_c() -> URIRef:
    """Returns the URI for QUDT unit: Centimetre of Mercury (0 °C) (http://qudt.org/vocab/unit/CentiM_HG_0DEG_C)"""
    return QUDT_UNIT["CENTIM_HG_0DEG_C"]


def get_qudt_unit_dyne_per_square_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Dyne per Square Centimetre (http://qudt.org/vocab/unit/DYN-PER-CentiM2)"""
    return QUDT_UNIT["DYN-PER-CENTIM2"]


def get_qudt_unit_decapascal() -> URIRef:
    """Returns the URI for QUDT unit: Decapascal (http://qudt.org/vocab/unit/DecaPA)"""
    return QUDT_UNIT["DECAPA"]


def get_qudt_unit_decibar() -> URIRef:
    """Returns the URI for QUDT unit: Decibar (http://qudt.org/vocab/unit/DeciBAR)"""
    return QUDT_UNIT["DECIBAR"]


def get_qudt_unit_foot_of_water() -> URIRef:
    """Returns the URI for QUDT unit: Foot of Water (http://qudt.org/vocab/unit/FT_H2O)"""
    return QUDT_UNIT["FT_H2O"]


def get_qudt_unit_foot_of_water_39_2_f() -> URIRef:
    """Returns the URI for QUDT unit: Foot of Water (39.2 °F) (http://qudt.org/vocab/unit/FT_H2O_39dot2DEG_F)"""
    return QUDT_UNIT["FT_H2O_39DOT2DEG_F"]


def get_qudt_unit_foot_of_mercury() -> URIRef:
    """Returns the URI for QUDT unit: Foot of Mercury (http://qudt.org/vocab/unit/FT_HG)"""
    return QUDT_UNIT["FT_HG"]


def get_qudt_unit_gram_force_per_square_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Gram Force per Square Centimetre (http://qudt.org/vocab/unit/GM_F-PER-CentiM2)"""
    return QUDT_UNIT["GM_F-PER-CENTIM2"]


def get_qudt_unit_gigapascal() -> URIRef:
    """Returns the URI for QUDT unit: Gigapascal (http://qudt.org/vocab/unit/GigaPA)"""
    return QUDT_UNIT["GIGAPA"]


def get_qudt_unit_hectobar() -> URIRef:
    """Returns the URI for QUDT unit: Hectobar (http://qudt.org/vocab/unit/HectoBAR)"""
    return QUDT_UNIT["HECTOBAR"]


def get_qudt_unit_hectopascal() -> URIRef:
    """Returns the URI for QUDT unit: Hectopascal (http://qudt.org/vocab/unit/HectoPA)"""
    return QUDT_UNIT["HECTOPA"]


def get_qudt_unit_inch_of_water() -> URIRef:
    """Returns the URI for QUDT unit: Inch of Water (http://qudt.org/vocab/unit/IN_H2O)"""
    return QUDT_UNIT["IN_H2O"]


def get_qudt_unit_inch_of_water_39_2_f() -> URIRef:
    """Returns the URI for QUDT unit: Inch of Water (39.2 °F) (http://qudt.org/vocab/unit/IN_H2O_39dot2DEG_F)"""
    return QUDT_UNIT["IN_H2O_39DOT2DEG_F"]


def get_qudt_unit_inch_of_water_60_f() -> URIRef:
    """Returns the URI for QUDT unit: Inch of Water (60 °F) (http://qudt.org/vocab/unit/IN_H2O_60DEG_F)"""
    return QUDT_UNIT["IN_H2O_60DEG_F"]


def get_qudt_unit_inch_of_mercury() -> URIRef:
    """Returns the URI for QUDT unit: Inch of Mercury (http://qudt.org/vocab/unit/IN_HG)"""
    return QUDT_UNIT["IN_HG"]


def get_qudt_unit_inch_of_mercury_32_f() -> URIRef:
    """Returns the URI for QUDT unit: Inch of Mercury (32 °F) (http://qudt.org/vocab/unit/IN_HG_32DEG_F)"""
    return QUDT_UNIT["IN_HG_32DEG_F"]


def get_qudt_unit_inch_of_mercury_60_f() -> URIRef:
    """Returns the URI for QUDT unit: Inch of Mercury (60 °F) (http://qudt.org/vocab/unit/IN_HG_60DEG_F)"""
    return QUDT_UNIT["IN_HG_60DEG_F"]


def get_qudt_unit_kip_per_square_inch() -> URIRef:
    """Returns the URI for QUDT unit: Kip per Square Inch (http://qudt.org/vocab/unit/KIP_F-PER-IN2)"""
    return QUDT_UNIT["KIP_F-PER-IN2"]


def get_qudt_unit_kilobar() -> URIRef:
    """Returns the URI for QUDT unit: Kilobar (http://qudt.org/vocab/unit/KiloBAR)"""
    return QUDT_UNIT["KILOBAR"]


def get_qudt_unit_kilogram_per_metre_square_second() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Metre Square Second (http://qudt.org/vocab/unit/KiloGM-PER-M-SEC2)"""
    return QUDT_UNIT["KILOGM-PER-M-SEC2"]


def get_qudt_unit_kilo_gram_force_per_square_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Kilo Gram Force per Square Centimetre (http://qudt.org/vocab/unit/KiloGM_F-PER-CentiM2)"""
    return QUDT_UNIT["KILOGM_F-PER-CENTIM2"]


def get_qudt_unit_kilo_gram_force_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kilo Gram Force per Square Metre (http://qudt.org/vocab/unit/KiloGM_F-PER-M2)"""
    return QUDT_UNIT["KILOGM_F-PER-M2"]


def get_qudt_unit_kilo_gram_force_per_square_millimetre() -> URIRef:
    """Returns the URI for QUDT unit: Kilo Gram Force per Square Millimetre (http://qudt.org/vocab/unit/KiloGM_F-PER-MilliM2)"""
    return QUDT_UNIT["KILOGM_F-PER-MILLIM2"]


def get_qudt_unit_kilo_pound_force_per_square_inch() -> URIRef:
    """Returns the URI for QUDT unit: Kilo Pound Force per Square Inch (http://qudt.org/vocab/unit/KiloLB_F-PER-IN2)"""
    return QUDT_UNIT["KILOLB_F-PER-IN2"]


def get_qudt_unit_kilonewton_per_square_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Kilonewton per Square Centimetre (http://qudt.org/vocab/unit/KiloN-PER-CentiM2)"""
    return QUDT_UNIT["KILON-PER-CENTIM2"]


def get_qudt_unit_kilonewton_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kilonewton per Square Metre (http://qudt.org/vocab/unit/KiloN-PER-M2)"""
    return QUDT_UNIT["KILON-PER-M2"]


def get_qudt_unit_kilonewton_per_square_millimetre() -> URIRef:
    """Returns the URI for QUDT unit: Kilonewton per Square Millimetre (http://qudt.org/vocab/unit/KiloN-PER-MilliM2)"""
    return QUDT_UNIT["KILON-PER-MILLIM2"]


def get_qudt_unit_kilopascal() -> URIRef:
    """Returns the URI for QUDT unit: Kilopascal (http://qudt.org/vocab/unit/KiloPA)"""
    return QUDT_UNIT["KILOPA"]


def get_qudt_unit_kilopascal_absolute() -> URIRef:
    """Returns the URI for QUDT unit: Kilopascal Absolute (http://qudt.org/vocab/unit/KiloPA_A)"""
    return QUDT_UNIT["KILOPA_A"]


def get_qudt_unit_pound_force_per_square_foot() -> URIRef:
    """Returns the URI for QUDT unit: Pound Force per Square Foot (http://qudt.org/vocab/unit/LB_F-PER-FT2)"""
    return QUDT_UNIT["LB_F-PER-FT2"]


def get_qudt_unit_pound_force_per_square_inch() -> URIRef:
    """Returns the URI for QUDT unit: Pound Force per Square Inch (http://qudt.org/vocab/unit/LB_F-PER-IN2)"""
    return QUDT_UNIT["LB_F-PER-IN2"]


def get_qudt_unit_conventional_metre_of_water() -> URIRef:
    """Returns the URI for QUDT unit: Conventional Metre of Water (http://qudt.org/vocab/unit/M_H2O)"""
    return QUDT_UNIT["M_H2O"]


def get_qudt_unit_megabar() -> URIRef:
    """Returns the URI for QUDT unit: Megabar (http://qudt.org/vocab/unit/MegaBAR)"""
    return QUDT_UNIT["MEGABAR"]


def get_qudt_unit_meganewton_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Meganewton per Square Metre (http://qudt.org/vocab/unit/MegaN-PER-M2)"""
    return QUDT_UNIT["MEGAN-PER-M2"]


def get_qudt_unit_megapascal() -> URIRef:
    """Returns the URI for QUDT unit: Megapascal (http://qudt.org/vocab/unit/MegaPA)"""
    return QUDT_UNIT["MEGAPA"]


def get_qudt_unit_megapsi() -> URIRef:
    """Returns the URI for QUDT unit: Megapsi (http://qudt.org/vocab/unit/MegaPSI)"""
    return QUDT_UNIT["MEGAPSI"]


def get_qudt_unit_micro_standard_atmosphere() -> URIRef:
    """Returns the URI for QUDT unit: Micro Standard Atmosphere (http://qudt.org/vocab/unit/MicroATM)"""
    return QUDT_UNIT["MICROATM"]


def get_qudt_unit_microbar() -> URIRef:
    """Returns the URI for QUDT unit: Microbar (http://qudt.org/vocab/unit/MicroBAR)"""
    return QUDT_UNIT["MICROBAR"]


def get_qudt_unit_micropascal() -> URIRef:
    """Returns the URI for QUDT unit: Micropascal (http://qudt.org/vocab/unit/MicroPA)"""
    return QUDT_UNIT["MICROPA"]


def get_qudt_unit_microtorr() -> URIRef:
    """Returns the URI for QUDT unit: Microtorr (http://qudt.org/vocab/unit/MicroTORR)"""
    return QUDT_UNIT["MICROTORR"]


def get_qudt_unit_millibar() -> URIRef:
    """Returns the URI for QUDT unit: Millibar (http://qudt.org/vocab/unit/MilliBAR)"""
    return QUDT_UNIT["MILLIBAR"]


def get_qudt_unit_milli_bar_absolute() -> URIRef:
    """Returns the URI for QUDT unit: Milli Bar Absolute (http://qudt.org/vocab/unit/MilliBAR_A)"""
    return QUDT_UNIT["MILLIBAR_A"]


def get_qudt_unit_conventional_millimetre_of_water() -> URIRef:
    """Returns the URI for QUDT unit: Conventional Millimetre of Water (http://qudt.org/vocab/unit/MilliM_H2O)"""
    return QUDT_UNIT["MILLIM_H2O"]


def get_qudt_unit_millimetre_of_mercury() -> URIRef:
    """Returns the URI for QUDT unit: Millimetre of Mercury (http://qudt.org/vocab/unit/MilliM_HG)"""
    return QUDT_UNIT["MILLIM_HG"]


def get_qudt_unit_millimetre_of_mercury_absolute() -> URIRef:
    """Returns the URI for QUDT unit: Millimetre of Mercury - Absolute (http://qudt.org/vocab/unit/MilliM_HGA)"""
    return QUDT_UNIT["MILLIM_HGA"]


def get_qudt_unit_millipascal() -> URIRef:
    """Returns the URI for QUDT unit: Millipascal (http://qudt.org/vocab/unit/MilliPA)"""
    return QUDT_UNIT["MILLIPA"]


def get_qudt_unit_millitorr() -> URIRef:
    """Returns the URI for QUDT unit: Millitorr (http://qudt.org/vocab/unit/MilliTORR)"""
    return QUDT_UNIT["MILLITORR"]


def get_qudt_unit_newton_per_square_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Newton per Square Centimetre (http://qudt.org/vocab/unit/N-PER-CentiM2)"""
    return QUDT_UNIT["N-PER-CENTIM2"]


def get_qudt_unit_newton_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Newton per Square Metre (http://qudt.org/vocab/unit/N-PER-M2)"""
    return QUDT_UNIT["N-PER-M2"]


def get_qudt_unit_newton_per_square_millimetre() -> URIRef:
    """Returns the URI for QUDT unit: Newton per Square Millimetre (http://qudt.org/vocab/unit/N-PER-MilliM2)"""
    return QUDT_UNIT["N-PER-MILLIM2"]


def get_qudt_unit_poundal_per_square_foot() -> URIRef:
    """Returns the URI for QUDT unit: Poundal per Square Foot (http://qudt.org/vocab/unit/PDL-PER-FT2)"""
    return QUDT_UNIT["PDL-PER-FT2"]


def get_qudt_unit_poundal_per_square_inch() -> URIRef:
    """Returns the URI for QUDT unit: Poundal per Square Inch (http://qudt.org/vocab/unit/PDL-PER-IN2)"""
    return QUDT_UNIT["PDL-PER-IN2"]


def get_qudt_unit_psi() -> URIRef:
    """Returns the URI for QUDT unit: Psi (http://qudt.org/vocab/unit/PSI)"""
    return QUDT_UNIT["PSI"]


def get_qudt_unit_picopascal() -> URIRef:
    """Returns the URI for QUDT unit: Picopascal (http://qudt.org/vocab/unit/PicoPA)"""
    return QUDT_UNIT["PICOPA"]


def get_qudt_unit_planck_pressure() -> URIRef:
    """Returns the URI for QUDT unit: Planck Pressure (http://qudt.org/vocab/unit/PlanckPressure)"""
    return QUDT_UNIT["PLANCKPRESSURE"]


def get_qudt_unit_torr() -> URIRef:
    """Returns the URI for QUDT unit: Torr (http://qudt.org/vocab/unit/TORR)"""
    return QUDT_UNIT["TORR"]


def get_qudt_unit_okta() -> URIRef:
    """Returns the URI for QUDT unit: Okta (http://qudt.org/vocab/unit/OKTA)"""
    return QUDT_UNIT["OKTA"]


def get_qudt_unit_centimole() -> URIRef:
    """Returns the URI for QUDT unit: Centimole (http://qudt.org/vocab/unit/CentiMOL)"""
    return QUDT_UNIT["CENTIMOL"]


def get_qudt_unit_femtomole() -> URIRef:
    """Returns the URI for QUDT unit: Femtomole (http://qudt.org/vocab/unit/FemtoMOL)"""
    return QUDT_UNIT["FEMTOMOL"]


def get_qudt_unit_international_unit() -> URIRef:
    """Returns the URI for QUDT unit: International Unit (http://qudt.org/vocab/unit/IU)"""
    return QUDT_UNIT["IU"]


def get_qudt_unit_kilomole() -> URIRef:
    """Returns the URI for QUDT unit: Kilomole (http://qudt.org/vocab/unit/KiloMOL)"""
    return QUDT_UNIT["KILOMOL"]


def get_qudt_unit_mole() -> URIRef:
    """Returns the URI for QUDT unit: Mole (http://qudt.org/vocab/unit/MOL)"""
    return QUDT_UNIT["MOL"]


def get_qudt_unit_pound_mole() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mole (http://qudt.org/vocab/unit/MOL_LB)"""
    return QUDT_UNIT["MOL_LB"]


def get_qudt_unit_micromole() -> URIRef:
    """Returns the URI for QUDT unit: Micromole (http://qudt.org/vocab/unit/MicroMOL)"""
    return QUDT_UNIT["MICROMOL"]


def get_qudt_unit_millimole() -> URIRef:
    """Returns the URI for QUDT unit: Millimole (http://qudt.org/vocab/unit/MilliMOL)"""
    return QUDT_UNIT["MILLIMOL"]


def get_qudt_unit_milliosmole() -> URIRef:
    """Returns the URI for QUDT unit: Milliosmole (http://qudt.org/vocab/unit/MilliOSM)"""
    return QUDT_UNIT["MILLIOSM"]


def get_qudt_unit_normal_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Normal Cubic Metre (http://qudt.org/vocab/unit/NCM)"""
    return QUDT_UNIT["NCM"]


def get_qudt_unit_nanomole() -> URIRef:
    """Returns the URI for QUDT unit: Nanomole (http://qudt.org/vocab/unit/NanoMOL)"""
    return QUDT_UNIT["NANOMOL"]


def get_qudt_unit_osmole() -> URIRef:
    """Returns the URI for QUDT unit: Osmole (http://qudt.org/vocab/unit/OSM)"""
    return QUDT_UNIT["OSM"]


def get_qudt_unit_picomole() -> URIRef:
    """Returns the URI for QUDT unit: Picomole (http://qudt.org/vocab/unit/PicoMOL)"""
    return QUDT_UNIT["PICOMOL"]


def get_qudt_unit_standard_cubic_foot() -> URIRef:
    """Returns the URI for QUDT unit: Standard Cubic Foot (http://qudt.org/vocab/unit/SCF)"""
    return QUDT_UNIT["SCF"]


def get_qudt_unit_standard_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Standard Cubic Metre (http://qudt.org/vocab/unit/SCM)"""
    return QUDT_UNIT["SCM"]


def get_qudt_unit_centimole_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: Centimole per Litre (http://qudt.org/vocab/unit/CentiMOL-PER-L)"""
    return QUDT_UNIT["CENTIMOL-PER-L"]


def get_qudt_unit_femtomole_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: Femtomole per Litre (http://qudt.org/vocab/unit/FemtoMOL-PER-L)"""
    return QUDT_UNIT["FEMTOMOL-PER-L"]


def get_qudt_unit_kilomole_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kilomole per Cubic Metre (http://qudt.org/vocab/unit/KiloMOL-PER-M3)"""
    return QUDT_UNIT["KILOMOL-PER-M3"]


def get_qudt_unit_mole_per_cubic_decimetre() -> URIRef:
    """Returns the URI for QUDT unit: Mole per Cubic Decimetre (http://qudt.org/vocab/unit/MOL-PER-DeciM3)"""
    return QUDT_UNIT["MOL-PER-DECIM3"]


def get_qudt_unit_mole_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: Mole per Litre (http://qudt.org/vocab/unit/MOL-PER-L)"""
    return QUDT_UNIT["MOL-PER-L"]


def get_qudt_unit_mole_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Mole per Cubic Metre (http://qudt.org/vocab/unit/MOL-PER-M3)"""
    return QUDT_UNIT["MOL-PER-M3"]


def get_qudt_unit_micromole_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: Micromole per Litre (http://qudt.org/vocab/unit/MicroMOL-PER-L)"""
    return QUDT_UNIT["MICROMOL-PER-L"]


def get_qudt_unit_millimole_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: Millimole per Litre (http://qudt.org/vocab/unit/MilliMOL-PER-L)"""
    return QUDT_UNIT["MILLIMOL-PER-L"]


def get_qudt_unit_millimole_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Millimole per Cubic Metre (http://qudt.org/vocab/unit/MilliMOL-PER-M3)"""
    return QUDT_UNIT["MILLIMOL-PER-M3"]


def get_qudt_unit_nanomole_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: Nanomole per Litre (http://qudt.org/vocab/unit/NanoMOL-PER-L)"""
    return QUDT_UNIT["NANOMOL-PER-L"]


def get_qudt_unit_picomole_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: Picomole per Litre (http://qudt.org/vocab/unit/PicoMOL-PER-L)"""
    return QUDT_UNIT["PICOMOL-PER-L"]


def get_qudt_unit_picomole_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Picomole per Cubic Metre (http://qudt.org/vocab/unit/PicoMOL-PER-M3)"""
    return QUDT_UNIT["PICOMOL-PER-M3"]


def get_qudt_unit_parts_per_billion() -> URIRef:
    """Returns the URI for QUDT unit: Parts per Billion (http://qudt.org/vocab/unit/PPB)"""
    return QUDT_UNIT["PPB"]


def get_qudt_unit_parts_per_million() -> URIRef:
    """Returns the URI for QUDT unit: Parts per Million (http://qudt.org/vocab/unit/PPM)"""
    return QUDT_UNIT["PPM"]


def get_qudt_unit_part_per_quadrillion() -> URIRef:
    """Returns the URI for QUDT unit: Part per Quadrillion (http://qudt.org/vocab/unit/PPQ)"""
    return QUDT_UNIT["PPQ"]


def get_qudt_unit_part_per_trillion() -> URIRef:
    """Returns the URI for QUDT unit: Part per Trillion (http://qudt.org/vocab/unit/PPT)"""
    return QUDT_UNIT["PPT"]


def get_qudt_unit_parts_per_thousand() -> URIRef:
    """Returns the URI for QUDT unit: Parts per Thousand (http://qudt.org/vocab/unit/PPTH)"""
    return QUDT_UNIT["PPTH"]


def get_qudt_unit_parts_per_ten_million() -> URIRef:
    """Returns the URI for QUDT unit: Parts per Ten Million (http://qudt.org/vocab/unit/PPTM)"""
    return QUDT_UNIT["PPTM"]


def get_qudt_unit_centimole_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Centimole per Kilogram (http://qudt.org/vocab/unit/CentiMOL-PER-KiloGM)"""
    return QUDT_UNIT["CENTIMOL-PER-KILOGM"]


def get_qudt_unit_femtomole_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Femtomole per Kilogram (http://qudt.org/vocab/unit/FemtoMOL-PER-KiloGM)"""
    return QUDT_UNIT["FEMTOMOL-PER-KILOGM"]


def get_qudt_unit_international_unit_per_milligram() -> URIRef:
    """Returns the URI for QUDT unit: International Unit per Milligram (http://qudt.org/vocab/unit/IU-PER-MilliGM)"""
    return QUDT_UNIT["IU-PER-MILLIGM"]


def get_qudt_unit_kilomole_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Kilomole per Kilogram (http://qudt.org/vocab/unit/KiloMOL-PER-KiloGM)"""
    return QUDT_UNIT["KILOMOL-PER-KILOGM"]


def get_qudt_unit_mole_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Mole per Kilogram (http://qudt.org/vocab/unit/MOL-PER-KiloGM)"""
    return QUDT_UNIT["MOL-PER-KILOGM"]


def get_qudt_unit_mole_per_tonne() -> URIRef:
    """Returns the URI for QUDT unit: Mole per Tonne (http://qudt.org/vocab/unit/MOL-PER-TONNE)"""
    return QUDT_UNIT["MOL-PER-TONNE"]


def get_qudt_unit_pound_mole_per_pound_mass() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mole per Pound Mass (http://qudt.org/vocab/unit/MOL_LB-PER-LB)"""
    return QUDT_UNIT["MOL_LB-PER-LB"]


def get_qudt_unit_micromole_per_gram() -> URIRef:
    """Returns the URI for QUDT unit: Micromole per Gram (http://qudt.org/vocab/unit/MicroMOL-PER-GM)"""
    return QUDT_UNIT["MICROMOL-PER-GM"]


def get_qudt_unit_micromole_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Micromole per Kilogram (http://qudt.org/vocab/unit/MicroMOL-PER-KiloGM)"""
    return QUDT_UNIT["MICROMOL-PER-KILOGM"]


def get_qudt_unit_millimole_per_gram() -> URIRef:
    """Returns the URI for QUDT unit: Millimole per Gram (http://qudt.org/vocab/unit/MilliMOL-PER-GM)"""
    return QUDT_UNIT["MILLIMOL-PER-GM"]


def get_qudt_unit_millimole_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Millimole per Kilogram (http://qudt.org/vocab/unit/MilliMOL-PER-KiloGM)"""
    return QUDT_UNIT["MILLIMOL-PER-KILOGM"]


def get_qudt_unit_milliosmole_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Milliosmole per Kilogram (http://qudt.org/vocab/unit/MilliOSM-PER-KiloGM)"""
    return QUDT_UNIT["MILLIOSM-PER-KILOGM"]


def get_qudt_unit_nanomole_per_gram() -> URIRef:
    """Returns the URI for QUDT unit: Nanomole per Gram (http://qudt.org/vocab/unit/NanoMOL-PER-GM)"""
    return QUDT_UNIT["NANOMOL-PER-GM"]


def get_qudt_unit_nanomole_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Nanomole per Kilogram (http://qudt.org/vocab/unit/NanoMOL-PER-KiloGM)"""
    return QUDT_UNIT["NANOMOL-PER-KILOGM"]


def get_qudt_unit_picomole_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Picomole per Kilogram (http://qudt.org/vocab/unit/PicoMOL-PER-KiloGM)"""
    return QUDT_UNIT["PICOMOL-PER-KILOGM"]


def get_qudt_unit_mole_per_kilogram_bar() -> URIRef:
    """Returns the URI for QUDT unit: Mole per Kilogram Bar (http://qudt.org/vocab/unit/MOL-PER-KiloGM-BAR)"""
    return QUDT_UNIT["MOL-PER-KILOGM-BAR"]


def get_qudt_unit_mole_per_kilogram_pascal() -> URIRef:
    """Returns the URI for QUDT unit: Mole per Kilogram Pascal (http://qudt.org/vocab/unit/MOL-PER-KiloGM-PA)"""
    return QUDT_UNIT["MOL-PER-KILOGM-PA"]


def get_qudt_unit_arcminute() -> URIRef:
    """Returns the URI for QUDT unit: Arcminute (http://qudt.org/vocab/unit/ARCMIN)"""
    return QUDT_UNIT["ARCMIN"]


def get_qudt_unit_arcsecond() -> URIRef:
    """Returns the URI for QUDT unit: Arcsecond (http://qudt.org/vocab/unit/ARCSEC)"""
    return QUDT_UNIT["ARCSEC"]


def get_qudt_unit_degree() -> URIRef:
    """Returns the URI for QUDT unit: Degree (http://qudt.org/vocab/unit/DEG)"""
    return QUDT_UNIT["DEG"]


def get_qudt_unit_gon() -> URIRef:
    """Returns the URI for QUDT unit: Gon (http://qudt.org/vocab/unit/GON)"""
    return QUDT_UNIT["GON"]


def get_qudt_unit_grad() -> URIRef:
    """Returns the URI for QUDT unit: Grad (http://qudt.org/vocab/unit/GRAD)"""
    return QUDT_UNIT["GRAD"]


def get_qudt_unit_mil_angle() -> URIRef:
    """Returns the URI for QUDT unit: Mil Angle (http://qudt.org/vocab/unit/MIL_Angle)"""
    return QUDT_UNIT["MIL_ANGLE"]


def get_qudt_unit_minute_angle() -> URIRef:
    """Returns the URI for QUDT unit: Minute Angle (http://qudt.org/vocab/unit/MIN_Angle)"""
    return QUDT_UNIT["MIN_ANGLE"]


def get_qudt_unit_microradian() -> URIRef:
    """Returns the URI for QUDT unit: Microradian (http://qudt.org/vocab/unit/MicroRAD)"""
    return QUDT_UNIT["MICRORAD"]


def get_qudt_unit_milliarcsecond() -> URIRef:
    """Returns the URI for QUDT unit: Milliarcsecond (http://qudt.org/vocab/unit/MilliARCSEC)"""
    return QUDT_UNIT["MILLIARCSEC"]


def get_qudt_unit_milliradian() -> URIRef:
    """Returns the URI for QUDT unit: Milliradian (http://qudt.org/vocab/unit/MilliRAD)"""
    return QUDT_UNIT["MILLIRAD"]


def get_qudt_unit_radian() -> URIRef:
    """Returns the URI for QUDT unit: Radian (http://qudt.org/vocab/unit/RAD)"""
    return QUDT_UNIT["RAD"]


def get_qudt_unit_revolution() -> URIRef:
    """Returns the URI for QUDT unit: Revolution (http://qudt.org/vocab/unit/REV)"""
    return QUDT_UNIT["REV"]


def get_qudt_unit_degree_per_square_second() -> URIRef:
    """Returns the URI for QUDT unit: Degree per Square Second (http://qudt.org/vocab/unit/DEG-PER-SEC2)"""
    return QUDT_UNIT["DEG-PER-SEC2"]


def get_qudt_unit_radian_per_square_second() -> URIRef:
    """Returns the URI for QUDT unit: Radian per Square Second (http://qudt.org/vocab/unit/RAD-PER-SEC2)"""
    return QUDT_UNIT["RAD-PER-SEC2"]


def get_qudt_unit_revolution_per_minute_second() -> URIRef:
    """Returns the URI for QUDT unit: Revolution per Minute Second (http://qudt.org/vocab/unit/REV-PER-MIN-SEC)"""
    return QUDT_UNIT["REV-PER-MIN-SEC"]


def get_qudt_unit_revolution_per_square_second() -> URIRef:
    """Returns the URI for QUDT unit: Revolution per Square Second (http://qudt.org/vocab/unit/REV-PER-SEC2)"""
    return QUDT_UNIT["REV-PER-SEC2"]


def get_qudt_unit_square_metre_per_steradian() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre per Steradian (http://qudt.org/vocab/unit/M2-PER-SR)"""
    return QUDT_UNIT["M2-PER-SR"]


def get_qudt_unit_degree_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Degree per Hour (http://qudt.org/vocab/unit/DEG-PER-HR)"""
    return QUDT_UNIT["DEG-PER-HR"]


def get_qudt_unit_degree_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Degree per Minute (http://qudt.org/vocab/unit/DEG-PER-MIN)"""
    return QUDT_UNIT["DEG-PER-MIN"]


def get_qudt_unit_degree_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Degree per Second (http://qudt.org/vocab/unit/DEG-PER-SEC)"""
    return QUDT_UNIT["DEG-PER-SEC"]


def get_qudt_unit_planck_angular_frequency() -> URIRef:
    """Returns the URI for QUDT unit: Planck Angular Frequency (http://qudt.org/vocab/unit/PlanckFrequency_Ang)"""
    return QUDT_UNIT["PLANCKFREQUENCY_ANG"]


def get_qudt_unit_radian_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Radian per Hour (http://qudt.org/vocab/unit/RAD-PER-HR)"""
    return QUDT_UNIT["RAD-PER-HR"]


def get_qudt_unit_radian_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Radian per Minute (http://qudt.org/vocab/unit/RAD-PER-MIN)"""
    return QUDT_UNIT["RAD-PER-MIN"]


def get_qudt_unit_radian_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Radian per Second (http://qudt.org/vocab/unit/RAD-PER-SEC)"""
    return QUDT_UNIT["RAD-PER-SEC"]


def get_qudt_unit_erg_second() -> URIRef:
    """Returns the URI for QUDT unit: Erg Second (http://qudt.org/vocab/unit/ERG-SEC)"""
    return QUDT_UNIT["ERG-SEC"]


def get_qudt_unit_foot_pound_force_second() -> URIRef:
    """Returns the URI for QUDT unit: Foot Pound Force Second (http://qudt.org/vocab/unit/FT-LB_F-SEC)"""
    return QUDT_UNIT["FT-LB_F-SEC"]


def get_qudt_unit_kilogram_square_metre_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram Square Metre per Second (http://qudt.org/vocab/unit/KiloGM-M2-PER-SEC)"""
    return QUDT_UNIT["KILOGM-M2-PER-SEC"]


def get_qudt_unit_newton_metre_second() -> URIRef:
    """Returns the URI for QUDT unit: Newton Metre Second (http://qudt.org/vocab/unit/N-M-SEC)"""
    return QUDT_UNIT["N-M-SEC"]


def get_qudt_unit_newton_metre_second_per_radian() -> URIRef:
    """Returns the URI for QUDT unit: Newton Metre Second per Radian (http://qudt.org/vocab/unit/N-M-SEC-PER-RAD)"""
    return QUDT_UNIT["N-M-SEC-PER-RAD"]


def get_qudt_unit_reciprocal_kilometre() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Kilometre (http://qudt.org/vocab/unit/PER-KiloM)"""
    return QUDT_UNIT["PER-KILOM"]


def get_qudt_unit_reciprocal_micrometre() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Micrometre (http://qudt.org/vocab/unit/PER-MicroM)"""
    return QUDT_UNIT["PER-MICROM"]


def get_qudt_unit_reciprocal_millimetre() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Millimetre (http://qudt.org/vocab/unit/PER-MilliM)"""
    return QUDT_UNIT["PER-MILLIM"]


def get_qudt_unit_reciprocal_nanometre() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Nanometre (http://qudt.org/vocab/unit/PER-NanoM)"""
    return QUDT_UNIT["PER-NANOM"]


def get_qudt_unit_reciprocal_picometre() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Picometre (http://qudt.org/vocab/unit/PER-PicoM)"""
    return QUDT_UNIT["PER-PICOM"]


def get_qudt_unit_degree_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Degree per Metre (http://qudt.org/vocab/unit/DEG-PER-M)"""
    return QUDT_UNIT["DEG-PER-M"]


def get_qudt_unit_radian_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Radian per Metre (http://qudt.org/vocab/unit/RAD-PER-M)"""
    return QUDT_UNIT["RAD-PER-M"]


def get_qudt_unit_exa_volt_ampere() -> URIRef:
    """Returns the URI for QUDT unit: Exa Volt Ampere (http://qudt.org/vocab/unit/ExaVA)"""
    return QUDT_UNIT["EXAVA"]


def get_qudt_unit_giga_volt_ampere() -> URIRef:
    """Returns the URI for QUDT unit: Giga Volt Ampere (http://qudt.org/vocab/unit/GigaVA)"""
    return QUDT_UNIT["GIGAVA"]


def get_qudt_unit_kilo_volt_ampere() -> URIRef:
    """Returns the URI for QUDT unit: Kilo Volt Ampere (http://qudt.org/vocab/unit/KiloVA)"""
    return QUDT_UNIT["KILOVA"]


def get_qudt_unit_mega_volt_ampere() -> URIRef:
    """Returns the URI for QUDT unit: Mega Volt Ampere (http://qudt.org/vocab/unit/MegaVA)"""
    return QUDT_UNIT["MEGAVA"]


def get_qudt_unit_micro_volt_ampere() -> URIRef:
    """Returns the URI for QUDT unit: Micro Volt Ampere (http://qudt.org/vocab/unit/MicroVA)"""
    return QUDT_UNIT["MICROVA"]


def get_qudt_unit_milli_volt_ampere() -> URIRef:
    """Returns the URI for QUDT unit: Milli Volt Ampere (http://qudt.org/vocab/unit/MilliVA)"""
    return QUDT_UNIT["MILLIVA"]


def get_qudt_unit_nano_volt_ampere() -> URIRef:
    """Returns the URI for QUDT unit: Nano Volt Ampere (http://qudt.org/vocab/unit/NanoVA)"""
    return QUDT_UNIT["NANOVA"]


def get_qudt_unit_peta_volt_ampere() -> URIRef:
    """Returns the URI for QUDT unit: Peta Volt Ampere (http://qudt.org/vocab/unit/PetaVA)"""
    return QUDT_UNIT["PETAVA"]


def get_qudt_unit_pico_volt_ampere() -> URIRef:
    """Returns the URI for QUDT unit: Pico Volt Ampere (http://qudt.org/vocab/unit/PicoVA)"""
    return QUDT_UNIT["PICOVA"]


def get_qudt_unit_tera_volt_ampere() -> URIRef:
    """Returns the URI for QUDT unit: Tera Volt Ampere (http://qudt.org/vocab/unit/TeraVA)"""
    return QUDT_UNIT["TERAVA"]


def get_qudt_unit_volt_ampere() -> URIRef:
    """Returns the URI for QUDT unit: Volt Ampere (http://qudt.org/vocab/unit/VA)"""
    return QUDT_UNIT["VA"]


def get_qudt_unit_reciprocal_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Kelvin (http://qudt.org/vocab/unit/PER-K)"""
    return QUDT_UNIT["PER-K"]


def get_qudt_unit_acre() -> URIRef:
    """Returns the URI for QUDT unit: Acre (http://qudt.org/vocab/unit/AC)"""
    return QUDT_UNIT["AC"]


def get_qudt_unit_are() -> URIRef:
    """Returns the URI for QUDT unit: Are (http://qudt.org/vocab/unit/ARE)"""
    return QUDT_UNIT["ARE"]


def get_qudt_unit_barn() -> URIRef:
    """Returns the URI for QUDT unit: Barn (http://qudt.org/vocab/unit/BARN)"""
    return QUDT_UNIT["BARN"]


def get_qudt_unit_square_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Square Centimetre (http://qudt.org/vocab/unit/CentiM2)"""
    return QUDT_UNIT["CENTIM2"]


def get_qudt_unit_decaare() -> URIRef:
    """Returns the URI for QUDT unit: Decaare (http://qudt.org/vocab/unit/DecaARE)"""
    return QUDT_UNIT["DECAARE"]


def get_qudt_unit_square_decimetre() -> URIRef:
    """Returns the URI for QUDT unit: Square Decimetre (http://qudt.org/vocab/unit/DeciM2)"""
    return QUDT_UNIT["DECIM2"]


def get_qudt_unit_square_foot() -> URIRef:
    """Returns the URI for QUDT unit: Square Foot (http://qudt.org/vocab/unit/FT2)"""
    return QUDT_UNIT["FT2"]


def get_qudt_unit_hectare() -> URIRef:
    """Returns the URI for QUDT unit: Hectare (http://qudt.org/vocab/unit/HA)"""
    return QUDT_UNIT["HA"]


def get_qudt_unit_square_inch() -> URIRef:
    """Returns the URI for QUDT unit: Square Inch (http://qudt.org/vocab/unit/IN2)"""
    return QUDT_UNIT["IN2"]


def get_qudt_unit_square_kilometre() -> URIRef:
    """Returns the URI for QUDT unit: Square Kilometre (http://qudt.org/vocab/unit/KiloM2)"""
    return QUDT_UNIT["KILOM2"]


def get_qudt_unit_kilo_circular_mil() -> URIRef:
    """Returns the URI for QUDT unit: Kilo Circular Mil (http://qudt.org/vocab/unit/KiloMIL_Circ)"""
    return QUDT_UNIT["KILOMIL_CIRC"]


def get_qudt_unit_square_international_mile() -> URIRef:
    """Returns the URI for QUDT unit: Square International Mile (http://qudt.org/vocab/unit/MI2)"""
    return QUDT_UNIT["MI2"]


def get_qudt_unit_circular_mil() -> URIRef:
    """Returns the URI for QUDT unit: Circular Mil (http://qudt.org/vocab/unit/MIL_Circ)"""
    return QUDT_UNIT["MIL_CIRC"]


def get_qudt_unit_square_us_survey_mile() -> URIRef:
    """Returns the URI for QUDT unit: Square Us Survey Mile (http://qudt.org/vocab/unit/MI_US2)"""
    return QUDT_UNIT["MI_US2"]


def get_qudt_unit_square_micrometre() -> URIRef:
    """Returns the URI for QUDT unit: Square Micrometre (http://qudt.org/vocab/unit/MicroM2)"""
    return QUDT_UNIT["MICROM2"]


def get_qudt_unit_square_millimetre() -> URIRef:
    """Returns the URI for QUDT unit: Square Millimetre (http://qudt.org/vocab/unit/MilliM2)"""
    return QUDT_UNIT["MILLIM2"]


def get_qudt_unit_square_nanometre() -> URIRef:
    """Returns the URI for QUDT unit: Square Nanometre (http://qudt.org/vocab/unit/NanoM2)"""
    return QUDT_UNIT["NANOM2"]


def get_qudt_unit_pixel_area() -> URIRef:
    """Returns the URI for QUDT unit: Pixel (area) (http://qudt.org/vocab/unit/PIXEL_AREA)"""
    return QUDT_UNIT["PIXEL_AREA"]


def get_qudt_unit_planck_area() -> URIRef:
    """Returns the URI for QUDT unit: Planck Area (http://qudt.org/vocab/unit/PlanckArea)"""
    return QUDT_UNIT["PLANCKAREA"]


def get_qudt_unit_square_yard() -> URIRef:
    """Returns the URI for QUDT unit: Square Yard (http://qudt.org/vocab/unit/YD2)"""
    return QUDT_UNIT["YD2"]


def get_qudt_unit_square_metre_steradian() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre Steradian (http://qudt.org/vocab/unit/M2-SR)"""
    return QUDT_UNIT["M2-SR"]


def get_qudt_unit_bit_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Bit per Square Metre (http://qudt.org/vocab/unit/BIT-PER-M2)"""
    return QUDT_UNIT["BIT-PER-M2"]


def get_qudt_unit_exbibit_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Exbibit per Square Metre (http://qudt.org/vocab/unit/ExbiBIT-PER-M2)"""
    return QUDT_UNIT["EXBIBIT-PER-M2"]


def get_qudt_unit_gibibit_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Gibibit per Square Metre (http://qudt.org/vocab/unit/GibiBIT-PER-M2)"""
    return QUDT_UNIT["GIBIBIT-PER-M2"]


def get_qudt_unit_kibibit_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kibibit per Square Metre (http://qudt.org/vocab/unit/KibiBIT-PER-M2)"""
    return QUDT_UNIT["KIBIBIT-PER-M2"]


def get_qudt_unit_mebibit_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Mebibit per Square Metre (http://qudt.org/vocab/unit/MebiBIT-PER-M2)"""
    return QUDT_UNIT["MEBIBIT-PER-M2"]


def get_qudt_unit_pebibit_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Pebibit per Square Metre (http://qudt.org/vocab/unit/PebiBIT-PER-M2)"""
    return QUDT_UNIT["PEBIBIT-PER-M2"]


def get_qudt_unit_tebibit_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Tebibit per Square Metre (http://qudt.org/vocab/unit/TebiBIT-PER-M2)"""
    return QUDT_UNIT["TEBIBIT-PER-M2"]


def get_qudt_unit_ampere_hour_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Ampere Hour per Square Metre (http://qudt.org/vocab/unit/A-HR-PER-M2)"""
    return QUDT_UNIT["A-HR-PER-M2"]


def get_qudt_unit_coulomb_per_square_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Coulomb per Square Centimetre (http://qudt.org/vocab/unit/C-PER-CentiM2)"""
    return QUDT_UNIT["C-PER-CENTIM2"]


def get_qudt_unit_coulomb_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Coulomb per Square Metre (http://qudt.org/vocab/unit/C-PER-M2)"""
    return QUDT_UNIT["C-PER-M2"]


def get_qudt_unit_coulomb_per_square_millimetre() -> URIRef:
    """Returns the URI for QUDT unit: Coulomb per Square Millimetre (http://qudt.org/vocab/unit/C-PER-MilliM2)"""
    return QUDT_UNIT["C-PER-MILLIM2"]


def get_qudt_unit_abcoulomb_per_square_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Abcoulomb per Square Centimetre (http://qudt.org/vocab/unit/C_Ab-PER-CentiM2)"""
    return QUDT_UNIT["C_AB-PER-CENTIM2"]


def get_qudt_unit_statcoulomb_per_square_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Statcoulomb per Square Centimetre (http://qudt.org/vocab/unit/C_Stat-PER-CentiM2)"""
    return QUDT_UNIT["C_STAT-PER-CENTIM2"]


def get_qudt_unit_kilocoulomb_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kilocoulomb per Square Metre (http://qudt.org/vocab/unit/KiloC-PER-M2)"""
    return QUDT_UNIT["KILOC-PER-M2"]


def get_qudt_unit_megacoulomb_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Megacoulomb per Square Metre (http://qudt.org/vocab/unit/MegaC-PER-M2)"""
    return QUDT_UNIT["MEGAC-PER-M2"]


def get_qudt_unit_microcoulomb_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Microcoulomb per Square Metre (http://qudt.org/vocab/unit/MicroC-PER-M2)"""
    return QUDT_UNIT["MICROC-PER-M2"]


def get_qudt_unit_millicoulomb_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Millicoulomb per Square Metre (http://qudt.org/vocab/unit/MilliC-PER-M2)"""
    return QUDT_UNIT["MILLIC-PER-M2"]


def get_qudt_unit_gram_per_square_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Square Centimetre (http://qudt.org/vocab/unit/GM-PER-CentiM2)"""
    return QUDT_UNIT["GM-PER-CENTIM2"]


def get_qudt_unit_gram_per_hectare() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Hectare (http://qudt.org/vocab/unit/GM-PER-HA)"""
    return QUDT_UNIT["GM-PER-HA"]


def get_qudt_unit_gram_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Square Metre (http://qudt.org/vocab/unit/GM-PER-M2)"""
    return QUDT_UNIT["GM-PER-M2"]


def get_qudt_unit_gram_per_square_millimetre() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Square Millimetre (http://qudt.org/vocab/unit/GM-PER-MilliM2)"""
    return QUDT_UNIT["GM-PER-MILLIM2"]


def get_qudt_unit_kilogram_per_square_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Square Centimetre (http://qudt.org/vocab/unit/KiloGM-PER-CentiM2)"""
    return QUDT_UNIT["KILOGM-PER-CENTIM2"]


def get_qudt_unit_kilogram_per_square_foot() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Square Foot (http://qudt.org/vocab/unit/KiloGM-PER-FT2)"""
    return QUDT_UNIT["KILOGM-PER-FT2"]


def get_qudt_unit_kilogram_per_hectare() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Hectare (http://qudt.org/vocab/unit/KiloGM-PER-HA)"""
    return QUDT_UNIT["KILOGM-PER-HA"]


def get_qudt_unit_kilogram_per_square_kilometre() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Square Kilometre (http://qudt.org/vocab/unit/KiloGM-PER-KiloM2)"""
    return QUDT_UNIT["KILOGM-PER-KILOM2"]


def get_qudt_unit_kilogram_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Square Metre (http://qudt.org/vocab/unit/KiloGM-PER-M2)"""
    return QUDT_UNIT["KILOGM-PER-M2"]


def get_qudt_unit_pound_mass_per_acre() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Acre (http://qudt.org/vocab/unit/LB-PER-AC)"""
    return QUDT_UNIT["LB-PER-AC"]


def get_qudt_unit_pound_mass_per_square_foot() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Square Foot (http://qudt.org/vocab/unit/LB-PER-FT2)"""
    return QUDT_UNIT["LB-PER-FT2"]


def get_qudt_unit_pound_mass_per_square_inch() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Square Inch (http://qudt.org/vocab/unit/LB-PER-IN2)"""
    return QUDT_UNIT["LB-PER-IN2"]


def get_qudt_unit_pound_mass_per_square_yard() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Square Yard (http://qudt.org/vocab/unit/LB-PER-YD2)"""
    return QUDT_UNIT["LB-PER-YD2"]


def get_qudt_unit_megagram_per_hectare() -> URIRef:
    """Returns the URI for QUDT unit: Megagram per Hectare (http://qudt.org/vocab/unit/MegaGM-PER-HA)"""
    return QUDT_UNIT["MEGAGM-PER-HA"]


def get_qudt_unit_microgram_per_square_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Microgram per Square Centimetre (http://qudt.org/vocab/unit/MicroGM-PER-CentiM2)"""
    return QUDT_UNIT["MICROGM-PER-CENTIM2"]


def get_qudt_unit_microgram_per_square_inch() -> URIRef:
    """Returns the URI for QUDT unit: Microgram per Square Inch (http://qudt.org/vocab/unit/MicroGM-PER-IN2)"""
    return QUDT_UNIT["MICROGM-PER-IN2"]


def get_qudt_unit_milligram_per_square_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Square Centimetre (http://qudt.org/vocab/unit/MilliGM-PER-CentiM2)"""
    return QUDT_UNIT["MILLIGM-PER-CENTIM2"]


def get_qudt_unit_milligram_per_square_decimetre() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Square Decimetre (http://qudt.org/vocab/unit/MilliGM-PER-DeciM2)"""
    return QUDT_UNIT["MILLIGM-PER-DECIM2"]


def get_qudt_unit_milligram_per_hectare() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Hectare (http://qudt.org/vocab/unit/MilliGM-PER-HA)"""
    return QUDT_UNIT["MILLIGM-PER-HA"]


def get_qudt_unit_milligram_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Square Metre (http://qudt.org/vocab/unit/MilliGM-PER-M2)"""
    return QUDT_UNIT["MILLIGM-PER-M2"]


def get_qudt_unit_nanogram_per_square_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Nanogram per Square Centimetre (http://qudt.org/vocab/unit/NanoGM-PER-CentiM2)"""
    return QUDT_UNIT["NANOGM-PER-CENTIM2"]


def get_qudt_unit_ounce_mass_per_square_foot() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass per Square Foot (http://qudt.org/vocab/unit/OZ-PER-FT2)"""
    return QUDT_UNIT["OZ-PER-FT2"]


def get_qudt_unit_ounce_mass_per_square_inch() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass per Square Inch (http://qudt.org/vocab/unit/OZ-PER-IN2)"""
    return QUDT_UNIT["OZ-PER-IN2"]


def get_qudt_unit_ounce_mass_per_square_yard() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass per Square Yard (http://qudt.org/vocab/unit/OZ-PER-YD2)"""
    return QUDT_UNIT["OZ-PER-YD2"]


def get_qudt_unit_slug_per_square_foot() -> URIRef:
    """Returns the URI for QUDT unit: Slug per Square Foot (http://qudt.org/vocab/unit/SLUG-PER-FT2)"""
    return QUDT_UNIT["SLUG-PER-FT2"]


def get_qudt_unit_tonne_per_hectare() -> URIRef:
    """Returns the URI for QUDT unit: Tonne per Hectare (http://qudt.org/vocab/unit/TONNE-PER-HA)"""
    return QUDT_UNIT["TONNE-PER-HA"]


def get_qudt_unit_metric_ton_per_hectare() -> URIRef:
    """Returns the URI for QUDT unit: Metric Ton per Hectare (http://qudt.org/vocab/unit/TON_Metric-PER-HA)"""
    return QUDT_UNIT["TON_METRIC-PER-HA"]


def get_qudt_unit_square_metre_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre per Metre (http://qudt.org/vocab/unit/M2-PER-M)"""
    return QUDT_UNIT["M2-PER-M"]


def get_qudt_unit_square_metre_per_kilowatt() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre per Kilowatt (http://qudt.org/vocab/unit/M2-PER-KiloW)"""
    return QUDT_UNIT["M2-PER-KILOW"]


def get_qudt_unit_square_metre_per_watt() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre per Watt (http://qudt.org/vocab/unit/M2-PER-W)"""
    return QUDT_UNIT["M2-PER-W"]


def get_qudt_unit_square_centimetre_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Square Centimetre per Second (http://qudt.org/vocab/unit/CentiM2-PER-SEC)"""
    return QUDT_UNIT["CENTIM2-PER-SEC"]


def get_qudt_unit_square_foot_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Square Foot per Hour (http://qudt.org/vocab/unit/FT2-PER-HR)"""
    return QUDT_UNIT["FT2-PER-HR"]


def get_qudt_unit_square_foot_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Square Foot per Second (http://qudt.org/vocab/unit/FT2-PER-SEC)"""
    return QUDT_UNIT["FT2-PER-SEC"]


def get_qudt_unit_square_inch_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Square Inch per Second (http://qudt.org/vocab/unit/IN2-PER-SEC)"""
    return QUDT_UNIT["IN2-PER-SEC"]


def get_qudt_unit_square_metre_hertz() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre Hertz (http://qudt.org/vocab/unit/M2-HZ)"""
    return QUDT_UNIT["M2-HZ"]


def get_qudt_unit_square_metre_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre per Hour (http://qudt.org/vocab/unit/M2-PER-HR)"""
    return QUDT_UNIT["M2-PER-HR"]


def get_qudt_unit_square_millimetre_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Square Millimetre per Second (http://qudt.org/vocab/unit/MilliM2-PER-SEC)"""
    return QUDT_UNIT["MILLIM2-PER-SEC"]


def get_qudt_unit_square_metre_per_hectare() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre per Hectare (http://qudt.org/vocab/unit/M2-PER-HA)"""
    return QUDT_UNIT["M2-PER-HA"]


def get_qudt_unit_square_metre_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre per Square Metre (http://qudt.org/vocab/unit/M2-PER-M2)"""
    return QUDT_UNIT["M2-PER-M2"]


def get_qudt_unit_square_foot_degree_fahrenheit() -> URIRef:
    """Returns the URI for QUDT unit: Square Foot Degree Fahrenheit (http://qudt.org/vocab/unit/FT2-DEG_F)"""
    return QUDT_UNIT["FT2-DEG_F"]


def get_qudt_unit_square_metre_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre Kelvin (http://qudt.org/vocab/unit/M2-K)"""
    return QUDT_UNIT["M2-K"]


def get_qudt_unit_square_metre_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre per Kelvin (http://qudt.org/vocab/unit/M2-PER-K)"""
    return QUDT_UNIT["M2-PER-K"]


def get_qudt_unit_square_centimetre_minute() -> URIRef:
    """Returns the URI for QUDT unit: Square Centimetre Minute (http://qudt.org/vocab/unit/CentiM2-MIN)"""
    return QUDT_UNIT["CENTIM2-MIN"]


def get_qudt_unit_square_centimetre_second() -> URIRef:
    """Returns the URI for QUDT unit: Square Centimetre Second (http://qudt.org/vocab/unit/CentiM2-SEC)"""
    return QUDT_UNIT["CENTIM2-SEC"]


def get_qudt_unit_hour_square_foot() -> URIRef:
    """Returns the URI for QUDT unit: Hour Square Foot (http://qudt.org/vocab/unit/HR-FT2)"""
    return QUDT_UNIT["HR-FT2"]


def get_qudt_unit_second_square_foot() -> URIRef:
    """Returns the URI for QUDT unit: Second Square Foot (http://qudt.org/vocab/unit/SEC-FT2)"""
    return QUDT_UNIT["SEC-FT2"]


def get_qudt_unit_square_foot_hour_degree_fahrenheit() -> URIRef:
    """Returns the URI for QUDT unit: Square Foot Hour Degree Fahrenheit (http://qudt.org/vocab/unit/FT2-HR-DEG_F)"""
    return QUDT_UNIT["FT2-HR-DEG_F"]


def get_qudt_unit_square_foot_second_degree_fahrenheit() -> URIRef:
    """Returns the URI for QUDT unit: Square Foot Second Degree Fahrenheit (http://qudt.org/vocab/unit/FT2-SEC-DEG_F)"""
    return QUDT_UNIT["FT2-SEC-DEG_F"]


def get_qudt_unit_british_thermal_unit_international_definition_per_square_foot_hour() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) per Square Foot Hour (http://qudt.org/vocab/unit/BTU_IT-PER-FT2-HR)"""
    return QUDT_UNIT["BTU_IT-PER-FT2-HR"]


def get_qudt_unit_british_thermal_unit_international_definition_per_square_foot_second() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) per Square Foot Second (http://qudt.org/vocab/unit/BTU_IT-PER-FT2-SEC)"""
    return QUDT_UNIT["BTU_IT-PER-FT2-SEC"]


def get_qudt_unit_british_thermal_unit_international_definition_per_hour_square_foot() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) per Hour Square Foot (http://qudt.org/vocab/unit/BTU_IT-PER-HR-FT2)"""
    return QUDT_UNIT["BTU_IT-PER-HR-FT2"]


def get_qudt_unit_british_thermal_unit_international_definition_per_square_inch_second() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) per Square Inch Second (http://qudt.org/vocab/unit/BTU_IT-PER-IN2-SEC)"""
    return QUDT_UNIT["BTU_IT-PER-IN2-SEC"]


def get_qudt_unit_british_thermal_unit_international_definition_per_second_square_foot() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) per Second Square Foot (http://qudt.org/vocab/unit/BTU_IT-PER-SEC-FT2)"""
    return QUDT_UNIT["BTU_IT-PER-SEC-FT2"]


def get_qudt_unit_british_thermal_unit_thermochemical_definition_per_square_foot_hour() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (thermochemical Definition) per Square Foot Hour (http://qudt.org/vocab/unit/BTU_TH-PER-FT2-HR)"""
    return QUDT_UNIT["BTU_TH-PER-FT2-HR"]


def get_qudt_unit_british_thermal_unit_thermochemical_definition_per_square_foot_minute() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (thermochemical Definition) per Square Foot Minute (http://qudt.org/vocab/unit/BTU_TH-PER-FT2-MIN)"""
    return QUDT_UNIT["BTU_TH-PER-FT2-MIN"]


def get_qudt_unit_british_thermal_unit_thermochemical_definition_per_square_foot_second() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (thermochemical Definition) per Square Foot Second (http://qudt.org/vocab/unit/BTU_TH-PER-FT2-SEC)"""
    return QUDT_UNIT["BTU_TH-PER-FT2-SEC"]


def get_qudt_unit_thermochemical_calorie_per_square_centimetre_minute() -> URIRef:
    """Returns the URI for QUDT unit: Thermochemical Calorie per Square Centimetre Minute (http://qudt.org/vocab/unit/CAL_TH-PER-CentiM2-MIN)"""
    return QUDT_UNIT["CAL_TH-PER-CENTIM2-MIN"]


def get_qudt_unit_thermochemical_calorie_per_square_centimetre_second() -> URIRef:
    """Returns the URI for QUDT unit: Thermochemical Calorie per Square Centimetre Second (http://qudt.org/vocab/unit/CAL_TH-PER-CentiM2-SEC)"""
    return QUDT_UNIT["CAL_TH-PER-CENTIM2-SEC"]


def get_qudt_unit_erg_per_square_centimetre_second() -> URIRef:
    """Returns the URI for QUDT unit: Erg per Square Centimetre Second (http://qudt.org/vocab/unit/ERG-PER-CentiM2-SEC)"""
    return QUDT_UNIT["ERG-PER-CENTIM2-SEC"]


def get_qudt_unit_foot_pound_force_per_square_foot_second() -> URIRef:
    """Returns the URI for QUDT unit: Foot Pound Force per Square Foot Second (http://qudt.org/vocab/unit/FT-LB_F-PER-FT2-SEC)"""
    return QUDT_UNIT["FT-LB_F-PER-FT2-SEC"]


def get_qudt_unit_joule_per_square_centimetre_day() -> URIRef:
    """Returns the URI for QUDT unit: Joule per Square Centimetre Day (http://qudt.org/vocab/unit/J-PER-CentiM2-DAY)"""
    return QUDT_UNIT["J-PER-CENTIM2-DAY"]


def get_qudt_unit_kilocalorie_per_square_centimetre_minute() -> URIRef:
    """Returns the URI for QUDT unit: Kilocalorie per Square Centimetre Minute (http://qudt.org/vocab/unit/KiloCAL-PER-CentiM2-MIN)"""
    return QUDT_UNIT["KILOCAL-PER-CENTIM2-MIN"]


def get_qudt_unit_kilocalorie_per_square_centimetre_second() -> URIRef:
    """Returns the URI for QUDT unit: Kilocalorie per Square Centimetre Second (http://qudt.org/vocab/unit/KiloCAL-PER-CentiM2-SEC)"""
    return QUDT_UNIT["KILOCAL-PER-CENTIM2-SEC"]


def get_qudt_unit_kilowatt_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kilowatt per Square Metre (http://qudt.org/vocab/unit/KiloW-PER-M2)"""
    return QUDT_UNIT["KILOW-PER-M2"]


def get_qudt_unit_metre_pascal_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Metre Pascal per Second (http://qudt.org/vocab/unit/M-PA-PER-SEC)"""
    return QUDT_UNIT["M-PA-PER-SEC"]


def get_qudt_unit_microwatt_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Microwatt per Square Metre (http://qudt.org/vocab/unit/MicroW-PER-M2)"""
    return QUDT_UNIT["MICROW-PER-M2"]


def get_qudt_unit_milliwatt_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Milliwatt per Square Metre (http://qudt.org/vocab/unit/MilliW-PER-M2)"""
    return QUDT_UNIT["MILLIW-PER-M2"]


def get_qudt_unit_nanowatt_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Nanowatt per Square Metre (http://qudt.org/vocab/unit/NanoW-PER-M2)"""
    return QUDT_UNIT["NANOW-PER-M2"]


def get_qudt_unit_picowatt_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Picowatt per Square Metre (http://qudt.org/vocab/unit/PicoW-PER-M2)"""
    return QUDT_UNIT["PICOW-PER-M2"]


def get_qudt_unit_watt_per_square_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Watt per Square Centimetre (http://qudt.org/vocab/unit/W-PER-CentiM2)"""
    return QUDT_UNIT["W-PER-CENTIM2"]


def get_qudt_unit_watt_per_square_foot() -> URIRef:
    """Returns the URI for QUDT unit: Watt per Square Foot (http://qudt.org/vocab/unit/W-PER-FT2)"""
    return QUDT_UNIT["W-PER-FT2"]


def get_qudt_unit_watt_per_square_inch() -> URIRef:
    """Returns the URI for QUDT unit: Watt per Square Inch (http://qudt.org/vocab/unit/W-PER-IN2)"""
    return QUDT_UNIT["W-PER-IN2"]


def get_qudt_unit_watt_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Watt per Square Metre (http://qudt.org/vocab/unit/W-PER-M2)"""
    return QUDT_UNIT["W-PER-M2"]


def get_qudt_unit_cubic_centimetre_per_mole_second() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Centimetre per Mole Second (http://qudt.org/vocab/unit/CentiM3-PER-MOL-SEC)"""
    return QUDT_UNIT["CENTIM3-PER-MOL-SEC"]


def get_qudt_unit_litre_per_mole_second() -> URIRef:
    """Returns the URI for QUDT unit: Litre per Mole Second (http://qudt.org/vocab/unit/L-PER-MOL-SEC)"""
    return QUDT_UNIT["L-PER-MOL-SEC"]


def get_qudt_unit_cubic_metre_per_mole_second() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Metre per Mole Second (http://qudt.org/vocab/unit/M3-PER-MOL-SEC)"""
    return QUDT_UNIT["M3-PER-MOL-SEC"]


def get_qudt_unit_ampere_hour() -> URIRef:
    """Returns the URI for QUDT unit: Ampere Hour (http://qudt.org/vocab/unit/A-HR)"""
    return QUDT_UNIT["A-HR"]


def get_qudt_unit_ampere_second() -> URIRef:
    """Returns the URI for QUDT unit: Ampere Second (http://qudt.org/vocab/unit/A-SEC)"""
    return QUDT_UNIT["A-SEC"]


def get_qudt_unit_attocoulomb() -> URIRef:
    """Returns the URI for QUDT unit: Attocoulomb (http://qudt.org/vocab/unit/AttoC)"""
    return QUDT_UNIT["ATTOC"]


def get_qudt_unit_abcoulomb() -> URIRef:
    """Returns the URI for QUDT unit: Abcoulomb (http://qudt.org/vocab/unit/C_Ab)"""
    return QUDT_UNIT["C_AB"]


def get_qudt_unit_statcoulomb() -> URIRef:
    """Returns the URI for QUDT unit: Statcoulomb (http://qudt.org/vocab/unit/C_Stat)"""
    return QUDT_UNIT["C_STAT"]


def get_qudt_unit_centicoulomb() -> URIRef:
    """Returns the URI for QUDT unit: Centicoulomb (http://qudt.org/vocab/unit/CentiC)"""
    return QUDT_UNIT["CENTIC"]


def get_qudt_unit_decacoulomb() -> URIRef:
    """Returns the URI for QUDT unit: Decacoulomb (http://qudt.org/vocab/unit/DecaC)"""
    return QUDT_UNIT["DECAC"]


def get_qudt_unit_decicoulomb() -> URIRef:
    """Returns the URI for QUDT unit: Decicoulomb (http://qudt.org/vocab/unit/DeciC)"""
    return QUDT_UNIT["DECIC"]


def get_qudt_unit_elementary_charge() -> URIRef:
    """Returns the URI for QUDT unit: Elementary Charge (http://qudt.org/vocab/unit/E)"""
    return QUDT_UNIT["E"]


def get_qudt_unit_exacoulomb() -> URIRef:
    """Returns the URI for QUDT unit: Exacoulomb (http://qudt.org/vocab/unit/ExaC)"""
    return QUDT_UNIT["EXAC"]


def get_qudt_unit_faraday() -> URIRef:
    """Returns the URI for QUDT unit: Faraday (http://qudt.org/vocab/unit/F)"""
    return QUDT_UNIT["F"]


def get_qudt_unit_franklin() -> URIRef:
    """Returns the URI for QUDT unit: Franklin (http://qudt.org/vocab/unit/FR)"""
    return QUDT_UNIT["FR"]


def get_qudt_unit_femtocoulomb() -> URIRef:
    """Returns the URI for QUDT unit: Femtocoulomb (http://qudt.org/vocab/unit/FemtoC)"""
    return QUDT_UNIT["FEMTOC"]


def get_qudt_unit_gigacoulomb() -> URIRef:
    """Returns the URI for QUDT unit: Gigacoulomb (http://qudt.org/vocab/unit/GigaC)"""
    return QUDT_UNIT["GIGAC"]


def get_qudt_unit_hectocoulomb() -> URIRef:
    """Returns the URI for QUDT unit: Hectocoulomb (http://qudt.org/vocab/unit/HectoC)"""
    return QUDT_UNIT["HECTOC"]


def get_qudt_unit_kiloampere_hour() -> URIRef:
    """Returns the URI for QUDT unit: Kiloampere Hour (http://qudt.org/vocab/unit/KiloA-HR)"""
    return QUDT_UNIT["KILOA-HR"]


def get_qudt_unit_kilocoulomb() -> URIRef:
    """Returns the URI for QUDT unit: Kilocoulomb (http://qudt.org/vocab/unit/KiloC)"""
    return QUDT_UNIT["KILOC"]


def get_qudt_unit_kilojoule_per_kilovolt() -> URIRef:
    """Returns the URI for QUDT unit: Kilojoule per Kilovolt (http://qudt.org/vocab/unit/KiloJ-PER-KiloV)"""
    return QUDT_UNIT["KILOJ-PER-KILOV"]


def get_qudt_unit_megacoulomb() -> URIRef:
    """Returns the URI for QUDT unit: Megacoulomb (http://qudt.org/vocab/unit/MegaC)"""
    return QUDT_UNIT["MEGAC"]


def get_qudt_unit_microcoulomb() -> URIRef:
    """Returns the URI for QUDT unit: Microcoulomb (http://qudt.org/vocab/unit/MicroC)"""
    return QUDT_UNIT["MICROC"]


def get_qudt_unit_milliampere_hour() -> URIRef:
    """Returns the URI for QUDT unit: Milliampere Hour (http://qudt.org/vocab/unit/MilliA-HR)"""
    return QUDT_UNIT["MILLIA-HR"]


def get_qudt_unit_milliampere_second() -> URIRef:
    """Returns the URI for QUDT unit: Milliampere Second (http://qudt.org/vocab/unit/MilliA-SEC)"""
    return QUDT_UNIT["MILLIA-SEC"]


def get_qudt_unit_millicoulomb() -> URIRef:
    """Returns the URI for QUDT unit: Millicoulomb (http://qudt.org/vocab/unit/MilliC)"""
    return QUDT_UNIT["MILLIC"]


def get_qudt_unit_nanocoulomb() -> URIRef:
    """Returns the URI for QUDT unit: Nanocoulomb (http://qudt.org/vocab/unit/NanoC)"""
    return QUDT_UNIT["NANOC"]


def get_qudt_unit_petacoulomb() -> URIRef:
    """Returns the URI for QUDT unit: Petacoulomb (http://qudt.org/vocab/unit/PetaC)"""
    return QUDT_UNIT["PETAC"]


def get_qudt_unit_picocoulomb() -> URIRef:
    """Returns the URI for QUDT unit: Picocoulomb (http://qudt.org/vocab/unit/PicoC)"""
    return QUDT_UNIT["PICOC"]


def get_qudt_unit_planck_charge() -> URIRef:
    """Returns the URI for QUDT unit: Planck Charge (http://qudt.org/vocab/unit/PlanckCharge)"""
    return QUDT_UNIT["PLANCKCHARGE"]


def get_qudt_unit_teracoulomb() -> URIRef:
    """Returns the URI for QUDT unit: Teracoulomb (http://qudt.org/vocab/unit/TeraC)"""
    return QUDT_UNIT["TERAC"]


def get_qudt_unit_yoctocoulomb() -> URIRef:
    """Returns the URI for QUDT unit: Yoctocoulomb (http://qudt.org/vocab/unit/YoctoC)"""
    return QUDT_UNIT["YOCTOC"]


def get_qudt_unit_yottacoulomb() -> URIRef:
    """Returns the URI for QUDT unit: Yottacoulomb (http://qudt.org/vocab/unit/YottaC)"""
    return QUDT_UNIT["YOTTAC"]


def get_qudt_unit_zeptocoulomb() -> URIRef:
    """Returns the URI for QUDT unit: Zeptocoulomb (http://qudt.org/vocab/unit/ZeptoC)"""
    return QUDT_UNIT["ZEPTOC"]


def get_qudt_unit_zettacoulomb() -> URIRef:
    """Returns the URI for QUDT unit: Zettacoulomb (http://qudt.org/vocab/unit/ZettaC)"""
    return QUDT_UNIT["ZETTAC"]


def get_qudt_unit_atomic_mass_unit() -> URIRef:
    """Returns the URI for QUDT unit: Atomic Mass Unit (http://qudt.org/vocab/unit/AMU)"""
    return QUDT_UNIT["AMU"]


def get_qudt_unit_carat() -> URIRef:
    """Returns the URI for QUDT unit: Carat (http://qudt.org/vocab/unit/CARAT)"""
    return QUDT_UNIT["CARAT"]


def get_qudt_unit_long_hundred_weight() -> URIRef:
    """Returns the URI for QUDT unit: Long Hundred Weight (http://qudt.org/vocab/unit/CWT_LONG)"""
    return QUDT_UNIT["CWT_LONG"]


def get_qudt_unit_hundred_weight_short() -> URIRef:
    """Returns the URI for QUDT unit: Hundred Weight - Short (http://qudt.org/vocab/unit/CWT_SHORT)"""
    return QUDT_UNIT["CWT_SHORT"]


def get_qudt_unit_centigram() -> URIRef:
    """Returns the URI for QUDT unit: Centigram (http://qudt.org/vocab/unit/CentiGM)"""
    return QUDT_UNIT["CENTIGM"]


def get_qudt_unit_dram_uk() -> URIRef:
    """Returns the URI for QUDT unit: Dram (UK) (http://qudt.org/vocab/unit/DRAM_UK)"""
    return QUDT_UNIT["DRAM_UK"]


def get_qudt_unit_dram_us() -> URIRef:
    """Returns the URI for QUDT unit: Dram (US) (http://qudt.org/vocab/unit/DRAM_US)"""
    return QUDT_UNIT["DRAM_US"]


def get_qudt_unit_penny_weight() -> URIRef:
    """Returns the URI for QUDT unit: Penny Weight (http://qudt.org/vocab/unit/DWT)"""
    return QUDT_UNIT["DWT"]


def get_qudt_unit_decagram() -> URIRef:
    """Returns the URI for QUDT unit: Decagram (http://qudt.org/vocab/unit/DecaGM)"""
    return QUDT_UNIT["DECAGM"]


def get_qudt_unit_decigram() -> URIRef:
    """Returns the URI for QUDT unit: Decigram (http://qudt.org/vocab/unit/DeciGM)"""
    return QUDT_UNIT["DECIGM"]


def get_qudt_unit_decitonne() -> URIRef:
    """Returns the URI for QUDT unit: Decitonne (http://qudt.org/vocab/unit/DeciTONNE)"""
    return QUDT_UNIT["DECITONNE"]


def get_qudt_unit_deci_metric_ton() -> URIRef:
    """Returns the URI for QUDT unit: Deci Metric Ton (http://qudt.org/vocab/unit/DeciTON_Metric)"""
    return QUDT_UNIT["DECITON_METRIC"]


def get_qudt_unit_earth_mass() -> URIRef:
    """Returns the URI for QUDT unit: Earth Mass (http://qudt.org/vocab/unit/EarthMass)"""
    return QUDT_UNIT["EARTHMASS"]


def get_qudt_unit_femtogram() -> URIRef:
    """Returns the URI for QUDT unit: Femtogram (http://qudt.org/vocab/unit/FemtoGM)"""
    return QUDT_UNIT["FEMTOGM"]


def get_qudt_unit_gram() -> URIRef:
    """Returns the URI for QUDT unit: Gram (http://qudt.org/vocab/unit/GM)"""
    return QUDT_UNIT["GM"]


def get_qudt_unit_gram_of_carbon() -> URIRef:
    """Returns the URI for QUDT unit: Gram of Carbon (http://qudt.org/vocab/unit/GM_Carbon)"""
    return QUDT_UNIT["GM_CARBON"]


def get_qudt_unit_dry_gram() -> URIRef:
    """Returns the URI for QUDT unit: Dry Gram (http://qudt.org/vocab/unit/GM_DRY)"""
    return QUDT_UNIT["GM_DRY"]


def get_qudt_unit_gram_of_nitrogen() -> URIRef:
    """Returns the URI for QUDT unit: Gram of Nitrogen (http://qudt.org/vocab/unit/GM_Nitrogen)"""
    return QUDT_UNIT["GM_NITROGEN"]


def get_qudt_unit_grain() -> URIRef:
    """Returns the URI for QUDT unit: Grain (http://qudt.org/vocab/unit/GRAIN)"""
    return QUDT_UNIT["GRAIN"]


def get_qudt_unit_hectogram() -> URIRef:
    """Returns the URI for QUDT unit: Hectogram (http://qudt.org/vocab/unit/HectoGM)"""
    return QUDT_UNIT["HECTOGM"]


def get_qudt_unit_hundredweight_uk() -> URIRef:
    """Returns the URI for QUDT unit: Hundredweight (UK) (http://qudt.org/vocab/unit/Hundredweight_UK)"""
    return QUDT_UNIT["HUNDREDWEIGHT_UK"]


def get_qudt_unit_hundredweight_us() -> URIRef:
    """Returns the URI for QUDT unit: Hundredweight (US) (http://qudt.org/vocab/unit/Hundredweight_US)"""
    return QUDT_UNIT["HUNDREDWEIGHT_US"]


def get_qudt_unit_kilo_pound_mass() -> URIRef:
    """Returns the URI for QUDT unit: Kilo Pound Mass (http://qudt.org/vocab/unit/KiloLB)"""
    return QUDT_UNIT["KILOLB"]


def get_qudt_unit_kilotonne() -> URIRef:
    """Returns the URI for QUDT unit: Kilotonne (http://qudt.org/vocab/unit/KiloTONNE)"""
    return QUDT_UNIT["KILOTONNE"]


def get_qudt_unit_kilo_metric_ton() -> URIRef:
    """Returns the URI for QUDT unit: Kilo Metric Ton (http://qudt.org/vocab/unit/KiloTON_Metric)"""
    return QUDT_UNIT["KILOTON_METRIC"]


def get_qudt_unit_pound_mass() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass (http://qudt.org/vocab/unit/LB)"""
    return QUDT_UNIT["LB"]


def get_qudt_unit_pound_troy() -> URIRef:
    """Returns the URI for QUDT unit: Pound Troy (http://qudt.org/vocab/unit/LB_T)"""
    return QUDT_UNIT["LB_T"]


def get_qudt_unit_lunar_mass() -> URIRef:
    """Returns the URI for QUDT unit: Lunar Mass (http://qudt.org/vocab/unit/LunarMass)"""
    return QUDT_UNIT["LUNARMASS"]


def get_qudt_unit_momme_pearl() -> URIRef:
    """Returns the URI for QUDT unit: Momme (pearl) (http://qudt.org/vocab/unit/MOMME_Pearl)"""
    return QUDT_UNIT["MOMME_PEARL"]


def get_qudt_unit_momme_textile() -> URIRef:
    """Returns the URI for QUDT unit: Momme (textile) (http://qudt.org/vocab/unit/MOMME_Textile)"""
    return QUDT_UNIT["MOMME_TEXTILE"]


def get_qudt_unit_megagram() -> URIRef:
    """Returns the URI for QUDT unit: Megagram (http://qudt.org/vocab/unit/MegaGM)"""
    return QUDT_UNIT["MEGAGM"]


def get_qudt_unit_megaton() -> URIRef:
    """Returns the URI for QUDT unit: Megaton (http://qudt.org/vocab/unit/MegaTON)"""
    return QUDT_UNIT["MEGATON"]


def get_qudt_unit_megatonne() -> URIRef:
    """Returns the URI for QUDT unit: Megatonne (http://qudt.org/vocab/unit/MegaTONNE)"""
    return QUDT_UNIT["MEGATONNE"]


def get_qudt_unit_microgram() -> URIRef:
    """Returns the URI for QUDT unit: Microgram (http://qudt.org/vocab/unit/MicroGM)"""
    return QUDT_UNIT["MICROGM"]


def get_qudt_unit_milligram() -> URIRef:
    """Returns the URI for QUDT unit: Milligram (http://qudt.org/vocab/unit/MilliGM)"""
    return QUDT_UNIT["MILLIGM"]


def get_qudt_unit_nanogram() -> URIRef:
    """Returns the URI for QUDT unit: Nanogram (http://qudt.org/vocab/unit/NanoGM)"""
    return QUDT_UNIT["NANOGM"]


def get_qudt_unit_ounce_mass() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass (http://qudt.org/vocab/unit/OZ)"""
    return QUDT_UNIT["OZ"]


def get_qudt_unit_ounce_troy() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Troy (http://qudt.org/vocab/unit/OZ_TROY)"""
    return QUDT_UNIT["OZ_TROY"]


def get_qudt_unit_pennyweight() -> URIRef:
    """Returns the URI for QUDT unit: Pennyweight (http://qudt.org/vocab/unit/PENNYWEIGHT)"""
    return QUDT_UNIT["PENNYWEIGHT"]


def get_qudt_unit_pfund() -> URIRef:
    """Returns the URI for QUDT unit: Pfund (http://qudt.org/vocab/unit/PFUND)"""
    return QUDT_UNIT["PFUND"]


def get_qudt_unit_picogram() -> URIRef:
    """Returns the URI for QUDT unit: Picogram (http://qudt.org/vocab/unit/PicoGM)"""
    return QUDT_UNIT["PICOGM"]


def get_qudt_unit_planck_mass() -> URIRef:
    """Returns the URI for QUDT unit: Planck Mass (http://qudt.org/vocab/unit/PlanckMass)"""
    return QUDT_UNIT["PLANCKMASS"]


def get_qudt_unit_quarter_uk() -> URIRef:
    """Returns the URI for QUDT unit: Quarter (UK) (http://qudt.org/vocab/unit/Quarter_UK)"""
    return QUDT_UNIT["QUARTER_UK"]


def get_qudt_unit_slug() -> URIRef:
    """Returns the URI for QUDT unit: Slug (http://qudt.org/vocab/unit/SLUG)"""
    return QUDT_UNIT["SLUG"]


def get_qudt_unit_solar_mass() -> URIRef:
    """Returns the URI for QUDT unit: Solar Mass (http://qudt.org/vocab/unit/SolarMass)"""
    return QUDT_UNIT["SOLARMASS"]


def get_qudt_unit_stone_uk() -> URIRef:
    """Returns the URI for QUDT unit: Stone (UK) (http://qudt.org/vocab/unit/Stone_UK)"""
    return QUDT_UNIT["STONE_UK"]


def get_qudt_unit_ton() -> URIRef:
    """Returns the URI for QUDT unit: Ton (http://qudt.org/vocab/unit/TON)"""
    return QUDT_UNIT["TON"]


def get_qudt_unit_tonne() -> URIRef:
    """Returns the URI for QUDT unit: Tonne (http://qudt.org/vocab/unit/TONNE)"""
    return QUDT_UNIT["TONNE"]


def get_qudt_unit_assay_ton() -> URIRef:
    """Returns the URI for QUDT unit: Assay Ton (http://qudt.org/vocab/unit/TON_Assay)"""
    return QUDT_UNIT["TON_ASSAY"]


def get_qudt_unit_long_ton() -> URIRef:
    """Returns the URI for QUDT unit: Long Ton (http://qudt.org/vocab/unit/TON_LONG)"""
    return QUDT_UNIT["TON_LONG"]


def get_qudt_unit_metric_ton() -> URIRef:
    """Returns the URI for QUDT unit: Metric Ton (http://qudt.org/vocab/unit/TON_Metric)"""
    return QUDT_UNIT["TON_METRIC"]


def get_qudt_unit_short_ton() -> URIRef:
    """Returns the URI for QUDT unit: Short Ton (http://qudt.org/vocab/unit/TON_SHORT)"""
    return QUDT_UNIT["TON_SHORT"]


def get_qudt_unit_ton_uk() -> URIRef:
    """Returns the URI for QUDT unit: Ton (UK) (http://qudt.org/vocab/unit/TON_UK)"""
    return QUDT_UNIT["TON_UK"]


def get_qudt_unit_ton_us() -> URIRef:
    """Returns the URI for QUDT unit: Ton (US) (http://qudt.org/vocab/unit/TON_US)"""
    return QUDT_UNIT["TON_US"]


def get_qudt_unit_atomic_number() -> URIRef:
    """Returns the URI for QUDT unit: Atomic-number (http://qudt.org/vocab/unit/Z)"""
    return QUDT_UNIT["Z"]


def get_qudt_unit_percent_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Percent per Metre (http://qudt.org/vocab/unit/PERCENT-PER-M)"""
    return QUDT_UNIT["PERCENT-PER-M"]


def get_qudt_unit_bel() -> URIRef:
    """Returns the URI for QUDT unit: Bel (http://qudt.org/vocab/unit/B)"""
    return QUDT_UNIT["B"]


def get_qudt_unit_decibel() -> URIRef:
    """Returns the URI for QUDT unit: Decibel (http://qudt.org/vocab/unit/DeciB)"""
    return QUDT_UNIT["DECIB"]


def get_qudt_unit_decibel_with_a_weighting() -> URIRef:
    """Returns the URI for QUDT unit: Decibel with A-weighting (http://qudt.org/vocab/unit/DeciB_A)"""
    return QUDT_UNIT["DECIB_A"]


def get_qudt_unit_decibel_isotropic() -> URIRef:
    """Returns the URI for QUDT unit: Decibel Isotropic (http://qudt.org/vocab/unit/DeciB_ISO)"""
    return QUDT_UNIT["DECIB_ISO"]


def get_qudt_unit_decibel_referred_to_1mw() -> URIRef:
    """Returns the URI for QUDT unit: Decibel Referred to 1mw (http://qudt.org/vocab/unit/DeciB_M)"""
    return QUDT_UNIT["DECIB_M"]


def get_qudt_unit_decibel_with_z_weighting() -> URIRef:
    """Returns the URI for QUDT unit: Decibel with Z-weighting (http://qudt.org/vocab/unit/DeciB_Z)"""
    return QUDT_UNIT["DECIB_Z"]


def get_qudt_unit_ampere_per_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Ampere per Centimetre (http://qudt.org/vocab/unit/A-PER-CentiM)"""
    return QUDT_UNIT["A-PER-CENTIM"]


def get_qudt_unit_ampere_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Ampere per Metre (http://qudt.org/vocab/unit/A-PER-M)"""
    return QUDT_UNIT["A-PER-M"]


def get_qudt_unit_ampere_per_millimetre() -> URIRef:
    """Returns the URI for QUDT unit: Ampere per Millimetre (http://qudt.org/vocab/unit/A-PER-MilliM)"""
    return QUDT_UNIT["A-PER-MILLIM"]


def get_qudt_unit_ampere_turn_per_inch() -> URIRef:
    """Returns the URI for QUDT unit: Ampere Turn per Inch (http://qudt.org/vocab/unit/AT-PER-IN)"""
    return QUDT_UNIT["AT-PER-IN"]


def get_qudt_unit_ampere_turn_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Ampere Turn per Metre (http://qudt.org/vocab/unit/AT-PER-M)"""
    return QUDT_UNIT["AT-PER-M"]


def get_qudt_unit_kiloampere_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kiloampere per Metre (http://qudt.org/vocab/unit/KiloA-PER-M)"""
    return QUDT_UNIT["KILOA-PER-M"]


def get_qudt_unit_milliampere_per_inch() -> URIRef:
    """Returns the URI for QUDT unit: Milliampere per Inch (http://qudt.org/vocab/unit/MilliA-PER-IN)"""
    return QUDT_UNIT["MILLIA-PER-IN"]


def get_qudt_unit_milliampere_per_millimetre() -> URIRef:
    """Returns the URI for QUDT unit: Milliampere per Millimetre (http://qudt.org/vocab/unit/MilliA-PER-MilliM)"""
    return QUDT_UNIT["MILLIA-PER-MILLIM"]


def get_qudt_unit_oersted() -> URIRef:
    """Returns the URI for QUDT unit: Oersted (http://qudt.org/vocab/unit/OERSTED)"""
    return QUDT_UNIT["OERSTED"]


def get_qudt_unit_centinewton() -> URIRef:
    """Returns the URI for QUDT unit: Centinewton (http://qudt.org/vocab/unit/CentiN)"""
    return QUDT_UNIT["CENTIN"]


def get_qudt_unit_dyne() -> URIRef:
    """Returns the URI for QUDT unit: Dyne (http://qudt.org/vocab/unit/DYN)"""
    return QUDT_UNIT["DYN"]


def get_qudt_unit_decinewton() -> URIRef:
    """Returns the URI for QUDT unit: Decinewton (http://qudt.org/vocab/unit/DeciN)"""
    return QUDT_UNIT["DECIN"]


def get_qudt_unit_gram_force() -> URIRef:
    """Returns the URI for QUDT unit: Gram Force (http://qudt.org/vocab/unit/GM_F)"""
    return QUDT_UNIT["GM_F"]


def get_qudt_unit_giganewton() -> URIRef:
    """Returns the URI for QUDT unit: Giganewton (http://qudt.org/vocab/unit/GigaN)"""
    return QUDT_UNIT["GIGAN"]


def get_qudt_unit_kip() -> URIRef:
    """Returns the URI for QUDT unit: Kip (http://qudt.org/vocab/unit/KIP_F)"""
    return QUDT_UNIT["KIP_F"]


def get_qudt_unit_kilogram_metre_per_square_second() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram Metre per Square Second (http://qudt.org/vocab/unit/KiloGM-M-PER-SEC2)"""
    return QUDT_UNIT["KILOGM-M-PER-SEC2"]


def get_qudt_unit_kilo_gram_force() -> URIRef:
    """Returns the URI for QUDT unit: Kilo Gram Force (http://qudt.org/vocab/unit/KiloGM_F)"""
    return QUDT_UNIT["KILOGM_F"]


def get_qudt_unit_kilo_pound_force() -> URIRef:
    """Returns the URI for QUDT unit: Kilo Pound Force (http://qudt.org/vocab/unit/KiloLB_F)"""
    return QUDT_UNIT["KILOLB_F"]


def get_qudt_unit_kilonewton() -> URIRef:
    """Returns the URI for QUDT unit: Kilonewton (http://qudt.org/vocab/unit/KiloN)"""
    return QUDT_UNIT["KILON"]


def get_qudt_unit_kilopond() -> URIRef:
    """Returns the URI for QUDT unit: Kilopond (http://qudt.org/vocab/unit/KiloPOND)"""
    return QUDT_UNIT["KILOPOND"]


def get_qudt_unit_pound_force() -> URIRef:
    """Returns the URI for QUDT unit: Pound Force (http://qudt.org/vocab/unit/LB_F)"""
    return QUDT_UNIT["LB_F"]


def get_qudt_unit_mega_pound_force() -> URIRef:
    """Returns the URI for QUDT unit: Mega Pound Force (http://qudt.org/vocab/unit/MegaLB_F)"""
    return QUDT_UNIT["MEGALB_F"]


def get_qudt_unit_meganewton() -> URIRef:
    """Returns the URI for QUDT unit: Meganewton (http://qudt.org/vocab/unit/MegaN)"""
    return QUDT_UNIT["MEGAN"]


def get_qudt_unit_micronewton() -> URIRef:
    """Returns the URI for QUDT unit: Micronewton (http://qudt.org/vocab/unit/MicroN)"""
    return QUDT_UNIT["MICRON"]


def get_qudt_unit_millinewton() -> URIRef:
    """Returns the URI for QUDT unit: Millinewton (http://qudt.org/vocab/unit/MilliN)"""
    return QUDT_UNIT["MILLIN"]


def get_qudt_unit_nanonewton() -> URIRef:
    """Returns the URI for QUDT unit: Nanonewton (http://qudt.org/vocab/unit/NanoN)"""
    return QUDT_UNIT["NANON"]


def get_qudt_unit_imperial_ounce_force() -> URIRef:
    """Returns the URI for QUDT unit: Imperial Ounce Force (http://qudt.org/vocab/unit/OZ_F)"""
    return QUDT_UNIT["OZ_F"]


def get_qudt_unit_poundal() -> URIRef:
    """Returns the URI for QUDT unit: Poundal (http://qudt.org/vocab/unit/PDL)"""
    return QUDT_UNIT["PDL"]


def get_qudt_unit_pond() -> URIRef:
    """Returns the URI for QUDT unit: Pond (http://qudt.org/vocab/unit/POND)"""
    return QUDT_UNIT["POND"]


def get_qudt_unit_planck_force() -> URIRef:
    """Returns the URI for QUDT unit: Planck Force (http://qudt.org/vocab/unit/PlanckForce)"""
    return QUDT_UNIT["PLANCKFORCE"]


def get_qudt_unit_ton_force_us_short() -> URIRef:
    """Returns the URI for QUDT unit: Ton Force (us Short) (http://qudt.org/vocab/unit/TON_F_US)"""
    return QUDT_UNIT["TON_F_US"]


def get_qudt_unit_ampere_minute() -> URIRef:
    """Returns the URI for QUDT unit: Ampere Minute (http://qudt.org/vocab/unit/A-MIN)"""
    return QUDT_UNIT["A-MIN"]


def get_qudt_unit_centinewton_metre() -> URIRef:
    """Returns the URI for QUDT unit: Centinewton Metre (http://qudt.org/vocab/unit/CentiN-M)"""
    return QUDT_UNIT["CENTIN-M"]


def get_qudt_unit_dyne_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Dyne Centimetre (http://qudt.org/vocab/unit/DYN-CentiM)"""
    return QUDT_UNIT["DYN-CENTIM"]


def get_qudt_unit_dyne_metre() -> URIRef:
    """Returns the URI for QUDT unit: Dyne Metre (http://qudt.org/vocab/unit/DYN-M)"""
    return QUDT_UNIT["DYN-M"]


def get_qudt_unit_decinewton_metre() -> URIRef:
    """Returns the URI for QUDT unit: Decinewton Metre (http://qudt.org/vocab/unit/DeciN-M)"""
    return QUDT_UNIT["DECIN-M"]


def get_qudt_unit_inch_poundal() -> URIRef:
    """Returns the URI for QUDT unit: Inch Poundal (http://qudt.org/vocab/unit/IN-PDL)"""
    return QUDT_UNIT["IN-PDL"]


def get_qudt_unit_kilo_gram_force_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kilo Gram Force Metre (http://qudt.org/vocab/unit/KiloGM_F-M)"""
    return QUDT_UNIT["KILOGM_F-M"]


def get_qudt_unit_kilonewton_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kilonewton Metre (http://qudt.org/vocab/unit/KiloN-M)"""
    return QUDT_UNIT["KILON-M"]


def get_qudt_unit_pound_force_foot() -> URIRef:
    """Returns the URI for QUDT unit: Pound Force Foot (http://qudt.org/vocab/unit/LB_F-FT)"""
    return QUDT_UNIT["LB_F-FT"]


def get_qudt_unit_pound_force_inch() -> URIRef:
    """Returns the URI for QUDT unit: Pound Force Inch (http://qudt.org/vocab/unit/LB_F-IN)"""
    return QUDT_UNIT["LB_F-IN"]


def get_qudt_unit_meganewton_metre() -> URIRef:
    """Returns the URI for QUDT unit: Meganewton Metre (http://qudt.org/vocab/unit/MegaN-M)"""
    return QUDT_UNIT["MEGAN-M"]


def get_qudt_unit_micronewton_metre() -> URIRef:
    """Returns the URI for QUDT unit: Micronewton Metre (http://qudt.org/vocab/unit/MicroN-M)"""
    return QUDT_UNIT["MICRON-M"]


def get_qudt_unit_millinewton_metre() -> URIRef:
    """Returns the URI for QUDT unit: Millinewton Metre (http://qudt.org/vocab/unit/MilliN-M)"""
    return QUDT_UNIT["MILLIN-M"]


def get_qudt_unit_newton_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Newton Centimetre (http://qudt.org/vocab/unit/N-CentiM)"""
    return QUDT_UNIT["N-CENTIM"]


def get_qudt_unit_newton_metre() -> URIRef:
    """Returns the URI for QUDT unit: Newton Metre (http://qudt.org/vocab/unit/N-M)"""
    return QUDT_UNIT["N-M"]


def get_qudt_unit_imperial_ounce_force_inch() -> URIRef:
    """Returns the URI for QUDT unit: Imperial Ounce Force Inch (http://qudt.org/vocab/unit/OZ_F-IN)"""
    return QUDT_UNIT["OZ_F-IN"]


def get_qudt_unit_poundal_foot() -> URIRef:
    """Returns the URI for QUDT unit: Poundal Foot (http://qudt.org/vocab/unit/PDL-FT)"""
    return QUDT_UNIT["PDL-FT"]


def get_qudt_unit_poundal_inch() -> URIRef:
    """Returns the URI for QUDT unit: Poundal Inch (http://qudt.org/vocab/unit/PDL-IN)"""
    return QUDT_UNIT["PDL-IN"]


def get_qudt_unit_octet_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Octet per Second (http://qudt.org/vocab/unit/OCTET-PER-SEC)"""
    return QUDT_UNIT["OCTET-PER-SEC"]


def get_qudt_unit_degree_celsius() -> URIRef:
    """Returns the URI for QUDT unit: Degree Celsius (http://qudt.org/vocab/unit/DEG_C)"""
    return QUDT_UNIT["DEG_C"]


def get_qudt_unit_degree_fahrenheit() -> URIRef:
    """Returns the URI for QUDT unit: Degree Fahrenheit (http://qudt.org/vocab/unit/DEG_F)"""
    return QUDT_UNIT["DEG_F"]


def get_qudt_unit_degree_rankine() -> URIRef:
    """Returns the URI for QUDT unit: Degree Rankine (http://qudt.org/vocab/unit/DEG_R)"""
    return QUDT_UNIT["DEG_R"]


def get_qudt_unit_decakelvin() -> URIRef:
    """Returns the URI for QUDT unit: Decakelvin (http://qudt.org/vocab/unit/DecaK)"""
    return QUDT_UNIT["DECAK"]


def get_qudt_unit_megakelvin() -> URIRef:
    """Returns the URI for QUDT unit: Megakelvin (http://qudt.org/vocab/unit/MegaK)"""
    return QUDT_UNIT["MEGAK"]


def get_qudt_unit_milli_degree_celsius() -> URIRef:
    """Returns the URI for QUDT unit: Milli Degree Celsius (http://qudt.org/vocab/unit/MilliDEG_C)"""
    return QUDT_UNIT["MILLIDEG_C"]


def get_qudt_unit_millikelvin() -> URIRef:
    """Returns the URI for QUDT unit: Millikelvin (http://qudt.org/vocab/unit/MilliK)"""
    return QUDT_UNIT["MILLIK"]


def get_qudt_unit_plancktemperature() -> URIRef:
    """Returns the URI for QUDT unit: Plancktemperature (http://qudt.org/vocab/unit/PlanckTemperature)"""
    return QUDT_UNIT["PLANCKTEMPERATURE"]


def get_qudt_unit_base_pair() -> URIRef:
    """Returns the URI for QUDT unit: Base Pair (http://qudt.org/vocab/unit/BasePair)"""
    return QUDT_UNIT["BASEPAIR"]


def get_qudt_unit_count() -> URIRef:
    """Returns the URI for QUDT unit: Count (http://qudt.org/vocab/unit/COUNT)"""
    return QUDT_UNIT["COUNT"]


def get_qudt_unit_dec() -> URIRef:
    """Returns the URI for QUDT unit: Dec (http://qudt.org/vocab/unit/DECADE)"""
    return QUDT_UNIT["DECADE"]


def get_qudt_unit_flight() -> URIRef:
    """Returns the URI for QUDT unit: Flight (http://qudt.org/vocab/unit/FLIGHT)"""
    return QUDT_UNIT["FLIGHT"]


def get_qudt_unit_giga_base_pair() -> URIRef:
    """Returns the URI for QUDT unit: Giga Base Pair (http://qudt.org/vocab/unit/GigaBasePair)"""
    return QUDT_UNIT["GIGABASEPAIR"]


def get_qudt_unit_neper() -> URIRef:
    """Returns the URI for QUDT unit: Neper (http://qudt.org/vocab/unit/NP)"""
    return QUDT_UNIT["NP"]


def get_qudt_unit_number() -> URIRef:
    """Returns the URI for QUDT unit: Number (http://qudt.org/vocab/unit/NUM)"""
    return QUDT_UNIT["NUM"]


def get_qudt_unit_oct() -> URIRef:
    """Returns the URI for QUDT unit: Oct (http://qudt.org/vocab/unit/OCT)"""
    return QUDT_UNIT["OCT"]


def get_qudt_unit_reads_per_kilobase() -> URIRef:
    """Returns the URI for QUDT unit: Reads per Kilobase (http://qudt.org/vocab/unit/RPK)"""
    return QUDT_UNIT["RPK"]


def get_qudt_unit_electric_susceptibility_unit() -> URIRef:
    """Returns the URI for QUDT unit: Electric Susceptibility Unit (http://qudt.org/vocab/unit/SUSCEPTIBILITY_ELEC)"""
    return QUDT_UNIT["SUSCEPTIBILITY_ELEC"]


def get_qudt_unit_magnetic_susceptibility_unit() -> URIRef:
    """Returns the URI for QUDT unit: Magnetic Susceptibility Unit (http://qudt.org/vocab/unit/SUSCEPTIBILITY_MAG)"""
    return QUDT_UNIT["SUSCEPTIBILITY_MAG"]


def get_qudt_unit_centimetre_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Centimetre per Hour (http://qudt.org/vocab/unit/CentiM-PER-HR)"""
    return QUDT_UNIT["CENTIM-PER-HR"]


def get_qudt_unit_centimetre_per_kiloyear() -> URIRef:
    """Returns the URI for QUDT unit: Centimetre per Kiloyear (http://qudt.org/vocab/unit/CentiM-PER-KiloYR)"""
    return QUDT_UNIT["CENTIM-PER-KILOYR"]


def get_qudt_unit_centimetre_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Centimetre per Second (http://qudt.org/vocab/unit/CentiM-PER-SEC)"""
    return QUDT_UNIT["CENTIM-PER-SEC"]


def get_qudt_unit_centimetre_per_year() -> URIRef:
    """Returns the URI for QUDT unit: Centimetre per Year (http://qudt.org/vocab/unit/CentiM-PER-YR)"""
    return QUDT_UNIT["CENTIM-PER-YR"]


def get_qudt_unit_foot_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Foot per Day (http://qudt.org/vocab/unit/FT-PER-DAY)"""
    return QUDT_UNIT["FT-PER-DAY"]


def get_qudt_unit_foot_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Foot per Hour (http://qudt.org/vocab/unit/FT-PER-HR)"""
    return QUDT_UNIT["FT-PER-HR"]


def get_qudt_unit_foot_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Foot per Minute (http://qudt.org/vocab/unit/FT-PER-MIN)"""
    return QUDT_UNIT["FT-PER-MIN"]


def get_qudt_unit_foot_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Foot per Second (http://qudt.org/vocab/unit/FT-PER-SEC)"""
    return QUDT_UNIT["FT-PER-SEC"]


def get_qudt_unit_gigahertz_metre() -> URIRef:
    """Returns the URI for QUDT unit: Gigahertz Metre (http://qudt.org/vocab/unit/GigaHZ-M)"""
    return QUDT_UNIT["GIGAHZ-M"]


def get_qudt_unit_inch_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Inch per Minute (http://qudt.org/vocab/unit/IN-PER-MIN)"""
    return QUDT_UNIT["IN-PER-MIN"]


def get_qudt_unit_inch_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Inch per Second (http://qudt.org/vocab/unit/IN-PER-SEC)"""
    return QUDT_UNIT["IN-PER-SEC"]


def get_qudt_unit_inch_per_year() -> URIRef:
    """Returns the URI for QUDT unit: Inch per Year (http://qudt.org/vocab/unit/IN-PER-YR)"""
    return QUDT_UNIT["IN-PER-YR"]


def get_qudt_unit_knot() -> URIRef:
    """Returns the URI for QUDT unit: Knot (http://qudt.org/vocab/unit/KN)"""
    return QUDT_UNIT["KN"]


def get_qudt_unit_kilometre_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Kilometre per Day (http://qudt.org/vocab/unit/KiloM-PER-DAY)"""
    return QUDT_UNIT["KILOM-PER-DAY"]


def get_qudt_unit_kilometre_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Kilometre per Hour (http://qudt.org/vocab/unit/KiloM-PER-HR)"""
    return QUDT_UNIT["KILOM-PER-HR"]


def get_qudt_unit_kilometre_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Kilometre per Second (http://qudt.org/vocab/unit/KiloM-PER-SEC)"""
    return QUDT_UNIT["KILOM-PER-SEC"]


def get_qudt_unit_metre_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Metre per Day (http://qudt.org/vocab/unit/M-PER-DAY)"""
    return QUDT_UNIT["M-PER-DAY"]


def get_qudt_unit_metre_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Metre per Hour (http://qudt.org/vocab/unit/M-PER-HR)"""
    return QUDT_UNIT["M-PER-HR"]


def get_qudt_unit_metre_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Metre per Minute (http://qudt.org/vocab/unit/M-PER-MIN)"""
    return QUDT_UNIT["M-PER-MIN"]


def get_qudt_unit_metre_per_year() -> URIRef:
    """Returns the URI for QUDT unit: Metre per Year (http://qudt.org/vocab/unit/M-PER-YR)"""
    return QUDT_UNIT["M-PER-YR"]


def get_qudt_unit_international_mile_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: International Mile per Minute (http://qudt.org/vocab/unit/MI-PER-MIN)"""
    return QUDT_UNIT["MI-PER-MIN"]


def get_qudt_unit_international_mile_per_second() -> URIRef:
    """Returns the URI for QUDT unit: International Mile per Second (http://qudt.org/vocab/unit/MI-PER-SEC)"""
    return QUDT_UNIT["MI-PER-SEC"]


def get_qudt_unit_nautical_mile_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Nautical Mile per Hour (http://qudt.org/vocab/unit/MI_N-PER-HR)"""
    return QUDT_UNIT["MI_N-PER-HR"]


def get_qudt_unit_nautical_mile_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Nautical Mile per Minute (http://qudt.org/vocab/unit/MI_N-PER-MIN)"""
    return QUDT_UNIT["MI_N-PER-MIN"]


def get_qudt_unit_micrometre_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Micrometre per Minute (http://qudt.org/vocab/unit/MicroM-PER-MIN)"""
    return QUDT_UNIT["MICROM-PER-MIN"]


def get_qudt_unit_micrometre_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Micrometre per Second (http://qudt.org/vocab/unit/MicroM-PER-SEC)"""
    return QUDT_UNIT["MICROM-PER-SEC"]


def get_qudt_unit_millimetre_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Millimetre per Day (http://qudt.org/vocab/unit/MilliM-PER-DAY)"""
    return QUDT_UNIT["MILLIM-PER-DAY"]


def get_qudt_unit_millimetre_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Millimetre per Hour (http://qudt.org/vocab/unit/MilliM-PER-HR)"""
    return QUDT_UNIT["MILLIM-PER-HR"]


def get_qudt_unit_millimetre_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Millimetre per Minute (http://qudt.org/vocab/unit/MilliM-PER-MIN)"""
    return QUDT_UNIT["MILLIM-PER-MIN"]


def get_qudt_unit_millimetre_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Millimetre per Second (http://qudt.org/vocab/unit/MilliM-PER-SEC)"""
    return QUDT_UNIT["MILLIM-PER-SEC"]


def get_qudt_unit_millimetre_per_year() -> URIRef:
    """Returns the URI for QUDT unit: Millimetre per Year (http://qudt.org/vocab/unit/MilliM-PER-YR)"""
    return QUDT_UNIT["MILLIM-PER-YR"]


def get_qudt_unit_yard_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Yard per Hour (http://qudt.org/vocab/unit/YD-PER-HR)"""
    return QUDT_UNIT["YD-PER-HR"]


def get_qudt_unit_yard_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Yard per Minute (http://qudt.org/vocab/unit/YD-PER-MIN)"""
    return QUDT_UNIT["YD-PER-MIN"]


def get_qudt_unit_yard_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Yard per Second (http://qudt.org/vocab/unit/YD-PER-SEC)"""
    return QUDT_UNIT["YD-PER-SEC"]


def get_qudt_unit_pascal_square_metre_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Pascal Square Metre per Kilogram (http://qudt.org/vocab/unit/PA-M2-PER-KiloGM)"""
    return QUDT_UNIT["PA-M2-PER-KILOGM"]


def get_qudt_unit_beat() -> URIRef:
    """Returns the URI for QUDT unit: Beat (http://qudt.org/vocab/unit/BEAT)"""
    return QUDT_UNIT["BEAT"]


def get_qudt_unit_billion_long_scale() -> URIRef:
    """Returns the URI for QUDT unit: Billion (Long Scale) (http://qudt.org/vocab/unit/BILLION_Long)"""
    return QUDT_UNIT["BILLION_LONG"]


def get_qudt_unit_billion_short_scale() -> URIRef:
    """Returns the URI for QUDT unit: Billion (Short Scale) (http://qudt.org/vocab/unit/BILLION_Short)"""
    return QUDT_UNIT["BILLION_SHORT"]


def get_qudt_unit_breath() -> URIRef:
    """Returns the URI for QUDT unit: Breath (http://qudt.org/vocab/unit/BREATH)"""
    return QUDT_UNIT["BREATH"]


def get_qudt_unit_cases() -> URIRef:
    """Returns the URI for QUDT unit: Cases (http://qudt.org/vocab/unit/CASES)"""
    return QUDT_UNIT["CASES"]


def get_qudt_unit_cycle() -> URIRef:
    """Returns the URI for QUDT unit: Cycle (http://qudt.org/vocab/unit/CYC)"""
    return QUDT_UNIT["CYC"]


def get_qudt_unit_deaths() -> URIRef:
    """Returns the URI for QUDT unit: Deaths (http://qudt.org/vocab/unit/DEATHS)"""
    return QUDT_UNIT["DEATHS"]


def get_qudt_unit_frame() -> URIRef:
    """Returns the URI for QUDT unit: Frame (http://qudt.org/vocab/unit/FRAME)"""
    return QUDT_UNIT["FRAME"]


def get_qudt_unit_hundred() -> URIRef:
    """Returns the URI for QUDT unit: Hundred (http://qudt.org/vocab/unit/HUNDRED)"""
    return QUDT_UNIT["HUNDRED"]


def get_qudt_unit_individual() -> URIRef:
    """Returns the URI for QUDT unit: Individual (http://qudt.org/vocab/unit/INDIV)"""
    return QUDT_UNIT["INDIV"]


def get_qudt_unit_thousand_individuals() -> URIRef:
    """Returns the URI for QUDT unit: Thousand Individuals (http://qudt.org/vocab/unit/KiloINDIV)"""
    return QUDT_UNIT["KILOINDIV"]


def get_qudt_unit_million() -> URIRef:
    """Returns the URI for QUDT unit: Million (http://qudt.org/vocab/unit/MILLION)"""
    return QUDT_UNIT["MILLION"]


def get_qudt_unit_million_individuals() -> URIRef:
    """Returns the URI for QUDT unit: Million Individuals (http://qudt.org/vocab/unit/MegaINDIV)"""
    return QUDT_UNIT["MEGAINDIV"]


def get_qudt_unit_one() -> URIRef:
    """Returns the URI for QUDT unit: One (http://qudt.org/vocab/unit/ONE)"""
    return QUDT_UNIT["ONE"]


def get_qudt_unit_pixel_count() -> URIRef:
    """Returns the URI for QUDT unit: Pixel (count) (http://qudt.org/vocab/unit/PIXEL_COUNT)"""
    return QUDT_UNIT["PIXEL_COUNT"]


def get_qudt_unit_sample() -> URIRef:
    """Returns the URI for QUDT unit: Sample (http://qudt.org/vocab/unit/SAMPLE)"""
    return QUDT_UNIT["SAMPLE"]


def get_qudt_unit_ten() -> URIRef:
    """Returns the URI for QUDT unit: Ten (http://qudt.org/vocab/unit/TEN)"""
    return QUDT_UNIT["TEN"]


def get_qudt_unit_thousand() -> URIRef:
    """Returns the URI for QUDT unit: Thousand (http://qudt.org/vocab/unit/THOUSAND)"""
    return QUDT_UNIT["THOUSAND"]


def get_qudt_unit_byte_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Byte per Second (http://qudt.org/vocab/unit/BYTE-PER-SEC)"""
    return QUDT_UNIT["BYTE-PER-SEC"]


def get_qudt_unit_gigabyte_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Gigabyte per Second (http://qudt.org/vocab/unit/GigaBYTE-PER-SEC)"""
    return QUDT_UNIT["GIGABYTE-PER-SEC"]


def get_qudt_unit_megabyte_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Megabyte per Second (http://qudt.org/vocab/unit/MegaBYTE-PER-SEC)"""
    return QUDT_UNIT["MEGABYTE-PER-SEC"]


def get_qudt_unit_attofarad() -> URIRef:
    """Returns the URI for QUDT unit: Attofarad (http://qudt.org/vocab/unit/AttoFARAD)"""
    return QUDT_UNIT["ATTOFARAD"]


def get_qudt_unit_farad() -> URIRef:
    """Returns the URI for QUDT unit: Farad (http://qudt.org/vocab/unit/FARAD)"""
    return QUDT_UNIT["FARAD"]


def get_qudt_unit_abfarad() -> URIRef:
    """Returns the URI for QUDT unit: Abfarad (http://qudt.org/vocab/unit/FARAD_Ab)"""
    return QUDT_UNIT["FARAD_AB"]


def get_qudt_unit_statfarad() -> URIRef:
    """Returns the URI for QUDT unit: Statfarad (http://qudt.org/vocab/unit/FARAD_Stat)"""
    return QUDT_UNIT["FARAD_STAT"]


def get_qudt_unit_femtofarad() -> URIRef:
    """Returns the URI for QUDT unit: Femtofarad (http://qudt.org/vocab/unit/FemtoFARAD)"""
    return QUDT_UNIT["FEMTOFARAD"]


def get_qudt_unit_kilofarad() -> URIRef:
    """Returns the URI for QUDT unit: Kilofarad (http://qudt.org/vocab/unit/KiloFARAD)"""
    return QUDT_UNIT["KILOFARAD"]


def get_qudt_unit_microfarad() -> URIRef:
    """Returns the URI for QUDT unit: Microfarad (http://qudt.org/vocab/unit/MicroFARAD)"""
    return QUDT_UNIT["MICROFARAD"]


def get_qudt_unit_millifarad() -> URIRef:
    """Returns the URI for QUDT unit: Millifarad (http://qudt.org/vocab/unit/MilliFARAD)"""
    return QUDT_UNIT["MILLIFARAD"]


def get_qudt_unit_nanofarad() -> URIRef:
    """Returns the URI for QUDT unit: Nanofarad (http://qudt.org/vocab/unit/NanoFARAD)"""
    return QUDT_UNIT["NANOFARAD"]


def get_qudt_unit_picofarad() -> URIRef:
    """Returns the URI for QUDT unit: Picofarad (http://qudt.org/vocab/unit/PicoFARAD)"""
    return QUDT_UNIT["PICOFARAD"]


def get_qudt_unit_acre_foot() -> URIRef:
    """Returns the URI for QUDT unit: Acre Foot (http://qudt.org/vocab/unit/AC-FT)"""
    return QUDT_UNIT["AC-FT"]


def get_qudt_unit_acre_us_survey_foot() -> URIRef:
    """Returns the URI for QUDT unit: Acre Us Survey Foot (http://qudt.org/vocab/unit/AC-FT_US)"""
    return QUDT_UNIT["AC-FT_US"]


def get_qudt_unit_cubic_angstrom() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Angstrom (http://qudt.org/vocab/unit/ANGSTROM3)"""
    return QUDT_UNIT["ANGSTROM3"]


def get_qudt_unit_barrel() -> URIRef:
    """Returns the URI for QUDT unit: Barrel (http://qudt.org/vocab/unit/BBL)"""
    return QUDT_UNIT["BBL"]


def get_qudt_unit_barrel_uk_petroleum() -> URIRef:
    """Returns the URI for QUDT unit: Barrel (UK Petroleum) (http://qudt.org/vocab/unit/BBL_UK_PET)"""
    return QUDT_UNIT["BBL_UK_PET"]


def get_qudt_unit_bushel_us_dry() -> URIRef:
    """Returns the URI for QUDT unit: Bushel (US Dry) (http://qudt.org/vocab/unit/BU_US_DRY)"""
    return QUDT_UNIT["BU_US_DRY"]


def get_qudt_unit_cubic_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Centimetre (http://qudt.org/vocab/unit/CentiM3)"""
    return QUDT_UNIT["CENTIM3"]


def get_qudt_unit_decalitre() -> URIRef:
    """Returns the URI for QUDT unit: Decalitre (http://qudt.org/vocab/unit/DecaL)"""
    return QUDT_UNIT["DECAL"]


def get_qudt_unit_cubic_decametre() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Decametre (http://qudt.org/vocab/unit/DecaM3)"""
    return QUDT_UNIT["DECAM3"]


def get_qudt_unit_decilitre() -> URIRef:
    """Returns the URI for QUDT unit: Decilitre (http://qudt.org/vocab/unit/DeciL)"""
    return QUDT_UNIT["DECIL"]


def get_qudt_unit_cubic_decimetre() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Decimetre (http://qudt.org/vocab/unit/DeciM3)"""
    return QUDT_UNIT["DECIM3"]


def get_qudt_unit_board_foot() -> URIRef:
    """Returns the URI for QUDT unit: Board Foot (http://qudt.org/vocab/unit/FBM)"""
    return QUDT_UNIT["FBM"]


def get_qudt_unit_cubic_foot() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Foot (http://qudt.org/vocab/unit/FT3)"""
    return QUDT_UNIT["FT3"]


def get_qudt_unit_femtolitre() -> URIRef:
    """Returns the URI for QUDT unit: Femtolitre (http://qudt.org/vocab/unit/FemtoL)"""
    return QUDT_UNIT["FEMTOL"]


def get_qudt_unit_gill_uk() -> URIRef:
    """Returns the URI for QUDT unit: Gill (UK) (http://qudt.org/vocab/unit/GI_UK)"""
    return QUDT_UNIT["GI_UK"]


def get_qudt_unit_gill_us() -> URIRef:
    """Returns the URI for QUDT unit: Gill (US) (http://qudt.org/vocab/unit/GI_US)"""
    return QUDT_UNIT["GI_US"]


def get_qudt_unit_gross_tonnage() -> URIRef:
    """Returns the URI for QUDT unit: Gross Tonnage (http://qudt.org/vocab/unit/GT)"""
    return QUDT_UNIT["GT"]


def get_qudt_unit_hectolitre() -> URIRef:
    """Returns the URI for QUDT unit: Hectolitre (http://qudt.org/vocab/unit/HectoL)"""
    return QUDT_UNIT["HECTOL"]


def get_qudt_unit_cubic_inch() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Inch (http://qudt.org/vocab/unit/IN3)"""
    return QUDT_UNIT["IN3"]


def get_qudt_unit_kilo_cubic_foot() -> URIRef:
    """Returns the URI for QUDT unit: Kilo Cubic Foot (http://qudt.org/vocab/unit/KiloCubicFT)"""
    return QUDT_UNIT["KILOCUBICFT"]


def get_qudt_unit_kilolitre() -> URIRef:
    """Returns the URI for QUDT unit: Kilolitre (http://qudt.org/vocab/unit/KiloL)"""
    return QUDT_UNIT["KILOL"]


def get_qudt_unit_litre() -> URIRef:
    """Returns the URI for QUDT unit: Litre (http://qudt.org/vocab/unit/L)"""
    return QUDT_UNIT["L"]


def get_qudt_unit_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Metre (http://qudt.org/vocab/unit/M3)"""
    return QUDT_UNIT["M3"]


def get_qudt_unit_cubic_international_mile() -> URIRef:
    """Returns the URI for QUDT unit: Cubic International Mile (http://qudt.org/vocab/unit/MI3)"""
    return QUDT_UNIT["MI3"]


def get_qudt_unit_cubic_imperial_mile() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Imperial Mile (http://qudt.org/vocab/unit/MI_UK3)"""
    return QUDT_UNIT["MI_UK3"]


def get_qudt_unit_megalitre() -> URIRef:
    """Returns the URI for QUDT unit: Megalitre (http://qudt.org/vocab/unit/MegaL)"""
    return QUDT_UNIT["MEGAL"]


def get_qudt_unit_microlitre() -> URIRef:
    """Returns the URI for QUDT unit: Microlitre (http://qudt.org/vocab/unit/MicroL)"""
    return QUDT_UNIT["MICROL"]


def get_qudt_unit_cubic_micrometre() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Micrometre (http://qudt.org/vocab/unit/MicroM3)"""
    return QUDT_UNIT["MICROM3"]


def get_qudt_unit_millilitre() -> URIRef:
    """Returns the URI for QUDT unit: Millilitre (http://qudt.org/vocab/unit/MilliL)"""
    return QUDT_UNIT["MILLIL"]


def get_qudt_unit_cubic_millimetre() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Millimetre (http://qudt.org/vocab/unit/MilliM3)"""
    return QUDT_UNIT["MILLIM3"]


def get_qudt_unit_net_tonnage() -> URIRef:
    """Returns the URI for QUDT unit: Net Tonnage (http://qudt.org/vocab/unit/NT)"""
    return QUDT_UNIT["NT"]


def get_qudt_unit_nanolitre() -> URIRef:
    """Returns the URI for QUDT unit: Nanolitre (http://qudt.org/vocab/unit/NanoL)"""
    return QUDT_UNIT["NANOL"]


def get_qudt_unit_fluid_ounce_uk() -> URIRef:
    """Returns the URI for QUDT unit: Fluid Ounce (UK) (http://qudt.org/vocab/unit/OZ_VOL_UK)"""
    return QUDT_UNIT["OZ_VOL_UK"]


def get_qudt_unit_imperial_pint() -> URIRef:
    """Returns the URI for QUDT unit: Imperial Pint (http://qudt.org/vocab/unit/PINT)"""
    return QUDT_UNIT["PINT"]


def get_qudt_unit_pint_uk() -> URIRef:
    """Returns the URI for QUDT unit: Pint (UK) (http://qudt.org/vocab/unit/PINT_UK)"""
    return QUDT_UNIT["PINT_UK"]


def get_qudt_unit_peck_uk() -> URIRef:
    """Returns the URI for QUDT unit: Peck (UK) (http://qudt.org/vocab/unit/PK_UK)"""
    return QUDT_UNIT["PK_UK"]


def get_qudt_unit_picolitre() -> URIRef:
    """Returns the URI for QUDT unit: Picolitre (http://qudt.org/vocab/unit/PicoL)"""
    return QUDT_UNIT["PICOL"]


def get_qudt_unit_planck_volume() -> URIRef:
    """Returns the URI for QUDT unit: Planck Volume (http://qudt.org/vocab/unit/PlanckVolume)"""
    return QUDT_UNIT["PLANCKVOLUME"]


def get_qudt_unit_quart_uk() -> URIRef:
    """Returns the URI for QUDT unit: Quart (UK) (http://qudt.org/vocab/unit/QT_UK)"""
    return QUDT_UNIT["QT_UK"]


def get_qudt_unit_us_liquid_quart() -> URIRef:
    """Returns the URI for QUDT unit: Us Liquid Quart (http://qudt.org/vocab/unit/QT_US)"""
    return QUDT_UNIT["QT_US"]


def get_qudt_unit_register_ton() -> URIRef:
    """Returns the URI for QUDT unit: Register Ton (http://qudt.org/vocab/unit/RT)"""
    return QUDT_UNIT["RT"]


def get_qudt_unit_standard() -> URIRef:
    """Returns the URI for QUDT unit: Standard (http://qudt.org/vocab/unit/STANDARD)"""
    return QUDT_UNIT["STANDARD"]


def get_qudt_unit_stere() -> URIRef:
    """Returns the URI for QUDT unit: Stere (http://qudt.org/vocab/unit/STR)"""
    return QUDT_UNIT["STR"]


def get_qudt_unit_tablespoon() -> URIRef:
    """Returns the URI for QUDT unit: Tablespoon (http://qudt.org/vocab/unit/TBSP)"""
    return QUDT_UNIT["TBSP"]


def get_qudt_unit_ton_register() -> URIRef:
    """Returns the URI for QUDT unit: Ton, Register (http://qudt.org/vocab/unit/TON_Register)"""
    return QUDT_UNIT["TON_REGISTER"]


def get_qudt_unit_ton_uk_shipping() -> URIRef:
    """Returns the URI for QUDT unit: Ton (uk Shipping) (http://qudt.org/vocab/unit/TON_SHIPPING_UK)"""
    return QUDT_UNIT["TON_SHIPPING_UK"]


def get_qudt_unit_ton_us_shipping() -> URIRef:
    """Returns the URI for QUDT unit: Ton (us Shipping) (http://qudt.org/vocab/unit/TON_SHIPPING_US)"""
    return QUDT_UNIT["TON_SHIPPING_US"]


def get_qudt_unit_teaspoon() -> URIRef:
    """Returns the URI for QUDT unit: Teaspoon (http://qudt.org/vocab/unit/TSP)"""
    return QUDT_UNIT["TSP"]


def get_qudt_unit_cubic_yard() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Yard (http://qudt.org/vocab/unit/YD3)"""
    return QUDT_UNIT["YD3"]


def get_qudt_unit_enzyme_unit() -> URIRef:
    """Returns the URI for QUDT unit: Enzyme Unit (http://qudt.org/vocab/unit/ENZ)"""
    return QUDT_UNIT["ENZ"]


def get_qudt_unit_katal() -> URIRef:
    """Returns the URI for QUDT unit: Katal (http://qudt.org/vocab/unit/KAT)"""
    return QUDT_UNIT["KAT"]


def get_qudt_unit_kilomole_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Kilomole per Hour (http://qudt.org/vocab/unit/KiloMOL-PER-HR)"""
    return QUDT_UNIT["KILOMOL-PER-HR"]


def get_qudt_unit_pound_mole_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mole per Minute (http://qudt.org/vocab/unit/MOL_LB-PER-MIN)"""
    return QUDT_UNIT["MOL_LB-PER-MIN"]


def get_qudt_unit_pound_mole_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mole per Second (http://qudt.org/vocab/unit/MOL_LB-PER-SEC)"""
    return QUDT_UNIT["MOL_LB-PER-SEC"]


def get_qudt_unit_microkatal() -> URIRef:
    """Returns the URI for QUDT unit: Microkatal (http://qudt.org/vocab/unit/MicroKAT)"""
    return QUDT_UNIT["MICROKAT"]


def get_qudt_unit_millikatal() -> URIRef:
    """Returns the URI for QUDT unit: Millikatal (http://qudt.org/vocab/unit/MilliKAT)"""
    return QUDT_UNIT["MILLIKAT"]


def get_qudt_unit_nanokatal() -> URIRef:
    """Returns the URI for QUDT unit: Nanokatal (http://qudt.org/vocab/unit/NanoKAT)"""
    return QUDT_UNIT["NANOKAT"]


def get_qudt_unit_picokatal() -> URIRef:
    """Returns the URI for QUDT unit: Picokatal (http://qudt.org/vocab/unit/PicoKAT)"""
    return QUDT_UNIT["PICOKAT"]


def get_qudt_unit_enzyme_unit_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: Enzyme Unit per Litre (http://qudt.org/vocab/unit/ENZ-PER-L)"""
    return QUDT_UNIT["ENZ-PER-L"]


def get_qudt_unit_katal_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: Katal per Litre (http://qudt.org/vocab/unit/KAT-PER-L)"""
    return QUDT_UNIT["KAT-PER-L"]


def get_qudt_unit_katal_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Katal per Cubic Metre (http://qudt.org/vocab/unit/KAT-PER-M3)"""
    return QUDT_UNIT["KAT-PER-M3"]


def get_qudt_unit_katal_per_microlitre() -> URIRef:
    """Returns the URI for QUDT unit: Katal per Microlitre (http://qudt.org/vocab/unit/KAT-PER-MicroL)"""
    return QUDT_UNIT["KAT-PER-MICROL"]


def get_qudt_unit_mole_per_square_metre_second_metre() -> URIRef:
    """Returns the URI for QUDT unit: Mole per Square Metre Second Metre (http://qudt.org/vocab/unit/MOL-PER-M2-SEC-M)"""
    return QUDT_UNIT["MOL-PER-M2-SEC-M"]


def get_qudt_unit_mole_per_cubic_metre_second() -> URIRef:
    """Returns the URI for QUDT unit: Mole per Cubic Metre Second (http://qudt.org/vocab/unit/MOL-PER-M3-SEC)"""
    return QUDT_UNIT["MOL-PER-M3-SEC"]


def get_qudt_unit_microkatal_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: Microkatal per Litre (http://qudt.org/vocab/unit/MicroKAT-PER-L)"""
    return QUDT_UNIT["MICROKAT-PER-L"]


def get_qudt_unit_micromole_per_litre_hour() -> URIRef:
    """Returns the URI for QUDT unit: Micromole per Litre Hour (http://qudt.org/vocab/unit/MicroMOL-PER-L-HR)"""
    return QUDT_UNIT["MICROMOL-PER-L-HR"]


def get_qudt_unit_millikatal_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: Millikatal per Litre (http://qudt.org/vocab/unit/MilliKAT-PER-L)"""
    return QUDT_UNIT["MILLIKAT-PER-L"]


def get_qudt_unit_millimole_per_cubic_metre_day() -> URIRef:
    """Returns the URI for QUDT unit: Millimole per Cubic Metre Day (http://qudt.org/vocab/unit/MilliMOL-PER-M3-DAY)"""
    return QUDT_UNIT["MILLIMOL-PER-M3-DAY"]


def get_qudt_unit_nanokatal_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: Nanokatal per Litre (http://qudt.org/vocab/unit/NanoKAT-PER-L)"""
    return QUDT_UNIT["NANOKAT-PER-L"]


def get_qudt_unit_nanomole_per_cubic_centimetre_hour() -> URIRef:
    """Returns the URI for QUDT unit: Nanomole per Cubic Centimetre Hour (http://qudt.org/vocab/unit/NanoMOL-PER-CentiM3-HR)"""
    return QUDT_UNIT["NANOMOL-PER-CENTIM3-HR"]


def get_qudt_unit_nanomole_per_litre_day() -> URIRef:
    """Returns the URI for QUDT unit: Nanomole per Litre Day (http://qudt.org/vocab/unit/NanoMOL-PER-L-DAY)"""
    return QUDT_UNIT["NANOMOL-PER-L-DAY"]


def get_qudt_unit_nanomole_per_litre_hour() -> URIRef:
    """Returns the URI for QUDT unit: Nanomole per Litre Hour (http://qudt.org/vocab/unit/NanoMOL-PER-L-HR)"""
    return QUDT_UNIT["NANOMOL-PER-L-HR"]


def get_qudt_unit_picokatal_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: Picokatal per Litre (http://qudt.org/vocab/unit/PicoKAT-PER-L)"""
    return QUDT_UNIT["PICOKAT-PER-L"]


def get_qudt_unit_picomole_per_litre_day() -> URIRef:
    """Returns the URI for QUDT unit: Picomole per Litre Day (http://qudt.org/vocab/unit/PicoMOL-PER-L-DAY)"""
    return QUDT_UNIT["PICOMOL-PER-L-DAY"]


def get_qudt_unit_picomole_per_litre_hour() -> URIRef:
    """Returns the URI for QUDT unit: Picomole per Litre Hour (http://qudt.org/vocab/unit/PicoMOL-PER-L-HR)"""
    return QUDT_UNIT["PICOMOL-PER-L-HR"]


def get_qudt_unit_picomole_per_cubic_metre_second() -> URIRef:
    """Returns the URI for QUDT unit: Picomole per Cubic Metre Second (http://qudt.org/vocab/unit/PicoMOL-PER-M3-SEC)"""
    return QUDT_UNIT["PICOMOL-PER-M3-SEC"]


def get_qudt_unit_degree_celsius_growing_cereal() -> URIRef:
    """Returns the URI for QUDT unit: Degree Celsius Growing Cereal (http://qudt.org/vocab/unit/DEG_C_GROWING_CEREAL)"""
    return QUDT_UNIT["DEG_C_GROWING_CEREAL"]


def get_qudt_unit_joule_per_mole() -> URIRef:
    """Returns the URI for QUDT unit: Joule per Mole (http://qudt.org/vocab/unit/J-PER-MOL)"""
    return QUDT_UNIT["J-PER-MOL"]


def get_qudt_unit_cubic_centimetre_per_gram() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Centimetre per Gram (http://qudt.org/vocab/unit/CentiM3-PER-GM)"""
    return QUDT_UNIT["CENTIM3-PER-GM"]


def get_qudt_unit_decilitre_per_gram() -> URIRef:
    """Returns the URI for QUDT unit: Decilitre per Gram (http://qudt.org/vocab/unit/DeciL-PER-GM)"""
    return QUDT_UNIT["DECIL-PER-GM"]


def get_qudt_unit_cubic_decimetre_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Decimetre per Kilogram (http://qudt.org/vocab/unit/DeciM3-PER-KiloGM)"""
    return QUDT_UNIT["DECIM3-PER-KILOGM"]


def get_qudt_unit_cubic_foot_per_pound_mass() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Foot per Pound Mass (http://qudt.org/vocab/unit/FT3-PER-LB)"""
    return QUDT_UNIT["FT3-PER-LB"]


def get_qudt_unit_cubic_inch_per_pound_mass() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Inch per Pound Mass (http://qudt.org/vocab/unit/IN3-PER-LB)"""
    return QUDT_UNIT["IN3-PER-LB"]


def get_qudt_unit_litre_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Litre per Kilogram (http://qudt.org/vocab/unit/L-PER-KiloGM)"""
    return QUDT_UNIT["L-PER-KILOGM"]


def get_qudt_unit_cubic_metre_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Metre per Kilogram (http://qudt.org/vocab/unit/M3-PER-KiloGM)"""
    return QUDT_UNIT["M3-PER-KILOGM"]


def get_qudt_unit_millilitre_per_gram() -> URIRef:
    """Returns the URI for QUDT unit: Millilitre per Gram (http://qudt.org/vocab/unit/MilliL-PER-GM)"""
    return QUDT_UNIT["MILLIL-PER-GM"]


def get_qudt_unit_millilitre_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Millilitre per Kilogram (http://qudt.org/vocab/unit/MilliL-PER-KiloGM)"""
    return QUDT_UNIT["MILLIL-PER-KILOGM"]


def get_qudt_unit_cubic_millimetre_per_gram() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Millimetre per Gram (http://qudt.org/vocab/unit/MilliM3-PER-GM)"""
    return QUDT_UNIT["MILLIM3-PER-GM"]


def get_qudt_unit_cubic_millimetre_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Millimetre per Kilogram (http://qudt.org/vocab/unit/MilliM3-PER-KiloGM)"""
    return QUDT_UNIT["MILLIM3-PER-KILOGM"]


def get_qudt_unit_kilocalorie_per_mole() -> URIRef:
    """Returns the URI for QUDT unit: Kilocalorie per Mole (http://qudt.org/vocab/unit/KiloCAL-PER-MOL)"""
    return QUDT_UNIT["KILOCAL-PER-MOL"]


def get_qudt_unit_kilojoule_per_mole() -> URIRef:
    """Returns the URI for QUDT unit: Kilojoule per Mole (http://qudt.org/vocab/unit/KiloJ-PER-MOL)"""
    return QUDT_UNIT["KILOJ-PER-MOL"]


def get_qudt_unit_watt_per_square_metre_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Watt per Square Metre Kelvin (http://qudt.org/vocab/unit/W-PER-M2-K)"""
    return QUDT_UNIT["W-PER-M2-K"]


def get_qudt_unit_british_thermal_unit_international_definition_per_square_foot_hour_degree_fahrenheit() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) per Square Foot Hour Degree Fahrenheit (http://qudt.org/vocab/unit/BTU_IT-PER-FT2-HR-DEG_F)"""
    return QUDT_UNIT["BTU_IT-PER-FT2-HR-DEG_F"]


def get_qudt_unit_british_thermal_unit_international_definition_per_square_foot_second_degree_fahrenheit() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) per Square Foot Second Degree Fahrenheit (http://qudt.org/vocab/unit/BTU_IT-PER-FT2-SEC-DEG_F)"""
    return QUDT_UNIT["BTU_IT-PER-FT2-SEC-DEG_F"]


def get_qudt_unit_british_thermal_unit_international_definition_per_hour_square_foot_degree_fahrenheit() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) per Hour Square Foot Degree Fahrenheit (http://qudt.org/vocab/unit/BTU_IT-PER-HR-FT2-DEG_F)"""
    return QUDT_UNIT["BTU_IT-PER-HR-FT2-DEG_F"]


def get_qudt_unit_british_thermal_unit_international_definition_per_hour_square_foot_degree_rankine() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) per Hour Square Foot Degree Rankine (http://qudt.org/vocab/unit/BTU_IT-PER-HR-FT2-DEG_R)"""
    return QUDT_UNIT["BTU_IT-PER-HR-FT2-DEG_R"]


def get_qudt_unit_british_thermal_unit_international_definition_per_second_square_foot_degree_fahrenheit() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) per Second Square Foot Degree Fahrenheit (http://qudt.org/vocab/unit/BTU_IT-PER-SEC-FT2-DEG_F)"""
    return QUDT_UNIT["BTU_IT-PER-SEC-FT2-DEG_F"]


def get_qudt_unit_british_thermal_unit_international_definition_per_second_square_foot_degree_rankine() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) per Second Square Foot Degree Rankine (http://qudt.org/vocab/unit/BTU_IT-PER-SEC-FT2-DEG_R)"""
    return QUDT_UNIT["BTU_IT-PER-SEC-FT2-DEG_R"]


def get_qudt_unit_british_thermal_unit_thermochemical_definition_per_hour_square_foot_degree_fahrenheit() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (thermochemical Definition) per Hour Square Foot Degree Fahrenheit (http://qudt.org/vocab/unit/BTU_TH-PER-HR-FT2-DEG_F)"""
    return QUDT_UNIT["BTU_TH-PER-HR-FT2-DEG_F"]


def get_qudt_unit_british_thermal_unit_thermochemical_definition_per_second_square_foot_degree_fahrenheit() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (thermochemical Definition) per Second Square Foot Degree Fahrenheit (http://qudt.org/vocab/unit/BTU_TH-PER-SEC-FT2-DEG_F)"""
    return QUDT_UNIT["BTU_TH-PER-SEC-FT2-DEG_F"]


def get_qudt_unit_international_table_calorie_per_second_square_centimetre_kelvin() -> (
    URIRef
):
    """Returns the URI for QUDT unit: International Table Calorie per Second Square Centimetre Kelvin (http://qudt.org/vocab/unit/CAL_IT-PER-SEC-CentiM2-K)"""
    return QUDT_UNIT["CAL_IT-PER-SEC-CENTIM2-K"]


def get_qudt_unit_thermochemical_calorie_per_second_square_centimetre_kelvin() -> (
    URIRef
):
    """Returns the URI for QUDT unit: Thermochemical Calorie per Second Square Centimetre Kelvin (http://qudt.org/vocab/unit/CAL_TH-PER-SEC-CentiM2-K)"""
    return QUDT_UNIT["CAL_TH-PER-SEC-CENTIM2-K"]


def get_qudt_unit_kilogram_per_cubic_second_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Cubic Second Kelvin (http://qudt.org/vocab/unit/KiloGM-PER-SEC3-K)"""
    return QUDT_UNIT["KILOGM-PER-SEC3-K"]


def get_qudt_unit_kilowatt_per_square_metre_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Kilowatt per Square Metre Kelvin (http://qudt.org/vocab/unit/KiloW-PER-M2-K)"""
    return QUDT_UNIT["KILOW-PER-M2-K"]


def get_qudt_unit_gigahertz() -> URIRef:
    """Returns the URI for QUDT unit: Gigahertz (http://qudt.org/vocab/unit/GigaHZ)"""
    return QUDT_UNIT["GIGAHZ"]


def get_qudt_unit_kilohertz() -> URIRef:
    """Returns the URI for QUDT unit: Kilohertz (http://qudt.org/vocab/unit/KiloHZ)"""
    return QUDT_UNIT["KILOHZ"]


def get_qudt_unit_megahertz() -> URIRef:
    """Returns the URI for QUDT unit: Megahertz (http://qudt.org/vocab/unit/MegaHZ)"""
    return QUDT_UNIT["MEGAHZ"]


def get_qudt_unit_millihertz() -> URIRef:
    """Returns the URI for QUDT unit: Millihertz (http://qudt.org/vocab/unit/MilliHZ)"""
    return QUDT_UNIT["MILLIHZ"]


def get_qudt_unit_number_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Number per Hour (http://qudt.org/vocab/unit/NUM-PER-HR)"""
    return QUDT_UNIT["NUM-PER-HR"]


def get_qudt_unit_number_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Number per Second (http://qudt.org/vocab/unit/NUM-PER-SEC)"""
    return QUDT_UNIT["NUM-PER-SEC"]


def get_qudt_unit_number_per_year() -> URIRef:
    """Returns the URI for QUDT unit: Number per Year (http://qudt.org/vocab/unit/NUM-PER-YR)"""
    return QUDT_UNIT["NUM-PER-YR"]


def get_qudt_unit_reciprocal_day() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Day (http://qudt.org/vocab/unit/PER-DAY)"""
    return QUDT_UNIT["PER-DAY"]


def get_qudt_unit_reciprocal_hour() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Hour (http://qudt.org/vocab/unit/PER-HR)"""
    return QUDT_UNIT["PER-HR"]


def get_qudt_unit_reciprocal_minute() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Minute (http://qudt.org/vocab/unit/PER-MIN)"""
    return QUDT_UNIT["PER-MIN"]


def get_qudt_unit_reciprocal_month() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Month (http://qudt.org/vocab/unit/PER-MO)"""
    return QUDT_UNIT["PER-MO"]


def get_qudt_unit_reciprocal_millisecond() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Millisecond (http://qudt.org/vocab/unit/PER-MilliSEC)"""
    return QUDT_UNIT["PER-MILLISEC"]


def get_qudt_unit_reciprocal_second() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Second (http://qudt.org/vocab/unit/PER-SEC)"""
    return QUDT_UNIT["PER-SEC"]


def get_qudt_unit_reciprocal_week() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Week (http://qudt.org/vocab/unit/PER-WK)"""
    return QUDT_UNIT["PER-WK"]


def get_qudt_unit_reciprocal_year() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Year (http://qudt.org/vocab/unit/PER-YR)"""
    return QUDT_UNIT["PER-YR"]


def get_qudt_unit_percent_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Percent per Day (http://qudt.org/vocab/unit/PERCENT-PER-DAY)"""
    return QUDT_UNIT["PERCENT-PER-DAY"]


def get_qudt_unit_percent_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Percent per Hour (http://qudt.org/vocab/unit/PERCENT-PER-HR)"""
    return QUDT_UNIT["PERCENT-PER-HR"]


def get_qudt_unit_percent_per_month() -> URIRef:
    """Returns the URI for QUDT unit: Percent per Month (http://qudt.org/vocab/unit/PERCENT-PER-MO)"""
    return QUDT_UNIT["PERCENT-PER-MO"]


def get_qudt_unit_parts_per_thousand_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Parts per Thousand per Hour (http://qudt.org/vocab/unit/PPTH-PER-HR)"""
    return QUDT_UNIT["PPTH-PER-HR"]


def get_qudt_unit_petahertz() -> URIRef:
    """Returns the URI for QUDT unit: Petahertz (http://qudt.org/vocab/unit/PetaHZ)"""
    return QUDT_UNIT["PETAHZ"]


def get_qudt_unit_planck_frequency() -> URIRef:
    """Returns the URI for QUDT unit: Planck Frequency (http://qudt.org/vocab/unit/PlanckFrequency)"""
    return QUDT_UNIT["PLANCKFREQUENCY"]


def get_qudt_unit_sample_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Sample per Second (http://qudt.org/vocab/unit/SAMPLE-PER-SEC)"""
    return QUDT_UNIT["SAMPLE-PER-SEC"]


def get_qudt_unit_terahertz() -> URIRef:
    """Returns the URI for QUDT unit: Terahertz (http://qudt.org/vocab/unit/TeraHZ)"""
    return QUDT_UNIT["TERAHZ"]


def get_qudt_unit_square_metre_per_newton() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre per Newton (http://qudt.org/vocab/unit/M2-PER-N)"""
    return QUDT_UNIT["M2-PER-N"]


def get_qudt_unit_reciprocal_bar() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Bar (http://qudt.org/vocab/unit/PER-BAR)"""
    return QUDT_UNIT["PER-BAR"]


def get_qudt_unit_reciprocal_megapascal() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Megapascal (http://qudt.org/vocab/unit/PER-MegaPA)"""
    return QUDT_UNIT["PER-MEGAPA"]


def get_qudt_unit_reciprocal_pascal() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Pascal (http://qudt.org/vocab/unit/PER-PA)"""
    return QUDT_UNIT["PER-PA"]


def get_qudt_unit_percent_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Percent per Bar (http://qudt.org/vocab/unit/PERCENT-PER-BAR)"""
    return QUDT_UNIT["PERCENT-PER-BAR"]


def get_qudt_unit_percent_per_hectobar() -> URIRef:
    """Returns the URI for QUDT unit: Percent per Hectobar (http://qudt.org/vocab/unit/PERCENT-PER-HectoBAR)"""
    return QUDT_UNIT["PERCENT-PER-HECTOBAR"]


def get_qudt_unit_permille_per_psi() -> URIRef:
    """Returns the URI for QUDT unit: Permille per Psi (http://qudt.org/vocab/unit/PERMILLE-PER-PSI)"""
    return QUDT_UNIT["PERMILLE-PER-PSI"]


def get_qudt_unit_fraction() -> URIRef:
    """Returns the URI for QUDT unit: Fraction (http://qudt.org/vocab/unit/FRACTION)"""
    return QUDT_UNIT["FRACTION"]


def get_qudt_unit_grade() -> URIRef:
    """Returns the URI for QUDT unit: Grade (http://qudt.org/vocab/unit/GR)"""
    return QUDT_UNIT["GR"]


def get_qudt_unit_one_per_one() -> URIRef:
    """Returns the URI for QUDT unit: One per One (http://qudt.org/vocab/unit/ONE-PER-ONE)"""
    return QUDT_UNIT["ONE-PER-ONE"]


def get_qudt_unit_percent() -> URIRef:
    """Returns the URI for QUDT unit: Percent (http://qudt.org/vocab/unit/PERCENT)"""
    return QUDT_UNIT["PERCENT"]


def get_qudt_unit_permille() -> URIRef:
    """Returns the URI for QUDT unit: Permille (http://qudt.org/vocab/unit/PERMILLE)"""
    return QUDT_UNIT["PERMILLE"]


def get_qudt_unit_relative_permittivity() -> URIRef:
    """Returns the URI for QUDT unit: Relative Permittivity (http://qudt.org/vocab/unit/PERMITTIVITY_REL)"""
    return QUDT_UNIT["PERMITTIVITY_REL"]


def get_qudt_unit_practical_salinity_unit() -> URIRef:
    """Returns the URI for QUDT unit: Practical Salinity Unit (http://qudt.org/vocab/unit/PSU)"""
    return QUDT_UNIT["PSU"]


def get_qudt_unit_kilohertz_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kilohertz Metre (http://qudt.org/vocab/unit/KiloHZ-M)"""
    return QUDT_UNIT["KILOHZ-M"]


def get_qudt_unit_british_thermal_unit_international_definition_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) per Hour (http://qudt.org/vocab/unit/BTU_IT-PER-HR)"""
    return QUDT_UNIT["BTU_IT-PER-HR"]


def get_qudt_unit_british_thermal_unit_international_definition_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) per Minute (http://qudt.org/vocab/unit/BTU_IT-PER-MIN)"""
    return QUDT_UNIT["BTU_IT-PER-MIN"]


def get_qudt_unit_british_thermal_unit_international_definition_per_second() -> URIRef:
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) per Second (http://qudt.org/vocab/unit/BTU_IT-PER-SEC)"""
    return QUDT_UNIT["BTU_IT-PER-SEC"]


def get_qudt_unit_british_thermal_unit_thermochemical_definition_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: British Thermal Unit (thermochemical Definition) per Hour (http://qudt.org/vocab/unit/BTU_TH-PER-HR)"""
    return QUDT_UNIT["BTU_TH-PER-HR"]


def get_qudt_unit_british_thermal_unit_thermochemical_definition_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: British Thermal Unit (thermochemical Definition) per Minute (http://qudt.org/vocab/unit/BTU_TH-PER-MIN)"""
    return QUDT_UNIT["BTU_TH-PER-MIN"]


def get_qudt_unit_british_thermal_unit_thermochemical_definition_per_second() -> URIRef:
    """Returns the URI for QUDT unit: British Thermal Unit (thermochemical Definition) per Second (http://qudt.org/vocab/unit/BTU_TH-PER-SEC)"""
    return QUDT_UNIT["BTU_TH-PER-SEC"]


def get_qudt_unit_thermochemical_calorie_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Thermochemical Calorie per Minute (http://qudt.org/vocab/unit/CAL_TH-PER-MIN)"""
    return QUDT_UNIT["CAL_TH-PER-MIN"]


def get_qudt_unit_thermochemical_calorie_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Thermochemical Calorie per Second (http://qudt.org/vocab/unit/CAL_TH-PER-SEC)"""
    return QUDT_UNIT["CAL_TH-PER-SEC"]


def get_qudt_unit_kilo_british_thermal_unit_international_definition_per_hour() -> (
    URIRef
):
    """Returns the URI for QUDT unit: Kilo British Thermal Unit (international Definition) per Hour (http://qudt.org/vocab/unit/KiloBTU_IT-PER-HR)"""
    return QUDT_UNIT["KILOBTU_IT-PER-HR"]


def get_qudt_unit_kilo_british_thermal_unit_thermochemical_definition_per_hour() -> (
    URIRef
):
    """Returns the URI for QUDT unit: Kilo British Thermal Unit (thermochemical Definition) per Hour (http://qudt.org/vocab/unit/KiloBTU_TH-PER-HR)"""
    return QUDT_UNIT["KILOBTU_TH-PER-HR"]


def get_qudt_unit_kilocalorie_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Kilocalorie per Minute (http://qudt.org/vocab/unit/KiloCAL-PER-MIN)"""
    return QUDT_UNIT["KILOCAL-PER-MIN"]


def get_qudt_unit_kilocalorie_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Kilocalorie per Second (http://qudt.org/vocab/unit/KiloCAL-PER-SEC)"""
    return QUDT_UNIT["KILOCAL-PER-SEC"]


def get_qudt_unit_kilo_thermochemical_calorie_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Kilo Thermochemical Calorie per Hour (http://qudt.org/vocab/unit/KiloCAL_TH-PER-HR)"""
    return QUDT_UNIT["KILOCAL_TH-PER-HR"]


def get_qudt_unit_kilo_thermochemical_calorie_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Kilo Thermochemical Calorie per Minute (http://qudt.org/vocab/unit/KiloCAL_TH-PER-MIN)"""
    return QUDT_UNIT["KILOCAL_TH-PER-MIN"]


def get_qudt_unit_kilo_thermochemical_calorie_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Kilo Thermochemical Calorie per Second (http://qudt.org/vocab/unit/KiloCAL_TH-PER-SEC)"""
    return QUDT_UNIT["KILOCAL_TH-PER-SEC"]


def get_qudt_unit_mega_british_thermal_unit_international_definition_per_hour() -> (
    URIRef
):
    """Returns the URI for QUDT unit: Mega British Thermal Unit (international Definition) per Hour (http://qudt.org/vocab/unit/MegaBTU_IT-PER-HR)"""
    return QUDT_UNIT["MEGABTU_IT-PER-HR"]


def get_qudt_unit_therm_us_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Therm Us per Hour (http://qudt.org/vocab/unit/THM_US-PER-HR)"""
    return QUDT_UNIT["THM_US-PER-HR"]


def get_qudt_unit_ton_of_refrigeration() -> URIRef:
    """Returns the URI for QUDT unit: Ton of Refrigeration (http://qudt.org/vocab/unit/TON_FG)"""
    return QUDT_UNIT["TON_FG"]


def get_qudt_unit_decisiemens_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Decisiemens per Metre (http://qudt.org/vocab/unit/DeciS-PER-M)"""
    return QUDT_UNIT["DECIS-PER-M"]


def get_qudt_unit_kilosiemens_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kilosiemens per Metre (http://qudt.org/vocab/unit/KiloS-PER-M)"""
    return QUDT_UNIT["KILOS-PER-M"]


def get_qudt_unit_megasiemens_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Megasiemens per Metre (http://qudt.org/vocab/unit/MegaS-PER-M)"""
    return QUDT_UNIT["MEGAS-PER-M"]


def get_qudt_unit_microsiemens_per_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Microsiemens per Centimetre (http://qudt.org/vocab/unit/MicroS-PER-CentiM)"""
    return QUDT_UNIT["MICROS-PER-CENTIM"]


def get_qudt_unit_microsiemens_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Microsiemens per Metre (http://qudt.org/vocab/unit/MicroS-PER-M)"""
    return QUDT_UNIT["MICROS-PER-M"]


def get_qudt_unit_millisiemens_per_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Millisiemens per Centimetre (http://qudt.org/vocab/unit/MilliS-PER-CentiM)"""
    return QUDT_UNIT["MILLIS-PER-CENTIM"]


def get_qudt_unit_millisiemens_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Millisiemens per Metre (http://qudt.org/vocab/unit/MilliS-PER-M)"""
    return QUDT_UNIT["MILLIS-PER-M"]


def get_qudt_unit_nanosiemens_per_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Nanosiemens per Centimetre (http://qudt.org/vocab/unit/NanoS-PER-CentiM)"""
    return QUDT_UNIT["NANOS-PER-CENTIM"]


def get_qudt_unit_nanosiemens_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Nanosiemens per Metre (http://qudt.org/vocab/unit/NanoS-PER-M)"""
    return QUDT_UNIT["NANOS-PER-M"]


def get_qudt_unit_picosiemens_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Picosiemens per Metre (http://qudt.org/vocab/unit/PicoS-PER-M)"""
    return QUDT_UNIT["PICOS-PER-M"]


def get_qudt_unit_siemens_per_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Siemens per Centimetre (http://qudt.org/vocab/unit/S-PER-CentiM)"""
    return QUDT_UNIT["S-PER-CENTIM"]


def get_qudt_unit_siemens_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Siemens per Metre (http://qudt.org/vocab/unit/S-PER-M)"""
    return QUDT_UNIT["S-PER-M"]


def get_qudt_unit_square_microsiemens_per_square_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Square Microsiemens per Square Centimetre (http://qudt.org/vocab/unit/MicroS2-PER-CentiM2)"""
    return QUDT_UNIT["MICROS2-PER-CENTIM2"]


def get_qudt_unit_kilowatt_per_ton_of_refrigeration() -> URIRef:
    """Returns the URI for QUDT unit: Kilowatt per Ton of Refrigeration (http://qudt.org/vocab/unit/KiloW-PER-TON_FG)"""
    return QUDT_UNIT["KILOW-PER-TON_FG"]


def get_qudt_unit_swiss_franc_per_hectare() -> URIRef:
    """Returns the URI for QUDT unit: Swiss Franc per Hectare (http://qudt.org/vocab/unit/CCY_CHF-PER-HA)"""
    return QUDT_UNIT["CCY_CHF-PER-HA"]


def get_qudt_unit_euro_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Euro per Square Metre (http://qudt.org/vocab/unit/CCY_EUR-PER-M2)"""
    return QUDT_UNIT["CCY_EUR-PER-M2"]


def get_qudt_unit_bulgarian_lev_per_kilowatt_hour() -> URIRef:
    """Returns the URI for QUDT unit: Bulgarian Lev per Kilowatt Hour (http://qudt.org/vocab/unit/CCY_BGN-PER-KiloW-HR)"""
    return QUDT_UNIT["CCY_BGN-PER-KILOW-HR"]


def get_qudt_unit_swiss_franc_per_kilowatt_hour() -> URIRef:
    """Returns the URI for QUDT unit: Swiss Franc per Kilowatt Hour (http://qudt.org/vocab/unit/CCY_CHF-PER-KiloW-HR)"""
    return QUDT_UNIT["CCY_CHF-PER-KILOW-HR"]


def get_qudt_unit_czech_koruna_per_kilowatt_hour() -> URIRef:
    """Returns the URI for QUDT unit: Czech Koruna per Kilowatt Hour (http://qudt.org/vocab/unit/CCY_CZK-PER-KiloW-HR)"""
    return QUDT_UNIT["CCY_CZK-PER-KILOW-HR"]


def get_qudt_unit_danish_krone_per_kilowatt_hour() -> URIRef:
    """Returns the URI for QUDT unit: Danish Krone per Kilowatt Hour (http://qudt.org/vocab/unit/CCY_DKK-PER-KiloW-HR)"""
    return QUDT_UNIT["CCY_DKK-PER-KILOW-HR"]


def get_qudt_unit_euro_per_kilowatt_hour() -> URIRef:
    """Returns the URI for QUDT unit: Euro per Kilowatt Hour (http://qudt.org/vocab/unit/CCY_EUR-PER-KiloW-HR)"""
    return QUDT_UNIT["CCY_EUR-PER-KILOW-HR"]


def get_qudt_unit_euro_per_watt_hour() -> URIRef:
    """Returns the URI for QUDT unit: Euro per Watt Hour (http://qudt.org/vocab/unit/CCY_EUR-PER-W-HR)"""
    return QUDT_UNIT["CCY_EUR-PER-W-HR"]


def get_qudt_unit_euro_per_watt_second() -> URIRef:
    """Returns the URI for QUDT unit: Euro per Watt Second (http://qudt.org/vocab/unit/CCY_EUR-PER-W-SEC)"""
    return QUDT_UNIT["CCY_EUR-PER-W-SEC"]


def get_qudt_unit_pound_sterling_per_kilowatt_hour() -> URIRef:
    """Returns the URI for QUDT unit: Pound Sterling per Kilowatt Hour (http://qudt.org/vocab/unit/CCY_GBP-PER-KiloW-HR)"""
    return QUDT_UNIT["CCY_GBP-PER-KILOW-HR"]


def get_qudt_unit_forint_per_kilowatt_hour() -> URIRef:
    """Returns the URI for QUDT unit: Forint per Kilowatt Hour (http://qudt.org/vocab/unit/CCY_HUF-PER-KiloW-HR)"""
    return QUDT_UNIT["CCY_HUF-PER-KILOW-HR"]


def get_qudt_unit_norwegian_krone_per_kilowatt_hour() -> URIRef:
    """Returns the URI for QUDT unit: Norwegian Krone per Kilowatt Hour (http://qudt.org/vocab/unit/CCY_NOK-PER-KiloW-HR)"""
    return QUDT_UNIT["CCY_NOK-PER-KILOW-HR"]


def get_qudt_unit_zloty_per_kilowatt_hour() -> URIRef:
    """Returns the URI for QUDT unit: Zloty per Kilowatt Hour (http://qudt.org/vocab/unit/CCY_PLN-PER-KiloW-HR)"""
    return QUDT_UNIT["CCY_PLN-PER-KILOW-HR"]


def get_qudt_unit_romanian_new_leu_per_kilowatt_hour() -> URIRef:
    """Returns the URI for QUDT unit: Romanian New Leu per Kilowatt Hour (http://qudt.org/vocab/unit/CCY_RON-PER-KiloW-HR)"""
    return QUDT_UNIT["CCY_RON-PER-KILOW-HR"]


def get_qudt_unit_swedish_krona_per_kilowatt_hour() -> URIRef:
    """Returns the URI for QUDT unit: Swedish Krona per Kilowatt Hour (http://qudt.org/vocab/unit/CCY_SEK-PER-KiloW-HR)"""
    return QUDT_UNIT["CCY_SEK-PER-KILOW-HR"]


def get_qudt_unit_swiss_franc_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Swiss Franc per Kilogram (http://qudt.org/vocab/unit/CCY_CHF-PER-KiloGM)"""
    return QUDT_UNIT["CCY_CHF-PER-KILOGM"]


def get_qudt_unit_euro_per_kilowatt() -> URIRef:
    """Returns the URI for QUDT unit: Euro per Kilowatt (http://qudt.org/vocab/unit/CCY_EUR-PER-KiloW)"""
    return QUDT_UNIT["CCY_EUR-PER-KILOW"]


def get_qudt_unit_euro_per_watt() -> URIRef:
    """Returns the URI for QUDT unit: Euro per Watt (http://qudt.org/vocab/unit/CCY_EUR-PER-W)"""
    return QUDT_UNIT["CCY_EUR-PER-W"]


def get_qudt_unit_number_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Number per Minute (http://qudt.org/vocab/unit/NUM-PER-MIN)"""
    return QUDT_UNIT["NUM-PER-MIN"]


def get_qudt_unit_metre_per_degree_celsius_metre() -> URIRef:
    """Returns the URI for QUDT unit: Metre per Degree Celsius Metre (http://qudt.org/vocab/unit/M-PER-DEG_C-M)"""
    return QUDT_UNIT["M-PER-DEG_C-M"]


def get_qudt_unit_millimetre_per_degree_celsius_metre() -> URIRef:
    """Returns the URI for QUDT unit: Millimetre per Degree Celsius Metre (http://qudt.org/vocab/unit/MilliM-PER-DEG_C-M)"""
    return QUDT_UNIT["MILLIM-PER-DEG_C-M"]


def get_qudt_unit_reciprocal_degree_fahrenheit() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Degree Fahrenheit (http://qudt.org/vocab/unit/PER-DEG_F)"""
    return QUDT_UNIT["PER-DEG_F"]


def get_qudt_unit_reciprocal_megakelvin() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Megakelvin (http://qudt.org/vocab/unit/PER-MegaK)"""
    return QUDT_UNIT["PER-MEGAK"]


def get_qudt_unit_parts_per_million_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Parts per Million per Kelvin (http://qudt.org/vocab/unit/PPM-PER-K)"""
    return QUDT_UNIT["PPM-PER-K"]


def get_qudt_unit_parts_per_ten_million_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Parts per Ten Million per Kelvin (http://qudt.org/vocab/unit/PPTM-PER-K)"""
    return QUDT_UNIT["PPTM-PER-K"]


def get_qudt_unit_bitcoin() -> URIRef:
    """Returns the URI for QUDT unit: Bitcoin (http://qudt.org/vocab/unit/CCY_BTC)"""
    return QUDT_UNIT["CCY_BTC"]


def get_qudt_unit_ether() -> URIRef:
    """Returns the URI for QUDT unit: Ether (http://qudt.org/vocab/unit/CCY_ETH)"""
    return QUDT_UNIT["CCY_ETH"]


def get_qudt_unit_tether_usd() -> URIRef:
    """Returns the URI for QUDT unit: Tether USD (http://qudt.org/vocab/unit/CCY_USDT)"""
    return QUDT_UNIT["CCY_USDT"]


def get_qudt_unit_mega_us_dollar() -> URIRef:
    """Returns the URI for QUDT unit: Mega Us Dollar (http://qudt.org/vocab/unit/MegaCCY_USD)"""
    return QUDT_UNIT["MEGACCY_USD"]


def get_qudt_unit_mega_us_dollar_per_flight() -> URIRef:
    """Returns the URI for QUDT unit: Mega Us Dollar per Flight (http://qudt.org/vocab/unit/MegaCCY_USD-PER-FLIGHT)"""
    return QUDT_UNIT["MEGACCY_USD-PER-FLIGHT"]


def get_qudt_unit_attoampere() -> URIRef:
    """Returns the URI for QUDT unit: Attoampere (http://qudt.org/vocab/unit/AttoA)"""
    return QUDT_UNIT["ATTOA"]


def get_qudt_unit_femtoampere() -> URIRef:
    """Returns the URI for QUDT unit: Femtoampere (http://qudt.org/vocab/unit/FemtoA)"""
    return QUDT_UNIT["FEMTOA"]


def get_qudt_unit_gigaampere() -> URIRef:
    """Returns the URI for QUDT unit: Gigaampere (http://qudt.org/vocab/unit/GigaA)"""
    return QUDT_UNIT["GIGAA"]


def get_qudt_unit_petaampere() -> URIRef:
    """Returns the URI for QUDT unit: Petaampere (http://qudt.org/vocab/unit/PetaA)"""
    return QUDT_UNIT["PETAA"]


def get_qudt_unit_teraampere() -> URIRef:
    """Returns the URI for QUDT unit: Teraampere (http://qudt.org/vocab/unit/TeraA)"""
    return QUDT_UNIT["TERAA"]


def get_qudt_unit_diopter() -> URIRef:
    """Returns the URI for QUDT unit: Diopter (http://qudt.org/vocab/unit/DIOPTER)"""
    return QUDT_UNIT["DIOPTER"]


def get_qudt_unit_bit_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Bit per Second (http://qudt.org/vocab/unit/BIT-PER-SEC)"""
    return QUDT_UNIT["BIT-PER-SEC"]


def get_qudt_unit_exabit_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Exabit per Second (http://qudt.org/vocab/unit/ExaBIT-PER-SEC)"""
    return QUDT_UNIT["EXABIT-PER-SEC"]


def get_qudt_unit_gigabit_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Gigabit per Second (http://qudt.org/vocab/unit/GigaBIT-PER-SEC)"""
    return QUDT_UNIT["GIGABIT-PER-SEC"]


def get_qudt_unit_kilobit_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Kilobit per Second (http://qudt.org/vocab/unit/KiloBIT-PER-SEC)"""
    return QUDT_UNIT["KILOBIT-PER-SEC"]


def get_qudt_unit_kilobyte_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Kilobyte per Second (http://qudt.org/vocab/unit/KiloBYTE-PER-SEC)"""
    return QUDT_UNIT["KILOBYTE-PER-SEC"]


def get_qudt_unit_megabit_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Megabit per Second (http://qudt.org/vocab/unit/MegaBIT-PER-SEC)"""
    return QUDT_UNIT["MEGABIT-PER-SEC"]


def get_qudt_unit_petabit_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Petabit per Second (http://qudt.org/vocab/unit/PetaBIT-PER-SEC)"""
    return QUDT_UNIT["PETABIT-PER-SEC"]


def get_qudt_unit_terabit_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Terabit per Second (http://qudt.org/vocab/unit/TeraBIT-PER-SEC)"""
    return QUDT_UNIT["TERABIT-PER-SEC"]


def get_qudt_unit_gibibit() -> URIRef:
    """Returns the URI for QUDT unit: Gibibit (http://qudt.org/vocab/unit/GibiBIT)"""
    return QUDT_UNIT["GIBIBIT"]


def get_qudt_unit_gigabit() -> URIRef:
    """Returns the URI for QUDT unit: Gigabit (http://qudt.org/vocab/unit/GigaBIT)"""
    return QUDT_UNIT["GIGABIT"]


def get_qudt_unit_kibibit() -> URIRef:
    """Returns the URI for QUDT unit: Kibibit (http://qudt.org/vocab/unit/KibiBIT)"""
    return QUDT_UNIT["KIBIBIT"]


def get_qudt_unit_kilobit() -> URIRef:
    """Returns the URI for QUDT unit: Kilobit (http://qudt.org/vocab/unit/KiloBIT)"""
    return QUDT_UNIT["KILOBIT"]


def get_qudt_unit_mebibit() -> URIRef:
    """Returns the URI for QUDT unit: Mebibit (http://qudt.org/vocab/unit/MebiBIT)"""
    return QUDT_UNIT["MEBIBIT"]


def get_qudt_unit_megabit() -> URIRef:
    """Returns the URI for QUDT unit: Megabit (http://qudt.org/vocab/unit/MegaBIT)"""
    return QUDT_UNIT["MEGABIT"]


def get_qudt_unit_octet() -> URIRef:
    """Returns the URI for QUDT unit: Octet (http://qudt.org/vocab/unit/OCTET)"""
    return QUDT_UNIT["OCTET"]


def get_qudt_unit_petabit() -> URIRef:
    """Returns the URI for QUDT unit: Petabit (http://qudt.org/vocab/unit/PetaBIT)"""
    return QUDT_UNIT["PETABIT"]


def get_qudt_unit_terabit() -> URIRef:
    """Returns the URI for QUDT unit: Terabit (http://qudt.org/vocab/unit/TeraBIT)"""
    return QUDT_UNIT["TERABIT"]


def get_qudt_unit_baud() -> URIRef:
    """Returns the URI for QUDT unit: Baud (http://qudt.org/vocab/unit/BAUD)"""
    return QUDT_UNIT["BAUD"]


def get_qudt_unit_kilobaud() -> URIRef:
    """Returns the URI for QUDT unit: Kilobaud (http://qudt.org/vocab/unit/KiloBAUD)"""
    return QUDT_UNIT["KILOBAUD"]


def get_qudt_unit_megabaud() -> URIRef:
    """Returns the URI for QUDT unit: Megabaud (http://qudt.org/vocab/unit/MegaBAUD)"""
    return QUDT_UNIT["MEGABAUD"]


def get_qudt_unit_ampere_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Ampere per Square Metre (http://qudt.org/vocab/unit/A-PER-M2)"""
    return QUDT_UNIT["A-PER-M2"]


def get_qudt_unit_mil() -> URIRef:
    """Returns the URI for QUDT unit: Mil (http://qudt.org/vocab/unit/MIL_Length)"""
    return QUDT_UNIT["MIL_LENGTH"]


def get_qudt_unit_big_point() -> URIRef:
    """Returns the URI for QUDT unit: Big Point (http://qudt.org/vocab/unit/PT_BIG)"""
    return QUDT_UNIT["PT_BIG"]


def get_qudt_unit_microsievert() -> URIRef:
    """Returns the URI for QUDT unit: Microsievert (http://qudt.org/vocab/unit/MicroSV)"""
    return QUDT_UNIT["MICROSV"]


def get_qudt_unit_milli_roentgen_equivalent_man() -> URIRef:
    """Returns the URI for QUDT unit: Milli Roentgen Equivalent Man (http://qudt.org/vocab/unit/MilliR_man)"""
    return QUDT_UNIT["MILLIR_MAN"]


def get_qudt_unit_millisievert() -> URIRef:
    """Returns the URI for QUDT unit: Millisievert (http://qudt.org/vocab/unit/MilliSV)"""
    return QUDT_UNIT["MILLISV"]


def get_qudt_unit_nanosievert() -> URIRef:
    """Returns the URI for QUDT unit: Nanosievert (http://qudt.org/vocab/unit/NanoSV)"""
    return QUDT_UNIT["NANOSV"]


def get_qudt_unit_rem() -> URIRef:
    """Returns the URI for QUDT unit: Rem (http://qudt.org/vocab/unit/REM)"""
    return QUDT_UNIT["REM"]


def get_qudt_unit_roentgen_equivalent_man() -> URIRef:
    """Returns the URI for QUDT unit: Roentgen Equivalent Man (http://qudt.org/vocab/unit/R_man)"""
    return QUDT_UNIT["R_MAN"]


def get_qudt_unit_sievert() -> URIRef:
    """Returns the URI for QUDT unit: Sievert (http://qudt.org/vocab/unit/SV)"""
    return QUDT_UNIT["SV"]


def get_qudt_unit_dots_per_inch() -> URIRef:
    """Returns the URI for QUDT unit: Dots per Inch (http://qudt.org/vocab/unit/DPI)"""
    return QUDT_UNIT["DPI"]


def get_qudt_unit_dry_barrel_us() -> URIRef:
    """Returns the URI for QUDT unit: Dry Barrel (US) (http://qudt.org/vocab/unit/BBL_US_DRY)"""
    return QUDT_UNIT["BBL_US_DRY"]


def get_qudt_unit_bushel_uk() -> URIRef:
    """Returns the URI for QUDT unit: Bushel (UK) (http://qudt.org/vocab/unit/BU_UK)"""
    return QUDT_UNIT["BU_UK"]


def get_qudt_unit_bushel_us() -> URIRef:
    """Returns the URI for QUDT unit: Bushel (US) (http://qudt.org/vocab/unit/BU_US)"""
    return QUDT_UNIT["BU_US"]


def get_qudt_unit_cord() -> URIRef:
    """Returns the URI for QUDT unit: Cord (http://qudt.org/vocab/unit/CORD)"""
    return QUDT_UNIT["CORD"]


def get_qudt_unit_dry_gallon_us() -> URIRef:
    """Returns the URI for QUDT unit: Dry Gallon Us (http://qudt.org/vocab/unit/GAL_US_DRY)"""
    return QUDT_UNIT["GAL_US_DRY"]


def get_qudt_unit_us_dry_pint() -> URIRef:
    """Returns the URI for QUDT unit: Us Dry Pint (http://qudt.org/vocab/unit/PINT_US_DRY)"""
    return QUDT_UNIT["PINT_US_DRY"]


def get_qudt_unit_us_peck() -> URIRef:
    """Returns the URI for QUDT unit: Us Peck (http://qudt.org/vocab/unit/PK_US_DRY)"""
    return QUDT_UNIT["PK_US_DRY"]


def get_qudt_unit_us_dry_quart() -> URIRef:
    """Returns the URI for QUDT unit: Us Dry Quart (http://qudt.org/vocab/unit/QT_US_DRY)"""
    return QUDT_UNIT["QT_US_DRY"]


def get_qudt_unit_centipoise() -> URIRef:
    """Returns the URI for QUDT unit: Centipoise (http://qudt.org/vocab/unit/CentiPOISE)"""
    return QUDT_UNIT["CENTIPOISE"]


def get_qudt_unit_decapoise() -> URIRef:
    """Returns the URI for QUDT unit: Decapoise (http://qudt.org/vocab/unit/DecaPOISE)"""
    return QUDT_UNIT["DECAPOISE"]


def get_qudt_unit_gram_per_centimetre_second() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Centimetre Second (http://qudt.org/vocab/unit/GM-PER-CentiM-SEC)"""
    return QUDT_UNIT["GM-PER-CENTIM-SEC"]


def get_qudt_unit_kilogram_per_metre_day() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Metre Day (http://qudt.org/vocab/unit/KiloGM-PER-M-DAY)"""
    return QUDT_UNIT["KILOGM-PER-M-DAY"]


def get_qudt_unit_kilogram_per_metre_hour() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Metre Hour (http://qudt.org/vocab/unit/KiloGM-PER-M-HR)"""
    return QUDT_UNIT["KILOGM-PER-M-HR"]


def get_qudt_unit_kilogram_per_metre_minute() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Metre Minute (http://qudt.org/vocab/unit/KiloGM-PER-M-MIN)"""
    return QUDT_UNIT["KILOGM-PER-M-MIN"]


def get_qudt_unit_kilogram_per_metre_second() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Metre Second (http://qudt.org/vocab/unit/KiloGM-PER-M-SEC)"""
    return QUDT_UNIT["KILOGM-PER-M-SEC"]


def get_qudt_unit_kilopoise() -> URIRef:
    """Returns the URI for QUDT unit: Kilopoise (http://qudt.org/vocab/unit/KiloPOISE)"""
    return QUDT_UNIT["KILOPOISE"]


def get_qudt_unit_pound_mass_per_foot_day() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Foot Day (http://qudt.org/vocab/unit/LB-PER-FT-DAY)"""
    return QUDT_UNIT["LB-PER-FT-DAY"]


def get_qudt_unit_pound_mass_per_foot_hour() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Foot Hour (http://qudt.org/vocab/unit/LB-PER-FT-HR)"""
    return QUDT_UNIT["LB-PER-FT-HR"]


def get_qudt_unit_pound_mass_per_foot_minute() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Foot Minute (http://qudt.org/vocab/unit/LB-PER-FT-MIN)"""
    return QUDT_UNIT["LB-PER-FT-MIN"]


def get_qudt_unit_pound_mass_per_foot_second() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Foot Second (http://qudt.org/vocab/unit/LB-PER-FT-SEC)"""
    return QUDT_UNIT["LB-PER-FT-SEC"]


def get_qudt_unit_pound_force_second_per_square_foot() -> URIRef:
    """Returns the URI for QUDT unit: Pound Force Second per Square Foot (http://qudt.org/vocab/unit/LB_F-SEC-PER-FT2)"""
    return QUDT_UNIT["LB_F-SEC-PER-FT2"]


def get_qudt_unit_pound_force_second_per_square_inch() -> URIRef:
    """Returns the URI for QUDT unit: Pound Force Second per Square Inch (http://qudt.org/vocab/unit/LB_F-SEC-PER-IN2)"""
    return QUDT_UNIT["LB_F-SEC-PER-IN2"]


def get_qudt_unit_micropoise() -> URIRef:
    """Returns the URI for QUDT unit: Micropoise (http://qudt.org/vocab/unit/MicroPOISE)"""
    return QUDT_UNIT["MICROPOISE"]


def get_qudt_unit_millipascal_second() -> URIRef:
    """Returns the URI for QUDT unit: Millipascal Second (http://qudt.org/vocab/unit/MilliPA-SEC)"""
    return QUDT_UNIT["MILLIPA-SEC"]


def get_qudt_unit_newton_second_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Newton Second per Square Metre (http://qudt.org/vocab/unit/N-SEC-PER-M2)"""
    return QUDT_UNIT["N-SEC-PER-M2"]


def get_qudt_unit_pascal_second() -> URIRef:
    """Returns the URI for QUDT unit: Pascal Second (http://qudt.org/vocab/unit/PA-SEC)"""
    return QUDT_UNIT["PA-SEC"]


def get_qudt_unit_poundal_second_per_square_foot() -> URIRef:
    """Returns the URI for QUDT unit: Poundal Second per Square Foot (http://qudt.org/vocab/unit/PDL-SEC-PER-FT2)"""
    return QUDT_UNIT["PDL-SEC-PER-FT2"]


def get_qudt_unit_poundal_second_per_square_inch() -> URIRef:
    """Returns the URI for QUDT unit: Poundal Second per Square Inch (http://qudt.org/vocab/unit/PDL-SEC-PER-IN2)"""
    return QUDT_UNIT["PDL-SEC-PER-IN2"]


def get_qudt_unit_poise() -> URIRef:
    """Returns the URI for QUDT unit: Poise (http://qudt.org/vocab/unit/POISE)"""
    return QUDT_UNIT["POISE"]


def get_qudt_unit_slug_per_foot_second() -> URIRef:
    """Returns the URI for QUDT unit: Slug per Foot Second (http://qudt.org/vocab/unit/SLUG-PER-FT-SEC)"""
    return QUDT_UNIT["SLUG-PER-FT-SEC"]


def get_qudt_unit_richter_magnitude() -> URIRef:
    """Returns the URI for QUDT unit: Richter Magnitude (http://qudt.org/vocab/unit/RichterMagnitude)"""
    return QUDT_UNIT["RICHTERMAGNITUDE"]


def get_qudt_unit_second_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Second per Kilogram (http://qudt.org/vocab/unit/SEC-PER-KiloGM)"""
    return QUDT_UNIT["SEC-PER-KILOGM"]


def get_qudt_unit_ampere_hour_per_cubic_decimetre() -> URIRef:
    """Returns the URI for QUDT unit: Ampere Hour per Cubic Decimetre (http://qudt.org/vocab/unit/A-HR-PER-DeciM3)"""
    return QUDT_UNIT["A-HR-PER-DECIM3"]


def get_qudt_unit_ampere_hour_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Ampere Hour per Cubic Metre (http://qudt.org/vocab/unit/A-HR-PER-M3)"""
    return QUDT_UNIT["A-HR-PER-M3"]


def get_qudt_unit_megacoulomb_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Megacoulomb per Cubic Metre (http://qudt.org/vocab/unit/MegaC-PER-M3)"""
    return QUDT_UNIT["MEGAC-PER-M3"]


def get_qudt_unit_microcoulomb_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Microcoulomb per Cubic Metre (http://qudt.org/vocab/unit/MicroC-PER-M3)"""
    return QUDT_UNIT["MICROC-PER-M3"]


def get_qudt_unit_coulomb_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Coulomb per Metre (http://qudt.org/vocab/unit/C-PER-M)"""
    return QUDT_UNIT["C-PER-M"]


def get_qudt_unit_statcoulomb_per_mole() -> URIRef:
    """Returns the URI for QUDT unit: Statcoulomb per Mole (http://qudt.org/vocab/unit/C_Stat-PER-MOL)"""
    return QUDT_UNIT["C_STAT-PER-MOL"]


def get_qudt_unit_ampere_hour_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Ampere Hour per Kilogram (http://qudt.org/vocab/unit/A-HR-PER-KiloGM)"""
    return QUDT_UNIT["A-HR-PER-KILOGM"]


def get_qudt_unit_kiloroentgen() -> URIRef:
    """Returns the URI for QUDT unit: Kiloroentgen (http://qudt.org/vocab/unit/KiloR)"""
    return QUDT_UNIT["KILOR"]


def get_qudt_unit_millicoulomb_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Millicoulomb per Kilogram (http://qudt.org/vocab/unit/MilliC-PER-KiloGM)"""
    return QUDT_UNIT["MILLIC-PER-KILOGM"]


def get_qudt_unit_milliroentgen() -> URIRef:
    """Returns the URI for QUDT unit: Milliroentgen (http://qudt.org/vocab/unit/MilliR)"""
    return QUDT_UNIT["MILLIR"]


def get_qudt_unit_roentgen() -> URIRef:
    """Returns the URI for QUDT unit: Roentgen (http://qudt.org/vocab/unit/R)"""
    return QUDT_UNIT["R"]


def get_qudt_unit_coulomb_per_cubic_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Coulomb per Cubic Centimetre (http://qudt.org/vocab/unit/C-PER-CentiM3)"""
    return QUDT_UNIT["C-PER-CENTIM3"]


def get_qudt_unit_coulomb_per_cubic_millimetre() -> URIRef:
    """Returns the URI for QUDT unit: Coulomb per Cubic Millimetre (http://qudt.org/vocab/unit/C-PER-MilliM3)"""
    return QUDT_UNIT["C-PER-MILLIM3"]


def get_qudt_unit_gigacoulomb_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Gigacoulomb per Cubic Metre (http://qudt.org/vocab/unit/GigaC-PER-M3)"""
    return QUDT_UNIT["GIGAC-PER-M3"]


def get_qudt_unit_kilocoulomb_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kilocoulomb per Cubic Metre (http://qudt.org/vocab/unit/KiloC-PER-M3)"""
    return QUDT_UNIT["KILOC-PER-M3"]


def get_qudt_unit_millicoulomb_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Millicoulomb per Cubic Metre (http://qudt.org/vocab/unit/MilliC-PER-M3)"""
    return QUDT_UNIT["MILLIC-PER-M3"]


def get_qudt_unit_statmho() -> URIRef:
    """Returns the URI for QUDT unit: Statmho (http://qudt.org/vocab/unit/MHO_Stat)"""
    return QUDT_UNIT["MHO_STAT"]


def get_qudt_unit_absiemen() -> URIRef:
    """Returns the URI for QUDT unit: Absiemen (http://qudt.org/vocab/unit/S_Ab)"""
    return QUDT_UNIT["S_AB"]


def get_qudt_unit_statsiemens() -> URIRef:
    """Returns the URI for QUDT unit: Statsiemens (http://qudt.org/vocab/unit/S_Stat)"""
    return QUDT_UNIT["S_STAT"]


def get_qudt_unit_abampere() -> URIRef:
    """Returns the URI for QUDT unit: Abampere (http://qudt.org/vocab/unit/A_Ab)"""
    return QUDT_UNIT["A_AB"]


def get_qudt_unit_statampere() -> URIRef:
    """Returns the URI for QUDT unit: Statampere (http://qudt.org/vocab/unit/A_Stat)"""
    return QUDT_UNIT["A_STAT"]


def get_qudt_unit_biot() -> URIRef:
    """Returns the URI for QUDT unit: Biot (http://qudt.org/vocab/unit/BIOT)"""
    return QUDT_UNIT["BIOT"]


def get_qudt_unit_kiloampere() -> URIRef:
    """Returns the URI for QUDT unit: Kiloampere (http://qudt.org/vocab/unit/KiloA)"""
    return QUDT_UNIT["KILOA"]


def get_qudt_unit_megaampere() -> URIRef:
    """Returns the URI for QUDT unit: Megaampere (http://qudt.org/vocab/unit/MegaA)"""
    return QUDT_UNIT["MEGAA"]


def get_qudt_unit_microampere() -> URIRef:
    """Returns the URI for QUDT unit: Microampere (http://qudt.org/vocab/unit/MicroA)"""
    return QUDT_UNIT["MICROA"]


def get_qudt_unit_milliampere() -> URIRef:
    """Returns the URI for QUDT unit: Milliampere (http://qudt.org/vocab/unit/MilliA)"""
    return QUDT_UNIT["MILLIA"]


def get_qudt_unit_nanoampere() -> URIRef:
    """Returns the URI for QUDT unit: Nanoampere (http://qudt.org/vocab/unit/NanoA)"""
    return QUDT_UNIT["NANOA"]


def get_qudt_unit_picoampere() -> URIRef:
    """Returns the URI for QUDT unit: Picoampere (http://qudt.org/vocab/unit/PicoA)"""
    return QUDT_UNIT["PICOA"]


def get_qudt_unit_planck_current() -> URIRef:
    """Returns the URI for QUDT unit: Planck Current (http://qudt.org/vocab/unit/PlanckCurrent)"""
    return QUDT_UNIT["PLANCKCURRENT"]


def get_qudt_unit_ampere_per_square_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Ampere per Square Centimetre (http://qudt.org/vocab/unit/A-PER-CentiM2)"""
    return QUDT_UNIT["A-PER-CENTIM2"]


def get_qudt_unit_ampere_per_square_millimetre() -> URIRef:
    """Returns the URI for QUDT unit: Ampere per Square Millimetre (http://qudt.org/vocab/unit/A-PER-MilliM2)"""
    return QUDT_UNIT["A-PER-MILLIM2"]


def get_qudt_unit_abampere_per_square_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Abampere per Square Centimetre (http://qudt.org/vocab/unit/A_Ab-PER-CentiM2)"""
    return QUDT_UNIT["A_AB-PER-CENTIM2"]


def get_qudt_unit_statampere_per_square_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Statampere per Square Centimetre (http://qudt.org/vocab/unit/A_Stat-PER-CentiM2)"""
    return QUDT_UNIT["A_STAT-PER-CENTIM2"]


def get_qudt_unit_kiloampere_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kiloampere per Square Metre (http://qudt.org/vocab/unit/KiloA-PER-M2)"""
    return QUDT_UNIT["KILOA-PER-M2"]


def get_qudt_unit_megaampere_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Megaampere per Square Metre (http://qudt.org/vocab/unit/MegaA-PER-M2)"""
    return QUDT_UNIT["MEGAA-PER-M2"]


def get_qudt_unit_planck_current_density() -> URIRef:
    """Returns the URI for QUDT unit: Planck Current Density (http://qudt.org/vocab/unit/PlanckCurrentDensity)"""
    return QUDT_UNIT["PLANCKCURRENTDENSITY"]


def get_qudt_unit_ampere_per_radian() -> URIRef:
    """Returns the URI for QUDT unit: Ampere per Radian (http://qudt.org/vocab/unit/A-PER-RAD)"""
    return QUDT_UNIT["A-PER-RAD"]


def get_qudt_unit_ampere_per_degree_celsius() -> URIRef:
    """Returns the URI for QUDT unit: Ampere per Degree Celsius (http://qudt.org/vocab/unit/A-PER-DEG_C)"""
    return QUDT_UNIT["A-PER-DEG_C"]


def get_qudt_unit_ampere_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Ampere per Kelvin (http://qudt.org/vocab/unit/A-PER-K)"""
    return QUDT_UNIT["A-PER-K"]


def get_qudt_unit_kiloampere_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Kiloampere per Kelvin (http://qudt.org/vocab/unit/KiloA-PER-K)"""
    return QUDT_UNIT["KILOA-PER-K"]


def get_qudt_unit_microampere_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Microampere per Kelvin (http://qudt.org/vocab/unit/MicroA-PER-K)"""
    return QUDT_UNIT["MICROA-PER-K"]


def get_qudt_unit_milliampere_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Milliampere per Kelvin (http://qudt.org/vocab/unit/MilliA-PER-K)"""
    return QUDT_UNIT["MILLIA-PER-K"]


def get_qudt_unit_nanoampere_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Nanoampere per Kelvin (http://qudt.org/vocab/unit/NanoA-PER-K)"""
    return QUDT_UNIT["NANOA-PER-K"]


def get_qudt_unit_debye() -> URIRef:
    """Returns the URI for QUDT unit: Debye (http://qudt.org/vocab/unit/DEBYE)"""
    return QUDT_UNIT["DEBYE"]


def get_qudt_unit_abvolt_per_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Abvolt per Centimetre (http://qudt.org/vocab/unit/V_Ab-PER-CentiM)"""
    return QUDT_UNIT["V_AB-PER-CENTIM"]


def get_qudt_unit_statvolt_per_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Statvolt per Centimetre (http://qudt.org/vocab/unit/V_Stat-PER-CentiM)"""
    return QUDT_UNIT["V_STAT-PER-CENTIM"]


def get_qudt_unit_kilovolt_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kilovolt per Metre (http://qudt.org/vocab/unit/KiloV-PER-M)"""
    return QUDT_UNIT["KILOV-PER-M"]


def get_qudt_unit_megavolt_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Megavolt per Metre (http://qudt.org/vocab/unit/MegaV-PER-M)"""
    return QUDT_UNIT["MEGAV-PER-M"]


def get_qudt_unit_microvolt_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Microvolt per Metre (http://qudt.org/vocab/unit/MicroV-PER-M)"""
    return QUDT_UNIT["MICROV-PER-M"]


def get_qudt_unit_millivolt_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Millivolt per Metre (http://qudt.org/vocab/unit/MilliV-PER-M)"""
    return QUDT_UNIT["MILLIV-PER-M"]


def get_qudt_unit_volt_per_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Volt per Centimetre (http://qudt.org/vocab/unit/V-PER-CentiM)"""
    return QUDT_UNIT["V-PER-CENTIM"]


def get_qudt_unit_volt_per_inch() -> URIRef:
    """Returns the URI for QUDT unit: Volt per Inch (http://qudt.org/vocab/unit/V-PER-IN)"""
    return QUDT_UNIT["V-PER-IN"]


def get_qudt_unit_volt_per_millimetre() -> URIRef:
    """Returns the URI for QUDT unit: Volt per Millimetre (http://qudt.org/vocab/unit/V-PER-MilliM)"""
    return QUDT_UNIT["V-PER-MILLIM"]


def get_qudt_unit_volt_metre() -> URIRef:
    """Returns the URI for QUDT unit: Volt Metre (http://qudt.org/vocab/unit/V-M)"""
    return QUDT_UNIT["V-M"]


def get_qudt_unit_statvolt_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Statvolt Centimetre (http://qudt.org/vocab/unit/V_Stat-CentiM)"""
    return QUDT_UNIT["V_STAT-CENTIM"]


def get_qudt_unit_exavolt() -> URIRef:
    """Returns the URI for QUDT unit: Exavolt (http://qudt.org/vocab/unit/ExaV)"""
    return QUDT_UNIT["EXAV"]


def get_qudt_unit_femtovolt() -> URIRef:
    """Returns the URI for QUDT unit: Femtovolt (http://qudt.org/vocab/unit/FemtoV)"""
    return QUDT_UNIT["FEMTOV"]


def get_qudt_unit_gigavolt() -> URIRef:
    """Returns the URI for QUDT unit: Gigavolt (http://qudt.org/vocab/unit/GigaV)"""
    return QUDT_UNIT["GIGAV"]


def get_qudt_unit_kilovolt() -> URIRef:
    """Returns the URI for QUDT unit: Kilovolt (http://qudt.org/vocab/unit/KiloV)"""
    return QUDT_UNIT["KILOV"]


def get_qudt_unit_megavolt() -> URIRef:
    """Returns the URI for QUDT unit: Megavolt (http://qudt.org/vocab/unit/MegaV)"""
    return QUDT_UNIT["MEGAV"]


def get_qudt_unit_microvolt() -> URIRef:
    """Returns the URI for QUDT unit: Microvolt (http://qudt.org/vocab/unit/MicroV)"""
    return QUDT_UNIT["MICROV"]


def get_qudt_unit_millivolt() -> URIRef:
    """Returns the URI for QUDT unit: Millivolt (http://qudt.org/vocab/unit/MilliV)"""
    return QUDT_UNIT["MILLIV"]


def get_qudt_unit_nanovolt() -> URIRef:
    """Returns the URI for QUDT unit: Nanovolt (http://qudt.org/vocab/unit/NanoV)"""
    return QUDT_UNIT["NANOV"]


def get_qudt_unit_petavolt() -> URIRef:
    """Returns the URI for QUDT unit: Petavolt (http://qudt.org/vocab/unit/PetaV)"""
    return QUDT_UNIT["PETAV"]


def get_qudt_unit_picovolt() -> URIRef:
    """Returns the URI for QUDT unit: Picovolt (http://qudt.org/vocab/unit/PicoV)"""
    return QUDT_UNIT["PICOV"]


def get_qudt_unit_planck_volt() -> URIRef:
    """Returns the URI for QUDT unit: Planck Volt (http://qudt.org/vocab/unit/PlanckVolt)"""
    return QUDT_UNIT["PLANCKVOLT"]


def get_qudt_unit_teravolt() -> URIRef:
    """Returns the URI for QUDT unit: Teravolt (http://qudt.org/vocab/unit/TeraV)"""
    return QUDT_UNIT["TERAV"]


def get_qudt_unit_abvolt() -> URIRef:
    """Returns the URI for QUDT unit: Abvolt (http://qudt.org/vocab/unit/V_Ab)"""
    return QUDT_UNIT["V_AB"]


def get_qudt_unit_statvolt() -> URIRef:
    """Returns the URI for QUDT unit: Statvolt (http://qudt.org/vocab/unit/V_Stat)"""
    return QUDT_UNIT["V_STAT"]


def get_qudt_unit_nanoohm() -> URIRef:
    """Returns the URI for QUDT unit: Nanoohm (http://qudt.org/vocab/unit/NanoOHM)"""
    return QUDT_UNIT["NANOOHM"]


def get_qudt_unit_joule_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Joule per Cubic Metre (http://qudt.org/vocab/unit/J-PER-M3)"""
    return QUDT_UNIT["J-PER-M3"]


def get_qudt_unit_stathenry_per_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Stathenry per Centimetre (http://qudt.org/vocab/unit/H_Stat-PER-CentiM)"""
    return QUDT_UNIT["H_STAT-PER-CENTIM"]


def get_qudt_unit_microhenry_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Microhenry per Metre (http://qudt.org/vocab/unit/MicroH-PER-M)"""
    return QUDT_UNIT["MICROH-PER-M"]


def get_qudt_unit_nanohenry_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Nanohenry per Metre (http://qudt.org/vocab/unit/NanoH-PER-M)"""
    return QUDT_UNIT["NANOH-PER-M"]


def get_qudt_unit_relative_electromagnetic_permeability() -> URIRef:
    """Returns the URI for QUDT unit: Relative Electromagnetic Permeability (http://qudt.org/vocab/unit/PERMEABILITY_EM_REL)"""
    return QUDT_UNIT["PERMEABILITY_EM_REL"]


def get_qudt_unit_square_centimetre_per_volt_second() -> URIRef:
    """Returns the URI for QUDT unit: Square Centimetre per Volt Second (http://qudt.org/vocab/unit/CentiM2-PER-V-SEC)"""
    return QUDT_UNIT["CENTIM2-PER-V-SEC"]


def get_qudt_unit_square_metre_per_volt_second() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre per Volt Second (http://qudt.org/vocab/unit/M2-PER-V-SEC)"""
    return QUDT_UNIT["M2-PER-V-SEC"]


def get_qudt_unit_british_thermal_unit_international_definition_per_cubic_foot() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) per Cubic Foot (http://qudt.org/vocab/unit/BTU_IT-PER-FT3)"""
    return QUDT_UNIT["BTU_IT-PER-FT3"]


def get_qudt_unit_british_thermal_unit_thermochemical_definition_per_cubic_foot() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (thermochemical Definition) per Cubic Foot (http://qudt.org/vocab/unit/BTU_TH-PER-FT3)"""
    return QUDT_UNIT["BTU_TH-PER-FT3"]


def get_qudt_unit_erg_per_cubic_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Erg per Cubic Centimetre (http://qudt.org/vocab/unit/ERG-PER-CentiM3)"""
    return QUDT_UNIT["ERG-PER-CENTIM3"]


def get_qudt_unit_megajoule_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Megajoule per Cubic Metre (http://qudt.org/vocab/unit/MegaJ-PER-M3)"""
    return QUDT_UNIT["MEGAJ-PER-M3"]


def get_qudt_unit_watt_hour_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Watt Hour per Cubic Metre (http://qudt.org/vocab/unit/W-HR-PER-M3)"""
    return QUDT_UNIT["W-HR-PER-M3"]


def get_qudt_unit_reciprocal_electron_volt_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Electron Volt Cubic Metre (http://qudt.org/vocab/unit/PER-EV-M3)"""
    return QUDT_UNIT["PER-EV-M3"]


def get_qudt_unit_reciprocal_joule_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Joule Cubic Metre (http://qudt.org/vocab/unit/PER-J-M3)"""
    return QUDT_UNIT["PER-J-M3"]


def get_qudt_unit_gigajoule_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Gigajoule per Square Metre (http://qudt.org/vocab/unit/GigaJ-PER-M2)"""
    return QUDT_UNIT["GIGAJ-PER-M2"]


def get_qudt_unit_joule_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Joule per Square Metre (http://qudt.org/vocab/unit/J-PER-M2)"""
    return QUDT_UNIT["J-PER-M2"]


def get_qudt_unit_langley() -> URIRef:
    """Returns the URI for QUDT unit: Langley (http://qudt.org/vocab/unit/LANGLEY)"""
    return QUDT_UNIT["LANGLEY"]


def get_qudt_unit_millijoule_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Millijoule per Square Metre (http://qudt.org/vocab/unit/MilliJ-PER-M2)"""
    return QUDT_UNIT["MILLIJ-PER-M2"]


def get_qudt_unit_british_thermal_unit_international_definition_per_square_foot() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) per Square Foot (http://qudt.org/vocab/unit/BTU_IT-PER-FT2)"""
    return QUDT_UNIT["BTU_IT-PER-FT2"]


def get_qudt_unit_british_thermal_unit_thermochemical_definition_per_square_foot() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (thermochemical Definition) per Square Foot (http://qudt.org/vocab/unit/BTU_TH-PER-FT2)"""
    return QUDT_UNIT["BTU_TH-PER-FT2"]


def get_qudt_unit_thermochemical_calorie_per_square_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Thermochemical Calorie per Square Centimetre (http://qudt.org/vocab/unit/CAL_TH-PER-CentiM2)"""
    return QUDT_UNIT["CAL_TH-PER-CENTIM2"]


def get_qudt_unit_centinewton_metre_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Centinewton Metre per Square Metre (http://qudt.org/vocab/unit/CentiN-M-PER-M2)"""
    return QUDT_UNIT["CENTIN-M-PER-M2"]


def get_qudt_unit_erg_per_square_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Erg per Square Centimetre (http://qudt.org/vocab/unit/ERG-PER-CentiM2)"""
    return QUDT_UNIT["ERG-PER-CENTIM2"]


def get_qudt_unit_foot_pound_force_per_square_foot() -> URIRef:
    """Returns the URI for QUDT unit: Foot Pound Force per Square Foot (http://qudt.org/vocab/unit/FT-LB_F-PER-FT2)"""
    return QUDT_UNIT["FT-LB_F-PER-FT2"]


def get_qudt_unit_foot_pound_force_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Foot Pound Force per Square Metre (http://qudt.org/vocab/unit/FT-LB_F-PER-M2)"""
    return QUDT_UNIT["FT-LB_F-PER-M2"]


def get_qudt_unit_giganewton_metre_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Giganewton Metre per Square Metre (http://qudt.org/vocab/unit/GigaN-M-PER-M2)"""
    return QUDT_UNIT["GIGAN-M-PER-M2"]


def get_qudt_unit_joule_per_square_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Joule per Square Centimetre (http://qudt.org/vocab/unit/J-PER-CentiM2)"""
    return QUDT_UNIT["J-PER-CENTIM2"]


def get_qudt_unit_kilo_british_thermal_unit_international_definition_per_square_foot() -> (
    URIRef
):
    """Returns the URI for QUDT unit: Kilo British Thermal Unit (international Definition) per Square Foot (http://qudt.org/vocab/unit/KiloBTU_IT-PER-FT2)"""
    return QUDT_UNIT["KILOBTU_IT-PER-FT2"]


def get_qudt_unit_kilocalorie_per_square_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Kilocalorie per Square Centimetre (http://qudt.org/vocab/unit/KiloCAL-PER-CentiM2)"""
    return QUDT_UNIT["KILOCAL-PER-CENTIM2"]


def get_qudt_unit_kilogram_per_square_second() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Square Second (http://qudt.org/vocab/unit/KiloGM-PER-SEC2)"""
    return QUDT_UNIT["KILOGM-PER-SEC2"]


def get_qudt_unit_kilonewton_metre_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kilonewton Metre per Square Metre (http://qudt.org/vocab/unit/KiloN-M-PER-M2)"""
    return QUDT_UNIT["KILON-M-PER-M2"]


def get_qudt_unit_kilowatt_hour_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kilowatt Hour per Square Metre (http://qudt.org/vocab/unit/KiloW-HR-PER-M2)"""
    return QUDT_UNIT["KILOW-HR-PER-M2"]


def get_qudt_unit_pound_force_per_inch() -> URIRef:
    """Returns the URI for QUDT unit: Pound Force per Inch (http://qudt.org/vocab/unit/LB_F-PER-IN)"""
    return QUDT_UNIT["LB_F-PER-IN"]


def get_qudt_unit_megajoule_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Megajoule per Square Metre (http://qudt.org/vocab/unit/MegaJ-PER-M2)"""
    return QUDT_UNIT["MEGAJ-PER-M2"]


def get_qudt_unit_meganewton_metre_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Meganewton Metre per Square Metre (http://qudt.org/vocab/unit/MegaN-M-PER-M2)"""
    return QUDT_UNIT["MEGAN-M-PER-M2"]


def get_qudt_unit_micronewton_metre_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Micronewton Metre per Square Metre (http://qudt.org/vocab/unit/MicroN-M-PER-M2)"""
    return QUDT_UNIT["MICRON-M-PER-M2"]


def get_qudt_unit_millinewton_metre_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Millinewton Metre per Square Metre (http://qudt.org/vocab/unit/MilliN-M-PER-M2)"""
    return QUDT_UNIT["MILLIN-M-PER-M2"]


def get_qudt_unit_newton_metre_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Newton Metre per Square Metre (http://qudt.org/vocab/unit/N-M-PER-M2)"""
    return QUDT_UNIT["N-M-PER-M2"]


def get_qudt_unit_nanonewton_metre_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Nanonewton Metre per Square Metre (http://qudt.org/vocab/unit/NanoN-M-PER-M2)"""
    return QUDT_UNIT["NANON-M-PER-M2"]


def get_qudt_unit_watt_hour_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Watt Hour per Square Metre (http://qudt.org/vocab/unit/W-HR-PER-M2)"""
    return QUDT_UNIT["W-HR-PER-M2"]


def get_qudt_unit_watt_second_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Watt Second per Square Metre (http://qudt.org/vocab/unit/W-SEC-PER-M2)"""
    return QUDT_UNIT["W-SEC-PER-M2"]


def get_qudt_unit_british_thermal_unit_international_definition_per_pound_mole() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) per Pound Mole (http://qudt.org/vocab/unit/BTU_IT-PER-MOL_LB)"""
    return QUDT_UNIT["BTU_IT-PER-MOL_LB"]


def get_qudt_unit_kilojoule_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Kilojoule per Kelvin (http://qudt.org/vocab/unit/KiloJ-PER-K)"""
    return QUDT_UNIT["KILOJ-PER-K"]


def get_qudt_unit_watt_per_square_metre_pascal() -> URIRef:
    """Returns the URI for QUDT unit: Watt per Square Metre Pascal (http://qudt.org/vocab/unit/W-PER-M2-PA)"""
    return QUDT_UNIT["W-PER-M2-PA"]


def get_qudt_unit_british_thermal_unit_international_definition_per_pound_mass_degree_fahrenheit() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) per Pound Mass Degree Fahrenheit (http://qudt.org/vocab/unit/BTU_IT-PER-LB-DEG_F)"""
    return QUDT_UNIT["BTU_IT-PER-LB-DEG_F"]


def get_qudt_unit_british_thermal_unit_international_definition_per_pound_mass_degree_rankine() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) per Pound Mass Degree Rankine (http://qudt.org/vocab/unit/BTU_IT-PER-LB-DEG_R)"""
    return QUDT_UNIT["BTU_IT-PER-LB-DEG_R"]


def get_qudt_unit_british_thermal_unit_thermochemical_definition_per_pound_mass_degree_fahrenheit() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (thermochemical Definition) per Pound Mass Degree Fahrenheit (http://qudt.org/vocab/unit/BTU_TH-PER-LB-DEG_F)"""
    return QUDT_UNIT["BTU_TH-PER-LB-DEG_F"]


def get_qudt_unit_international_table_calorie_per_gram_degree_celsius() -> URIRef:
    """Returns the URI for QUDT unit: International Table Calorie per Gram Degree Celsius (http://qudt.org/vocab/unit/CAL_IT-PER-GM-DEG_C)"""
    return QUDT_UNIT["CAL_IT-PER-GM-DEG_C"]


def get_qudt_unit_international_table_calorie_per_gram_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: International Table Calorie per Gram Kelvin (http://qudt.org/vocab/unit/CAL_IT-PER-GM-K)"""
    return QUDT_UNIT["CAL_IT-PER-GM-K"]


def get_qudt_unit_thermochemical_calorie_per_gram_degree_celsius() -> URIRef:
    """Returns the URI for QUDT unit: Thermochemical Calorie per Gram Degree Celsius (http://qudt.org/vocab/unit/CAL_TH-PER-GM-DEG_C)"""
    return QUDT_UNIT["CAL_TH-PER-GM-DEG_C"]


def get_qudt_unit_thermochemical_calorie_per_gram_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Thermochemical Calorie per Gram Kelvin (http://qudt.org/vocab/unit/CAL_TH-PER-GM-K)"""
    return QUDT_UNIT["CAL_TH-PER-GM-K"]


def get_qudt_unit_joule_per_gram_degree_celsius() -> URIRef:
    """Returns the URI for QUDT unit: Joule per Gram Degree Celsius (http://qudt.org/vocab/unit/J-PER-GM-DEG_C)"""
    return QUDT_UNIT["J-PER-GM-DEG_C"]


def get_qudt_unit_joule_per_gram_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Joule per Gram Kelvin (http://qudt.org/vocab/unit/J-PER-GM-K)"""
    return QUDT_UNIT["J-PER-GM-K"]


def get_qudt_unit_joule_per_kilogram_degree_celsius() -> URIRef:
    """Returns the URI for QUDT unit: Joule per Kilogram Degree Celsius (http://qudt.org/vocab/unit/J-PER-KiloGM-DEG_C)"""
    return QUDT_UNIT["J-PER-KILOGM-DEG_C"]


def get_qudt_unit_joule_per_kilogram_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Joule per Kilogram Kelvin (http://qudt.org/vocab/unit/J-PER-KiloGM-K)"""
    return QUDT_UNIT["J-PER-KILOGM-K"]


def get_qudt_unit_kilocalorie_per_gram_degree_celsius() -> URIRef:
    """Returns the URI for QUDT unit: Kilocalorie per Gram Degree Celsius (http://qudt.org/vocab/unit/KiloCAL-PER-GM-DEG_C)"""
    return QUDT_UNIT["KILOCAL-PER-GM-DEG_C"]


def get_qudt_unit_kilojoule_per_kilogram_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Kilojoule per Kilogram Kelvin (http://qudt.org/vocab/unit/KiloJ-PER-KiloGM-K)"""
    return QUDT_UNIT["KILOJ-PER-KILOGM-K"]


def get_qudt_unit_square_metre_per_square_second_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre per Square Second Kelvin (http://qudt.org/vocab/unit/M2-PER-SEC2-K)"""
    return QUDT_UNIT["M2-PER-SEC2-K"]


def get_qudt_unit_bar_litre_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Bar Litre per Second (http://qudt.org/vocab/unit/BAR-L-PER-SEC)"""
    return QUDT_UNIT["BAR-L-PER-SEC"]


def get_qudt_unit_bar_cubic_metre_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Bar Cubic Metre per Second (http://qudt.org/vocab/unit/BAR-M3-PER-SEC)"""
    return QUDT_UNIT["BAR-M3-PER-SEC"]


def get_qudt_unit_erg_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Erg per Second (http://qudt.org/vocab/unit/ERG-PER-SEC)"""
    return QUDT_UNIT["ERG-PER-SEC"]


def get_qudt_unit_exajoule_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Exajoule per Second (http://qudt.org/vocab/unit/ExaJ-PER-SEC)"""
    return QUDT_UNIT["EXAJ-PER-SEC"]


def get_qudt_unit_foot_pound_force_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Foot Pound Force per Hour (http://qudt.org/vocab/unit/FT-LB_F-PER-HR)"""
    return QUDT_UNIT["FT-LB_F-PER-HR"]


def get_qudt_unit_foot_pound_force_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Foot Pound Force per Minute (http://qudt.org/vocab/unit/FT-LB_F-PER-MIN)"""
    return QUDT_UNIT["FT-LB_F-PER-MIN"]


def get_qudt_unit_foot_pound_force_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Foot Pound Force per Second (http://qudt.org/vocab/unit/FT-LB_F-PER-SEC)"""
    return QUDT_UNIT["FT-LB_F-PER-SEC"]


def get_qudt_unit_gigajoule_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Gigajoule per Hour (http://qudt.org/vocab/unit/GigaJ-PER-HR)"""
    return QUDT_UNIT["GIGAJ-PER-HR"]


def get_qudt_unit_gigajoule_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Gigajoule per Second (http://qudt.org/vocab/unit/GigaJ-PER-SEC)"""
    return QUDT_UNIT["GIGAJ-PER-SEC"]


def get_qudt_unit_horsepower() -> URIRef:
    """Returns the URI for QUDT unit: Horsepower (http://qudt.org/vocab/unit/HP)"""
    return QUDT_UNIT["HP"]


def get_qudt_unit_boiler_horsepower() -> URIRef:
    """Returns the URI for QUDT unit: Boiler Horsepower (http://qudt.org/vocab/unit/HP_Boiler)"""
    return QUDT_UNIT["HP_BOILER"]


def get_qudt_unit_horsepower_brake() -> URIRef:
    """Returns the URI for QUDT unit: Horsepower (brake) (http://qudt.org/vocab/unit/HP_Brake)"""
    return QUDT_UNIT["HP_BRAKE"]


def get_qudt_unit_horsepower_electric() -> URIRef:
    """Returns the URI for QUDT unit: Horsepower (electric) (http://qudt.org/vocab/unit/HP_Electric)"""
    return QUDT_UNIT["HP_ELECTRIC"]


def get_qudt_unit_horsepower_water() -> URIRef:
    """Returns the URI for QUDT unit: Horsepower (water) (http://qudt.org/vocab/unit/HP_H2O)"""
    return QUDT_UNIT["HP_H2O"]


def get_qudt_unit_horsepower_metric() -> URIRef:
    """Returns the URI for QUDT unit: Horsepower (metric) (http://qudt.org/vocab/unit/HP_Metric)"""
    return QUDT_UNIT["HP_METRIC"]


def get_qudt_unit_hectopascal_litre_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Hectopascal Litre per Second (http://qudt.org/vocab/unit/HectoPA-L-PER-SEC)"""
    return QUDT_UNIT["HECTOPA-L-PER-SEC"]


def get_qudt_unit_hectopascal_cubic_metre_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Hectopascal Cubic Metre per Second (http://qudt.org/vocab/unit/HectoPA-M3-PER-SEC)"""
    return QUDT_UNIT["HECTOPA-M3-PER-SEC"]


def get_qudt_unit_joule_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Joule per Day (http://qudt.org/vocab/unit/J-PER-DAY)"""
    return QUDT_UNIT["J-PER-DAY"]


def get_qudt_unit_joule_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Joule per Hour (http://qudt.org/vocab/unit/J-PER-HR)"""
    return QUDT_UNIT["J-PER-HR"]


def get_qudt_unit_joule_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Joule per Minute (http://qudt.org/vocab/unit/J-PER-MIN)"""
    return QUDT_UNIT["J-PER-MIN"]


def get_qudt_unit_joule_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Joule per Second (http://qudt.org/vocab/unit/J-PER-SEC)"""
    return QUDT_UNIT["J-PER-SEC"]


def get_qudt_unit_kilo_gram_force_metre_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Kilo Gram Force Metre per Second (http://qudt.org/vocab/unit/KiloGM_F-M-PER-SEC)"""
    return QUDT_UNIT["KILOGM_F-M-PER-SEC"]


def get_qudt_unit_kilojoule_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Kilojoule per Day (http://qudt.org/vocab/unit/KiloJ-PER-DAY)"""
    return QUDT_UNIT["KILOJ-PER-DAY"]


def get_qudt_unit_kilojoule_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Kilojoule per Hour (http://qudt.org/vocab/unit/KiloJ-PER-HR)"""
    return QUDT_UNIT["KILOJ-PER-HR"]


def get_qudt_unit_kilojoule_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Kilojoule per Minute (http://qudt.org/vocab/unit/KiloJ-PER-MIN)"""
    return QUDT_UNIT["KILOJ-PER-MIN"]


def get_qudt_unit_kilojoule_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Kilojoule per Second (http://qudt.org/vocab/unit/KiloJ-PER-SEC)"""
    return QUDT_UNIT["KILOJ-PER-SEC"]


def get_qudt_unit_megajoule_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Megajoule per Hour (http://qudt.org/vocab/unit/MegaJ-PER-HR)"""
    return QUDT_UNIT["MEGAJ-PER-HR"]


def get_qudt_unit_megajoule_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Megajoule per Second (http://qudt.org/vocab/unit/MegaJ-PER-SEC)"""
    return QUDT_UNIT["MEGAJ-PER-SEC"]


def get_qudt_unit_megapascal_litre_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Megapascal Litre per Second (http://qudt.org/vocab/unit/MegaPA-L-PER-SEC)"""
    return QUDT_UNIT["MEGAPA-L-PER-SEC"]


def get_qudt_unit_megapascal_cubic_metre_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Megapascal Cubic Metre per Second (http://qudt.org/vocab/unit/MegaPA-M3-PER-SEC)"""
    return QUDT_UNIT["MEGAPA-M3-PER-SEC"]


def get_qudt_unit_microjoule_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Microjoule per Second (http://qudt.org/vocab/unit/MicroJ-PER-SEC)"""
    return QUDT_UNIT["MICROJ-PER-SEC"]


def get_qudt_unit_millibar_litre_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Millibar Litre per Second (http://qudt.org/vocab/unit/MilliBAR-L-PER-SEC)"""
    return QUDT_UNIT["MILLIBAR-L-PER-SEC"]


def get_qudt_unit_millibar_cubic_metre_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Millibar Cubic Metre per Second (http://qudt.org/vocab/unit/MilliBAR-M3-PER-SEC)"""
    return QUDT_UNIT["MILLIBAR-M3-PER-SEC"]


def get_qudt_unit_millijoule_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Millijoule per Second (http://qudt.org/vocab/unit/MilliJ-PER-SEC)"""
    return QUDT_UNIT["MILLIJ-PER-SEC"]


def get_qudt_unit_nanojoule_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Nanojoule per Second (http://qudt.org/vocab/unit/NanoJ-PER-SEC)"""
    return QUDT_UNIT["NANOJ-PER-SEC"]


def get_qudt_unit_pascal_litre_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Pascal Litre per Second (http://qudt.org/vocab/unit/PA-L-PER-SEC)"""
    return QUDT_UNIT["PA-L-PER-SEC"]


def get_qudt_unit_pascal_cubic_metre_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Pascal Cubic Metre per Second (http://qudt.org/vocab/unit/PA-M3-PER-SEC)"""
    return QUDT_UNIT["PA-M3-PER-SEC"]


def get_qudt_unit_pferdestaerke() -> URIRef:
    """Returns the URI for QUDT unit: Pferdestaerke (http://qudt.org/vocab/unit/PFERDESTAERKE)"""
    return QUDT_UNIT["PFERDESTAERKE"]


def get_qudt_unit_psi_cubic_inch_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Psi Cubic Inch per Second (http://qudt.org/vocab/unit/PSI-IN3-PER-SEC)"""
    return QUDT_UNIT["PSI-IN3-PER-SEC"]


def get_qudt_unit_psi_litre_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Psi Litre per Second (http://qudt.org/vocab/unit/PSI-L-PER-SEC)"""
    return QUDT_UNIT["PSI-L-PER-SEC"]


def get_qudt_unit_psi_cubic_metre_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Psi Cubic Metre per Second (http://qudt.org/vocab/unit/PSI-M3-PER-SEC)"""
    return QUDT_UNIT["PSI-M3-PER-SEC"]


def get_qudt_unit_psi_cubic_yard_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Psi Cubic Yard per Second (http://qudt.org/vocab/unit/PSI-YD3-PER-SEC)"""
    return QUDT_UNIT["PSI-YD3-PER-SEC"]


def get_qudt_unit_petajoule_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Petajoule per Second (http://qudt.org/vocab/unit/PetaJ-PER-SEC)"""
    return QUDT_UNIT["PETAJ-PER-SEC"]


def get_qudt_unit_picojoule_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Picojoule per Second (http://qudt.org/vocab/unit/PicoJ-PER-SEC)"""
    return QUDT_UNIT["PICOJ-PER-SEC"]


def get_qudt_unit_planck_power() -> URIRef:
    """Returns the URI for QUDT unit: Planck Power (http://qudt.org/vocab/unit/PlanckPower)"""
    return QUDT_UNIT["PLANCKPOWER"]


def get_qudt_unit_terawatt_hour_per_year() -> URIRef:
    """Returns the URI for QUDT unit: Terawatt Hour per Year (http://qudt.org/vocab/unit/TeraW-HR-PER-YR)"""
    return QUDT_UNIT["TERAW-HR-PER-YR"]


def get_qudt_unit_coulomb_per_kilogram_second() -> URIRef:
    """Returns the URI for QUDT unit: Coulomb per Kilogram Second (http://qudt.org/vocab/unit/C-PER-KiloGM-SEC)"""
    return QUDT_UNIT["C-PER-KILOGM-SEC"]


def get_qudt_unit_roentgen_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Roentgen per Second (http://qudt.org/vocab/unit/R-PER-SEC)"""
    return QUDT_UNIT["R-PER-SEC"]


def get_qudt_unit_femtogram_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Femtogram per Kilogram (http://qudt.org/vocab/unit/FemtoGM-PER-KiloGM)"""
    return QUDT_UNIT["FEMTOGM-PER-KILOGM"]


def get_qudt_unit_gram_per_gram() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Gram (http://qudt.org/vocab/unit/GM-PER-GM)"""
    return QUDT_UNIT["GM-PER-GM"]


def get_qudt_unit_gram_per_hectogram() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Hectogram (http://qudt.org/vocab/unit/GM-PER-HectoGM)"""
    return QUDT_UNIT["GM-PER-HECTOGM"]


def get_qudt_unit_gram_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Kilogram (http://qudt.org/vocab/unit/GM-PER-KiloGM)"""
    return QUDT_UNIT["GM-PER-KILOGM"]


def get_qudt_unit_kilogram_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Kilogram (http://qudt.org/vocab/unit/KiloGM-PER-KiloGM)"""
    return QUDT_UNIT["KILOGM-PER-KILOGM"]


def get_qudt_unit_pound_mass_per_pound_mass() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Pound Mass (http://qudt.org/vocab/unit/LB-PER-LB)"""
    return QUDT_UNIT["LB-PER-LB"]


def get_qudt_unit_microgram_per_gram() -> URIRef:
    """Returns the URI for QUDT unit: Microgram per Gram (http://qudt.org/vocab/unit/MicroGM-PER-GM)"""
    return QUDT_UNIT["MICROGM-PER-GM"]


def get_qudt_unit_microgram_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Microgram per Kilogram (http://qudt.org/vocab/unit/MicroGM-PER-KiloGM)"""
    return QUDT_UNIT["MICROGM-PER-KILOGM"]


def get_qudt_unit_microgram_per_milligram() -> URIRef:
    """Returns the URI for QUDT unit: Microgram per Milligram (http://qudt.org/vocab/unit/MicroGM-PER-MilliGM)"""
    return QUDT_UNIT["MICROGM-PER-MILLIGM"]


def get_qudt_unit_milligram_per_gram() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Gram (http://qudt.org/vocab/unit/MilliGM-PER-GM)"""
    return QUDT_UNIT["MILLIGM-PER-GM"]


def get_qudt_unit_milligram_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Kilogram (http://qudt.org/vocab/unit/MilliGM-PER-KiloGM)"""
    return QUDT_UNIT["MILLIGM-PER-KILOGM"]


def get_qudt_unit_nanogram_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Nanogram per Kilogram (http://qudt.org/vocab/unit/NanoGM-PER-KiloGM)"""
    return QUDT_UNIT["NANOGM-PER-KILOGM"]


def get_qudt_unit_nanogram_per_milligram() -> URIRef:
    """Returns the URI for QUDT unit: Nanogram per Milligram (http://qudt.org/vocab/unit/NanoGM-PER-MilliGM)"""
    return QUDT_UNIT["NANOGM-PER-MILLIGM"]


def get_qudt_unit_picogram_per_gram() -> URIRef:
    """Returns the URI for QUDT unit: Picogram per Gram (http://qudt.org/vocab/unit/PicoGM-PER-GM)"""
    return QUDT_UNIT["PICOGM-PER-GM"]


def get_qudt_unit_picogram_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Picogram per Kilogram (http://qudt.org/vocab/unit/PicoGM-PER-KiloGM)"""
    return QUDT_UNIT["PICOGM-PER-KILOGM"]


def get_qudt_unit_picogram_per_milligram() -> URIRef:
    """Returns the URI for QUDT unit: Picogram per Milligram (http://qudt.org/vocab/unit/PicoGM-PER-MilliGM)"""
    return QUDT_UNIT["PICOGM-PER-MILLIGM"]


def get_qudt_unit_floating_point_operations_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Floating Point Operations per Second (http://qudt.org/vocab/unit/FLOPS)"""
    return QUDT_UNIT["FLOPS"]


def get_qudt_unit_giga_floating_point_operations_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Giga Floating Point Operations per Second (http://qudt.org/vocab/unit/GigaFLOPS)"""
    return QUDT_UNIT["GIGAFLOPS"]


def get_qudt_unit_mega_floating_point_operations_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Mega Floating Point Operations per Second (http://qudt.org/vocab/unit/MegaFLOPS)"""
    return QUDT_UNIT["MEGAFLOPS"]


def get_qudt_unit_peta_floating_point_operations_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Peta Floating Point Operations per Second (http://qudt.org/vocab/unit/PetaFLOPS)"""
    return QUDT_UNIT["PETAFLOPS"]


def get_qudt_unit_tera_floating_point_operations_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Tera Floating Point Operations per Second (http://qudt.org/vocab/unit/TeraFLOPS)"""
    return QUDT_UNIT["TERAFLOPS"]


def get_qudt_unit_percent_square_foot_per_pound_force_second() -> URIRef:
    """Returns the URI for QUDT unit: Percent Square Foot per Pound Force Second (http://qudt.org/vocab/unit/PERCENT-FT2-PER-LB_F-SEC)"""
    return QUDT_UNIT["PERCENT-FT2-PER-LB_F-SEC"]


def get_qudt_unit_percent_square_inch_per_pound_force_second() -> URIRef:
    """Returns the URI for QUDT unit: Percent Square Inch per Pound Force Second (http://qudt.org/vocab/unit/PERCENT-IN2-PER-LB_F-SEC)"""
    return QUDT_UNIT["PERCENT-IN2-PER-LB_F-SEC"]


def get_qudt_unit_rhe() -> URIRef:
    """Returns the URI for QUDT unit: Rhe (http://qudt.org/vocab/unit/RHE)"""
    return QUDT_UNIT["RHE"]


def get_qudt_unit_micrometre_per_litre_day() -> URIRef:
    """Returns the URI for QUDT unit: Micrometre per Litre Day (http://qudt.org/vocab/unit/MicroM-PER-L-DAY)"""
    return QUDT_UNIT["MICROM-PER-L-DAY"]


def get_qudt_unit_number_per_hectare_year() -> URIRef:
    """Returns the URI for QUDT unit: Number per Hectare Year (http://qudt.org/vocab/unit/NUM-PER-HA-YR)"""
    return QUDT_UNIT["NUM-PER-HA-YR"]


def get_qudt_unit_number_per_square_metre_day() -> URIRef:
    """Returns the URI for QUDT unit: Number per Square Metre Day (http://qudt.org/vocab/unit/NUM-PER-M2-DAY)"""
    return QUDT_UNIT["NUM-PER-M2-DAY"]


def get_qudt_unit_reciprocal_square_metre_second() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Square Metre Second (http://qudt.org/vocab/unit/PER-M2-SEC)"""
    return QUDT_UNIT["PER-M2-SEC"]


def get_qudt_unit_reciprocal_second_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Second Square Metre (http://qudt.org/vocab/unit/PER-SEC-M2)"""
    return QUDT_UNIT["PER-SEC-M2"]


def get_qudt_unit_newton_per_radian() -> URIRef:
    """Returns the URI for QUDT unit: Newton per Radian (http://qudt.org/vocab/unit/N-PER-RAD)"""
    return QUDT_UNIT["N-PER-RAD"]


def get_qudt_unit_decibar_per_year() -> URIRef:
    """Returns the URI for QUDT unit: Decibar per Year (http://qudt.org/vocab/unit/DeciBAR-PER-YR)"""
    return QUDT_UNIT["DECIBAR-PER-YR"]


def get_qudt_unit_hectopascal_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Hectopascal per Hour (http://qudt.org/vocab/unit/HectoPA-PER-HR)"""
    return QUDT_UNIT["HECTOPA-PER-HR"]


def get_qudt_unit_pound_force_per_square_inch_second() -> URIRef:
    """Returns the URI for QUDT unit: Pound Force per Square Inch Second (http://qudt.org/vocab/unit/LB_F-PER-IN2-SEC)"""
    return QUDT_UNIT["LB_F-PER-IN2-SEC"]


def get_qudt_unit_milliwatt_per_square_metre_nanometre() -> URIRef:
    """Returns the URI for QUDT unit: Milliwatt per Square Metre Nanometre (http://qudt.org/vocab/unit/MilliW-PER-M2-NanoM)"""
    return QUDT_UNIT["MILLIW-PER-M2-NANOM"]


def get_qudt_unit_pascal_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Pascal per Hour (http://qudt.org/vocab/unit/PA-PER-HR)"""
    return QUDT_UNIT["PA-PER-HR"]


def get_qudt_unit_pascal_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Pascal per Minute (http://qudt.org/vocab/unit/PA-PER-MIN)"""
    return QUDT_UNIT["PA-PER-MIN"]


def get_qudt_unit_pascal_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Pascal per Second (http://qudt.org/vocab/unit/PA-PER-SEC)"""
    return QUDT_UNIT["PA-PER-SEC"]


def get_qudt_unit_newton_per_coulomb() -> URIRef:
    """Returns the URI for QUDT unit: Newton per Coulomb (http://qudt.org/vocab/unit/N-PER-C)"""
    return QUDT_UNIT["N-PER-C"]


def get_qudt_unit_dyne_per_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Dyne per Centimetre (http://qudt.org/vocab/unit/DYN-PER-CentiM)"""
    return QUDT_UNIT["DYN-PER-CENTIM"]


def get_qudt_unit_kilo_gram_force_metre_per_square_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Kilo Gram Force Metre per Square Centimetre (http://qudt.org/vocab/unit/KiloGM_F-M-PER-CentiM2)"""
    return QUDT_UNIT["KILOGM_F-M-PER-CENTIM2"]


def get_qudt_unit_kilo_pound_force_per_foot() -> URIRef:
    """Returns the URI for QUDT unit: Kilo Pound Force per Foot (http://qudt.org/vocab/unit/KiloLB_F-PER-FT)"""
    return QUDT_UNIT["KILOLB_F-PER-FT"]


def get_qudt_unit_kilonewton_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kilonewton per Metre (http://qudt.org/vocab/unit/KiloN-PER-M)"""
    return QUDT_UNIT["KILON-PER-M"]


def get_qudt_unit_pound_force_per_foot() -> URIRef:
    """Returns the URI for QUDT unit: Pound Force per Foot (http://qudt.org/vocab/unit/LB_F-PER-FT)"""
    return QUDT_UNIT["LB_F-PER-FT"]


def get_qudt_unit_pound_force_per_yard() -> URIRef:
    """Returns the URI for QUDT unit: Pound Force per Yard (http://qudt.org/vocab/unit/LB_F-PER-YD)"""
    return QUDT_UNIT["LB_F-PER-YD"]


def get_qudt_unit_millinewton_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Millinewton per Metre (http://qudt.org/vocab/unit/MilliN-PER-M)"""
    return QUDT_UNIT["MILLIN-PER-M"]


def get_qudt_unit_newton_per_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Newton per Centimetre (http://qudt.org/vocab/unit/N-PER-CentiM)"""
    return QUDT_UNIT["N-PER-CENTIM"]


def get_qudt_unit_newton_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Newton per Metre (http://qudt.org/vocab/unit/N-PER-M)"""
    return QUDT_UNIT["N-PER-M"]


def get_qudt_unit_newton_per_millimetre() -> URIRef:
    """Returns the URI for QUDT unit: Newton per Millimetre (http://qudt.org/vocab/unit/N-PER-MilliM)"""
    return QUDT_UNIT["N-PER-MILLIM"]


def get_qudt_unit_poundal_per_inch() -> URIRef:
    """Returns the URI for QUDT unit: Poundal per Inch (http://qudt.org/vocab/unit/PDL-PER-IN)"""
    return QUDT_UNIT["PDL-PER-IN"]


def get_qudt_unit_micrometre_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Micrometre per Metre (http://qudt.org/vocab/unit/MicroM-PER-M)"""
    return QUDT_UNIT["MICROM-PER-M"]


def get_qudt_unit_millimetre_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Millimetre per Metre (http://qudt.org/vocab/unit/MilliM-PER-M)"""
    return QUDT_UNIT["MILLIM-PER-M"]


def get_qudt_unit_degree_celsius_growing_cereal_day() -> URIRef:
    """Returns the URI for QUDT unit: Degree Celsius Growing Cereal Day (http://qudt.org/vocab/unit/DEG_C_GROWING_CEREAL-DAY)"""
    return QUDT_UNIT["DEG_C_GROWING_CEREAL-DAY"]


def get_qudt_unit_degree_celsius_day() -> URIRef:
    """Returns the URI for QUDT unit: Degree Celsius Day (http://qudt.org/vocab/unit/DEG_C-DAY)"""
    return QUDT_UNIT["DEG_C-DAY"]


def get_qudt_unit_degree_celsius_hour() -> URIRef:
    """Returns the URI for QUDT unit: Degree Celsius Hour (http://qudt.org/vocab/unit/DEG_C-HR)"""
    return QUDT_UNIT["DEG_C-HR"]


def get_qudt_unit_degree_celsius_week() -> URIRef:
    """Returns the URI for QUDT unit: Degree Celsius Week (http://qudt.org/vocab/unit/DEG_C-WK)"""
    return QUDT_UNIT["DEG_C-WK"]


def get_qudt_unit_degree_fahrenheit_day() -> URIRef:
    """Returns the URI for QUDT unit: Degree Fahrenheit Day (http://qudt.org/vocab/unit/DEG_F-DAY)"""
    return QUDT_UNIT["DEG_F-DAY"]


def get_qudt_unit_degree_fahrenheit_hour() -> URIRef:
    """Returns the URI for QUDT unit: Degree Fahrenheit Hour (http://qudt.org/vocab/unit/DEG_F-HR)"""
    return QUDT_UNIT["DEG_F-HR"]


def get_qudt_unit_kelvin_day() -> URIRef:
    """Returns the URI for QUDT unit: Kelvin Day (http://qudt.org/vocab/unit/K-DAY)"""
    return QUDT_UNIT["K-DAY"]


def get_qudt_unit_kelvin_second() -> URIRef:
    """Returns the URI for QUDT unit: Kelvin Second (http://qudt.org/vocab/unit/K-SEC)"""
    return QUDT_UNIT["K-SEC"]


def get_qudt_unit_cubic_metre_per_coulomb() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Metre per Coulomb (http://qudt.org/vocab/unit/M3-PER-C)"""
    return QUDT_UNIT["M3-PER-C"]


def get_qudt_unit_volt_square_inch_per_pound_force() -> URIRef:
    """Returns the URI for QUDT unit: Volt Square Inch per Pound Force (http://qudt.org/vocab/unit/V-IN2-PER-LB_F)"""
    return QUDT_UNIT["V-IN2-PER-LB_F"]


def get_qudt_unit_volt_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Volt per Bar (http://qudt.org/vocab/unit/V-PER-BAR)"""
    return QUDT_UNIT["V-PER-BAR"]


def get_qudt_unit_volt_per_pascal() -> URIRef:
    """Returns the URI for QUDT unit: Volt per Pascal (http://qudt.org/vocab/unit/V-PER-PA)"""
    return QUDT_UNIT["V-PER-PA"]


def get_qudt_unit_beat_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Beat per Minute (http://qudt.org/vocab/unit/BEAT-PER-MIN)"""
    return QUDT_UNIT["BEAT-PER-MIN"]


def get_qudt_unit_british_thermal_unit_39_f() -> URIRef:
    """Returns the URI for QUDT unit: British Thermal Unit (39 °F) (http://qudt.org/vocab/unit/BTU_39DEG_F)"""
    return QUDT_UNIT["BTU_39DEG_F"]


def get_qudt_unit_british_thermal_unit_59_f() -> URIRef:
    """Returns the URI for QUDT unit: British Thermal Unit (59 °F) (http://qudt.org/vocab/unit/BTU_59DEG_F)"""
    return QUDT_UNIT["BTU_59DEG_F"]


def get_qudt_unit_british_thermal_unit_60_f() -> URIRef:
    """Returns the URI for QUDT unit: British Thermal Unit (60 °F) (http://qudt.org/vocab/unit/BTU_60DEG_F)"""
    return QUDT_UNIT["BTU_60DEG_F"]


def get_qudt_unit_british_thermal_unit_mean() -> URIRef:
    """Returns the URI for QUDT unit: British Thermal Unit (mean) (http://qudt.org/vocab/unit/BTU_MEAN)"""
    return QUDT_UNIT["BTU_MEAN"]


def get_qudt_unit_calorie_15_degrees_c() -> URIRef:
    """Returns the URI for QUDT unit: Calorie (15 Degrees C) (http://qudt.org/vocab/unit/CAL_15DEG_C)"""
    return QUDT_UNIT["CAL_15DEG_C"]


def get_qudt_unit_calorie_20_c() -> URIRef:
    """Returns the URI for QUDT unit: Calorie (20 °C) (http://qudt.org/vocab/unit/CAL_20DEG_C)"""
    return QUDT_UNIT["CAL_20DEG_C"]


def get_qudt_unit_calorie_mean() -> URIRef:
    """Returns the URI for QUDT unit: Calorie (Mean) (http://qudt.org/vocab/unit/CAL_MEAN)"""
    return QUDT_UNIT["CAL_MEAN"]


def get_qudt_unit_kilo_international_table_calorie() -> URIRef:
    """Returns the URI for QUDT unit: Kilo International Table Calorie (http://qudt.org/vocab/unit/KiloCAL_IT)"""
    return QUDT_UNIT["KILOCAL_IT"]


def get_qudt_unit_kilocalorie_mean() -> URIRef:
    """Returns the URI for QUDT unit: Kilocalorie (Mean) (http://qudt.org/vocab/unit/KiloCAL_Mean)"""
    return QUDT_UNIT["KILOCAL_MEAN"]


def get_qudt_unit_kilo_thermochemical_calorie() -> URIRef:
    """Returns the URI for QUDT unit: Kilo Thermochemical Calorie (http://qudt.org/vocab/unit/KiloCAL_TH)"""
    return QUDT_UNIT["KILOCAL_TH"]


def get_qudt_unit_ton_of_refrigeration_hour() -> URIRef:
    """Returns the URI for QUDT unit: Ton of Refrigeration Hour (http://qudt.org/vocab/unit/TON_FG-HR)"""
    return QUDT_UNIT["TON_FG-HR"]


def get_qudt_unit_british_thermal_unit_international_definition_per_degree_fahrenheit() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) per Degree Fahrenheit (http://qudt.org/vocab/unit/BTU_IT-PER-DEG_F)"""
    return QUDT_UNIT["BTU_IT-PER-DEG_F"]


def get_qudt_unit_british_thermal_unit_international_definition_per_degree_rankine() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) per Degree Rankine (http://qudt.org/vocab/unit/BTU_IT-PER-DEG_R)"""
    return QUDT_UNIT["BTU_IT-PER-DEG_R"]


def get_qudt_unit_megajoule_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Megajoule per Kelvin (http://qudt.org/vocab/unit/MegaJ-PER-K)"""
    return QUDT_UNIT["MEGAJ-PER-K"]


def get_qudt_unit_british_thermal_unit_international_definition_per_pound_mass() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) per Pound Mass (http://qudt.org/vocab/unit/BTU_IT-PER-LB)"""
    return QUDT_UNIT["BTU_IT-PER-LB"]


def get_qudt_unit_british_thermal_unit_thermochemical_definition_per_pound_mass() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (thermochemical Definition) per Pound Mass (http://qudt.org/vocab/unit/BTU_TH-PER-LB)"""
    return QUDT_UNIT["BTU_TH-PER-LB"]


def get_qudt_unit_international_table_calorie_per_gram() -> URIRef:
    """Returns the URI for QUDT unit: International Table Calorie per Gram (http://qudt.org/vocab/unit/CAL_IT-PER-GM)"""
    return QUDT_UNIT["CAL_IT-PER-GM"]


def get_qudt_unit_thermochemical_calorie_per_gram() -> URIRef:
    """Returns the URI for QUDT unit: Thermochemical Calorie per Gram (http://qudt.org/vocab/unit/CAL_TH-PER-GM)"""
    return QUDT_UNIT["CAL_TH-PER-GM"]


def get_qudt_unit_erg_per_gram() -> URIRef:
    """Returns the URI for QUDT unit: Erg per Gram (http://qudt.org/vocab/unit/ERG-PER-GM)"""
    return QUDT_UNIT["ERG-PER-GM"]


def get_qudt_unit_joule_per_gram() -> URIRef:
    """Returns the URI for QUDT unit: Joule per Gram (http://qudt.org/vocab/unit/J-PER-GM)"""
    return QUDT_UNIT["J-PER-GM"]


def get_qudt_unit_joule_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Joule per Kilogram (http://qudt.org/vocab/unit/J-PER-KiloGM)"""
    return QUDT_UNIT["J-PER-KILOGM"]


def get_qudt_unit_kilocalorie_per_gram() -> URIRef:
    """Returns the URI for QUDT unit: Kilocalorie per Gram (http://qudt.org/vocab/unit/KiloCAL-PER-GM)"""
    return QUDT_UNIT["KILOCAL-PER-GM"]


def get_qudt_unit_kilojoule_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Kilojoule per Kilogram (http://qudt.org/vocab/unit/KiloJ-PER-KiloGM)"""
    return QUDT_UNIT["KILOJ-PER-KILOGM"]


def get_qudt_unit_kilo_pound_force_foot_per_pound_mass() -> URIRef:
    """Returns the URI for QUDT unit: Kilo Pound Force Foot per Pound Mass (http://qudt.org/vocab/unit/KiloLB_F-FT-PER-LB)"""
    return QUDT_UNIT["KILOLB_F-FT-PER-LB"]


def get_qudt_unit_megajoule_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Megajoule per Kilogram (http://qudt.org/vocab/unit/MegaJ-PER-KiloGM)"""
    return QUDT_UNIT["MEGAJ-PER-KILOGM"]


def get_qudt_unit_millijoule_per_gram() -> URIRef:
    """Returns the URI for QUDT unit: Millijoule per Gram (http://qudt.org/vocab/unit/MilliJ-PER-GM)"""
    return QUDT_UNIT["MILLIJ-PER-GM"]


def get_qudt_unit_newton_metre_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Newton Metre per Kilogram (http://qudt.org/vocab/unit/N-M-PER-KiloGM)"""
    return QUDT_UNIT["N-M-PER-KILOGM"]


def get_qudt_unit_watt_hour_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Watt Hour per Kilogram (http://qudt.org/vocab/unit/W-HR-PER-KiloGM)"""
    return QUDT_UNIT["W-HR-PER-KILOGM"]


def get_qudt_unit_standard_atmosphere_cubic_metre_per_mole() -> URIRef:
    """Returns the URI for QUDT unit: Standard Atmosphere Cubic Metre per Mole (http://qudt.org/vocab/unit/ATM-M3-PER-MOL)"""
    return QUDT_UNIT["ATM-M3-PER-MOL"]


def get_qudt_unit_darcy() -> URIRef:
    """Returns the URI for QUDT unit: Darcy (http://qudt.org/vocab/unit/DARCY)"""
    return QUDT_UNIT["DARCY"]


def get_qudt_unit_millidarcy() -> URIRef:
    """Returns the URI for QUDT unit: Millidarcy (http://qudt.org/vocab/unit/MilliDARCY)"""
    return QUDT_UNIT["MILLIDARCY"]


def get_qudt_unit_foot_candle() -> URIRef:
    """Returns the URI for QUDT unit: Foot Candle (http://qudt.org/vocab/unit/FC)"""
    return QUDT_UNIT["FC"]


def get_qudt_unit_lux() -> URIRef:
    """Returns the URI for QUDT unit: Lux (http://qudt.org/vocab/unit/LUX)"""
    return QUDT_UNIT["LUX"]


def get_qudt_unit_phot() -> URIRef:
    """Returns the URI for QUDT unit: Phot (http://qudt.org/vocab/unit/PHOT)"""
    return QUDT_UNIT["PHOT"]


def get_qudt_unit_gram_centimetre_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Gram Centimetre per Second (http://qudt.org/vocab/unit/GM-CentiM-PER-SEC)"""
    return QUDT_UNIT["GM-CENTIM-PER-SEC"]


def get_qudt_unit_kilogram_centimetre_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram Centimetre per Second (http://qudt.org/vocab/unit/KiloGM-CentiM-PER-SEC)"""
    return QUDT_UNIT["KILOGM-CENTIM-PER-SEC"]


def get_qudt_unit_pound_mass_foot_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Foot per Second (http://qudt.org/vocab/unit/LB-FT-PER-SEC)"""
    return QUDT_UNIT["LB-FT-PER-SEC"]


def get_qudt_unit_pound_mass_inch_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Inch per Second (http://qudt.org/vocab/unit/LB-IN-PER-SEC)"""
    return QUDT_UNIT["LB-IN-PER-SEC"]


def get_qudt_unit_henry() -> URIRef:
    """Returns the URI for QUDT unit: Henry (http://qudt.org/vocab/unit/H)"""
    return QUDT_UNIT["H"]


def get_qudt_unit_abhenry() -> URIRef:
    """Returns the URI for QUDT unit: Abhenry (http://qudt.org/vocab/unit/H_Ab)"""
    return QUDT_UNIT["H_AB"]


def get_qudt_unit_stathenry() -> URIRef:
    """Returns the URI for QUDT unit: Stathenry (http://qudt.org/vocab/unit/H_Stat)"""
    return QUDT_UNIT["H_STAT"]


def get_qudt_unit_kilohenry() -> URIRef:
    """Returns the URI for QUDT unit: Kilohenry (http://qudt.org/vocab/unit/KiloH)"""
    return QUDT_UNIT["KILOH"]


def get_qudt_unit_microhenry() -> URIRef:
    """Returns the URI for QUDT unit: Microhenry (http://qudt.org/vocab/unit/MicroH)"""
    return QUDT_UNIT["MICROH"]


def get_qudt_unit_millihenry() -> URIRef:
    """Returns the URI for QUDT unit: Millihenry (http://qudt.org/vocab/unit/MilliH)"""
    return QUDT_UNIT["MILLIH"]


def get_qudt_unit_nanohenry() -> URIRef:
    """Returns the URI for QUDT unit: Nanohenry (http://qudt.org/vocab/unit/NanoH)"""
    return QUDT_UNIT["NANOH"]


def get_qudt_unit_picohenry() -> URIRef:
    """Returns the URI for QUDT unit: Picohenry (http://qudt.org/vocab/unit/PicoH)"""
    return QUDT_UNIT["PICOH"]


def get_qudt_unit_ban() -> URIRef:
    """Returns the URI for QUDT unit: Ban (http://qudt.org/vocab/unit/BAN)"""
    return QUDT_UNIT["BAN"]


def get_qudt_unit_bit() -> URIRef:
    """Returns the URI for QUDT unit: Bit (http://qudt.org/vocab/unit/BIT)"""
    return QUDT_UNIT["BIT"]


def get_qudt_unit_byte() -> URIRef:
    """Returns the URI for QUDT unit: Byte (http://qudt.org/vocab/unit/BYTE)"""
    return QUDT_UNIT["BYTE"]


def get_qudt_unit_erlang() -> URIRef:
    """Returns the URI for QUDT unit: Erlang (http://qudt.org/vocab/unit/ERLANG)"""
    return QUDT_UNIT["ERLANG"]


def get_qudt_unit_exabit() -> URIRef:
    """Returns the URI for QUDT unit: Exabit (http://qudt.org/vocab/unit/ExaBIT)"""
    return QUDT_UNIT["EXABIT"]


def get_qudt_unit_exabyte() -> URIRef:
    """Returns the URI for QUDT unit: Exabyte (http://qudt.org/vocab/unit/ExaBYTE)"""
    return QUDT_UNIT["EXABYTE"]


def get_qudt_unit_exbibit() -> URIRef:
    """Returns the URI for QUDT unit: Exbibit (http://qudt.org/vocab/unit/ExbiBIT)"""
    return QUDT_UNIT["EXBIBIT"]


def get_qudt_unit_exbibyte() -> URIRef:
    """Returns the URI for QUDT unit: Exbibyte (http://qudt.org/vocab/unit/ExbiBYTE)"""
    return QUDT_UNIT["EXBIBYTE"]


def get_qudt_unit_gibibyte() -> URIRef:
    """Returns the URI for QUDT unit: Gibibyte (http://qudt.org/vocab/unit/GibiBYTE)"""
    return QUDT_UNIT["GIBIBYTE"]


def get_qudt_unit_gigabyte() -> URIRef:
    """Returns the URI for QUDT unit: Gigabyte (http://qudt.org/vocab/unit/GigaBYTE)"""
    return QUDT_UNIT["GIGABYTE"]


def get_qudt_unit_hartley() -> URIRef:
    """Returns the URI for QUDT unit: Hartley (http://qudt.org/vocab/unit/HART)"""
    return QUDT_UNIT["HART"]


def get_qudt_unit_kibibyte() -> URIRef:
    """Returns the URI for QUDT unit: Kibibyte (http://qudt.org/vocab/unit/KibiBYTE)"""
    return QUDT_UNIT["KIBIBYTE"]


def get_qudt_unit_kilobyte() -> URIRef:
    """Returns the URI for QUDT unit: Kilobyte (http://qudt.org/vocab/unit/KiloBYTE)"""
    return QUDT_UNIT["KILOBYTE"]


def get_qudt_unit_mebibyte() -> URIRef:
    """Returns the URI for QUDT unit: Mebibyte (http://qudt.org/vocab/unit/MebiBYTE)"""
    return QUDT_UNIT["MEBIBYTE"]


def get_qudt_unit_megabyte() -> URIRef:
    """Returns the URI for QUDT unit: Megabyte (http://qudt.org/vocab/unit/MegaBYTE)"""
    return QUDT_UNIT["MEGABYTE"]


def get_qudt_unit_nat() -> URIRef:
    """Returns the URI for QUDT unit: Nat (http://qudt.org/vocab/unit/NAT)"""
    return QUDT_UNIT["NAT"]


def get_qudt_unit_pebibit() -> URIRef:
    """Returns the URI for QUDT unit: Pebibit (http://qudt.org/vocab/unit/PebiBIT)"""
    return QUDT_UNIT["PEBIBIT"]


def get_qudt_unit_pebibyte() -> URIRef:
    """Returns the URI for QUDT unit: Pebibyte (http://qudt.org/vocab/unit/PebiBYTE)"""
    return QUDT_UNIT["PEBIBYTE"]


def get_qudt_unit_petabyte() -> URIRef:
    """Returns the URI for QUDT unit: Petabyte (http://qudt.org/vocab/unit/PetaBYTE)"""
    return QUDT_UNIT["PETABYTE"]


def get_qudt_unit_shannon() -> URIRef:
    """Returns the URI for QUDT unit: Shannon (http://qudt.org/vocab/unit/SHANNON)"""
    return QUDT_UNIT["SHANNON"]


def get_qudt_unit_tebibit() -> URIRef:
    """Returns the URI for QUDT unit: Tebibit (http://qudt.org/vocab/unit/TebiBIT)"""
    return QUDT_UNIT["TEBIBIT"]


def get_qudt_unit_tebibyte() -> URIRef:
    """Returns the URI for QUDT unit: Tebibyte (http://qudt.org/vocab/unit/TebiBYTE)"""
    return QUDT_UNIT["TEBIBYTE"]


def get_qudt_unit_terabyte() -> URIRef:
    """Returns the URI for QUDT unit: Terabyte (http://qudt.org/vocab/unit/TeraBYTE)"""
    return QUDT_UNIT["TERABYTE"]


def get_qudt_unit_hartley_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Hartley per Second (http://qudt.org/vocab/unit/HART-PER-SEC)"""
    return QUDT_UNIT["HART-PER-SEC"]


def get_qudt_unit_nat_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Nat per Second (http://qudt.org/vocab/unit/NAT-PER-SEC)"""
    return QUDT_UNIT["NAT-PER-SEC"]


def get_qudt_unit_shannon_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Shannon per Second (http://qudt.org/vocab/unit/SHANNON-PER-SEC)"""
    return QUDT_UNIT["SHANNON-PER-SEC"]


def get_qudt_unit_reciprocal_joule() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Joule (http://qudt.org/vocab/unit/PER-J)"""
    return QUDT_UNIT["PER-J"]


def get_qudt_unit_reciprocal_kilo_volt_ampere_hour() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Kilo Volt Ampere Hour (http://qudt.org/vocab/unit/PER-KiloVA-HR)"""
    return QUDT_UNIT["PER-KILOVA-HR"]


def get_qudt_unit_reciprocal_volt_ampere_second() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Volt Ampere Second (http://qudt.org/vocab/unit/PER-VA-SEC)"""
    return QUDT_UNIT["PER-VA-SEC"]


def get_qudt_unit_kayser() -> URIRef:
    """Returns the URI for QUDT unit: Kayser (http://qudt.org/vocab/unit/KY)"""
    return QUDT_UNIT["KY"]


def get_qudt_unit_metre_per_hectare() -> URIRef:
    """Returns the URI for QUDT unit: Metre per Hectare (http://qudt.org/vocab/unit/M-PER-HA)"""
    return QUDT_UNIT["M-PER-HA"]


def get_qudt_unit_metre_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Metre per Square Metre (http://qudt.org/vocab/unit/M-PER-M2)"""
    return QUDT_UNIT["M-PER-M2"]


def get_qudt_unit_mesh() -> URIRef:
    """Returns the URI for QUDT unit: Mesh (http://qudt.org/vocab/unit/MESH)"""
    return QUDT_UNIT["MESH"]


def get_qudt_unit_number_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Number per Metre (http://qudt.org/vocab/unit/NUM-PER-M)"""
    return QUDT_UNIT["NUM-PER-M"]


def get_qudt_unit_reciprocal_angstrom() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Angstrom (http://qudt.org/vocab/unit/PER-ANGSTROM)"""
    return QUDT_UNIT["PER-ANGSTROM"]


def get_qudt_unit_reciprocal_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Centimetre (http://qudt.org/vocab/unit/PER-CentiM)"""
    return QUDT_UNIT["PER-CENTIM"]


def get_qudt_unit_reciprocal_gram() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Gram (http://qudt.org/vocab/unit/PER-GM)"""
    return QUDT_UNIT["PER-GM"]


def get_qudt_unit_reciprocal_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Kilogram (http://qudt.org/vocab/unit/PER-KiloGM)"""
    return QUDT_UNIT["PER-KILOGM"]


def get_qudt_unit_reciprocal_pound_mass() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Pound Mass (http://qudt.org/vocab/unit/PER-LB)"""
    return QUDT_UNIT["PER-LB"]


def get_qudt_unit_reciprocal_milligram() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Milligram (http://qudt.org/vocab/unit/PER-MilliGM)"""
    return QUDT_UNIT["PER-MILLIGM"]


def get_qudt_unit_reciprocal_ounce_mass() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Ounce Mass (http://qudt.org/vocab/unit/PER-OZ)"""
    return QUDT_UNIT["PER-OZ"]


def get_qudt_unit_reciprocal_ton() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Ton (http://qudt.org/vocab/unit/PER-TON)"""
    return QUDT_UNIT["PER-TON"]


def get_qudt_unit_reciprocal_tonne() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Tonne (http://qudt.org/vocab/unit/PER-TONNE)"""
    return QUDT_UNIT["PER-TONNE"]


def get_qudt_unit_metre_per_farad() -> URIRef:
    """Returns the URI for QUDT unit: Metre per Farad (http://qudt.org/vocab/unit/M-PER-FARAD)"""
    return QUDT_UNIT["M-PER-FARAD"]


def get_qudt_unit_reciprocal_psi() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Psi (http://qudt.org/vocab/unit/PER-PSI)"""
    return QUDT_UNIT["PER-PSI"]


def get_qudt_unit_reciprocal_square_electron_volt() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Square Electron Volt (http://qudt.org/vocab/unit/PER-EV2)"""
    return QUDT_UNIT["PER-EV2"]


def get_qudt_unit_reciprocal_square_joule() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Square Joule (http://qudt.org/vocab/unit/PER-J2)"""
    return QUDT_UNIT["PER-J2"]


def get_qudt_unit_reciprocal_square_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Square Kilogram (http://qudt.org/vocab/unit/PER-KiloGM2)"""
    return QUDT_UNIT["PER-KILOGM2"]


def get_qudt_unit_reciprocal_square_second() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Square Second (http://qudt.org/vocab/unit/PER-SEC2)"""
    return QUDT_UNIT["PER-SEC2"]


def get_qudt_unit_megahertz_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Megahertz per Kelvin (http://qudt.org/vocab/unit/MegaHZ-PER-K)"""
    return QUDT_UNIT["MEGAHZ-PER-K"]


def get_qudt_unit_reciprocal_cubic_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Cubic Centimetre (http://qudt.org/vocab/unit/PER-CentiM3)"""
    return QUDT_UNIT["PER-CENTIM3"]


def get_qudt_unit_reciprocal_cubic_foot() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Cubic Foot (http://qudt.org/vocab/unit/PER-FT3)"""
    return QUDT_UNIT["PER-FT3"]


def get_qudt_unit_reciprocal_cubic_inch() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Cubic Inch (http://qudt.org/vocab/unit/PER-IN3)"""
    return QUDT_UNIT["PER-IN3"]


def get_qudt_unit_reciprocal_litre() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Litre (http://qudt.org/vocab/unit/PER-L)"""
    return QUDT_UNIT["PER-L"]


def get_qudt_unit_reciprocal_millilitre() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Millilitre (http://qudt.org/vocab/unit/PER-MilliL)"""
    return QUDT_UNIT["PER-MILLIL"]


def get_qudt_unit_reciprocal_cubic_millimetre() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Cubic Millimetre (http://qudt.org/vocab/unit/PER-MilliM3)"""
    return QUDT_UNIT["PER-MILLIM3"]


def get_qudt_unit_reciprocal_cubic_yard() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Cubic Yard (http://qudt.org/vocab/unit/PER-YD3)"""
    return QUDT_UNIT["PER-YD3"]


def get_qudt_unit_megajoule_per_square_metre_day() -> URIRef:
    """Returns the URI for QUDT unit: Megajoule per Square Metre Day (http://qudt.org/vocab/unit/MegaJ-PER-M2-DAY)"""
    return QUDT_UNIT["MEGAJ-PER-M2-DAY"]


def get_qudt_unit_centistokes() -> URIRef:
    """Returns the URI for QUDT unit: Centistokes (http://qudt.org/vocab/unit/CentiST)"""
    return QUDT_UNIT["CENTIST"]


def get_qudt_unit_stokes() -> URIRef:
    """Returns the URI for QUDT unit: Stokes (http://qudt.org/vocab/unit/ST)"""
    return QUDT_UNIT["ST"]


def get_qudt_unit_gram_millimetre() -> URIRef:
    """Returns the URI for QUDT unit: Gram Millimetre (http://qudt.org/vocab/unit/GM-MilliM)"""
    return QUDT_UNIT["GM-MILLIM"]


def get_qudt_unit_pound_mass_inch() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Inch (http://qudt.org/vocab/unit/LB-IN)"""
    return QUDT_UNIT["LB-IN"]


def get_qudt_unit_metre_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Metre Kilogram (http://qudt.org/vocab/unit/M-KiloGM)"""
    return QUDT_UNIT["M-KILOGM"]


def get_qudt_unit_ounce_mass_foot() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass Foot (http://qudt.org/vocab/unit/OZ-FT)"""
    return QUDT_UNIT["OZ-FT"]


def get_qudt_unit_ounce_mass_inch() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass Inch (http://qudt.org/vocab/unit/OZ-IN)"""
    return QUDT_UNIT["OZ-IN"]


def get_qudt_unit_degree_celsius_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Degree Celsius Centimetre (http://qudt.org/vocab/unit/DEG_C-CentiM)"""
    return QUDT_UNIT["DEG_C-CENTIM"]


def get_qudt_unit_kelvin_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kelvin Metre (http://qudt.org/vocab/unit/K-M)"""
    return QUDT_UNIT["K-M"]


def get_qudt_unit_centimetre_second_degree_celsius() -> URIRef:
    """Returns the URI for QUDT unit: Centimetre Second Degree Celsius (http://qudt.org/vocab/unit/CentiM-SEC-DEG_C)"""
    return QUDT_UNIT["CENTIM-SEC-DEG_C"]


def get_qudt_unit_bit_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Bit per Metre (http://qudt.org/vocab/unit/BIT-PER-M)"""
    return QUDT_UNIT["BIT-PER-M"]


def get_qudt_unit_exbibit_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Exbibit per Metre (http://qudt.org/vocab/unit/ExbiBIT-PER-M)"""
    return QUDT_UNIT["EXBIBIT-PER-M"]


def get_qudt_unit_gibibit_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Gibibit per Metre (http://qudt.org/vocab/unit/GibiBIT-PER-M)"""
    return QUDT_UNIT["GIBIBIT-PER-M"]


def get_qudt_unit_gigabit_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Gigabit per Metre (http://qudt.org/vocab/unit/GigaBIT-PER-M)"""
    return QUDT_UNIT["GIGABIT-PER-M"]


def get_qudt_unit_kibibit_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kibibit per Metre (http://qudt.org/vocab/unit/KibiBIT-PER-M)"""
    return QUDT_UNIT["KIBIBIT-PER-M"]


def get_qudt_unit_mebibit_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Mebibit per Metre (http://qudt.org/vocab/unit/MebiBIT-PER-M)"""
    return QUDT_UNIT["MEBIBIT-PER-M"]


def get_qudt_unit_pebibit_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Pebibit per Metre (http://qudt.org/vocab/unit/PebiBIT-PER-M)"""
    return QUDT_UNIT["PEBIBIT-PER-M"]


def get_qudt_unit_tebibit_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Tebibit per Metre (http://qudt.org/vocab/unit/TebiBIT-PER-M)"""
    return QUDT_UNIT["TEBIBIT-PER-M"]


def get_qudt_unit_micrometre_per_newton() -> URIRef:
    """Returns the URI for QUDT unit: Micrometre per Newton (http://qudt.org/vocab/unit/MicroM-PER-N)"""
    return QUDT_UNIT["MICROM-PER-N"]


def get_qudt_unit_kilogram_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Metre (http://qudt.org/vocab/unit/KiloGM-PER-M)"""
    return QUDT_UNIT["KILOGM-PER-M"]


def get_qudt_unit_kilogram_per_millimetre() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Millimetre (http://qudt.org/vocab/unit/KiloGM-PER-MilliM)"""
    return QUDT_UNIT["KILOGM-PER-MILLIM"]


def get_qudt_unit_joule_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Joule per Metre (http://qudt.org/vocab/unit/J-PER-M)"""
    return QUDT_UNIT["J-PER-M"]


def get_qudt_unit_kilo_electron_volt_per_micrometre() -> URIRef:
    """Returns the URI for QUDT unit: Kilo Electron Volt per Micrometre (http://qudt.org/vocab/unit/KiloEV-PER-MicroM)"""
    return QUDT_UNIT["KILOEV-PER-MICROM"]


def get_qudt_unit_mega_electron_volt_per_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Mega Electron Volt per Centimetre (http://qudt.org/vocab/unit/MegaEV-PER-CentiM)"""
    return QUDT_UNIT["MEGAEV-PER-CENTIM"]


def get_qudt_unit_percent_per_decakelvin() -> URIRef:
    """Returns the URI for QUDT unit: Percent per Decakelvin (http://qudt.org/vocab/unit/PERCENT-PER-DecaK)"""
    return QUDT_UNIT["PERCENT-PER-DECAK"]


def get_qudt_unit_percent_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Percent per Kelvin (http://qudt.org/vocab/unit/PERCENT-PER-K)"""
    return QUDT_UNIT["PERCENT-PER-K"]


def get_qudt_unit_bel_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Bel per Metre (http://qudt.org/vocab/unit/B-PER-M)"""
    return QUDT_UNIT["B-PER-M"]


def get_qudt_unit_decibel_per_kilometre() -> URIRef:
    """Returns the URI for QUDT unit: Decibel per Kilometre (http://qudt.org/vocab/unit/DeciB-PER-KiloM)"""
    return QUDT_UNIT["DECIB-PER-KILOM"]


def get_qudt_unit_decibel_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Decibel per Metre (http://qudt.org/vocab/unit/DeciB-PER-M)"""
    return QUDT_UNIT["DECIB-PER-M"]


def get_qudt_unit_kilogram_per_kilometre() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Kilometre (http://qudt.org/vocab/unit/KiloGM-PER-KiloM)"""
    return QUDT_UNIT["KILOGM-PER-KILOM"]


def get_qudt_unit_pound_mass_per_yard() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Yard (http://qudt.org/vocab/unit/LB-PER-YD)"""
    return QUDT_UNIT["LB-PER-YD"]


def get_qudt_unit_newton_metre_second_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Newton Metre Second per Metre (http://qudt.org/vocab/unit/N-M-SEC-PER-M)"""
    return QUDT_UNIT["N-M-SEC-PER-M"]


def get_qudt_unit_newton_second() -> URIRef:
    """Returns the URI for QUDT unit: Newton Second (http://qudt.org/vocab/unit/N-SEC)"""
    return QUDT_UNIT["N-SEC"]


def get_qudt_unit_planck_momentum() -> URIRef:
    """Returns the URI for QUDT unit: Planck Momentum (http://qudt.org/vocab/unit/PlanckMomentum)"""
    return QUDT_UNIT["PLANCKMOMENTUM"]


def get_qudt_unit_gigaohm_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Gigaohm per Metre (http://qudt.org/vocab/unit/GigaOHM-PER-M)"""
    return QUDT_UNIT["GIGAOHM-PER-M"]


def get_qudt_unit_kiloohm_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kiloohm per Metre (http://qudt.org/vocab/unit/KiloOHM-PER-M)"""
    return QUDT_UNIT["KILOOHM-PER-M"]


def get_qudt_unit_megaohm_per_kilometre() -> URIRef:
    """Returns the URI for QUDT unit: Megaohm per Kilometre (http://qudt.org/vocab/unit/MegaOHM-PER-KiloM)"""
    return QUDT_UNIT["MEGAOHM-PER-KILOM"]


def get_qudt_unit_megaohm_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Megaohm per Metre (http://qudt.org/vocab/unit/MegaOHM-PER-M)"""
    return QUDT_UNIT["MEGAOHM-PER-M"]


def get_qudt_unit_milliohm_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Milliohm per Metre (http://qudt.org/vocab/unit/MilliOHM-PER-M)"""
    return QUDT_UNIT["MILLIOHM-PER-M"]


def get_qudt_unit_ohm_per_kilometre() -> URIRef:
    """Returns the URI for QUDT unit: Ohm per Kilometre (http://qudt.org/vocab/unit/OHM-PER-KiloM)"""
    return QUDT_UNIT["OHM-PER-KILOM"]


def get_qudt_unit_ohm_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Ohm per Metre (http://qudt.org/vocab/unit/OHM-PER-M)"""
    return QUDT_UNIT["OHM-PER-M"]


def get_qudt_unit_ohm_per_international_mile() -> URIRef:
    """Returns the URI for QUDT unit: Ohm per International Mile (http://qudt.org/vocab/unit/OHM-PER-MI)"""
    return QUDT_UNIT["OHM-PER-MI"]


def get_qudt_unit_british_thermal_unit_international_definition_per_pound_force_degree_fahrenheit() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) per Pound Force Degree Fahrenheit (http://qudt.org/vocab/unit/BTU_IT-PER-LB_F-DEG_F)"""
    return QUDT_UNIT["BTU_IT-PER-LB_F-DEG_F"]


def get_qudt_unit_british_thermal_unit_international_definition_per_pound_force_degree_rankine() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) per Pound Force Degree Rankine (http://qudt.org/vocab/unit/BTU_IT-PER-LB_F-DEG_R)"""
    return QUDT_UNIT["BTU_IT-PER-LB_F-DEG_R"]


def get_qudt_unit_centimetre_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Centimetre per Kelvin (http://qudt.org/vocab/unit/CentiM-PER-K)"""
    return QUDT_UNIT["CENTIM-PER-K"]


def get_qudt_unit_foot_per_degree_fahrenheit() -> URIRef:
    """Returns the URI for QUDT unit: Foot per Degree Fahrenheit (http://qudt.org/vocab/unit/FT-PER-DEG_F)"""
    return QUDT_UNIT["FT-PER-DEG_F"]


def get_qudt_unit_inch_per_degree_fahrenheit() -> URIRef:
    """Returns the URI for QUDT unit: Inch per Degree Fahrenheit (http://qudt.org/vocab/unit/IN-PER-DEG_F)"""
    return QUDT_UNIT["IN-PER-DEG_F"]


def get_qudt_unit_metre_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Metre per Kelvin (http://qudt.org/vocab/unit/M-PER-K)"""
    return QUDT_UNIT["M-PER-K"]


def get_qudt_unit_micrometre_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Micrometre per Kelvin (http://qudt.org/vocab/unit/MicroM-PER-K)"""
    return QUDT_UNIT["MICROM-PER-K"]


def get_qudt_unit_millimetre_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Millimetre per Kelvin (http://qudt.org/vocab/unit/MilliM-PER-K)"""
    return QUDT_UNIT["MILLIM-PER-K"]


def get_qudt_unit_yard_per_degree_fahrenheit() -> URIRef:
    """Returns the URI for QUDT unit: Yard per Degree Fahrenheit (http://qudt.org/vocab/unit/YD-PER-DEG_F)"""
    return QUDT_UNIT["YD-PER-DEG_F"]


def get_qudt_unit_pound_force_foot_per_inch() -> URIRef:
    """Returns the URI for QUDT unit: Pound Force Foot per Inch (http://qudt.org/vocab/unit/LB_F-FT-PER-IN)"""
    return QUDT_UNIT["LB_F-FT-PER-IN"]


def get_qudt_unit_pound_force_inch_per_inch() -> URIRef:
    """Returns the URI for QUDT unit: Pound Force Inch per Inch (http://qudt.org/vocab/unit/LB_F-IN-PER-IN)"""
    return QUDT_UNIT["LB_F-IN-PER-IN"]


def get_qudt_unit_watt_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Watt per Metre (http://qudt.org/vocab/unit/W-PER-M)"""
    return QUDT_UNIT["W-PER-M"]


def get_qudt_unit_kilo_pound_force_foot_per_ampere() -> URIRef:
    """Returns the URI for QUDT unit: Kilo Pound Force Foot per Ampere (http://qudt.org/vocab/unit/KiloLB_F-FT-PER-A)"""
    return QUDT_UNIT["KILOLB_F-FT-PER-A"]


def get_qudt_unit_kiloweber() -> URIRef:
    """Returns the URI for QUDT unit: Kiloweber (http://qudt.org/vocab/unit/KiloWB)"""
    return QUDT_UNIT["KILOWB"]


def get_qudt_unit_maxwell() -> URIRef:
    """Returns the URI for QUDT unit: Maxwell (http://qudt.org/vocab/unit/MX)"""
    return QUDT_UNIT["MX"]


def get_qudt_unit_milliweber() -> URIRef:
    """Returns the URI for QUDT unit: Milliweber (http://qudt.org/vocab/unit/MilliWB)"""
    return QUDT_UNIT["MILLIWB"]


def get_qudt_unit_newton_metre_per_ampere() -> URIRef:
    """Returns the URI for QUDT unit: Newton Metre per Ampere (http://qudt.org/vocab/unit/N-M-PER-A)"""
    return QUDT_UNIT["N-M-PER-A"]


def get_qudt_unit_unit_pole() -> URIRef:
    """Returns the URI for QUDT unit: Unit Pole (http://qudt.org/vocab/unit/UnitPole)"""
    return QUDT_UNIT["UNITPOLE"]


def get_qudt_unit_abvolt_second() -> URIRef:
    """Returns the URI for QUDT unit: Abvolt Second (http://qudt.org/vocab/unit/V_Ab-SEC)"""
    return QUDT_UNIT["V_AB-SEC"]


def get_qudt_unit_barrel_us() -> URIRef:
    """Returns the URI for QUDT unit: Barrel (US) (http://qudt.org/vocab/unit/BBL_US)"""
    return QUDT_UNIT["BBL_US"]


def get_qudt_unit_barrel_us_petroleum() -> URIRef:
    """Returns the URI for QUDT unit: Barrel (us Petroleum) (http://qudt.org/vocab/unit/BBL_US_PET)"""
    return QUDT_UNIT["BBL_US_PET"]


def get_qudt_unit_us_liquid_cup() -> URIRef:
    """Returns the URI for QUDT unit: Us Liquid Cup (http://qudt.org/vocab/unit/CUP)"""
    return QUDT_UNIT["CUP"]


def get_qudt_unit_cup_us() -> URIRef:
    """Returns the URI for QUDT unit: Cup (US) (http://qudt.org/vocab/unit/CUP_US)"""
    return QUDT_UNIT["CUP_US"]


def get_qudt_unit_centilitre() -> URIRef:
    """Returns the URI for QUDT unit: Centilitre (http://qudt.org/vocab/unit/CentiL)"""
    return QUDT_UNIT["CENTIL"]


def get_qudt_unit_imperial_gallon() -> URIRef:
    """Returns the URI for QUDT unit: Imperial Gallon (http://qudt.org/vocab/unit/GAL_IMP)"""
    return QUDT_UNIT["GAL_IMP"]


def get_qudt_unit_gallon_uk() -> URIRef:
    """Returns the URI for QUDT unit: Gallon (UK) (http://qudt.org/vocab/unit/GAL_UK)"""
    return QUDT_UNIT["GAL_UK"]


def get_qudt_unit_us_gallon() -> URIRef:
    """Returns the URI for QUDT unit: Us Gallon (http://qudt.org/vocab/unit/GAL_US)"""
    return QUDT_UNIT["GAL_US"]


def get_qudt_unit_us_liquid_ounce() -> URIRef:
    """Returns the URI for QUDT unit: Us Liquid Ounce (http://qudt.org/vocab/unit/OZ_VOL_US)"""
    return QUDT_UNIT["OZ_VOL_US"]


def get_qudt_unit_us_liquid_pint() -> URIRef:
    """Returns the URI for QUDT unit: Us Liquid Pint (http://qudt.org/vocab/unit/PINT_US)"""
    return QUDT_UNIT["PINT_US"]


def get_qudt_unit_square_volt_per_square_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Square Volt per Square Kelvin (http://qudt.org/vocab/unit/V2-PER-K2)"""
    return QUDT_UNIT["V2-PER-K2"]


def get_qudt_unit_gamma() -> URIRef:
    """Returns the URI for QUDT unit: Gamma (http://qudt.org/vocab/unit/GAMMA)"""
    return QUDT_UNIT["GAMMA"]


def get_qudt_unit_gauss() -> URIRef:
    """Returns the URI for QUDT unit: Gauss (http://qudt.org/vocab/unit/GAUSS)"""
    return QUDT_UNIT["GAUSS"]


def get_qudt_unit_kilogauss() -> URIRef:
    """Returns the URI for QUDT unit: Kilogauss (http://qudt.org/vocab/unit/KiloGAUSS)"""
    return QUDT_UNIT["KILOGAUSS"]


def get_qudt_unit_kilotesla() -> URIRef:
    """Returns the URI for QUDT unit: Kilotesla (http://qudt.org/vocab/unit/KiloT)"""
    return QUDT_UNIT["KILOT"]


def get_qudt_unit_microtesla() -> URIRef:
    """Returns the URI for QUDT unit: Microtesla (http://qudt.org/vocab/unit/MicroT)"""
    return QUDT_UNIT["MICROT"]


def get_qudt_unit_millitesla() -> URIRef:
    """Returns the URI for QUDT unit: Millitesla (http://qudt.org/vocab/unit/MilliT)"""
    return QUDT_UNIT["MILLIT"]


def get_qudt_unit_nanotesla() -> URIRef:
    """Returns the URI for QUDT unit: Nanotesla (http://qudt.org/vocab/unit/NanoT)"""
    return QUDT_UNIT["NANOT"]


def get_qudt_unit_abtesla() -> URIRef:
    """Returns the URI for QUDT unit: Abtesla (http://qudt.org/vocab/unit/T_Ab)"""
    return QUDT_UNIT["T_AB"]


def get_qudt_unit_candela_per_square_foot() -> URIRef:
    """Returns the URI for QUDT unit: Candela per Square Foot (http://qudt.org/vocab/unit/CD-PER-FT2)"""
    return QUDT_UNIT["CD-PER-FT2"]


def get_qudt_unit_candela_per_square_inch() -> URIRef:
    """Returns the URI for QUDT unit: Candela per Square Inch (http://qudt.org/vocab/unit/CD-PER-IN2)"""
    return QUDT_UNIT["CD-PER-IN2"]


def get_qudt_unit_candela_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Candela per Square Metre (http://qudt.org/vocab/unit/CD-PER-M2)"""
    return QUDT_UNIT["CD-PER-M2"]


def get_qudt_unit_lambert() -> URIRef:
    """Returns the URI for QUDT unit: Lambert (http://qudt.org/vocab/unit/LA)"""
    return QUDT_UNIT["LA"]


def get_qudt_unit_foot_lambert() -> URIRef:
    """Returns the URI for QUDT unit: Foot Lambert (http://qudt.org/vocab/unit/LA_FT)"""
    return QUDT_UNIT["LA_FT"]


def get_qudt_unit_lumen_per_square_foot() -> URIRef:
    """Returns the URI for QUDT unit: Lumen per Square Foot (http://qudt.org/vocab/unit/LM-PER-FT2)"""
    return QUDT_UNIT["LM-PER-FT2"]


def get_qudt_unit_lumen_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Lumen per Square Metre (http://qudt.org/vocab/unit/LM-PER-M2)"""
    return QUDT_UNIT["LM-PER-M2"]


def get_qudt_unit_stilb() -> URIRef:
    """Returns the URI for QUDT unit: Stilb (http://qudt.org/vocab/unit/STILB)"""
    return QUDT_UNIT["STILB"]


def get_qudt_unit_lumen_per_watt() -> URIRef:
    """Returns the URI for QUDT unit: Lumen per Watt (http://qudt.org/vocab/unit/LM-PER-W)"""
    return QUDT_UNIT["LM-PER-W"]


def get_qudt_unit_lumen_hour() -> URIRef:
    """Returns the URI for QUDT unit: Lumen Hour (http://qudt.org/vocab/unit/LM-HR)"""
    return QUDT_UNIT["LM-HR"]


def get_qudt_unit_lumen_second() -> URIRef:
    """Returns the URI for QUDT unit: Lumen Second (http://qudt.org/vocab/unit/LM-SEC)"""
    return QUDT_UNIT["LM-SEC"]


def get_qudt_unit_lux_hour() -> URIRef:
    """Returns the URI for QUDT unit: Lux Hour (http://qudt.org/vocab/unit/LUX-HR)"""
    return QUDT_UNIT["LUX-HR"]


def get_qudt_unit_lux_second() -> URIRef:
    """Returns the URI for QUDT unit: Lux Second (http://qudt.org/vocab/unit/LUX-SEC)"""
    return QUDT_UNIT["LUX-SEC"]


def get_qudt_unit_kilolumen() -> URIRef:
    """Returns the URI for QUDT unit: Kilolumen (http://qudt.org/vocab/unit/KiloLM)"""
    return QUDT_UNIT["KILOLM"]


def get_qudt_unit_lumen() -> URIRef:
    """Returns the URI for QUDT unit: Lumen (http://qudt.org/vocab/unit/LM)"""
    return QUDT_UNIT["LM"]


def get_qudt_unit_candela() -> URIRef:
    """Returns the URI for QUDT unit: Candela (http://qudt.org/vocab/unit/CD)"""
    return QUDT_UNIT["CD"]


def get_qudt_unit_international_candle() -> URIRef:
    """Returns the URI for QUDT unit: International Candle (http://qudt.org/vocab/unit/CD_IN)"""
    return QUDT_UNIT["CD_IN"]


def get_qudt_unit_candlepower() -> URIRef:
    """Returns the URI for QUDT unit: Candlepower (http://qudt.org/vocab/unit/CP)"""
    return QUDT_UNIT["CP"]


def get_qudt_unit_hefner_kerze() -> URIRef:
    """Returns the URI for QUDT unit: Hefner-kerze (http://qudt.org/vocab/unit/HK)"""
    return QUDT_UNIT["HK"]


def get_qudt_unit_kilocandela() -> URIRef:
    """Returns the URI for QUDT unit: Kilocandela (http://qudt.org/vocab/unit/KiloCD)"""
    return QUDT_UNIT["KILOCD"]


def get_qudt_unit_millicandela() -> URIRef:
    """Returns the URI for QUDT unit: Millicandela (http://qudt.org/vocab/unit/MilliCD)"""
    return QUDT_UNIT["MILLICD"]


def get_qudt_unit_candela_per_kilolumen() -> URIRef:
    """Returns the URI for QUDT unit: Candela per Kilolumen (http://qudt.org/vocab/unit/CD-PER-KiloLM)"""
    return QUDT_UNIT["CD-PER-KILOLM"]


def get_qudt_unit_candela_per_lumen() -> URIRef:
    """Returns the URI for QUDT unit: Candela per Lumen (http://qudt.org/vocab/unit/CD-PER-LM)"""
    return QUDT_UNIT["CD-PER-LM"]


def get_qudt_unit_kilogram_square_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram Square Centimetre (http://qudt.org/vocab/unit/KiloGM-CentiM2)"""
    return QUDT_UNIT["KILOGM-CENTIM2"]


def get_qudt_unit_kilogram_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram Square Metre (http://qudt.org/vocab/unit/KiloGM-M2)"""
    return QUDT_UNIT["KILOGM-M2"]


def get_qudt_unit_kilogram_square_millimetre() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram Square Millimetre (http://qudt.org/vocab/unit/KiloGM-MilliM2)"""
    return QUDT_UNIT["KILOGM-MILLIM2"]


def get_qudt_unit_pound_mass_square_foot() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Square Foot (http://qudt.org/vocab/unit/LB-FT2)"""
    return QUDT_UNIT["LB-FT2"]


def get_qudt_unit_pound_mass_square_inch() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Square Inch (http://qudt.org/vocab/unit/LB-IN2)"""
    return QUDT_UNIT["LB-IN2"]


def get_qudt_unit_mach() -> URIRef:
    """Returns the URI for QUDT unit: Mach (http://qudt.org/vocab/unit/MACH)"""
    return QUDT_UNIT["MACH"]


def get_qudt_unit_ampere_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Ampere Square Metre (http://qudt.org/vocab/unit/A-M2)"""
    return QUDT_UNIT["A-M2"]


def get_qudt_unit_abampere_square_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Abampere Square Centimetre (http://qudt.org/vocab/unit/A_Ab-CentiM2)"""
    return QUDT_UNIT["A_AB-CENTIM2"]


def get_qudt_unit_newton_square_metre_per_ampere() -> URIRef:
    """Returns the URI for QUDT unit: Newton Square Metre per Ampere (http://qudt.org/vocab/unit/N-M2-PER-A)"""
    return QUDT_UNIT["N-M2-PER-A"]


def get_qudt_unit_weber_metre() -> URIRef:
    """Returns the URI for QUDT unit: Weber Metre (http://qudt.org/vocab/unit/WB-M)"""
    return QUDT_UNIT["WB-M"]


def get_qudt_unit_newton_per_ampere() -> URIRef:
    """Returns the URI for QUDT unit: Newton per Ampere (http://qudt.org/vocab/unit/N-PER-A)"""
    return QUDT_UNIT["N-PER-A"]


def get_qudt_unit_tesla_metre() -> URIRef:
    """Returns the URI for QUDT unit: Tesla Metre (http://qudt.org/vocab/unit/T-M)"""
    return QUDT_UNIT["T-M"]


def get_qudt_unit_volt_second_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Volt Second per Metre (http://qudt.org/vocab/unit/V-SEC-PER-M)"""
    return QUDT_UNIT["V-SEC-PER-M"]


def get_qudt_unit_metre_per_volt_second() -> URIRef:
    """Returns the URI for QUDT unit: Metre per Volt Second (http://qudt.org/vocab/unit/M-PER-V-SEC)"""
    return QUDT_UNIT["M-PER-V-SEC"]


def get_qudt_unit_kiloweber_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kiloweber per Metre (http://qudt.org/vocab/unit/KiloWB-PER-M)"""
    return QUDT_UNIT["KILOWB-PER-M"]


def get_qudt_unit_weber_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Weber per Metre (http://qudt.org/vocab/unit/WB-PER-M)"""
    return QUDT_UNIT["WB-PER-M"]


def get_qudt_unit_weber_per_millimetre() -> URIRef:
    """Returns the URI for QUDT unit: Weber per Millimetre (http://qudt.org/vocab/unit/WB-PER-MilliM)"""
    return QUDT_UNIT["WB-PER-MILLIM"]


def get_qudt_unit_ampere_turn() -> URIRef:
    """Returns the URI for QUDT unit: Ampere Turn (http://qudt.org/vocab/unit/AT)"""
    return QUDT_UNIT["AT"]


def get_qudt_unit_gilbert() -> URIRef:
    """Returns the URI for QUDT unit: Gilbert (http://qudt.org/vocab/unit/GI)"""
    return QUDT_UNIT["GI"]


def get_qudt_unit_oersted_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Oersted Centimetre (http://qudt.org/vocab/unit/OERSTED-CentiM)"""
    return QUDT_UNIT["OERSTED-CENTIM"]


def get_qudt_unit_square_metre_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre per Kilogram (http://qudt.org/vocab/unit/M2-PER-KiloGM)"""
    return QUDT_UNIT["M2-PER-KILOGM"]


def get_qudt_unit_pound_mole_degree_fahrenheit() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mole Degree Fahrenheit (http://qudt.org/vocab/unit/MOL_LB-DEG_F)"""
    return QUDT_UNIT["MOL_LB-DEG_F"]


def get_qudt_unit_square_centimetre_per_gram() -> URIRef:
    """Returns the URI for QUDT unit: Square Centimetre per Gram (http://qudt.org/vocab/unit/CentiM2-PER-GM)"""
    return QUDT_UNIT["CENTIM2-PER-GM"]


def get_qudt_unit_square_metre_per_gram() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre per Gram (http://qudt.org/vocab/unit/M2-PER-GM)"""
    return QUDT_UNIT["M2-PER-GM"]


def get_qudt_unit_square_metre_per_dry_gram() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre per Dry Gram (http://qudt.org/vocab/unit/M2-PER-GM_DRY)"""
    return QUDT_UNIT["M2-PER-GM_DRY"]


def get_qudt_unit_microgram_per_litre_day() -> URIRef:
    """Returns the URI for QUDT unit: Microgram per Litre Day (http://qudt.org/vocab/unit/MicroGM-PER-L-DAY)"""
    return QUDT_UNIT["MICROGM-PER-L-DAY"]


def get_qudt_unit_dyne_second_per_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Dyne Second per Centimetre (http://qudt.org/vocab/unit/DYN-SEC-PER-CentiM)"""
    return QUDT_UNIT["DYN-SEC-PER-CENTIM"]


def get_qudt_unit_gram_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Day (http://qudt.org/vocab/unit/GM-PER-DAY)"""
    return QUDT_UNIT["GM-PER-DAY"]


def get_qudt_unit_gram_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Hour (http://qudt.org/vocab/unit/GM-PER-HR)"""
    return QUDT_UNIT["GM-PER-HR"]


def get_qudt_unit_gram_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Minute (http://qudt.org/vocab/unit/GM-PER-MIN)"""
    return QUDT_UNIT["GM-PER-MIN"]


def get_qudt_unit_gram_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Second (http://qudt.org/vocab/unit/GM-PER-SEC)"""
    return QUDT_UNIT["GM-PER-SEC"]


def get_qudt_unit_kilogram_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Day (http://qudt.org/vocab/unit/KiloGM-PER-DAY)"""
    return QUDT_UNIT["KILOGM-PER-DAY"]


def get_qudt_unit_kilogram_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Hour (http://qudt.org/vocab/unit/KiloGM-PER-HR)"""
    return QUDT_UNIT["KILOGM-PER-HR"]


def get_qudt_unit_kilogram_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Minute (http://qudt.org/vocab/unit/KiloGM-PER-MIN)"""
    return QUDT_UNIT["KILOGM-PER-MIN"]


def get_qudt_unit_kilogram_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Second (http://qudt.org/vocab/unit/KiloGM-PER-SEC)"""
    return QUDT_UNIT["KILOGM-PER-SEC"]


def get_qudt_unit_kilogram_per_year() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Year (http://qudt.org/vocab/unit/KiloGM-PER-YR)"""
    return QUDT_UNIT["KILOGM-PER-YR"]


def get_qudt_unit_kilo_pound_mass_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Kilo Pound Mass per Hour (http://qudt.org/vocab/unit/KiloLB-PER-HR)"""
    return QUDT_UNIT["KILOLB-PER-HR"]


def get_qudt_unit_kilotonne_per_year() -> URIRef:
    """Returns the URI for QUDT unit: Kilotonne per Year (http://qudt.org/vocab/unit/KiloTONNE-PER-YR)"""
    return QUDT_UNIT["KILOTONNE-PER-YR"]


def get_qudt_unit_pound_mass_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Day (http://qudt.org/vocab/unit/LB-PER-DAY)"""
    return QUDT_UNIT["LB-PER-DAY"]


def get_qudt_unit_pound_mass_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Hour (http://qudt.org/vocab/unit/LB-PER-HR)"""
    return QUDT_UNIT["LB-PER-HR"]


def get_qudt_unit_pound_mass_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Minute (http://qudt.org/vocab/unit/LB-PER-MIN)"""
    return QUDT_UNIT["LB-PER-MIN"]


def get_qudt_unit_pound_mass_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Second (http://qudt.org/vocab/unit/LB-PER-SEC)"""
    return QUDT_UNIT["LB-PER-SEC"]


def get_qudt_unit_megatonne_per_year() -> URIRef:
    """Returns the URI for QUDT unit: Megatonne per Year (http://qudt.org/vocab/unit/MegaTONNE-PER-YR)"""
    return QUDT_UNIT["MEGATONNE-PER-YR"]


def get_qudt_unit_milligram_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Day (http://qudt.org/vocab/unit/MilliGM-PER-DAY)"""
    return QUDT_UNIT["MILLIGM-PER-DAY"]


def get_qudt_unit_milligram_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Hour (http://qudt.org/vocab/unit/MilliGM-PER-HR)"""
    return QUDT_UNIT["MILLIGM-PER-HR"]


def get_qudt_unit_milligram_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Minute (http://qudt.org/vocab/unit/MilliGM-PER-MIN)"""
    return QUDT_UNIT["MILLIGM-PER-MIN"]


def get_qudt_unit_milligram_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Second (http://qudt.org/vocab/unit/MilliGM-PER-SEC)"""
    return QUDT_UNIT["MILLIGM-PER-SEC"]


def get_qudt_unit_ounce_mass_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass per Day (http://qudt.org/vocab/unit/OZ-PER-DAY)"""
    return QUDT_UNIT["OZ-PER-DAY"]


def get_qudt_unit_ounce_mass_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass per Hour (http://qudt.org/vocab/unit/OZ-PER-HR)"""
    return QUDT_UNIT["OZ-PER-HR"]


def get_qudt_unit_ounce_mass_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass per Minute (http://qudt.org/vocab/unit/OZ-PER-MIN)"""
    return QUDT_UNIT["OZ-PER-MIN"]


def get_qudt_unit_ounce_mass_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass per Second (http://qudt.org/vocab/unit/OZ-PER-SEC)"""
    return QUDT_UNIT["OZ-PER-SEC"]


def get_qudt_unit_slug_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Slug per Day (http://qudt.org/vocab/unit/SLUG-PER-DAY)"""
    return QUDT_UNIT["SLUG-PER-DAY"]


def get_qudt_unit_slug_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Slug per Hour (http://qudt.org/vocab/unit/SLUG-PER-HR)"""
    return QUDT_UNIT["SLUG-PER-HR"]


def get_qudt_unit_slug_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Slug per Minute (http://qudt.org/vocab/unit/SLUG-PER-MIN)"""
    return QUDT_UNIT["SLUG-PER-MIN"]


def get_qudt_unit_slug_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Slug per Second (http://qudt.org/vocab/unit/SLUG-PER-SEC)"""
    return QUDT_UNIT["SLUG-PER-SEC"]


def get_qudt_unit_tonne_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Tonne per Day (http://qudt.org/vocab/unit/TONNE-PER-DAY)"""
    return QUDT_UNIT["TONNE-PER-DAY"]


def get_qudt_unit_tonne_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Tonne per Hour (http://qudt.org/vocab/unit/TONNE-PER-HR)"""
    return QUDT_UNIT["TONNE-PER-HR"]


def get_qudt_unit_tonne_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Tonne per Minute (http://qudt.org/vocab/unit/TONNE-PER-MIN)"""
    return QUDT_UNIT["TONNE-PER-MIN"]


def get_qudt_unit_tonne_per_month() -> URIRef:
    """Returns the URI for QUDT unit: Tonne per Month (http://qudt.org/vocab/unit/TONNE-PER-MO)"""
    return QUDT_UNIT["TONNE-PER-MO"]


def get_qudt_unit_tonne_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Tonne per Second (http://qudt.org/vocab/unit/TONNE-PER-SEC)"""
    return QUDT_UNIT["TONNE-PER-SEC"]


def get_qudt_unit_tonne_per_year() -> URIRef:
    """Returns the URI for QUDT unit: Tonne per Year (http://qudt.org/vocab/unit/TONNE-PER-YR)"""
    return QUDT_UNIT["TONNE-PER-YR"]


def get_qudt_unit_metric_ton_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Metric Ton per Day (http://qudt.org/vocab/unit/TON_Metric-PER-DAY)"""
    return QUDT_UNIT["TON_METRIC-PER-DAY"]


def get_qudt_unit_metric_ton_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Metric Ton per Hour (http://qudt.org/vocab/unit/TON_Metric-PER-HR)"""
    return QUDT_UNIT["TON_METRIC-PER-HR"]


def get_qudt_unit_metric_ton_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Metric Ton per Minute (http://qudt.org/vocab/unit/TON_Metric-PER-MIN)"""
    return QUDT_UNIT["TON_METRIC-PER-MIN"]


def get_qudt_unit_metric_ton_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Metric Ton per Second (http://qudt.org/vocab/unit/TON_Metric-PER-SEC)"""
    return QUDT_UNIT["TON_METRIC-PER-SEC"]


def get_qudt_unit_short_ton_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Short Ton per Hour (http://qudt.org/vocab/unit/TON_SHORT-PER-HR)"""
    return QUDT_UNIT["TON_SHORT-PER-HR"]


def get_qudt_unit_ton_uk_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Ton (UK) per Day (http://qudt.org/vocab/unit/TON_UK-PER-DAY)"""
    return QUDT_UNIT["TON_UK-PER-DAY"]


def get_qudt_unit_ton_uk_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Ton (UK) per Hour (http://qudt.org/vocab/unit/TON_UK-PER-HR)"""
    return QUDT_UNIT["TON_UK-PER-HR"]


def get_qudt_unit_ton_us_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Ton (US) per Day (http://qudt.org/vocab/unit/TON_US-PER-DAY)"""
    return QUDT_UNIT["TON_US-PER-DAY"]


def get_qudt_unit_ton_us_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Ton (US) per Hour (http://qudt.org/vocab/unit/TON_US-PER-HR)"""
    return QUDT_UNIT["TON_US-PER-HR"]


def get_qudt_unit_dyne_second_per_cubic_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Dyne Second per Cubic Centimetre (http://qudt.org/vocab/unit/DYN-SEC-PER-CentiM3)"""
    return QUDT_UNIT["DYN-SEC-PER-CENTIM3"]


def get_qudt_unit_gram_per_square_centimetre_year() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Square Centimetre Year (http://qudt.org/vocab/unit/GM-PER-CentiM2-YR)"""
    return QUDT_UNIT["GM-PER-CENTIM2-YR"]


def get_qudt_unit_gram_per_square_metre_day() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Square Metre Day (http://qudt.org/vocab/unit/GM-PER-M2-DAY)"""
    return QUDT_UNIT["GM-PER-M2-DAY"]


def get_qudt_unit_gram_per_square_metre_hour() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Square Metre Hour (http://qudt.org/vocab/unit/GM-PER-M2-HR)"""
    return QUDT_UNIT["GM-PER-M2-HR"]


def get_qudt_unit_gram_per_square_metre_year() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Square Metre Year (http://qudt.org/vocab/unit/GM-PER-M2-YR)"""
    return QUDT_UNIT["GM-PER-M2-YR"]


def get_qudt_unit_gram_of_carbon_per_square_metre_day() -> URIRef:
    """Returns the URI for QUDT unit: Gram of Carbon per Square Metre Day (http://qudt.org/vocab/unit/GM_Carbon-PER-M2-DAY)"""
    return QUDT_UNIT["GM_CARBON-PER-M2-DAY"]


def get_qudt_unit_gram_of_nitrogen_per_square_metre_day() -> URIRef:
    """Returns the URI for QUDT unit: Gram of Nitrogen per Square Metre Day (http://qudt.org/vocab/unit/GM_Nitrogen-PER-M2-DAY)"""
    return QUDT_UNIT["GM_NITROGEN-PER-M2-DAY"]


def get_qudt_unit_kilogram_per_hectare_year() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Hectare Year (http://qudt.org/vocab/unit/KiloGM-PER-HA-YR)"""
    return QUDT_UNIT["KILOGM-PER-HA-YR"]


def get_qudt_unit_kilogram_per_square_metre_day() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Square Metre Day (http://qudt.org/vocab/unit/KiloGM-PER-M2-DAY)"""
    return QUDT_UNIT["KILOGM-PER-M2-DAY"]


def get_qudt_unit_kilogram_per_square_metre_second() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Square Metre Second (http://qudt.org/vocab/unit/KiloGM-PER-M2-SEC)"""
    return QUDT_UNIT["KILOGM-PER-M2-SEC"]


def get_qudt_unit_kilogram_per_second_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Second Square Metre (http://qudt.org/vocab/unit/KiloGM-PER-SEC-M2)"""
    return QUDT_UNIT["KILOGM-PER-SEC-M2"]


def get_qudt_unit_megagram_per_hectare_year() -> URIRef:
    """Returns the URI for QUDT unit: Megagram per Hectare Year (http://qudt.org/vocab/unit/MegaGM-PER-HA-YR)"""
    return QUDT_UNIT["MEGAGM-PER-HA-YR"]


def get_qudt_unit_microgram_per_square_centimetre_week() -> URIRef:
    """Returns the URI for QUDT unit: Microgram per Square Centimetre Week (http://qudt.org/vocab/unit/MicroGM-PER-CentiM2-WK)"""
    return QUDT_UNIT["MICROGM-PER-CENTIM2-WK"]


def get_qudt_unit_microgram_per_square_metre_day() -> URIRef:
    """Returns the URI for QUDT unit: Microgram per Square Metre Day (http://qudt.org/vocab/unit/MicroGM-PER-M2-DAY)"""
    return QUDT_UNIT["MICROGM-PER-M2-DAY"]


def get_qudt_unit_milligram_per_square_metre_day() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Square Metre Day (http://qudt.org/vocab/unit/MilliGM-PER-M2-DAY)"""
    return QUDT_UNIT["MILLIGM-PER-M2-DAY"]


def get_qudt_unit_milligram_per_square_metre_hour() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Square Metre Hour (http://qudt.org/vocab/unit/MilliGM-PER-M2-HR)"""
    return QUDT_UNIT["MILLIGM-PER-M2-HR"]


def get_qudt_unit_milligram_per_square_metre_second() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Square Metre Second (http://qudt.org/vocab/unit/MilliGM-PER-M2-SEC)"""
    return QUDT_UNIT["MILLIGM-PER-M2-SEC"]


def get_qudt_unit_nanogram_per_square_centimetre_day() -> URIRef:
    """Returns the URI for QUDT unit: Nanogram per Square Centimetre Day (http://qudt.org/vocab/unit/NanoGM-PER-CentiM2-DAY)"""
    return QUDT_UNIT["NANOGM-PER-CENTIM2-DAY"]


def get_qudt_unit_tonne_per_hectare_year() -> URIRef:
    """Returns the URI for QUDT unit: Tonne per Hectare Year (http://qudt.org/vocab/unit/TONNE-PER-HA-YR)"""
    return QUDT_UNIT["TONNE-PER-HA-YR"]


def get_qudt_unit_tesla_second() -> URIRef:
    """Returns the URI for QUDT unit: Tesla Second (http://qudt.org/vocab/unit/T-SEC)"""
    return QUDT_UNIT["T-SEC"]


def get_qudt_unit_gram_per_cubic_centimetre_bar() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Cubic Centimetre Bar (http://qudt.org/vocab/unit/GM-PER-CentiM3-BAR)"""
    return QUDT_UNIT["GM-PER-CENTIM3-BAR"]


def get_qudt_unit_gram_per_cubic_decimetre_bar() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Cubic Decimetre Bar (http://qudt.org/vocab/unit/GM-PER-DeciM3-BAR)"""
    return QUDT_UNIT["GM-PER-DECIM3-BAR"]


def get_qudt_unit_gram_per_litre_bar() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Litre Bar (http://qudt.org/vocab/unit/GM-PER-L-BAR)"""
    return QUDT_UNIT["GM-PER-L-BAR"]


def get_qudt_unit_gram_per_cubic_metre_bar() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Cubic Metre Bar (http://qudt.org/vocab/unit/GM-PER-M3-BAR)"""
    return QUDT_UNIT["GM-PER-M3-BAR"]


def get_qudt_unit_gram_per_millilitre_bar() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Millilitre Bar (http://qudt.org/vocab/unit/GM-PER-MilliL-BAR)"""
    return QUDT_UNIT["GM-PER-MILLIL-BAR"]


def get_qudt_unit_kilogram_per_cubic_centimetre_bar() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Cubic Centimetre Bar (http://qudt.org/vocab/unit/KiloGM-PER-CentiM3-BAR)"""
    return QUDT_UNIT["KILOGM-PER-CENTIM3-BAR"]


def get_qudt_unit_kilogram_per_cubic_decimetre_bar() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Cubic Decimetre Bar (http://qudt.org/vocab/unit/KiloGM-PER-DeciM3-BAR)"""
    return QUDT_UNIT["KILOGM-PER-DECIM3-BAR"]


def get_qudt_unit_kilogram_per_gigajoule() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Gigajoule (http://qudt.org/vocab/unit/KiloGM-PER-GigaJ)"""
    return QUDT_UNIT["KILOGM-PER-GIGAJ"]


def get_qudt_unit_kilogram_per_joule() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Joule (http://qudt.org/vocab/unit/KiloGM-PER-J)"""
    return QUDT_UNIT["KILOGM-PER-J"]


def get_qudt_unit_kilogram_per_litre_bar() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Litre Bar (http://qudt.org/vocab/unit/KiloGM-PER-L-BAR)"""
    return QUDT_UNIT["KILOGM-PER-L-BAR"]


def get_qudt_unit_kilogram_per_cubic_metre_bar() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Cubic Metre Bar (http://qudt.org/vocab/unit/KiloGM-PER-M3-BAR)"""
    return QUDT_UNIT["KILOGM-PER-M3-BAR"]


def get_qudt_unit_kilogram_per_cubic_metre_pascal() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Cubic Metre Pascal (http://qudt.org/vocab/unit/KiloGM-PER-M3-PA)"""
    return QUDT_UNIT["KILOGM-PER-M3-PA"]


def get_qudt_unit_kilogram_per_mega_british_thermal_unit_international_definition() -> (
    URIRef
):
    """Returns the URI for QUDT unit: Kilogram per Mega British Thermal Unit (international Definition) (http://qudt.org/vocab/unit/KiloGM-PER-MegaBTU_IT)"""
    return QUDT_UNIT["KILOGM-PER-MEGABTU_IT"]


def get_qudt_unit_pound_mass_per_cubic_foot_psi() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Cubic Foot Psi (http://qudt.org/vocab/unit/LB-PER-FT3-PSI)"""
    return QUDT_UNIT["LB-PER-FT3-PSI"]


def get_qudt_unit_pound_mass_per_cubic_inch_psi() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Cubic Inch Psi (http://qudt.org/vocab/unit/LB-PER-IN3-PSI)"""
    return QUDT_UNIT["LB-PER-IN3-PSI"]


def get_qudt_unit_microgram_per_cubic_metre_bar() -> URIRef:
    """Returns the URI for QUDT unit: Microgram per Cubic Metre Bar (http://qudt.org/vocab/unit/MicroGM-PER-M3-BAR)"""
    return QUDT_UNIT["MICROGM-PER-M3-BAR"]


def get_qudt_unit_milligram_per_cubic_metre_bar() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Cubic Metre Bar (http://qudt.org/vocab/unit/MilliGM-PER-M3-BAR)"""
    return QUDT_UNIT["MILLIGM-PER-M3-BAR"]


def get_qudt_unit_tonne_per_cubic_metre_bar() -> URIRef:
    """Returns the URI for QUDT unit: Tonne per Cubic Metre Bar (http://qudt.org/vocab/unit/TONNE-PER-M3-BAR)"""
    return QUDT_UNIT["TONNE-PER-M3-BAR"]


def get_qudt_unit_denier() -> URIRef:
    """Returns the URI for QUDT unit: Denier (http://qudt.org/vocab/unit/DENIER)"""
    return QUDT_UNIT["DENIER"]


def get_qudt_unit_gram_per_kilometre() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Kilometre (http://qudt.org/vocab/unit/GM-PER-KiloM)"""
    return QUDT_UNIT["GM-PER-KILOM"]


def get_qudt_unit_gram_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Metre (http://qudt.org/vocab/unit/GM-PER-M)"""
    return QUDT_UNIT["GM-PER-M"]


def get_qudt_unit_gram_per_millimetre() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Millimetre (http://qudt.org/vocab/unit/GM-PER-MilliM)"""
    return QUDT_UNIT["GM-PER-MILLIM"]


def get_qudt_unit_pound_mass_per_foot() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Foot (http://qudt.org/vocab/unit/LB-PER-FT)"""
    return QUDT_UNIT["LB-PER-FT"]


def get_qudt_unit_pound_mass_per_inch() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Inch (http://qudt.org/vocab/unit/LB-PER-IN)"""
    return QUDT_UNIT["LB-PER-IN"]


def get_qudt_unit_milligram_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Metre (http://qudt.org/vocab/unit/MilliGM-PER-M)"""
    return QUDT_UNIT["MILLIGM-PER-M"]


def get_qudt_unit_slug_per_foot() -> URIRef:
    """Returns the URI for QUDT unit: Slug per Foot (http://qudt.org/vocab/unit/SLUG-PER-FT)"""
    return QUDT_UNIT["SLUG-PER-FT"]


def get_qudt_unit_tex() -> URIRef:
    """Returns the URI for QUDT unit: Tex (http://qudt.org/vocab/unit/TEX)"""
    return QUDT_UNIT["TEX"]


def get_qudt_unit_newton_second_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Newton Second per Metre (http://qudt.org/vocab/unit/N-SEC-PER-M)"""
    return QUDT_UNIT["N-SEC-PER-M"]


def get_qudt_unit_nanogram_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Nanogram per Day (http://qudt.org/vocab/unit/NanoGM-PER-DAY)"""
    return QUDT_UNIT["NANOGM-PER-DAY"]


def get_qudt_unit_microgram_per_gram_day() -> URIRef:
    """Returns the URI for QUDT unit: Microgram per Gram Day (http://qudt.org/vocab/unit/MicroGM-PER-GM-DAY)"""
    return QUDT_UNIT["MICROGM-PER-GM-DAY"]


def get_qudt_unit_microgram_per_gram_hour() -> URIRef:
    """Returns the URI for QUDT unit: Microgram per Gram Hour (http://qudt.org/vocab/unit/MicroGM-PER-GM-HR)"""
    return QUDT_UNIT["MICROGM-PER-GM-HR"]


def get_qudt_unit_milligram_per_gram_hour() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Gram Hour (http://qudt.org/vocab/unit/MilliGM-PER-GM-HR)"""
    return QUDT_UNIT["MILLIGM-PER-GM-HR"]


def get_qudt_unit_milligram_per_kilogram_day() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Kilogram Day (http://qudt.org/vocab/unit/MilliGM-PER-KiloGM-DAY)"""
    return QUDT_UNIT["MILLIGM-PER-KILOGM-DAY"]


def get_qudt_unit_erg_square_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Erg Square Centimetre (http://qudt.org/vocab/unit/ERG-CentiM2)"""
    return QUDT_UNIT["ERG-CENTIM2"]


def get_qudt_unit_kilogram_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram Kelvin (http://qudt.org/vocab/unit/KiloGM-K)"""
    return QUDT_UNIT["KILOGM-K"]


def get_qudt_unit_pound_mass_degree_fahrenheit() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Degree Fahrenheit (http://qudt.org/vocab/unit/LB-DEG_F)"""
    return QUDT_UNIT["LB-DEG_F"]


def get_qudt_unit_pound_mass_degree_rankine() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Degree Rankine (http://qudt.org/vocab/unit/LB-DEG_R)"""
    return QUDT_UNIT["LB-DEG_R"]


def get_qudt_unit_ampere_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Ampere per Kilogram (http://qudt.org/vocab/unit/A-PER-KiloGM)"""
    return QUDT_UNIT["A-PER-KILOGM"]


def get_qudt_unit_british_thermal_unit_thermochemical_definition_per_pound_mass_degree_rankine() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (thermochemical Definition) per Pound Mass Degree Rankine (http://qudt.org/vocab/unit/BTU_TH-PER-LB-DEG_R)"""
    return QUDT_UNIT["BTU_TH-PER-LB-DEG_R"]


def get_qudt_unit_kilo_international_table_calorie_per_gram_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Kilo International Table Calorie per Gram Kelvin (http://qudt.org/vocab/unit/KiloCAL_IT-PER-GM-K)"""
    return QUDT_UNIT["KILOCAL_IT-PER-GM-K"]


def get_qudt_unit_mohm() -> URIRef:
    """Returns the URI for QUDT unit: Mohm (http://qudt.org/vocab/unit/MOHM)"""
    return QUDT_UNIT["MOHM"]


def get_qudt_unit_kilonewton_metre_per_degree_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kilonewton Metre per Degree Metre (http://qudt.org/vocab/unit/KiloN-M-PER-DEG-M)"""
    return QUDT_UNIT["KILON-M-PER-DEG-M"]


def get_qudt_unit_newton_metre_per_degree_metre() -> URIRef:
    """Returns the URI for QUDT unit: Newton Metre per Degree Metre (http://qudt.org/vocab/unit/N-M-PER-DEG-M)"""
    return QUDT_UNIT["N-M-PER-DEG-M"]


def get_qudt_unit_newton_metre_per_metre_radian() -> URIRef:
    """Returns the URI for QUDT unit: Newton Metre per Metre Radian (http://qudt.org/vocab/unit/N-M-PER-M-RAD)"""
    return QUDT_UNIT["N-M-PER-M-RAD"]


def get_qudt_unit_kilonewton_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kilonewton per Cubic Metre (http://qudt.org/vocab/unit/KiloN-PER-M3)"""
    return QUDT_UNIT["KILON-PER-M3"]


def get_qudt_unit_meganewton_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Meganewton per Cubic Metre (http://qudt.org/vocab/unit/MegaN-PER-M3)"""
    return QUDT_UNIT["MEGAN-PER-M3"]


def get_qudt_unit_newton_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Newton per Cubic Metre (http://qudt.org/vocab/unit/N-PER-M3)"""
    return QUDT_UNIT["N-PER-M3"]


def get_qudt_unit_barrel_uk_petroleum_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Barrel (UK Petroleum) per Day (http://qudt.org/vocab/unit/BBL_UK_PET-PER-DAY)"""
    return QUDT_UNIT["BBL_UK_PET-PER-DAY"]


def get_qudt_unit_barrel_uk_petroleum_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Barrel (UK Petroleum) per Hour (http://qudt.org/vocab/unit/BBL_UK_PET-PER-HR)"""
    return QUDT_UNIT["BBL_UK_PET-PER-HR"]


def get_qudt_unit_barrel_uk_petroleum_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Barrel (UK Petroleum) per Minute (http://qudt.org/vocab/unit/BBL_UK_PET-PER-MIN)"""
    return QUDT_UNIT["BBL_UK_PET-PER-MIN"]


def get_qudt_unit_barrel_uk_petroleum_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Barrel (UK Petroleum) per Second (http://qudt.org/vocab/unit/BBL_UK_PET-PER-SEC)"""
    return QUDT_UNIT["BBL_UK_PET-PER-SEC"]


def get_qudt_unit_barrel_us_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Barrel (US) per Day (http://qudt.org/vocab/unit/BBL_US-PER-DAY)"""
    return QUDT_UNIT["BBL_US-PER-DAY"]


def get_qudt_unit_barrel_us_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Barrel (US) per Minute (http://qudt.org/vocab/unit/BBL_US-PER-MIN)"""
    return QUDT_UNIT["BBL_US-PER-MIN"]


def get_qudt_unit_barrel_us_petroleum_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Barrel (us Petroleum) per Hour (http://qudt.org/vocab/unit/BBL_US_PET-PER-HR)"""
    return QUDT_UNIT["BBL_US_PET-PER-HR"]


def get_qudt_unit_barrel_us_petroleum_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Barrel (us Petroleum) per Second (http://qudt.org/vocab/unit/BBL_US_PET-PER-SEC)"""
    return QUDT_UNIT["BBL_US_PET-PER-SEC"]


def get_qudt_unit_bushel_uk_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Bushel (UK) per Day (http://qudt.org/vocab/unit/BU_UK-PER-DAY)"""
    return QUDT_UNIT["BU_UK-PER-DAY"]


def get_qudt_unit_bushel_uk_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Bushel (UK) per Hour (http://qudt.org/vocab/unit/BU_UK-PER-HR)"""
    return QUDT_UNIT["BU_UK-PER-HR"]


def get_qudt_unit_bushel_uk_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Bushel (UK) per Minute (http://qudt.org/vocab/unit/BU_UK-PER-MIN)"""
    return QUDT_UNIT["BU_UK-PER-MIN"]


def get_qudt_unit_bushel_uk_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Bushel (UK) per Second (http://qudt.org/vocab/unit/BU_UK-PER-SEC)"""
    return QUDT_UNIT["BU_UK-PER-SEC"]


def get_qudt_unit_bushel_us_dry_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Bushel (US Dry) per Day (http://qudt.org/vocab/unit/BU_US_DRY-PER-DAY)"""
    return QUDT_UNIT["BU_US_DRY-PER-DAY"]


def get_qudt_unit_bushel_us_dry_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Bushel (US Dry) per Hour (http://qudt.org/vocab/unit/BU_US_DRY-PER-HR)"""
    return QUDT_UNIT["BU_US_DRY-PER-HR"]


def get_qudt_unit_bushel_us_dry_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Bushel (US Dry) per Minute (http://qudt.org/vocab/unit/BU_US_DRY-PER-MIN)"""
    return QUDT_UNIT["BU_US_DRY-PER-MIN"]


def get_qudt_unit_bushel_us_dry_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Bushel (US Dry) per Second (http://qudt.org/vocab/unit/BU_US_DRY-PER-SEC)"""
    return QUDT_UNIT["BU_US_DRY-PER-SEC"]


def get_qudt_unit_cubic_centimetre_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Centimetre per Day (http://qudt.org/vocab/unit/CentiM3-PER-DAY)"""
    return QUDT_UNIT["CENTIM3-PER-DAY"]


def get_qudt_unit_cubic_centimetre_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Centimetre per Hour (http://qudt.org/vocab/unit/CentiM3-PER-HR)"""
    return QUDT_UNIT["CENTIM3-PER-HR"]


def get_qudt_unit_cubic_centimetre_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Centimetre per Minute (http://qudt.org/vocab/unit/CentiM3-PER-MIN)"""
    return QUDT_UNIT["CENTIM3-PER-MIN"]


def get_qudt_unit_cubic_centimetre_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Centimetre per Second (http://qudt.org/vocab/unit/CentiM3-PER-SEC)"""
    return QUDT_UNIT["CENTIM3-PER-SEC"]


def get_qudt_unit_cubic_decimetre_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Decimetre per Day (http://qudt.org/vocab/unit/DeciM3-PER-DAY)"""
    return QUDT_UNIT["DECIM3-PER-DAY"]


def get_qudt_unit_cubic_decimetre_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Decimetre per Hour (http://qudt.org/vocab/unit/DeciM3-PER-HR)"""
    return QUDT_UNIT["DECIM3-PER-HR"]


def get_qudt_unit_cubic_decimetre_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Decimetre per Minute (http://qudt.org/vocab/unit/DeciM3-PER-MIN)"""
    return QUDT_UNIT["DECIM3-PER-MIN"]


def get_qudt_unit_cubic_decimetre_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Decimetre per Second (http://qudt.org/vocab/unit/DeciM3-PER-SEC)"""
    return QUDT_UNIT["DECIM3-PER-SEC"]


def get_qudt_unit_cubic_foot_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Foot per Day (http://qudt.org/vocab/unit/FT3-PER-DAY)"""
    return QUDT_UNIT["FT3-PER-DAY"]


def get_qudt_unit_cubic_foot_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Foot per Hour (http://qudt.org/vocab/unit/FT3-PER-HR)"""
    return QUDT_UNIT["FT3-PER-HR"]


def get_qudt_unit_cubic_foot_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Foot per Minute (http://qudt.org/vocab/unit/FT3-PER-MIN)"""
    return QUDT_UNIT["FT3-PER-MIN"]


def get_qudt_unit_cubic_foot_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Foot per Second (http://qudt.org/vocab/unit/FT3-PER-SEC)"""
    return QUDT_UNIT["FT3-PER-SEC"]


def get_qudt_unit_gallon_uk_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Gallon (UK) per Day (http://qudt.org/vocab/unit/GAL_UK-PER-DAY)"""
    return QUDT_UNIT["GAL_UK-PER-DAY"]


def get_qudt_unit_gallon_uk_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Gallon (UK) per Hour (http://qudt.org/vocab/unit/GAL_UK-PER-HR)"""
    return QUDT_UNIT["GAL_UK-PER-HR"]


def get_qudt_unit_gallon_uk_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Gallon (UK) per Minute (http://qudt.org/vocab/unit/GAL_UK-PER-MIN)"""
    return QUDT_UNIT["GAL_UK-PER-MIN"]


def get_qudt_unit_gallon_uk_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Gallon (UK) per Second (http://qudt.org/vocab/unit/GAL_UK-PER-SEC)"""
    return QUDT_UNIT["GAL_UK-PER-SEC"]


def get_qudt_unit_us_gallon_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Us Gallon per Day (http://qudt.org/vocab/unit/GAL_US-PER-DAY)"""
    return QUDT_UNIT["GAL_US-PER-DAY"]


def get_qudt_unit_us_gallon_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Us Gallon per Hour (http://qudt.org/vocab/unit/GAL_US-PER-HR)"""
    return QUDT_UNIT["GAL_US-PER-HR"]


def get_qudt_unit_us_gallon_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Us Gallon per Minute (http://qudt.org/vocab/unit/GAL_US-PER-MIN)"""
    return QUDT_UNIT["GAL_US-PER-MIN"]


def get_qudt_unit_us_gallon_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Us Gallon per Second (http://qudt.org/vocab/unit/GAL_US-PER-SEC)"""
    return QUDT_UNIT["GAL_US-PER-SEC"]


def get_qudt_unit_gill_uk_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Gill (UK) per Day (http://qudt.org/vocab/unit/GI_UK-PER-DAY)"""
    return QUDT_UNIT["GI_UK-PER-DAY"]


def get_qudt_unit_gill_uk_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Gill (UK) per Hour (http://qudt.org/vocab/unit/GI_UK-PER-HR)"""
    return QUDT_UNIT["GI_UK-PER-HR"]


def get_qudt_unit_gill_uk_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Gill (UK) per Minute (http://qudt.org/vocab/unit/GI_UK-PER-MIN)"""
    return QUDT_UNIT["GI_UK-PER-MIN"]


def get_qudt_unit_gill_uk_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Gill (UK) per Second (http://qudt.org/vocab/unit/GI_UK-PER-SEC)"""
    return QUDT_UNIT["GI_UK-PER-SEC"]


def get_qudt_unit_gill_us_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Gill (US) per Day (http://qudt.org/vocab/unit/GI_US-PER-DAY)"""
    return QUDT_UNIT["GI_US-PER-DAY"]


def get_qudt_unit_gill_us_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Gill (US) per Hour (http://qudt.org/vocab/unit/GI_US-PER-HR)"""
    return QUDT_UNIT["GI_US-PER-HR"]


def get_qudt_unit_gill_us_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Gill (US) per Minute (http://qudt.org/vocab/unit/GI_US-PER-MIN)"""
    return QUDT_UNIT["GI_US-PER-MIN"]


def get_qudt_unit_gill_us_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Gill (US) per Second (http://qudt.org/vocab/unit/GI_US-PER-SEC)"""
    return QUDT_UNIT["GI_US-PER-SEC"]


def get_qudt_unit_cubic_inch_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Inch per Hour (http://qudt.org/vocab/unit/IN3-PER-HR)"""
    return QUDT_UNIT["IN3-PER-HR"]


def get_qudt_unit_cubic_inch_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Inch per Minute (http://qudt.org/vocab/unit/IN3-PER-MIN)"""
    return QUDT_UNIT["IN3-PER-MIN"]


def get_qudt_unit_cubic_inch_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Inch per Second (http://qudt.org/vocab/unit/IN3-PER-SEC)"""
    return QUDT_UNIT["IN3-PER-SEC"]


def get_qudt_unit_kilolitre_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Kilolitre per Hour (http://qudt.org/vocab/unit/KiloL-PER-HR)"""
    return QUDT_UNIT["KILOL-PER-HR"]


def get_qudt_unit_litre_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Litre per Day (http://qudt.org/vocab/unit/L-PER-DAY)"""
    return QUDT_UNIT["L-PER-DAY"]


def get_qudt_unit_litre_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Litre per Hour (http://qudt.org/vocab/unit/L-PER-HR)"""
    return QUDT_UNIT["L-PER-HR"]


def get_qudt_unit_litre_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Litre per Minute (http://qudt.org/vocab/unit/L-PER-MIN)"""
    return QUDT_UNIT["L-PER-MIN"]


def get_qudt_unit_litre_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Litre per Second (http://qudt.org/vocab/unit/L-PER-SEC)"""
    return QUDT_UNIT["L-PER-SEC"]


def get_qudt_unit_cubic_metre_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Metre per Day (http://qudt.org/vocab/unit/M3-PER-DAY)"""
    return QUDT_UNIT["M3-PER-DAY"]


def get_qudt_unit_cubic_metre_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Metre per Hour (http://qudt.org/vocab/unit/M3-PER-HR)"""
    return QUDT_UNIT["M3-PER-HR"]


def get_qudt_unit_cubic_metre_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Metre per Minute (http://qudt.org/vocab/unit/M3-PER-MIN)"""
    return QUDT_UNIT["M3-PER-MIN"]


def get_qudt_unit_cubic_metre_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Metre per Second (http://qudt.org/vocab/unit/M3-PER-SEC)"""
    return QUDT_UNIT["M3-PER-SEC"]


def get_qudt_unit_cubic_metre_per_year() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Metre per Year (http://qudt.org/vocab/unit/M3-PER-YR)"""
    return QUDT_UNIT["M3-PER-YR"]


def get_qudt_unit_millilitre_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Millilitre per Day (http://qudt.org/vocab/unit/MilliL-PER-DAY)"""
    return QUDT_UNIT["MILLIL-PER-DAY"]


def get_qudt_unit_millilitre_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Millilitre per Hour (http://qudt.org/vocab/unit/MilliL-PER-HR)"""
    return QUDT_UNIT["MILLIL-PER-HR"]


def get_qudt_unit_millilitre_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Millilitre per Minute (http://qudt.org/vocab/unit/MilliL-PER-MIN)"""
    return QUDT_UNIT["MILLIL-PER-MIN"]


def get_qudt_unit_millilitre_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Millilitre per Second (http://qudt.org/vocab/unit/MilliL-PER-SEC)"""
    return QUDT_UNIT["MILLIL-PER-SEC"]


def get_qudt_unit_fluid_ounce_uk_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Fluid Ounce (UK) per Day (http://qudt.org/vocab/unit/OZ_VOL_UK-PER-DAY)"""
    return QUDT_UNIT["OZ_VOL_UK-PER-DAY"]


def get_qudt_unit_fluid_ounce_uk_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Fluid Ounce (UK) per Hour (http://qudt.org/vocab/unit/OZ_VOL_UK-PER-HR)"""
    return QUDT_UNIT["OZ_VOL_UK-PER-HR"]


def get_qudt_unit_fluid_ounce_uk_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Fluid Ounce (UK) per Minute (http://qudt.org/vocab/unit/OZ_VOL_UK-PER-MIN)"""
    return QUDT_UNIT["OZ_VOL_UK-PER-MIN"]


def get_qudt_unit_fluid_ounce_uk_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Fluid Ounce (UK) per Second (http://qudt.org/vocab/unit/OZ_VOL_UK-PER-SEC)"""
    return QUDT_UNIT["OZ_VOL_UK-PER-SEC"]


def get_qudt_unit_us_liquid_ounce_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Us Liquid Ounce per Day (http://qudt.org/vocab/unit/OZ_VOL_US-PER-DAY)"""
    return QUDT_UNIT["OZ_VOL_US-PER-DAY"]


def get_qudt_unit_us_liquid_ounce_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Us Liquid Ounce per Hour (http://qudt.org/vocab/unit/OZ_VOL_US-PER-HR)"""
    return QUDT_UNIT["OZ_VOL_US-PER-HR"]


def get_qudt_unit_us_liquid_ounce_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Us Liquid Ounce per Minute (http://qudt.org/vocab/unit/OZ_VOL_US-PER-MIN)"""
    return QUDT_UNIT["OZ_VOL_US-PER-MIN"]


def get_qudt_unit_us_liquid_ounce_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Us Liquid Ounce per Second (http://qudt.org/vocab/unit/OZ_VOL_US-PER-SEC)"""
    return QUDT_UNIT["OZ_VOL_US-PER-SEC"]


def get_qudt_unit_pint_uk_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Pint (UK) per Day (http://qudt.org/vocab/unit/PINT_UK-PER-DAY)"""
    return QUDT_UNIT["PINT_UK-PER-DAY"]


def get_qudt_unit_pint_uk_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Pint (UK) per Hour (http://qudt.org/vocab/unit/PINT_UK-PER-HR)"""
    return QUDT_UNIT["PINT_UK-PER-HR"]


def get_qudt_unit_pint_uk_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Pint (UK) per Minute (http://qudt.org/vocab/unit/PINT_UK-PER-MIN)"""
    return QUDT_UNIT["PINT_UK-PER-MIN"]


def get_qudt_unit_pint_uk_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Pint (UK) per Second (http://qudt.org/vocab/unit/PINT_UK-PER-SEC)"""
    return QUDT_UNIT["PINT_UK-PER-SEC"]


def get_qudt_unit_us_liquid_pint_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Us Liquid Pint per Day (http://qudt.org/vocab/unit/PINT_US-PER-DAY)"""
    return QUDT_UNIT["PINT_US-PER-DAY"]


def get_qudt_unit_us_liquid_pint_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Us Liquid Pint per Hour (http://qudt.org/vocab/unit/PINT_US-PER-HR)"""
    return QUDT_UNIT["PINT_US-PER-HR"]


def get_qudt_unit_us_liquid_pint_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Us Liquid Pint per Minute (http://qudt.org/vocab/unit/PINT_US-PER-MIN)"""
    return QUDT_UNIT["PINT_US-PER-MIN"]


def get_qudt_unit_us_liquid_pint_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Us Liquid Pint per Second (http://qudt.org/vocab/unit/PINT_US-PER-SEC)"""
    return QUDT_UNIT["PINT_US-PER-SEC"]


def get_qudt_unit_peck_uk_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Peck (UK) per Day (http://qudt.org/vocab/unit/PK_UK-PER-DAY)"""
    return QUDT_UNIT["PK_UK-PER-DAY"]


def get_qudt_unit_peck_uk_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Peck (UK) per Hour (http://qudt.org/vocab/unit/PK_UK-PER-HR)"""
    return QUDT_UNIT["PK_UK-PER-HR"]


def get_qudt_unit_peck_uk_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Peck (UK) per Minute (http://qudt.org/vocab/unit/PK_UK-PER-MIN)"""
    return QUDT_UNIT["PK_UK-PER-MIN"]


def get_qudt_unit_peck_uk_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Peck (UK) per Second (http://qudt.org/vocab/unit/PK_UK-PER-SEC)"""
    return QUDT_UNIT["PK_UK-PER-SEC"]


def get_qudt_unit_us_peck_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Us Peck per Day (http://qudt.org/vocab/unit/PK_US_DRY-PER-DAY)"""
    return QUDT_UNIT["PK_US_DRY-PER-DAY"]


def get_qudt_unit_us_peck_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Us Peck per Hour (http://qudt.org/vocab/unit/PK_US_DRY-PER-HR)"""
    return QUDT_UNIT["PK_US_DRY-PER-HR"]


def get_qudt_unit_us_peck_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Us Peck per Minute (http://qudt.org/vocab/unit/PK_US_DRY-PER-MIN)"""
    return QUDT_UNIT["PK_US_DRY-PER-MIN"]


def get_qudt_unit_us_peck_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Us Peck per Second (http://qudt.org/vocab/unit/PK_US_DRY-PER-SEC)"""
    return QUDT_UNIT["PK_US_DRY-PER-SEC"]


def get_qudt_unit_quart_uk_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Quart (UK) per Day (http://qudt.org/vocab/unit/QT_UK-PER-DAY)"""
    return QUDT_UNIT["QT_UK-PER-DAY"]


def get_qudt_unit_quart_uk_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Quart (UK) per Hour (http://qudt.org/vocab/unit/QT_UK-PER-HR)"""
    return QUDT_UNIT["QT_UK-PER-HR"]


def get_qudt_unit_quart_uk_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Quart (UK) per Minute (http://qudt.org/vocab/unit/QT_UK-PER-MIN)"""
    return QUDT_UNIT["QT_UK-PER-MIN"]


def get_qudt_unit_quart_uk_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Quart (UK) per Second (http://qudt.org/vocab/unit/QT_UK-PER-SEC)"""
    return QUDT_UNIT["QT_UK-PER-SEC"]


def get_qudt_unit_us_liquid_quart_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Us Liquid Quart per Day (http://qudt.org/vocab/unit/QT_US-PER-DAY)"""
    return QUDT_UNIT["QT_US-PER-DAY"]


def get_qudt_unit_us_liquid_quart_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Us Liquid Quart per Hour (http://qudt.org/vocab/unit/QT_US-PER-HR)"""
    return QUDT_UNIT["QT_US-PER-HR"]


def get_qudt_unit_us_liquid_quart_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Us Liquid Quart per Minute (http://qudt.org/vocab/unit/QT_US-PER-MIN)"""
    return QUDT_UNIT["QT_US-PER-MIN"]


def get_qudt_unit_us_liquid_quart_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Us Liquid Quart per Second (http://qudt.org/vocab/unit/QT_US-PER-SEC)"""
    return QUDT_UNIT["QT_US-PER-SEC"]


def get_qudt_unit_cubic_yard_per_day() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Yard per Day (http://qudt.org/vocab/unit/YD3-PER-DAY)"""
    return QUDT_UNIT["YD3-PER-DAY"]


def get_qudt_unit_cubic_yard_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Yard per Hour (http://qudt.org/vocab/unit/YD3-PER-HR)"""
    return QUDT_UNIT["YD3-PER-HR"]


def get_qudt_unit_cubic_yard_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Yard per Minute (http://qudt.org/vocab/unit/YD3-PER-MIN)"""
    return QUDT_UNIT["YD3-PER-MIN"]


def get_qudt_unit_cubic_yard_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Yard per Second (http://qudt.org/vocab/unit/YD3-PER-SEC)"""
    return QUDT_UNIT["YD3-PER-SEC"]


def get_qudt_unit_square_metre_per_mole() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre per Mole (http://qudt.org/vocab/unit/M2-PER-MOL)"""
    return QUDT_UNIT["M2-PER-MOL"]


def get_qudt_unit_siemens_square_metre_per_mole() -> URIRef:
    """Returns the URI for QUDT unit: Siemens Square Metre per Mole (http://qudt.org/vocab/unit/S-M2-PER-MOL)"""
    return QUDT_UNIT["S-M2-PER-MOL"]


def get_qudt_unit_kilomole_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Kilomole per Minute (http://qudt.org/vocab/unit/KiloMOL-PER-MIN)"""
    return QUDT_UNIT["KILOMOL-PER-MIN"]


def get_qudt_unit_kilomole_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Kilomole per Second (http://qudt.org/vocab/unit/KiloMOL-PER-SEC)"""
    return QUDT_UNIT["KILOMOL-PER-SEC"]


def get_qudt_unit_mole_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Mole per Hour (http://qudt.org/vocab/unit/MOL-PER-HR)"""
    return QUDT_UNIT["MOL-PER-HR"]


def get_qudt_unit_mole_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Mole per Minute (http://qudt.org/vocab/unit/MOL-PER-MIN)"""
    return QUDT_UNIT["MOL-PER-MIN"]


def get_qudt_unit_mole_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Mole per Second (http://qudt.org/vocab/unit/MOL-PER-SEC)"""
    return QUDT_UNIT["MOL-PER-SEC"]


def get_qudt_unit_standard_cubic_foot_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Standard Cubic Foot per Hour (http://qudt.org/vocab/unit/SCF-PER-HR)"""
    return QUDT_UNIT["SCF-PER-HR"]


def get_qudt_unit_standard_cubic_foot_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Standard Cubic Foot per Minute (http://qudt.org/vocab/unit/SCF-PER-MIN)"""
    return QUDT_UNIT["SCF-PER-MIN"]


def get_qudt_unit_standard_cubic_metre_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Standard Cubic Metre per Hour (http://qudt.org/vocab/unit/SCM-PER-HR)"""
    return QUDT_UNIT["SCM-PER-HR"]


def get_qudt_unit_standard_cubic_metre_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Standard Cubic Metre per Minute (http://qudt.org/vocab/unit/SCM-PER-MIN)"""
    return QUDT_UNIT["SCM-PER-MIN"]


def get_qudt_unit_millimole_per_square_metre_hour() -> URIRef:
    """Returns the URI for QUDT unit: Millimole per Square Metre Hour (http://qudt.org/vocab/unit/MilliMOL-PER-M2-HR)"""
    return QUDT_UNIT["MILLIMOL-PER-M2-HR"]


def get_qudt_unit_nanomole_per_square_metre_second() -> URIRef:
    """Returns the URI for QUDT unit: Nanomole per Square Metre Second (http://qudt.org/vocab/unit/NanoMOL-PER-M2-SEC)"""
    return QUDT_UNIT["NANOMOL-PER-M2-SEC"]


def get_qudt_unit_square_micromole_per_quartic_metre_square_second() -> URIRef:
    """Returns the URI for QUDT unit: Square Micromole per Quartic Metre Square Second (http://qudt.org/vocab/unit/MicroMOL2-PER-M4-SEC2)"""
    return QUDT_UNIT["MICROMOL2-PER-M4-SEC2"]


def get_qudt_unit_british_thermal_unit_international_definition_per_pound_mole_degree_fahrenheit() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) per Pound Mole Degree Fahrenheit (http://qudt.org/vocab/unit/BTU_IT-PER-MOL_LB-DEG_F)"""
    return QUDT_UNIT["BTU_IT-PER-MOL_LB-DEG_F"]


def get_qudt_unit_kilocalorie_per_mole_degree_celsius() -> URIRef:
    """Returns the URI for QUDT unit: Kilocalorie per Mole Degree Celsius (http://qudt.org/vocab/unit/KiloCAL-PER-MOL-DEG_C)"""
    return QUDT_UNIT["KILOCAL-PER-MOL-DEG_C"]


def get_qudt_unit_gram_per_mole() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Mole (http://qudt.org/vocab/unit/GM-PER-MOL)"""
    return QUDT_UNIT["GM-PER-MOL"]


def get_qudt_unit_kilogram_per_kilomole() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Kilomole (http://qudt.org/vocab/unit/KiloGM-PER-KiloMOL)"""
    return QUDT_UNIT["KILOGM-PER-KILOMOL"]


def get_qudt_unit_radian_square_metre_per_mole() -> URIRef:
    """Returns the URI for QUDT unit: Radian Square Metre per Mole (http://qudt.org/vocab/unit/RAD-M2-PER-MOL)"""
    return QUDT_UNIT["RAD-M2-PER-MOL"]


def get_qudt_unit_cubic_centimetre_per_mole() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Centimetre per Mole (http://qudt.org/vocab/unit/CentiM3-PER-MOL)"""
    return QUDT_UNIT["CENTIM3-PER-MOL"]


def get_qudt_unit_cubic_decimetre_per_mole() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Decimetre per Mole (http://qudt.org/vocab/unit/DeciM3-PER-MOL)"""
    return QUDT_UNIT["DECIM3-PER-MOL"]


def get_qudt_unit_litre_per_mole() -> URIRef:
    """Returns the URI for QUDT unit: Litre per Mole (http://qudt.org/vocab/unit/L-PER-MOL)"""
    return QUDT_UNIT["L-PER-MOL"]


def get_qudt_unit_litre_per_micromole() -> URIRef:
    """Returns the URI for QUDT unit: Litre per Micromole (http://qudt.org/vocab/unit/L-PER-MicroMOL)"""
    return QUDT_UNIT["L-PER-MICROMOL"]


def get_qudt_unit_dalton() -> URIRef:
    """Returns the URI for QUDT unit: Dalton (http://qudt.org/vocab/unit/DA)"""
    return QUDT_UNIT["DA"]


def get_qudt_unit_newton_second_per_radian() -> URIRef:
    """Returns the URI for QUDT unit: Newton Second per Radian (http://qudt.org/vocab/unit/N-SEC-PER-RAD)"""
    return QUDT_UNIT["N-SEC-PER-RAD"]


def get_qudt_unit_cases_per_thousand_individuals_year() -> URIRef:
    """Returns the URI for QUDT unit: Cases per Thousand Individuals Year (http://qudt.org/vocab/unit/CASES-PER-KiloINDIV-YR)"""
    return QUDT_UNIT["CASES-PER-KILOINDIV-YR"]


def get_qudt_unit_deaths_per_thousand_individuals_year() -> URIRef:
    """Returns the URI for QUDT unit: Deaths per Thousand Individuals Year (http://qudt.org/vocab/unit/DEATHS-PER-KiloINDIV-YR)"""
    return QUDT_UNIT["DEATHS-PER-KILOINDIV-YR"]


def get_qudt_unit_deaths_per_million_individuals_year() -> URIRef:
    """Returns the URI for QUDT unit: Deaths per Million Individuals Year (http://qudt.org/vocab/unit/DEATHS-PER-MegaINDIV-YR)"""
    return QUDT_UNIT["DEATHS-PER-MEGAINDIV-YR"]


def get_qudt_unit_minute_per_kilometre() -> URIRef:
    """Returns the URI for QUDT unit: Minute per Kilometre (http://qudt.org/vocab/unit/MIN-PER-KiloM)"""
    return QUDT_UNIT["MIN-PER-KILOM"]


def get_qudt_unit_minute_per_international_mile() -> URIRef:
    """Returns the URI for QUDT unit: Minute per International Mile (http://qudt.org/vocab/unit/MIN-PER-MI)"""
    return QUDT_UNIT["MIN-PER-MI"]


def get_qudt_unit_number_per_hectare() -> URIRef:
    """Returns the URI for QUDT unit: Number per Hectare (http://qudt.org/vocab/unit/NUM-PER-HA)"""
    return QUDT_UNIT["NUM-PER-HA"]


def get_qudt_unit_number_per_square_kilometre() -> URIRef:
    """Returns the URI for QUDT unit: Number per Square Kilometre (http://qudt.org/vocab/unit/NUM-PER-KiloM2)"""
    return QUDT_UNIT["NUM-PER-KILOM2"]


def get_qudt_unit_number_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Number per Square Metre (http://qudt.org/vocab/unit/NUM-PER-M2)"""
    return QUDT_UNIT["NUM-PER-M2"]


def get_qudt_unit_reciprocal_square_inch() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Square Inch (http://qudt.org/vocab/unit/PER-IN2)"""
    return QUDT_UNIT["PER-IN2"]


def get_qudt_unit_reciprocal_metre_nanometre() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Metre Nanometre (http://qudt.org/vocab/unit/PER-M-NanoM)"""
    return QUDT_UNIT["PER-M-NANOM"]


def get_qudt_unit_reciprocal_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Square Metre (http://qudt.org/vocab/unit/PER-M2)"""
    return QUDT_UNIT["PER-M2"]


def get_qudt_unit_reciprocal_cubic_metre_second() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Cubic Metre Second (http://qudt.org/vocab/unit/PER-M3-SEC)"""
    return QUDT_UNIT["PER-M3-SEC"]


def get_qudt_unit_relative_permeability() -> URIRef:
    """Returns the URI for QUDT unit: Relative Permeability (http://qudt.org/vocab/unit/PERMEABILITY_REL)"""
    return QUDT_UNIT["PERMEABILITY_REL"]


def get_qudt_unit_farad_per_kilometre() -> URIRef:
    """Returns the URI for QUDT unit: Farad per Kilometre (http://qudt.org/vocab/unit/FARAD-PER-KiloM)"""
    return QUDT_UNIT["FARAD-PER-KILOM"]


def get_qudt_unit_abfarad_per_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Abfarad per Centimetre (http://qudt.org/vocab/unit/FARAD_Ab-PER-CentiM)"""
    return QUDT_UNIT["FARAD_AB-PER-CENTIM"]


def get_qudt_unit_microfarad_per_kilometre() -> URIRef:
    """Returns the URI for QUDT unit: Microfarad per Kilometre (http://qudt.org/vocab/unit/MicroFARAD-PER-KiloM)"""
    return QUDT_UNIT["MICROFARAD-PER-KILOM"]


def get_qudt_unit_microfarad_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Microfarad per Metre (http://qudt.org/vocab/unit/MicroFARAD-PER-M)"""
    return QUDT_UNIT["MICROFARAD-PER-M"]


def get_qudt_unit_nanofarad_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Nanofarad per Metre (http://qudt.org/vocab/unit/NanoFARAD-PER-M)"""
    return QUDT_UNIT["NANOFARAD-PER-M"]


def get_qudt_unit_picofarad_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Picofarad per Metre (http://qudt.org/vocab/unit/PicoFARAD-PER-M)"""
    return QUDT_UNIT["PICOFARAD-PER-M"]


def get_qudt_unit_reciprocal_second_steradian() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Second Steradian (http://qudt.org/vocab/unit/PER-SEC-SR)"""
    return QUDT_UNIT["PER-SEC-SR"]


def get_qudt_unit_reciprocal_second_square_metre_steradian() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Second Square Metre Steradian (http://qudt.org/vocab/unit/PER-SEC-M2-SR)"""
    return QUDT_UNIT["PER-SEC-M2-SR"]


def get_qudt_unit_micromole_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Micromole per Second (http://qudt.org/vocab/unit/MicroMOL-PER-SEC)"""
    return QUDT_UNIT["MICROMOL-PER-SEC"]


def get_qudt_unit_mole_per_square_metre_day() -> URIRef:
    """Returns the URI for QUDT unit: Mole per Square Metre Day (http://qudt.org/vocab/unit/MOL-PER-M2-DAY)"""
    return QUDT_UNIT["MOL-PER-M2-DAY"]


def get_qudt_unit_mole_per_square_metre_second() -> URIRef:
    """Returns the URI for QUDT unit: Mole per Square Metre Second (http://qudt.org/vocab/unit/MOL-PER-M2-SEC)"""
    return QUDT_UNIT["MOL-PER-M2-SEC"]


def get_qudt_unit_micromole_per_square_metre_day() -> URIRef:
    """Returns the URI for QUDT unit: Micromole per Square Metre Day (http://qudt.org/vocab/unit/MicroMOL-PER-M2-DAY)"""
    return QUDT_UNIT["MICROMOL-PER-M2-DAY"]


def get_qudt_unit_micromole_per_square_metre_hour() -> URIRef:
    """Returns the URI for QUDT unit: Micromole per Square Metre Hour (http://qudt.org/vocab/unit/MicroMOL-PER-M2-HR)"""
    return QUDT_UNIT["MICROMOL-PER-M2-HR"]


def get_qudt_unit_micromole_per_square_metre_second() -> URIRef:
    """Returns the URI for QUDT unit: Micromole per Square Metre Second (http://qudt.org/vocab/unit/MicroMOL-PER-M2-SEC)"""
    return QUDT_UNIT["MICROMOL-PER-M2-SEC"]


def get_qudt_unit_millimole_per_square_metre_day() -> URIRef:
    """Returns the URI for QUDT unit: Millimole per Square Metre Day (http://qudt.org/vocab/unit/MilliMOL-PER-M2-DAY)"""
    return QUDT_UNIT["MILLIMOL-PER-M2-DAY"]


def get_qudt_unit_millimole_per_square_metre_second() -> URIRef:
    """Returns the URI for QUDT unit: Millimole per Square Metre Second (http://qudt.org/vocab/unit/MilliMOL-PER-M2-SEC)"""
    return QUDT_UNIT["MILLIMOL-PER-M2-SEC"]


def get_qudt_unit_nanomole_per_square_metre_day() -> URIRef:
    """Returns the URI for QUDT unit: Nanomole per Square Metre Day (http://qudt.org/vocab/unit/NanoMOL-PER-M2-DAY)"""
    return QUDT_UNIT["NANOMOL-PER-M2-DAY"]


def get_qudt_unit_picomole_per_square_metre_day() -> URIRef:
    """Returns the URI for QUDT unit: Picomole per Square Metre Day (http://qudt.org/vocab/unit/PicoMOL-PER-M2-DAY)"""
    return QUDT_UNIT["PICOMOL-PER-M2-DAY"]


def get_qudt_unit_international_unit_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: International Unit per Litre (http://qudt.org/vocab/unit/IU-PER-L)"""
    return QUDT_UNIT["IU-PER-L"]


def get_qudt_unit_international_unit_per_millilitre() -> URIRef:
    """Returns the URI for QUDT unit: International Unit per Millilitre (http://qudt.org/vocab/unit/IU-PER-MilliL)"""
    return QUDT_UNIT["IU-PER-MILLIL"]


def get_qudt_unit_coulomb_square_metre_per_volt() -> URIRef:
    """Returns the URI for QUDT unit: Coulomb Square Metre per Volt (http://qudt.org/vocab/unit/C-M2-PER-V)"""
    return QUDT_UNIT["C-M2-PER-V"]


def get_qudt_unit_watt_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Watt per Cubic Metre (http://qudt.org/vocab/unit/W-PER-M3)"""
    return QUDT_UNIT["W-PER-M3"]


def get_qudt_unit_millivolt_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Millivolt per Minute (http://qudt.org/vocab/unit/MilliV-PER-MIN)"""
    return QUDT_UNIT["MILLIV-PER-MIN"]


def get_qudt_unit_volt_per_microsecond() -> URIRef:
    """Returns the URI for QUDT unit: Volt per Microsecond (http://qudt.org/vocab/unit/V-PER-MicroSEC)"""
    return QUDT_UNIT["V-PER-MICROSEC"]


def get_qudt_unit_volt_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Volt per Second (http://qudt.org/vocab/unit/V-PER-SEC)"""
    return QUDT_UNIT["V-PER-SEC"]


def get_qudt_unit_bar_per_degree_celsius() -> URIRef:
    """Returns the URI for QUDT unit: Bar per Degree Celsius (http://qudt.org/vocab/unit/BAR-PER-DEG_C)"""
    return QUDT_UNIT["BAR-PER-DEG_C"]


def get_qudt_unit_bar_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Bar per Kelvin (http://qudt.org/vocab/unit/BAR-PER-K)"""
    return QUDT_UNIT["BAR-PER-K"]


def get_qudt_unit_hectopascal_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Hectopascal per Kelvin (http://qudt.org/vocab/unit/HectoPA-PER-K)"""
    return QUDT_UNIT["HECTOPA-PER-K"]


def get_qudt_unit_kilopascal_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Kilopascal per Kelvin (http://qudt.org/vocab/unit/KiloPA-PER-K)"""
    return QUDT_UNIT["KILOPA-PER-K"]


def get_qudt_unit_megapascal_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Megapascal per Kelvin (http://qudt.org/vocab/unit/MegaPA-PER-K)"""
    return QUDT_UNIT["MEGAPA-PER-K"]


def get_qudt_unit_pascal_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Pascal per Kelvin (http://qudt.org/vocab/unit/PA-PER-K)"""
    return QUDT_UNIT["PA-PER-K"]


def get_qudt_unit_standard_atmosphere_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Standard Atmosphere per Metre (http://qudt.org/vocab/unit/ATM-PER-M)"""
    return QUDT_UNIT["ATM-PER-M"]


def get_qudt_unit_technical_atmosphere_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Technical Atmosphere per Metre (http://qudt.org/vocab/unit/ATM_T-PER-M)"""
    return QUDT_UNIT["ATM_T-PER-M"]


def get_qudt_unit_hectopascal_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Hectopascal per Metre (http://qudt.org/vocab/unit/HectoPA-PER-M)"""
    return QUDT_UNIT["HECTOPA-PER-M"]


def get_qudt_unit_kilopascal_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kilopascal per Metre (http://qudt.org/vocab/unit/KiloPA-PER-M)"""
    return QUDT_UNIT["KILOPA-PER-M"]


def get_qudt_unit_millipascal_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Millipascal per Metre (http://qudt.org/vocab/unit/MilliPA-PER-M)"""
    return QUDT_UNIT["MILLIPA-PER-M"]


def get_qudt_unit_psi_per_inch() -> URIRef:
    """Returns the URI for QUDT unit: Psi per Inch (http://qudt.org/vocab/unit/PSI-PER-IN)"""
    return QUDT_UNIT["PSI-PER-IN"]


def get_qudt_unit_torr_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Torr per Metre (http://qudt.org/vocab/unit/TORR-PER-M)"""
    return QUDT_UNIT["TORR-PER-M"]


def get_qudt_unit_dyne_second_per_quintic_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Dyne Second per Quintic Centimetre (http://qudt.org/vocab/unit/DYN-SEC-PER-CentiM5)"""
    return QUDT_UNIT["DYN-SEC-PER-CENTIM5"]


def get_qudt_unit_pascal_second_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: Pascal Second per Litre (http://qudt.org/vocab/unit/PA-SEC-PER-L)"""
    return QUDT_UNIT["PA-SEC-PER-L"]


def get_qudt_unit_pascal_second_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Pascal Second per Cubic Metre (http://qudt.org/vocab/unit/PA-SEC-PER-M3)"""
    return QUDT_UNIT["PA-SEC-PER-M3"]


def get_qudt_unit_kilogram_per_square_metre_square_second() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Square Metre Square Second (http://qudt.org/vocab/unit/KiloGM-PER-M2-SEC2)"""
    return QUDT_UNIT["KILOGM-PER-M2-SEC2"]


def get_qudt_unit_bar_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Bar per Bar (http://qudt.org/vocab/unit/BAR-PER-BAR)"""
    return QUDT_UNIT["BAR-PER-BAR"]


def get_qudt_unit_hectopascal_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Hectopascal per Bar (http://qudt.org/vocab/unit/HectoPA-PER-BAR)"""
    return QUDT_UNIT["HECTOPA-PER-BAR"]


def get_qudt_unit_kilopascal_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Kilopascal per Bar (http://qudt.org/vocab/unit/KiloPA-PER-BAR)"""
    return QUDT_UNIT["KILOPA-PER-BAR"]


def get_qudt_unit_megapascal_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Megapascal per Bar (http://qudt.org/vocab/unit/MegaPA-PER-BAR)"""
    return QUDT_UNIT["MEGAPA-PER-BAR"]


def get_qudt_unit_millibar_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Millibar per Bar (http://qudt.org/vocab/unit/MilliBAR-PER-BAR)"""
    return QUDT_UNIT["MILLIBAR-PER-BAR"]


def get_qudt_unit_pascal_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Pascal per Bar (http://qudt.org/vocab/unit/PA-PER-BAR)"""
    return QUDT_UNIT["PA-PER-BAR"]


def get_qudt_unit_psi_per_psi() -> URIRef:
    """Returns the URI for QUDT unit: Psi per Psi (http://qudt.org/vocab/unit/PSI-PER-PSI)"""
    return QUDT_UNIT["PSI-PER-PSI"]


def get_qudt_unit_watt_per_square_metre_steradian() -> URIRef:
    """Returns the URI for QUDT unit: Watt per Square Metre Steradian (http://qudt.org/vocab/unit/W-PER-M2-SR)"""
    return QUDT_UNIT["W-PER-M2-SR"]


def get_qudt_unit_watt_per_steradian() -> URIRef:
    """Returns the URI for QUDT unit: Watt per Steradian (http://qudt.org/vocab/unit/W-PER-SR)"""
    return QUDT_UNIT["W-PER-SR"]


def get_qudt_unit_percent_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Percent per Second (http://qudt.org/vocab/unit/PERCENT-PER-SEC)"""
    return QUDT_UNIT["PERCENT-PER-SEC"]


def get_qudt_unit_percent_per_week() -> URIRef:
    """Returns the URI for QUDT unit: Percent per Week (http://qudt.org/vocab/unit/PERCENT-PER-WK)"""
    return QUDT_UNIT["PERCENT-PER-WK"]


def get_qudt_unit_percent_per_year() -> URIRef:
    """Returns the URI for QUDT unit: Percent per Year (http://qudt.org/vocab/unit/PERCENT-PER-YR)"""
    return QUDT_UNIT["PERCENT-PER-YR"]


def get_qudt_unit_giga_volt_ampere_reactive() -> URIRef:
    """Returns the URI for QUDT unit: Giga Volt Ampere Reactive (http://qudt.org/vocab/unit/GigaVAR)"""
    return QUDT_UNIT["GIGAVAR"]


def get_qudt_unit_kilo_volt_ampere_reactive() -> URIRef:
    """Returns the URI for QUDT unit: Kilo Volt Ampere Reactive (http://qudt.org/vocab/unit/KiloVAR)"""
    return QUDT_UNIT["KILOVAR"]


def get_qudt_unit_mega_volt_ampere_reactive() -> URIRef:
    """Returns the URI for QUDT unit: Mega Volt Ampere Reactive (http://qudt.org/vocab/unit/MegaVAR)"""
    return QUDT_UNIT["MEGAVAR"]


def get_qudt_unit_micro_volt_ampere_reactive() -> URIRef:
    """Returns the URI for QUDT unit: Micro Volt Ampere Reactive (http://qudt.org/vocab/unit/MicroVAR)"""
    return QUDT_UNIT["MICROVAR"]


def get_qudt_unit_milli_volt_ampere_reactive() -> URIRef:
    """Returns the URI for QUDT unit: Milli Volt Ampere Reactive (http://qudt.org/vocab/unit/MilliVAR)"""
    return QUDT_UNIT["MILLIVAR"]


def get_qudt_unit_nano_volt_ampere_reactive() -> URIRef:
    """Returns the URI for QUDT unit: Nano Volt Ampere Reactive (http://qudt.org/vocab/unit/NanoVAR)"""
    return QUDT_UNIT["NANOVAR"]


def get_qudt_unit_pico_volt_ampere_reactive() -> URIRef:
    """Returns the URI for QUDT unit: Pico Volt Ampere Reactive (http://qudt.org/vocab/unit/PicoVAR)"""
    return QUDT_UNIT["PICOVAR"]


def get_qudt_unit_tera_volt_ampere_reactive() -> URIRef:
    """Returns the URI for QUDT unit: Tera Volt Ampere Reactive (http://qudt.org/vocab/unit/TeraVAR)"""
    return QUDT_UNIT["TERAVAR"]


def get_qudt_unit_volt_ampere_reactive() -> URIRef:
    """Returns the URI for QUDT unit: Volt Ampere Reactive (http://qudt.org/vocab/unit/VAR)"""
    return QUDT_UNIT["VAR"]


def get_qudt_unit_reciprocal_volt() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Volt (http://qudt.org/vocab/unit/PER-V)"""
    return QUDT_UNIT["PER-V"]


def get_qudt_unit_percent_relative_humidity() -> URIRef:
    """Returns the URI for QUDT unit: Percent Relative Humidity (http://qudt.org/vocab/unit/PERCENT_RH)"""
    return QUDT_UNIT["PERCENT_RH"]


def get_qudt_unit_reciprocal_henry() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Henry (http://qudt.org/vocab/unit/PER-H)"""
    return QUDT_UNIT["PER-H"]


def get_qudt_unit_reciprocal_inch() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Inch (http://qudt.org/vocab/unit/PER-IN)"""
    return QUDT_UNIT["PER-IN"]


def get_qudt_unit_percent_per_inch() -> URIRef:
    """Returns the URI for QUDT unit: Percent per Inch (http://qudt.org/vocab/unit/PERCENT-PER-IN)"""
    return QUDT_UNIT["PERCENT-PER-IN"]


def get_qudt_unit_percent_per_millimetre() -> URIRef:
    """Returns the URI for QUDT unit: Percent per Millimetre (http://qudt.org/vocab/unit/PERCENT-PER-MilliM)"""
    return QUDT_UNIT["PERCENT-PER-MILLIM"]


def get_qudt_unit_megaohm_kilometre() -> URIRef:
    """Returns the URI for QUDT unit: Megaohm Kilometre (http://qudt.org/vocab/unit/MegaOHM-KiloM)"""
    return QUDT_UNIT["MEGAOHM-KILOM"]


def get_qudt_unit_ohm_kilometre() -> URIRef:
    """Returns the URI for QUDT unit: Ohm Kilometre (http://qudt.org/vocab/unit/OHM-KiloM)"""
    return QUDT_UNIT["OHM-KILOM"]


def get_qudt_unit_ohm_metre() -> URIRef:
    """Returns the URI for QUDT unit: Ohm Metre (http://qudt.org/vocab/unit/OHM-M)"""
    return QUDT_UNIT["OHM-M"]


def get_qudt_unit_gigaohm() -> URIRef:
    """Returns the URI for QUDT unit: Gigaohm (http://qudt.org/vocab/unit/GigaOHM)"""
    return QUDT_UNIT["GIGAOHM"]


def get_qudt_unit_kiloohm() -> URIRef:
    """Returns the URI for QUDT unit: Kiloohm (http://qudt.org/vocab/unit/KiloOHM)"""
    return QUDT_UNIT["KILOOHM"]


def get_qudt_unit_megaohm() -> URIRef:
    """Returns the URI for QUDT unit: Megaohm (http://qudt.org/vocab/unit/MegaOHM)"""
    return QUDT_UNIT["MEGAOHM"]


def get_qudt_unit_microohm() -> URIRef:
    """Returns the URI for QUDT unit: Microohm (http://qudt.org/vocab/unit/MicroOHM)"""
    return QUDT_UNIT["MICROOHM"]


def get_qudt_unit_milliohm() -> URIRef:
    """Returns the URI for QUDT unit: Milliohm (http://qudt.org/vocab/unit/MilliOHM)"""
    return QUDT_UNIT["MILLIOHM"]


def get_qudt_unit_abohm() -> URIRef:
    """Returns the URI for QUDT unit: Abohm (http://qudt.org/vocab/unit/OHM_Ab)"""
    return QUDT_UNIT["OHM_AB"]


def get_qudt_unit_statohm() -> URIRef:
    """Returns the URI for QUDT unit: Statohm (http://qudt.org/vocab/unit/OHM_Stat)"""
    return QUDT_UNIT["OHM_STAT"]


def get_qudt_unit_planck_impedance() -> URIRef:
    """Returns the URI for QUDT unit: Planck Impedance (http://qudt.org/vocab/unit/PlanckImpedance)"""
    return QUDT_UNIT["PLANCKIMPEDANCE"]


def get_qudt_unit_teraohm() -> URIRef:
    """Returns the URI for QUDT unit: Teraohm (http://qudt.org/vocab/unit/TeraOHM)"""
    return QUDT_UNIT["TERAOHM"]


def get_qudt_unit_gigaohm_metre() -> URIRef:
    """Returns the URI for QUDT unit: Gigaohm Metre (http://qudt.org/vocab/unit/GigaOHM-M)"""
    return QUDT_UNIT["GIGAOHM-M"]


def get_qudt_unit_kiloohm_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kiloohm Metre (http://qudt.org/vocab/unit/KiloOHM-M)"""
    return QUDT_UNIT["KILOOHM-M"]


def get_qudt_unit_megaohm_metre() -> URIRef:
    """Returns the URI for QUDT unit: Megaohm Metre (http://qudt.org/vocab/unit/MegaOHM-M)"""
    return QUDT_UNIT["MEGAOHM-M"]


def get_qudt_unit_microohm_metre() -> URIRef:
    """Returns the URI for QUDT unit: Microohm Metre (http://qudt.org/vocab/unit/MicroOHM-M)"""
    return QUDT_UNIT["MICROOHM-M"]


def get_qudt_unit_milliohm_metre() -> URIRef:
    """Returns the URI for QUDT unit: Milliohm Metre (http://qudt.org/vocab/unit/MilliOHM-M)"""
    return QUDT_UNIT["MILLIOHM-M"]


def get_qudt_unit_nanoohm_metre() -> URIRef:
    """Returns the URI for QUDT unit: Nanoohm Metre (http://qudt.org/vocab/unit/NanoOHM-M)"""
    return QUDT_UNIT["NANOOHM-M"]


def get_qudt_unit_ohm_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Ohm Centimetre (http://qudt.org/vocab/unit/OHM-CentiM)"""
    return QUDT_UNIT["OHM-CENTIM"]


def get_qudt_unit_ohm_square_metre_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Ohm Square Metre per Metre (http://qudt.org/vocab/unit/OHM-M2-PER-M)"""
    return QUDT_UNIT["OHM-M2-PER-M"]


def get_qudt_unit_ohm_circular_mil_per_foot() -> URIRef:
    """Returns the URI for QUDT unit: Ohm Circular Mil per Foot (http://qudt.org/vocab/unit/OHM-MIL_Circ-PER-FT)"""
    return QUDT_UNIT["OHM-MIL_CIRC-PER-FT"]


def get_qudt_unit_breath_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Breath per Minute (http://qudt.org/vocab/unit/BREATH-PER-MIN)"""
    return QUDT_UNIT["BREATH-PER-MIN"]


def get_qudt_unit_ampere_per_square_metre_square_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Ampere per Square Metre Square Kelvin (http://qudt.org/vocab/unit/A-PER-M2-K2)"""
    return QUDT_UNIT["A-PER-M2-K2"]


def get_qudt_unit_inch_per_revolution() -> URIRef:
    """Returns the URI for QUDT unit: Inch per Revolution (http://qudt.org/vocab/unit/IN-PER-REV)"""
    return QUDT_UNIT["IN-PER-REV"]


def get_qudt_unit_metre_per_radian() -> URIRef:
    """Returns the URI for QUDT unit: Metre per Radian (http://qudt.org/vocab/unit/M-PER-RAD)"""
    return QUDT_UNIT["M-PER-RAD"]


def get_qudt_unit_cycle_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Cycle per Second (http://qudt.org/vocab/unit/CYC-PER-SEC)"""
    return QUDT_UNIT["CYC-PER-SEC"]


def get_qudt_unit_revolution_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Revolution per Hour (http://qudt.org/vocab/unit/REV-PER-HR)"""
    return QUDT_UNIT["REV-PER-HR"]


def get_qudt_unit_revolution_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Revolution per Minute (http://qudt.org/vocab/unit/REV-PER-MIN)"""
    return QUDT_UNIT["REV-PER-MIN"]


def get_qudt_unit_revolution_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Revolution per Second (http://qudt.org/vocab/unit/REV-PER-SEC)"""
    return QUDT_UNIT["REV-PER-SEC"]


def get_qudt_unit_newton_metre_per_arcminute() -> URIRef:
    """Returns the URI for QUDT unit: Newton Metre per Arcminute (http://qudt.org/vocab/unit/N-M-PER-ARCMIN)"""
    return QUDT_UNIT["N-M-PER-ARCMIN"]


def get_qudt_unit_newton_metre_per_degree() -> URIRef:
    """Returns the URI for QUDT unit: Newton Metre per Degree (http://qudt.org/vocab/unit/N-M-PER-DEG)"""
    return QUDT_UNIT["N-M-PER-DEG"]


def get_qudt_unit_newton_metre_per_minute_angle() -> URIRef:
    """Returns the URI for QUDT unit: Newton Metre per Minute Angle (http://qudt.org/vocab/unit/N-M-PER-MIN_Angle)"""
    return QUDT_UNIT["N-M-PER-MIN_ANGLE"]


def get_qudt_unit_newton_metre_per_radian() -> URIRef:
    """Returns the URI for QUDT unit: Newton Metre per Radian (http://qudt.org/vocab/unit/N-M-PER-RAD)"""
    return QUDT_UNIT["N-M-PER-RAD"]


def get_qudt_unit_quartic_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Quartic Centimetre (http://qudt.org/vocab/unit/CentiM4)"""
    return QUDT_UNIT["CENTIM4"]


def get_qudt_unit_quartic_foot() -> URIRef:
    """Returns the URI for QUDT unit: Quartic Foot (http://qudt.org/vocab/unit/FT4)"""
    return QUDT_UNIT["FT4"]


def get_qudt_unit_quartic_inch() -> URIRef:
    """Returns the URI for QUDT unit: Quartic Inch (http://qudt.org/vocab/unit/IN4)"""
    return QUDT_UNIT["IN4"]


def get_qudt_unit_quartic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Quartic Metre (http://qudt.org/vocab/unit/M4)"""
    return QUDT_UNIT["M4"]


def get_qudt_unit_quartic_millimetre() -> URIRef:
    """Returns the URI for QUDT unit: Quartic Millimetre (http://qudt.org/vocab/unit/MilliM4)"""
    return QUDT_UNIT["MILLIM4"]


def get_qudt_unit_quintic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Quintic Metre (http://qudt.org/vocab/unit/M5)"""
    return QUDT_UNIT["M5"]


def get_qudt_unit_volt_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Volt per Kelvin (http://qudt.org/vocab/unit/V-PER-K)"""
    return QUDT_UNIT["V-PER-K"]


def get_qudt_unit_decibel_carrier_unit() -> URIRef:
    """Returns the URI for QUDT unit: Decibel Carrier Unit (http://qudt.org/vocab/unit/DeciB_C)"""
    return QUDT_UNIT["DECIB_C"]


def get_qudt_unit_reciprocal_second_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Second Cubic Metre (http://qudt.org/vocab/unit/PER-SEC-M3)"""
    return QUDT_UNIT["PER-SEC-M3"]


def get_qudt_unit_square_degree() -> URIRef:
    """Returns the URI for QUDT unit: Square Degree (http://qudt.org/vocab/unit/DEG2)"""
    return QUDT_UNIT["DEG2"]


def get_qudt_unit_fractional_area() -> URIRef:
    """Returns the URI for QUDT unit: Fractional Area (http://qudt.org/vocab/unit/FA)"""
    return QUDT_UNIT["FA"]


def get_qudt_unit_steradian() -> URIRef:
    """Returns the URI for QUDT unit: Steradian (http://qudt.org/vocab/unit/SR)"""
    return QUDT_UNIT["SR"]


def get_qudt_unit_square_pascal_second() -> URIRef:
    """Returns the URI for QUDT unit: Square Pascal Second (http://qudt.org/vocab/unit/PA2-SEC)"""
    return QUDT_UNIT["PA2-SEC"]


def get_qudt_unit_phon() -> URIRef:
    """Returns the URI for QUDT unit: Phon (http://qudt.org/vocab/unit/PHON)"""
    return QUDT_UNIT["PHON"]


def get_qudt_unit_newton_second_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Newton Second per Cubic Metre (http://qudt.org/vocab/unit/N-SEC-PER-M3)"""
    return QUDT_UNIT["N-SEC-PER-M3"]


def get_qudt_unit_rayl() -> URIRef:
    """Returns the URI for QUDT unit: Rayl (http://qudt.org/vocab/unit/RAYL)"""
    return QUDT_UNIT["RAYL"]


def get_qudt_unit_rayl_mks() -> URIRef:
    """Returns the URI for QUDT unit: Rayl_MKS (http://qudt.org/vocab/unit/RAYL_MKS)"""
    return QUDT_UNIT["RAYL_MKS"]


def get_qudt_unit_microbecquerel_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Microbecquerel per Kilogram (http://qudt.org/vocab/unit/MicroBQ-PER-KiloGM)"""
    return QUDT_UNIT["MICROBQ-PER-KILOGM"]


def get_qudt_unit_millibecquerel_per_gram() -> URIRef:
    """Returns the URI for QUDT unit: Millibecquerel per Gram (http://qudt.org/vocab/unit/MilliBQ-PER-GM)"""
    return QUDT_UNIT["MILLIBQ-PER-GM"]


def get_qudt_unit_millibecquerel_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Millibecquerel per Kilogram (http://qudt.org/vocab/unit/MilliBQ-PER-KiloGM)"""
    return QUDT_UNIT["MILLIBQ-PER-KILOGM"]


def get_qudt_unit_milliampere_hour_per_gram() -> URIRef:
    """Returns the URI for QUDT unit: Milliampere Hour per Gram (http://qudt.org/vocab/unit/MilliA-HR-PER-GM)"""
    return QUDT_UNIT["MILLIA-HR-PER-GM"]


def get_qudt_unit_ampere_per_gram() -> URIRef:
    """Returns the URI for QUDT unit: Ampere per Gram (http://qudt.org/vocab/unit/A-PER-GM)"""
    return QUDT_UNIT["A-PER-GM"]


def get_qudt_unit_joule_per_kilogram_kelvin_pascal() -> URIRef:
    """Returns the URI for QUDT unit: Joule per Kilogram Kelvin Pascal (http://qudt.org/vocab/unit/J-PER-KiloGM-K-PA)"""
    return QUDT_UNIT["J-PER-KILOGM-K-PA"]


def get_qudt_unit_joule_per_kilogram_kelvin_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Joule per Kilogram Kelvin Cubic Metre (http://qudt.org/vocab/unit/J-PER-KiloGM-K-M3)"""
    return QUDT_UNIT["J-PER-KILOGM-K-M3"]


def get_qudt_unit_gigapascal_cubic_centimetre_per_gram() -> URIRef:
    """Returns the URI for QUDT unit: Gigapascal Cubic Centimetre per Gram (http://qudt.org/vocab/unit/GigaPA-CentiM3-PER-GM)"""
    return QUDT_UNIT["GIGAPA-CENTIM3-PER-GM"]


def get_qudt_unit_square_kilometre_per_square_second() -> URIRef:
    """Returns the URI for QUDT unit: Square Kilometre per Square Second (http://qudt.org/vocab/unit/KiloM2-PER-SEC2)"""
    return QUDT_UNIT["KILOM2-PER-SEC2"]


def get_qudt_unit_square_metre_per_square_second() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre per Square Second (http://qudt.org/vocab/unit/M2-PER-SEC2)"""
    return QUDT_UNIT["M2-PER-SEC2"]


def get_qudt_unit_radian_square_metre_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Radian Square Metre per Kilogram (http://qudt.org/vocab/unit/RAD-M2-PER-KiloGM)"""
    return QUDT_UNIT["RAD-M2-PER-KILOGM"]


def get_qudt_unit_imperial_ounce_force_per_cubic_inch() -> URIRef:
    """Returns the URI for QUDT unit: Imperial Ounce Force per Cubic Inch (http://qudt.org/vocab/unit/OZ_F-PER-IN3)"""
    return QUDT_UNIT["OZ_F-PER-IN3"]


def get_qudt_unit_square_centimetre_per_steradian_erg() -> URIRef:
    """Returns the URI for QUDT unit: Square Centimetre per Steradian Erg (http://qudt.org/vocab/unit/CentiM2-PER-SR-ERG)"""
    return QUDT_UNIT["CENTIM2-PER-SR-ERG"]


def get_qudt_unit_square_metre_per_steradian_joule() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre per Steradian Joule (http://qudt.org/vocab/unit/M2-PER-SR-J)"""
    return QUDT_UNIT["M2-PER-SR-J"]


def get_qudt_unit_square_centimetre_per_erg() -> URIRef:
    """Returns the URI for QUDT unit: Square Centimetre per Erg (http://qudt.org/vocab/unit/CentiM2-PER-ERG)"""
    return QUDT_UNIT["CENTIM2-PER-ERG"]


def get_qudt_unit_square_metre_per_joule() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre per Joule (http://qudt.org/vocab/unit/M2-PER-J)"""
    return QUDT_UNIT["M2-PER-J"]


def get_qudt_unit_second_per_cubic_metre_radian() -> URIRef:
    """Returns the URI for QUDT unit: Second per Cubic Metre Radian (http://qudt.org/vocab/unit/SEC-PER-M3-RAD)"""
    return QUDT_UNIT["SEC-PER-M3-RAD"]


def get_qudt_unit_microwatt_per_square_centimetre_micrometre_steradian() -> URIRef:
    """Returns the URI for QUDT unit: Microwatt per Square Centimetre Micrometre Steradian (http://qudt.org/vocab/unit/MicroW-PER-CentiM2-MicroM-SR)"""
    return QUDT_UNIT["MICROW-PER-CENTIM2-MICROM-SR"]


def get_qudt_unit_milliwatt_per_square_metre_nanometre_steradian() -> URIRef:
    """Returns the URI for QUDT unit: Milliwatt per Square Metre Nanometre Steradian (http://qudt.org/vocab/unit/MilliW-PER-M2-NanoM-SR)"""
    return QUDT_UNIT["MILLIW-PER-M2-NANOM-SR"]


def get_qudt_unit_watt_per_square_metre_micrometre() -> URIRef:
    """Returns the URI for QUDT unit: Watt per Square Metre Micrometre (http://qudt.org/vocab/unit/W-PER-M2-MicroM)"""
    return QUDT_UNIT["W-PER-M2-MICROM"]


def get_qudt_unit_watt_per_square_metre_micrometre_steradian() -> URIRef:
    """Returns the URI for QUDT unit: Watt per Square Metre Micrometre Steradian (http://qudt.org/vocab/unit/W-PER-M2-MicroM-SR)"""
    return QUDT_UNIT["W-PER-M2-MICROM-SR"]


def get_qudt_unit_watt_per_square_metre_nanometre_steradian() -> URIRef:
    """Returns the URI for QUDT unit: Watt per Square Metre Nanometre Steradian (http://qudt.org/vocab/unit/W-PER-M2-NanoM-SR)"""
    return QUDT_UNIT["W-PER-M2-NANOM-SR"]


def get_qudt_unit_joule_per_quartic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Joule per Quartic Metre (http://qudt.org/vocab/unit/J-PER-M4)"""
    return QUDT_UNIT["J-PER-M4"]


def get_qudt_unit_kilopascal_per_millimetre() -> URIRef:
    """Returns the URI for QUDT unit: Kilopascal per Millimetre (http://qudt.org/vocab/unit/KiloPA-PER-MilliM)"""
    return QUDT_UNIT["KILOPA-PER-MILLIM"]


def get_qudt_unit_pascal_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Pascal per Metre (http://qudt.org/vocab/unit/PA-PER-M)"""
    return QUDT_UNIT["PA-PER-M"]


def get_qudt_unit_picopascal_per_kilometre() -> URIRef:
    """Returns the URI for QUDT unit: Picopascal per Kilometre (http://qudt.org/vocab/unit/PicoPA-PER-KiloM)"""
    return QUDT_UNIT["PICOPA-PER-KILOM"]


def get_qudt_unit_beaufort() -> URIRef:
    """Returns the URI for QUDT unit: Beaufort (http://qudt.org/vocab/unit/BFT)"""
    return QUDT_UNIT["BFT"]


def get_qudt_unit_cubic_foot_per_minute_square_foot() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Foot per Minute Square Foot (http://qudt.org/vocab/unit/FT3-PER-MIN-FT2)"""
    return QUDT_UNIT["FT3-PER-MIN-FT2"]


def get_qudt_unit_hertz_metre() -> URIRef:
    """Returns the URI for QUDT unit: Hertz Metre (http://qudt.org/vocab/unit/HZ-M)"""
    return QUDT_UNIT["HZ-M"]


def get_qudt_unit_megahertz_metre() -> URIRef:
    """Returns the URI for QUDT unit: Megahertz Metre (http://qudt.org/vocab/unit/MegaHZ-M)"""
    return QUDT_UNIT["MEGAHZ-M"]


def get_qudt_unit_speed_of_light() -> URIRef:
    """Returns the URI for QUDT unit: Speed of Light (http://qudt.org/vocab/unit/SpeedOfLight)"""
    return QUDT_UNIT["SPEEDOFLIGHT"]


def get_qudt_unit_gram_per_centimetre_bar() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Centimetre Bar (http://qudt.org/vocab/unit/GM-PER-CentiM-BAR)"""
    return QUDT_UNIT["GM-PER-CENTIM-BAR"]


def get_qudt_unit_gram_per_millimetre_bar() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Millimetre Bar (http://qudt.org/vocab/unit/GM-PER-MilliM-BAR)"""
    return QUDT_UNIT["GM-PER-MILLIM-BAR"]


def get_qudt_unit_square_second() -> URIRef:
    """Returns the URI for QUDT unit: Square Second (http://qudt.org/vocab/unit/SEC2)"""
    return QUDT_UNIT["SEC2"]


def get_qudt_unit_cubic_kilometre_per_square_second() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Kilometre per Square Second (http://qudt.org/vocab/unit/KiloM3-PER-SEC2)"""
    return QUDT_UNIT["KILOM3-PER-SEC2"]


def get_qudt_unit_cubic_metre_per_square_second() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Metre per Square Second (http://qudt.org/vocab/unit/M3-PER-SEC2)"""
    return QUDT_UNIT["M3-PER-SEC2"]


def get_qudt_unit_megapascal_quintic_placeholder() -> URIRef:
    """Returns the URI for QUDT unit: Megapascal Quintic Placeholder (http://qudt.org/vocab/unit/MegaPA-M0dot5)"""
    return QUDT_UNIT["MEGAPA-M0DOT5"]


def get_qudt_unit_pascal_quintic_placeholder() -> URIRef:
    """Returns the URI for QUDT unit: Pascal Quintic Placeholder (http://qudt.org/vocab/unit/PA-M0dot5)"""
    return QUDT_UNIT["PA-M0DOT5"]


def get_qudt_unit_brewster() -> URIRef:
    """Returns the URI for QUDT unit: Brewster (http://qudt.org/vocab/unit/BREWSTER)"""
    return QUDT_UNIT["BREWSTER"]


def get_qudt_unit_nanometre_per_centimetre_megapascal() -> URIRef:
    """Returns the URI for QUDT unit: Nanometre per Centimetre Megapascal (http://qudt.org/vocab/unit/NanoM-PER-CentiM-MegaPA)"""
    return QUDT_UNIT["NANOM-PER-CENTIM-MEGAPA"]


def get_qudt_unit_nanometre_per_centimetre_psi() -> URIRef:
    """Returns the URI for QUDT unit: Nanometre per Centimetre Psi (http://qudt.org/vocab/unit/NanoM-PER-CentiM-PSI)"""
    return QUDT_UNIT["NANOM-PER-CENTIM-PSI"]


def get_qudt_unit_nanometre_per_millimetre_megapascal() -> URIRef:
    """Returns the URI for QUDT unit: Nanometre per Millimetre Megapascal (http://qudt.org/vocab/unit/NanoM-PER-MilliM-MegaPA)"""
    return QUDT_UNIT["NANOM-PER-MILLIM-MEGAPA"]


def get_qudt_unit_sun_protection_factor() -> URIRef:
    """Returns the URI for QUDT unit: Sun Protection Factor (http://qudt.org/vocab/unit/SPF)"""
    return QUDT_UNIT["SPF"]


def get_qudt_unit_becquerel_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Becquerel per Square Metre (http://qudt.org/vocab/unit/BQ-PER-M2)"""
    return QUDT_UNIT["BQ-PER-M2"]


def get_qudt_unit_cubic_metre_per_hectare_year() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Metre per Hectare Year (http://qudt.org/vocab/unit/M3-PER-HA-YR)"""
    return QUDT_UNIT["M3-PER-HA-YR"]


def get_qudt_unit_cubic_metre_per_second_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Metre per Second Square Metre (http://qudt.org/vocab/unit/M3-PER-SEC-M2)"""
    return QUDT_UNIT["M3-PER-SEC-M2"]


def get_qudt_unit_mole_degree_celsius() -> URIRef:
    """Returns the URI for QUDT unit: Mole Degree Celsius (http://qudt.org/vocab/unit/MOL-DEG_C)"""
    return QUDT_UNIT["MOL-DEG_C"]


def get_qudt_unit_mole_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Mole Kelvin (http://qudt.org/vocab/unit/MOL-K)"""
    return QUDT_UNIT["MOL-K"]


def get_qudt_unit_degree_celsius_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Degree Celsius per Metre (http://qudt.org/vocab/unit/DEG_C-PER-M)"""
    return QUDT_UNIT["DEG_C-PER-M"]


def get_qudt_unit_kelvin_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kelvin per Metre (http://qudt.org/vocab/unit/K-PER-M)"""
    return QUDT_UNIT["K-PER-M"]


def get_qudt_unit_degree_fahrenheit_per_square_second() -> URIRef:
    """Returns the URI for QUDT unit: Degree Fahrenheit per Square Second (http://qudt.org/vocab/unit/DEG_F-PER-SEC2)"""
    return QUDT_UNIT["DEG_F-PER-SEC2"]


def get_qudt_unit_kelvin_per_square_second() -> URIRef:
    """Returns the URI for QUDT unit: Kelvin per Square Second (http://qudt.org/vocab/unit/K-PER-SEC2)"""
    return QUDT_UNIT["K-PER-SEC2"]


def get_qudt_unit_degree_celsius_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Degree Celsius per Hour (http://qudt.org/vocab/unit/DEG_C-PER-HR)"""
    return QUDT_UNIT["DEG_C-PER-HR"]


def get_qudt_unit_degree_celsius_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Degree Celsius per Minute (http://qudt.org/vocab/unit/DEG_C-PER-MIN)"""
    return QUDT_UNIT["DEG_C-PER-MIN"]


def get_qudt_unit_degree_celsius_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Degree Celsius per Second (http://qudt.org/vocab/unit/DEG_C-PER-SEC)"""
    return QUDT_UNIT["DEG_C-PER-SEC"]


def get_qudt_unit_degree_celsius_per_year() -> URIRef:
    """Returns the URI for QUDT unit: Degree Celsius per Year (http://qudt.org/vocab/unit/DEG_C-PER-YR)"""
    return QUDT_UNIT["DEG_C-PER-YR"]


def get_qudt_unit_degree_fahrenheit_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Degree Fahrenheit per Hour (http://qudt.org/vocab/unit/DEG_F-PER-HR)"""
    return QUDT_UNIT["DEG_F-PER-HR"]


def get_qudt_unit_degree_fahrenheit_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Degree Fahrenheit per Minute (http://qudt.org/vocab/unit/DEG_F-PER-MIN)"""
    return QUDT_UNIT["DEG_F-PER-MIN"]


def get_qudt_unit_degree_fahrenheit_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Degree Fahrenheit per Second (http://qudt.org/vocab/unit/DEG_F-PER-SEC)"""
    return QUDT_UNIT["DEG_F-PER-SEC"]


def get_qudt_unit_degree_rankine_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Degree Rankine per Hour (http://qudt.org/vocab/unit/DEG_R-PER-HR)"""
    return QUDT_UNIT["DEG_R-PER-HR"]


def get_qudt_unit_degree_rankine_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Degree Rankine per Minute (http://qudt.org/vocab/unit/DEG_R-PER-MIN)"""
    return QUDT_UNIT["DEG_R-PER-MIN"]


def get_qudt_unit_degree_rankine_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Degree Rankine per Second (http://qudt.org/vocab/unit/DEG_R-PER-SEC)"""
    return QUDT_UNIT["DEG_R-PER-SEC"]


def get_qudt_unit_kelvin_per_hour() -> URIRef:
    """Returns the URI for QUDT unit: Kelvin per Hour (http://qudt.org/vocab/unit/K-PER-HR)"""
    return QUDT_UNIT["K-PER-HR"]


def get_qudt_unit_kelvin_per_minute() -> URIRef:
    """Returns the URI for QUDT unit: Kelvin per Minute (http://qudt.org/vocab/unit/K-PER-MIN)"""
    return QUDT_UNIT["K-PER-MIN"]


def get_qudt_unit_kelvin_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Kelvin per Second (http://qudt.org/vocab/unit/K-PER-SEC)"""
    return QUDT_UNIT["K-PER-SEC"]


def get_qudt_unit_degree_celsius_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Degree Celsius per Kelvin (http://qudt.org/vocab/unit/DEG_C-PER-K)"""
    return QUDT_UNIT["DEG_C-PER-K"]


def get_qudt_unit_degree_fahrenheit_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Degree Fahrenheit per Kelvin (http://qudt.org/vocab/unit/DEG_F-PER-K)"""
    return QUDT_UNIT["DEG_F-PER-K"]


def get_qudt_unit_kelvin_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Kelvin per Kelvin (http://qudt.org/vocab/unit/K-PER-K)"""
    return QUDT_UNIT["K-PER-K"]


def get_qudt_unit_millikelvin_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Millikelvin per Kelvin (http://qudt.org/vocab/unit/MilliK-PER-K)"""
    return QUDT_UNIT["MILLIK-PER-K"]


def get_qudt_unit_square_degree_celsius() -> URIRef:
    """Returns the URI for QUDT unit: Square Degree Celsius (http://qudt.org/vocab/unit/DEG_C2)"""
    return QUDT_UNIT["DEG_C2"]


def get_qudt_unit_british_thermal_unit_thermochemical_definition_per_degree_fahrenheit() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (thermochemical Definition) per Degree Fahrenheit (http://qudt.org/vocab/unit/BTU_TH-PER-DEG_F)"""
    return QUDT_UNIT["BTU_TH-PER-DEG_F"]


def get_qudt_unit_british_thermal_unit_thermochemical_definition_per_degree_rankine() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (thermochemical Definition) per Degree Rankine (http://qudt.org/vocab/unit/BTU_TH-PER-DEG_R)"""
    return QUDT_UNIT["BTU_TH-PER-DEG_R"]


def get_qudt_unit_kilo_volt_ampere_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Kilo Volt Ampere per Kelvin (http://qudt.org/vocab/unit/KiloVA-PER-K)"""
    return QUDT_UNIT["KILOVA-PER-K"]


def get_qudt_unit_micro_volt_ampere_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Micro Volt Ampere per Kelvin (http://qudt.org/vocab/unit/MicroVA-PER-K)"""
    return QUDT_UNIT["MICROVA-PER-K"]


def get_qudt_unit_milli_volt_ampere_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Milli Volt Ampere per Kelvin (http://qudt.org/vocab/unit/MilliVA-PER-K)"""
    return QUDT_UNIT["MILLIVA-PER-K"]


def get_qudt_unit_volt_ampere_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Volt Ampere per Kelvin (http://qudt.org/vocab/unit/VA-PER-K)"""
    return QUDT_UNIT["VA-PER-K"]


def get_qudt_unit_watt_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Watt per Kelvin (http://qudt.org/vocab/unit/W-PER-K)"""
    return QUDT_UNIT["W-PER-K"]


def get_qudt_unit_british_thermal_unit_international_definition_foot_per_square_foot_hour_degree_fahrenheit() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) Foot per Square Foot Hour Degree Fahrenheit (http://qudt.org/vocab/unit/BTU_IT-FT-PER-FT2-HR-DEG_F)"""
    return QUDT_UNIT["BTU_IT-FT-PER-FT2-HR-DEG_F"]


def get_qudt_unit_british_thermal_unit_international_definition_inch_per_square_foot_hour_degree_fahrenheit() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) Inch per Square Foot Hour Degree Fahrenheit (http://qudt.org/vocab/unit/BTU_IT-IN-PER-FT2-HR-DEG_F)"""
    return QUDT_UNIT["BTU_IT-IN-PER-FT2-HR-DEG_F"]


def get_qudt_unit_british_thermal_unit_international_definition_inch_per_square_foot_second_degree_fahrenheit() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) Inch per Square Foot Second Degree Fahrenheit (http://qudt.org/vocab/unit/BTU_IT-IN-PER-FT2-SEC-DEG_F)"""
    return QUDT_UNIT["BTU_IT-IN-PER-FT2-SEC-DEG_F"]


def get_qudt_unit_british_thermal_unit_international_definition_inch_per_hour_square_foot_degree_fahrenheit() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) Inch per Hour Square Foot Degree Fahrenheit (http://qudt.org/vocab/unit/BTU_IT-IN-PER-HR-FT2-DEG_F)"""
    return QUDT_UNIT["BTU_IT-IN-PER-HR-FT2-DEG_F"]


def get_qudt_unit_british_thermal_unit_international_definition_inch_per_second_square_foot_degree_fahrenheit() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) Inch per Second Square Foot Degree Fahrenheit (http://qudt.org/vocab/unit/BTU_IT-IN-PER-SEC-FT2-DEG_F)"""
    return QUDT_UNIT["BTU_IT-IN-PER-SEC-FT2-DEG_F"]


def get_qudt_unit_british_thermal_unit_international_definition_per_second_foot_degree_rankine() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) per Second Foot Degree Rankine (http://qudt.org/vocab/unit/BTU_IT-PER-SEC-FT-DEG_R)"""
    return QUDT_UNIT["BTU_IT-PER-SEC-FT-DEG_R"]


def get_qudt_unit_british_thermal_unit_thermochemical_definition_foot_per_square_foot_hour_degree_fahrenheit() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (thermochemical Definition) Foot per Square Foot Hour Degree Fahrenheit (http://qudt.org/vocab/unit/BTU_TH-FT-PER-FT2-HR-DEG_F)"""
    return QUDT_UNIT["BTU_TH-FT-PER-FT2-HR-DEG_F"]


def get_qudt_unit_british_thermal_unit_thermochemical_definition_foot_per_hour_square_foot_degree_fahrenheit() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (thermochemical Definition) Foot per Hour Square Foot Degree Fahrenheit (http://qudt.org/vocab/unit/BTU_TH-FT-PER-HR-FT2-DEG_F)"""
    return QUDT_UNIT["BTU_TH-FT-PER-HR-FT2-DEG_F"]


def get_qudt_unit_british_thermal_unit_thermochemical_definition_inch_per_square_foot_hour_degree_fahrenheit() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (thermochemical Definition) Inch per Square Foot Hour Degree Fahrenheit (http://qudt.org/vocab/unit/BTU_TH-IN-PER-FT2-HR-DEG_F)"""
    return QUDT_UNIT["BTU_TH-IN-PER-FT2-HR-DEG_F"]


def get_qudt_unit_british_thermal_unit_thermochemical_definition_inch_per_square_foot_second_degree_fahrenheit() -> (
    URIRef
):
    """Returns the URI for QUDT unit: British Thermal Unit (thermochemical Definition) Inch per Square Foot Second Degree Fahrenheit (http://qudt.org/vocab/unit/BTU_TH-IN-PER-FT2-SEC-DEG_F)"""
    return QUDT_UNIT["BTU_TH-IN-PER-FT2-SEC-DEG_F"]


def get_qudt_unit_international_table_calorie_per_second_centimetre_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: International Table Calorie per Second Centimetre Kelvin (http://qudt.org/vocab/unit/CAL_IT-PER-SEC-CentiM-K)"""
    return QUDT_UNIT["CAL_IT-PER-SEC-CENTIM-K"]


def get_qudt_unit_thermochemical_calorie_per_centimetre_second_degree_celsius() -> (
    URIRef
):
    """Returns the URI for QUDT unit: Thermochemical Calorie per Centimetre Second Degree Celsius (http://qudt.org/vocab/unit/CAL_TH-PER-CentiM-SEC-DEG_C)"""
    return QUDT_UNIT["CAL_TH-PER-CENTIM-SEC-DEG_C"]


def get_qudt_unit_thermochemical_calorie_per_second_centimetre_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Thermochemical Calorie per Second Centimetre Kelvin (http://qudt.org/vocab/unit/CAL_TH-PER-SEC-CentiM-K)"""
    return QUDT_UNIT["CAL_TH-PER-SEC-CENTIM-K"]


def get_qudt_unit_kilocalorie_per_centimetre_second_degree_celsius() -> URIRef:
    """Returns the URI for QUDT unit: Kilocalorie per Centimetre Second Degree Celsius (http://qudt.org/vocab/unit/KiloCAL-PER-CentiM-SEC-DEG_C)"""
    return QUDT_UNIT["KILOCAL-PER-CENTIM-SEC-DEG_C"]


def get_qudt_unit_kilo_international_table_calorie_per_hour_metre_degree_celsius() -> (
    URIRef
):
    """Returns the URI for QUDT unit: Kilo International Table Calorie per Hour Metre Degree Celsius (http://qudt.org/vocab/unit/KiloCAL_IT-PER-HR-M-DEG_C)"""
    return QUDT_UNIT["KILOCAL_IT-PER-HR-M-DEG_C"]


def get_qudt_unit_kilowatt_per_metre_degree_celsius() -> URIRef:
    """Returns the URI for QUDT unit: Kilowatt per Metre Degree Celsius (http://qudt.org/vocab/unit/KiloW-PER-M-DEG_C)"""
    return QUDT_UNIT["KILOW-PER-M-DEG_C"]


def get_qudt_unit_kilowatt_per_metre_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Kilowatt per Metre Kelvin (http://qudt.org/vocab/unit/KiloW-PER-M-K)"""
    return QUDT_UNIT["KILOW-PER-M-K"]


def get_qudt_unit_watt_per_metre_degree_celsius() -> URIRef:
    """Returns the URI for QUDT unit: Watt per Metre Degree Celsius (http://qudt.org/vocab/unit/W-PER-M-DEG_C)"""
    return QUDT_UNIT["W-PER-M-DEG_C"]


def get_qudt_unit_watt_per_metre_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Watt per Metre Kelvin (http://qudt.org/vocab/unit/W-PER-M-K)"""
    return QUDT_UNIT["W-PER-M-K"]


def get_qudt_unit_british_thermal_unit_international_definition_foot() -> URIRef:
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) Foot (http://qudt.org/vocab/unit/BTU_IT-FT)"""
    return QUDT_UNIT["BTU_IT-FT"]


def get_qudt_unit_british_thermal_unit_international_definition_inch() -> URIRef:
    """Returns the URI for QUDT unit: British Thermal Unit (international Definition) Inch (http://qudt.org/vocab/unit/BTU_IT-IN)"""
    return QUDT_UNIT["BTU_IT-IN"]


def get_qudt_unit_reciprocal_degree_celsius() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Degree Celsius (http://qudt.org/vocab/unit/PER-DEG_C)"""
    return QUDT_UNIT["PER-DEG_C"]


def get_qudt_unit_percent_per_degree_celsius() -> URIRef:
    """Returns the URI for QUDT unit: Percent per Degree Celsius (http://qudt.org/vocab/unit/PERCENT-PER-DEG_C)"""
    return QUDT_UNIT["PERCENT-PER-DEG_C"]


def get_qudt_unit_clo() -> URIRef:
    """Returns the URI for QUDT unit: Clo (http://qudt.org/vocab/unit/CLO)"""
    return QUDT_UNIT["CLO"]


def get_qudt_unit_degree_fahrenheit_hour_square_foot_per_british_thermal_unit_international_definition() -> (
    URIRef
):
    """Returns the URI for QUDT unit: Degree Fahrenheit Hour Square Foot per British Thermal Unit (international Definition) (http://qudt.org/vocab/unit/DEG_F-HR-FT2-PER-BTU_IT)"""
    return QUDT_UNIT["DEG_F-HR-FT2-PER-BTU_IT"]


def get_qudt_unit_degree_fahrenheit_hour_square_foot_per_british_thermal_unit_thermochemical_definition() -> (
    URIRef
):
    """Returns the URI for QUDT unit: Degree Fahrenheit Hour Square Foot per British Thermal Unit (thermochemical Definition) (http://qudt.org/vocab/unit/DEG_F-HR-FT2-PER-BTU_TH)"""
    return QUDT_UNIT["DEG_F-HR-FT2-PER-BTU_TH"]


def get_qudt_unit_square_foot_hour_degree_fahrenheit_per_british_thermal_unit_international_definition() -> (
    URIRef
):
    """Returns the URI for QUDT unit: Square Foot Hour Degree Fahrenheit per British Thermal Unit (international Definition) (http://qudt.org/vocab/unit/FT2-HR-DEG_F-PER-BTU_IT)"""
    return QUDT_UNIT["FT2-HR-DEG_F-PER-BTU_IT"]


def get_qudt_unit_square_metre_hour_degree_celsius_per_kilo_international_table_calorie() -> (
    URIRef
):
    """Returns the URI for QUDT unit: Square Metre Hour Degree Celsius per Kilo International Table Calorie (http://qudt.org/vocab/unit/M2-HR-DEG_C-PER-KiloCAL_IT)"""
    return QUDT_UNIT["M2-HR-DEG_C-PER-KILOCAL_IT"]


def get_qudt_unit_square_metre_kelvin_per_watt() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre Kelvin per Watt (http://qudt.org/vocab/unit/M2-K-PER-W)"""
    return QUDT_UNIT["M2-K-PER-W"]


def get_qudt_unit_degree_fahrenheit_hour_per_british_thermal_unit_international_definition() -> (
    URIRef
):
    """Returns the URI for QUDT unit: Degree Fahrenheit Hour per British Thermal Unit (international Definition) (http://qudt.org/vocab/unit/DEG_F-HR-PER-BTU_IT)"""
    return QUDT_UNIT["DEG_F-HR-PER-BTU_IT"]


def get_qudt_unit_degree_fahrenheit_hour_per_british_thermal_unit_thermochemical_definition() -> (
    URIRef
):
    """Returns the URI for QUDT unit: Degree Fahrenheit Hour per British Thermal Unit (thermochemical Definition) (http://qudt.org/vocab/unit/DEG_F-HR-PER-BTU_TH)"""
    return QUDT_UNIT["DEG_F-HR-PER-BTU_TH"]


def get_qudt_unit_degree_fahrenheit_second_per_british_thermal_unit_international_definition() -> (
    URIRef
):
    """Returns the URI for QUDT unit: Degree Fahrenheit Second per British Thermal Unit (international Definition) (http://qudt.org/vocab/unit/DEG_F-SEC-PER-BTU_IT)"""
    return QUDT_UNIT["DEG_F-SEC-PER-BTU_IT"]


def get_qudt_unit_degree_fahrenheit_second_per_british_thermal_unit_thermochemical_definition() -> (
    URIRef
):
    """Returns the URI for QUDT unit: Degree Fahrenheit Second per British Thermal Unit (thermochemical Definition) (http://qudt.org/vocab/unit/DEG_F-SEC-PER-BTU_TH)"""
    return QUDT_UNIT["DEG_F-SEC-PER-BTU_TH"]


def get_qudt_unit_kelvin_per_watt() -> URIRef:
    """Returns the URI for QUDT unit: Kelvin per Watt (http://qudt.org/vocab/unit/K-PER-W)"""
    return QUDT_UNIT["K-PER-W"]


def get_qudt_unit_degree_fahrenheit_hour_square_foot_per_british_thermal_unit_international_definition_inch() -> (
    URIRef
):
    """Returns the URI for QUDT unit: Degree Fahrenheit Hour Square Foot per British Thermal Unit (international Definition) Inch (http://qudt.org/vocab/unit/DEG_F-HR-FT2-PER-BTU_IT-IN)"""
    return QUDT_UNIT["DEG_F-HR-FT2-PER-BTU_IT-IN"]


def get_qudt_unit_degree_fahrenheit_hour_square_foot_per_british_thermal_unit_thermochemical_definition_inch() -> (
    URIRef
):
    """Returns the URI for QUDT unit: Degree Fahrenheit Hour Square Foot per British Thermal Unit (thermochemical Definition) Inch (http://qudt.org/vocab/unit/DEG_F-HR-FT2-PER-BTU_TH-IN)"""
    return QUDT_UNIT["DEG_F-HR-FT2-PER-BTU_TH-IN"]


def get_qudt_unit_kelvin_metre_per_watt() -> URIRef:
    """Returns the URI for QUDT unit: Kelvin Metre per Watt (http://qudt.org/vocab/unit/K-M-PER-W)"""
    return QUDT_UNIT["K-M-PER-W"]


def get_qudt_unit_metre_kelvin_per_watt() -> URIRef:
    """Returns the URI for QUDT unit: Metre Kelvin per Watt (http://qudt.org/vocab/unit/M-K-PER-W)"""
    return QUDT_UNIT["M-K-PER-W"]


def get_qudt_unit_pound_force_per_pound_mass() -> URIRef:
    """Returns the URI for QUDT unit: Pound Force per Pound Mass (http://qudt.org/vocab/unit/LB_F-PER-LB)"""
    return QUDT_UNIT["LB_F-PER-LB"]


def get_qudt_unit_newton_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Newton per Kilogram (http://qudt.org/vocab/unit/N-PER-KiloGM)"""
    return QUDT_UNIT["N-PER-KILOGM"]


def get_qudt_unit_pound_mass_per_hour_psi() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Hour Psi (http://qudt.org/vocab/unit/LB-PER-HR-PSI)"""
    return QUDT_UNIT["LB-PER-HR-PSI"]


def get_qudt_unit_pound_mass_per_minute_psi() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Minute Psi (http://qudt.org/vocab/unit/LB-PER-MIN-PSI)"""
    return QUDT_UNIT["LB-PER-MIN-PSI"]


def get_qudt_unit_pound_mass_per_second_psi() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Second Psi (http://qudt.org/vocab/unit/LB-PER-SEC-PSI)"""
    return QUDT_UNIT["LB-PER-SEC-PSI"]


def get_qudt_unit_day_per_number() -> URIRef:
    """Returns the URI for QUDT unit: Day per Number (http://qudt.org/vocab/unit/DAY-PER-NUM)"""
    return QUDT_UNIT["DAY-PER-NUM"]


def get_qudt_unit_hour_per_number() -> URIRef:
    """Returns the URI for QUDT unit: Hour per Number (http://qudt.org/vocab/unit/HR-PER-NUM)"""
    return QUDT_UNIT["HR-PER-NUM"]


def get_qudt_unit_minute_per_number() -> URIRef:
    """Returns the URI for QUDT unit: Minute per Number (http://qudt.org/vocab/unit/MIN-PER-NUM)"""
    return QUDT_UNIT["MIN-PER-NUM"]


def get_qudt_unit_month_per_number() -> URIRef:
    """Returns the URI for QUDT unit: Month per Number (http://qudt.org/vocab/unit/MO-PER-NUM)"""
    return QUDT_UNIT["MO-PER-NUM"]


def get_qudt_unit_second_per_number() -> URIRef:
    """Returns the URI for QUDT unit: Second per Number (http://qudt.org/vocab/unit/SEC-PER-NUM)"""
    return QUDT_UNIT["SEC-PER-NUM"]


def get_qudt_unit_week_per_number() -> URIRef:
    """Returns the URI for QUDT unit: Week per Number (http://qudt.org/vocab/unit/WK-PER-NUM)"""
    return QUDT_UNIT["WK-PER-NUM"]


def get_qudt_unit_year_per_number() -> URIRef:
    """Returns the URI for QUDT unit: Year per Number (http://qudt.org/vocab/unit/YR-PER-NUM)"""
    return QUDT_UNIT["YR-PER-NUM"]


def get_qudt_unit_hour_per_year() -> URIRef:
    """Returns the URI for QUDT unit: Hour per Year (http://qudt.org/vocab/unit/HR-PER-YR)"""
    return QUDT_UNIT["HR-PER-YR"]


def get_qudt_unit_kilonewton_metre_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kilonewton Metre per Metre (http://qudt.org/vocab/unit/KiloN-M-PER-M)"""
    return QUDT_UNIT["KILON-M-PER-M"]


def get_qudt_unit_newton_metre_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Newton Metre per Metre (http://qudt.org/vocab/unit/N-M-PER-M)"""
    return QUDT_UNIT["N-M-PER-M"]


def get_qudt_unit_kilonewton_metre_per_degree() -> URIRef:
    """Returns the URI for QUDT unit: Kilonewton Metre per Degree (http://qudt.org/vocab/unit/KiloN-M-PER-DEG)"""
    return QUDT_UNIT["KILON-M-PER-DEG"]


def get_qudt_unit_electron_volt_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Electron Volt Square Metre (http://qudt.org/vocab/unit/EV-M2)"""
    return QUDT_UNIT["EV-M2"]


def get_qudt_unit_joule_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Joule Square Metre (http://qudt.org/vocab/unit/J-M2)"""
    return QUDT_UNIT["J-M2"]


def get_qudt_unit_erg_per_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Erg per Centimetre (http://qudt.org/vocab/unit/ERG-PER-CentiM)"""
    return QUDT_UNIT["ERG-PER-CENTIM"]


def get_qudt_unit_electron_volt_per_angstrom() -> URIRef:
    """Returns the URI for QUDT unit: Electron Volt per Angstrom (http://qudt.org/vocab/unit/EV-PER-ANGSTROM)"""
    return QUDT_UNIT["EV-PER-ANGSTROM"]


def get_qudt_unit_electron_volt_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Electron Volt per Metre (http://qudt.org/vocab/unit/EV-PER-M)"""
    return QUDT_UNIT["EV-PER-M"]


def get_qudt_unit_erg_square_centimetre_per_gram() -> URIRef:
    """Returns the URI for QUDT unit: Erg Square Centimetre per Gram (http://qudt.org/vocab/unit/ERG-CentiM2-PER-GM)"""
    return QUDT_UNIT["ERG-CENTIM2-PER-GM"]


def get_qudt_unit_electron_volt_square_metre_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Electron Volt Square Metre per Kilogram (http://qudt.org/vocab/unit/EV-M2-PER-KiloGM)"""
    return QUDT_UNIT["EV-M2-PER-KILOGM"]


def get_qudt_unit_joule_square_metre_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Joule Square Metre per Kilogram (http://qudt.org/vocab/unit/J-M2-PER-KiloGM)"""
    return QUDT_UNIT["J-M2-PER-KILOGM"]


def get_qudt_unit_nephelometry_turbidity_unit() -> URIRef:
    """Returns the URI for QUDT unit: Nephelometry Turbidity Unit (http://qudt.org/vocab/unit/NTU)"""
    return QUDT_UNIT["NTU"]


def get_qudt_unit_kilogram_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram Metre (http://qudt.org/vocab/unit/KiloGM-M)"""
    return QUDT_UNIT["KILOGM-M"]


def get_qudt_unit_ampere_hour_per_degree_celsius() -> URIRef:
    """Returns the URI for QUDT unit: Ampere Hour per Degree Celsius (http://qudt.org/vocab/unit/A-HR-PER-DEG_C)"""
    return QUDT_UNIT["A-HR-PER-DEG_C"]


def get_qudt_unit_ampere_per_ampere_hour() -> URIRef:
    """Returns the URI for QUDT unit: Ampere per Ampere Hour (http://qudt.org/vocab/unit/A-PER-A-HR)"""
    return QUDT_UNIT["A-PER-A-HR"]


def get_qudt_unit_ampere_per_pascal() -> URIRef:
    """Returns the URI for QUDT unit: Ampere per Pascal (http://qudt.org/vocab/unit/A-PER-PA)"""
    return QUDT_UNIT["A-PER-PA"]


def get_qudt_unit_ampere_square_second() -> URIRef:
    """Returns the URI for QUDT unit: Ampere Square Second (http://qudt.org/vocab/unit/A-SEC2)"""
    return QUDT_UNIT["A-SEC2"]


def get_qudt_unit_square_ampere_second() -> URIRef:
    """Returns the URI for QUDT unit: Square Ampere Second (http://qudt.org/vocab/unit/A2-SEC)"""
    return QUDT_UNIT["A2-SEC"]


def get_qudt_unit_american_wire_gage() -> URIRef:
    """Returns the URI for QUDT unit: American Wire Gage (http://qudt.org/vocab/unit/AWG)"""
    return QUDT_UNIT["AWG"]


def get_qudt_unit_barn_per_electron_volt() -> URIRef:
    """Returns the URI for QUDT unit: Barn per Electron Volt (http://qudt.org/vocab/unit/BARN-PER-EV)"""
    return QUDT_UNIT["BARN-PER-EV"]


def get_qudt_unit_barn_per_steradian() -> URIRef:
    """Returns the URI for QUDT unit: Barn per Steradian (http://qudt.org/vocab/unit/BARN-PER-SR)"""
    return QUDT_UNIT["BARN-PER-SR"]


def get_qudt_unit_barn_per_steradian_electron_volt() -> URIRef:
    """Returns the URI for QUDT unit: Barn per Steradian Electron Volt (http://qudt.org/vocab/unit/BARN-PER-SR-EV)"""
    return QUDT_UNIT["BARN-PER-SR-EV"]


def get_qudt_unit_coulomb_square_metre_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Coulomb Square Metre per Kilogram (http://qudt.org/vocab/unit/C-M2-PER-KiloGM)"""
    return QUDT_UNIT["C-M2-PER-KILOGM"]


def get_qudt_unit_centimetre_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Centimetre per Bar (http://qudt.org/vocab/unit/CentiM-PER-BAR)"""
    return QUDT_UNIT["CENTIM-PER-BAR"]


def get_qudt_unit_centimetre_per_second_bar() -> URIRef:
    """Returns the URI for QUDT unit: Centimetre per Second Bar (http://qudt.org/vocab/unit/CentiM-PER-SEC-BAR)"""
    return QUDT_UNIT["CENTIM-PER-SEC-BAR"]


def get_qudt_unit_centimetre_per_second_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Centimetre per Second Kelvin (http://qudt.org/vocab/unit/CentiM-PER-SEC-K)"""
    return QUDT_UNIT["CENTIM-PER-SEC-K"]


def get_qudt_unit_square_centimetre_per_cubic_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Square Centimetre per Cubic Centimetre (http://qudt.org/vocab/unit/CentiM2-PER-CentiM3)"""
    return QUDT_UNIT["CENTIM2-PER-CENTIM3"]


def get_qudt_unit_cubic_centimetre_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Centimetre per Bar (http://qudt.org/vocab/unit/CentiM3-PER-BAR)"""
    return QUDT_UNIT["CENTIM3-PER-BAR"]


def get_qudt_unit_cubic_centimetre_per_day_bar() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Centimetre per Day Bar (http://qudt.org/vocab/unit/CentiM3-PER-DAY-BAR)"""
    return QUDT_UNIT["CENTIM3-PER-DAY-BAR"]


def get_qudt_unit_cubic_centimetre_per_day_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Centimetre per Day Kelvin (http://qudt.org/vocab/unit/CentiM3-PER-DAY-K)"""
    return QUDT_UNIT["CENTIM3-PER-DAY-K"]


def get_qudt_unit_cubic_centimetre_per_hour_bar() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Centimetre per Hour Bar (http://qudt.org/vocab/unit/CentiM3-PER-HR-BAR)"""
    return QUDT_UNIT["CENTIM3-PER-HR-BAR"]


def get_qudt_unit_cubic_centimetre_per_hour_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Centimetre per Hour Kelvin (http://qudt.org/vocab/unit/CentiM3-PER-HR-K)"""
    return QUDT_UNIT["CENTIM3-PER-HR-K"]


def get_qudt_unit_cubic_centimetre_per_minute_bar() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Centimetre per Minute Bar (http://qudt.org/vocab/unit/CentiM3-PER-MIN-BAR)"""
    return QUDT_UNIT["CENTIM3-PER-MIN-BAR"]


def get_qudt_unit_cubic_centimetre_per_minute_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Centimetre per Minute Kelvin (http://qudt.org/vocab/unit/CentiM3-PER-MIN-K)"""
    return QUDT_UNIT["CENTIM3-PER-MIN-K"]


def get_qudt_unit_cubic_centimetre_per_second_bar() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Centimetre per Second Bar (http://qudt.org/vocab/unit/CentiM3-PER-SEC-BAR)"""
    return QUDT_UNIT["CENTIM3-PER-SEC-BAR"]


def get_qudt_unit_cubic_centimetre_per_second_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Centimetre per Second Kelvin (http://qudt.org/vocab/unit/CentiM3-PER-SEC-K)"""
    return QUDT_UNIT["CENTIM3-PER-SEC-K"]


def get_qudt_unit_centipoise_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Centipoise per Kelvin (http://qudt.org/vocab/unit/CentiPOISE-PER-K)"""
    return QUDT_UNIT["CENTIPOISE-PER-K"]


def get_qudt_unit_degree_celsius_kilogram_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Degree Celsius Kilogram per Square Metre (http://qudt.org/vocab/unit/DEG_C-KiloGM-PER-M2)"""
    return QUDT_UNIT["DEG_C-KILOGM-PER-M2"]


def get_qudt_unit_degree_celsius_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Degree Celsius per Bar (http://qudt.org/vocab/unit/DEG_C-PER-BAR)"""
    return QUDT_UNIT["DEG_C-PER-BAR"]


def get_qudt_unit_square_degree_celsius_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Square Degree Celsius per Second (http://qudt.org/vocab/unit/DEG_C2-PER-SEC)"""
    return QUDT_UNIT["DEG_C2-PER-SEC"]


def get_qudt_unit_degree_fahrenheit_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Degree Fahrenheit per Bar (http://qudt.org/vocab/unit/DEG_F-PER-BAR)"""
    return QUDT_UNIT["DEG_F-PER-BAR"]


def get_qudt_unit_decibel_milliwatt() -> URIRef:
    """Returns the URI for QUDT unit: Decibel Milliwatt (http://qudt.org/vocab/unit/DeciB-MilliW)"""
    return QUDT_UNIT["DECIB-MILLIW"]


def get_qudt_unit_decibel_milliwatt_per_megahertz() -> URIRef:
    """Returns the URI for QUDT unit: Decibel Milliwatt per Megahertz (http://qudt.org/vocab/unit/DeciB-MilliW-PER-MegaHZ)"""
    return QUDT_UNIT["DECIB-MILLIW-PER-MEGAHZ"]


def get_qudt_unit_decibel_watt() -> URIRef:
    """Returns the URI for QUDT unit: Decibel Watt (http://qudt.org/vocab/unit/DeciB-W)"""
    return QUDT_UNIT["DECIB-W"]


def get_qudt_unit_foot_hour_per_gallon_uk() -> URIRef:
    """Returns the URI for QUDT unit: Foot Hour per Gallon (UK) (http://qudt.org/vocab/unit/FT-HR-PER-GAL_UK)"""
    return QUDT_UNIT["FT-HR-PER-GAL_UK"]


def get_qudt_unit_foot_hour_per_us_gallon() -> URIRef:
    """Returns the URI for QUDT unit: Foot Hour per Us Gallon (http://qudt.org/vocab/unit/FT-HR-PER-GAL_US)"""
    return QUDT_UNIT["FT-HR-PER-GAL_US"]


def get_qudt_unit_foot_hour_per_cubic_inch() -> URIRef:
    """Returns the URI for QUDT unit: Foot Hour per Cubic Inch (http://qudt.org/vocab/unit/FT-HR-PER-IN3)"""
    return QUDT_UNIT["FT-HR-PER-IN3"]


def get_qudt_unit_foot_per_psi() -> URIRef:
    """Returns the URI for QUDT unit: Foot per Psi (http://qudt.org/vocab/unit/FT-PER-PSI)"""
    return QUDT_UNIT["FT-PER-PSI"]


def get_qudt_unit_foot_per_second_degree_fahrenheit() -> URIRef:
    """Returns the URI for QUDT unit: Foot per Second Degree Fahrenheit (http://qudt.org/vocab/unit/FT-PER-SEC-DEG_F)"""
    return QUDT_UNIT["FT-PER-SEC-DEG_F"]


def get_qudt_unit_foot_per_second_psi() -> URIRef:
    """Returns the URI for QUDT unit: Foot per Second Psi (http://qudt.org/vocab/unit/FT-PER-SEC-PSI)"""
    return QUDT_UNIT["FT-PER-SEC-PSI"]


def get_qudt_unit_foot_second_per_gallon_uk() -> URIRef:
    """Returns the URI for QUDT unit: Foot Second per Gallon (UK) (http://qudt.org/vocab/unit/FT-SEC-PER-GAL_UK)"""
    return QUDT_UNIT["FT-SEC-PER-GAL_UK"]


def get_qudt_unit_foot_second_per_us_gallon() -> URIRef:
    """Returns the URI for QUDT unit: Foot Second per Us Gallon (http://qudt.org/vocab/unit/FT-SEC-PER-GAL_US)"""
    return QUDT_UNIT["FT-SEC-PER-GAL_US"]


def get_qudt_unit_foot_second_per_cubic_inch() -> URIRef:
    """Returns the URI for QUDT unit: Foot Second per Cubic Inch (http://qudt.org/vocab/unit/FT-SEC-PER-IN3)"""
    return QUDT_UNIT["FT-SEC-PER-IN3"]


def get_qudt_unit_square_foot_per_british_thermal_unit_international_definition_inch() -> (
    URIRef
):
    """Returns the URI for QUDT unit: Square Foot per British Thermal Unit (international Definition) Inch (http://qudt.org/vocab/unit/FT2-PER-BTU_IT-IN)"""
    return QUDT_UNIT["FT2-PER-BTU_IT-IN"]


def get_qudt_unit_cubic_foot_per_psi() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Foot per Psi (http://qudt.org/vocab/unit/FT3-PER-PSI)"""
    return QUDT_UNIT["FT3-PER-PSI"]


def get_qudt_unit_gram_hour_per_litre_cubic_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Gram Hour per Litre Cubic Centimetre (http://qudt.org/vocab/unit/GM-HR-PER-L-CentiM3)"""
    return QUDT_UNIT["GM-HR-PER-L-CENTIM3"]


def get_qudt_unit_gram_hour_per_litre_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Gram Hour per Litre Cubic Metre (http://qudt.org/vocab/unit/GM-HR-PER-L-M3)"""
    return QUDT_UNIT["GM-HR-PER-L-M3"]


def get_qudt_unit_gram_hour_per_square_litre() -> URIRef:
    """Returns the URI for QUDT unit: Gram Hour per Square Litre (http://qudt.org/vocab/unit/GM-HR-PER-L2)"""
    return QUDT_UNIT["GM-HR-PER-L2"]


def get_qudt_unit_gram_hour_per_cubic_metre_cubic_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Gram Hour per Cubic Metre Cubic Centimetre (http://qudt.org/vocab/unit/GM-HR-PER-M3-CentiM3)"""
    return QUDT_UNIT["GM-HR-PER-M3-CENTIM3"]


def get_qudt_unit_gram_hour_per_cubic_metre_litre() -> URIRef:
    """Returns the URI for QUDT unit: Gram Hour per Cubic Metre Litre (http://qudt.org/vocab/unit/GM-HR-PER-M3-L)"""
    return QUDT_UNIT["GM-HR-PER-M3-L"]


def get_qudt_unit_gram_hour_per_sextic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Gram Hour per Sextic Metre (http://qudt.org/vocab/unit/GM-HR-PER-M6)"""
    return QUDT_UNIT["GM-HR-PER-M6"]


def get_qudt_unit_gram_minute_per_litre_cubic_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Gram Minute per Litre Cubic Centimetre (http://qudt.org/vocab/unit/GM-MIN-PER-L-CentiM3)"""
    return QUDT_UNIT["GM-MIN-PER-L-CENTIM3"]


def get_qudt_unit_gram_minute_per_litre_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Gram Minute per Litre Cubic Metre (http://qudt.org/vocab/unit/GM-MIN-PER-L-M3)"""
    return QUDT_UNIT["GM-MIN-PER-L-M3"]


def get_qudt_unit_gram_minute_per_square_litre() -> URIRef:
    """Returns the URI for QUDT unit: Gram Minute per Square Litre (http://qudt.org/vocab/unit/GM-MIN-PER-L2)"""
    return QUDT_UNIT["GM-MIN-PER-L2"]


def get_qudt_unit_gram_minute_per_cubic_metre_cubic_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Gram Minute per Cubic Metre Cubic Centimetre (http://qudt.org/vocab/unit/GM-MIN-PER-M3-CentiM3)"""
    return QUDT_UNIT["GM-MIN-PER-M3-CENTIM3"]


def get_qudt_unit_gram_minute_per_cubic_metre_litre() -> URIRef:
    """Returns the URI for QUDT unit: Gram Minute per Cubic Metre Litre (http://qudt.org/vocab/unit/GM-MIN-PER-M3-L)"""
    return QUDT_UNIT["GM-MIN-PER-M3-L"]


def get_qudt_unit_gram_minute_per_sextic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Gram Minute per Sextic Metre (http://qudt.org/vocab/unit/GM-MIN-PER-M6)"""
    return QUDT_UNIT["GM-MIN-PER-M6"]


def get_qudt_unit_gram_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Bar (http://qudt.org/vocab/unit/GM-PER-BAR)"""
    return QUDT_UNIT["GM-PER-BAR"]


def get_qudt_unit_gram_per_cubic_centimetre_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Cubic Centimetre Kelvin (http://qudt.org/vocab/unit/GM-PER-CentiM3-K)"""
    return QUDT_UNIT["GM-PER-CENTIM3-K"]


def get_qudt_unit_gram_per_day_bar() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Day Bar (http://qudt.org/vocab/unit/GM-PER-DAY-BAR)"""
    return QUDT_UNIT["GM-PER-DAY-BAR"]


def get_qudt_unit_gram_per_day_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Day Kelvin (http://qudt.org/vocab/unit/GM-PER-DAY-K)"""
    return QUDT_UNIT["GM-PER-DAY-K"]


def get_qudt_unit_gram_per_degree_celsius() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Degree Celsius (http://qudt.org/vocab/unit/GM-PER-DEG_C)"""
    return QUDT_UNIT["GM-PER-DEG_C"]


def get_qudt_unit_gram_per_cubic_decimetre_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Cubic Decimetre Kelvin (http://qudt.org/vocab/unit/GM-PER-DeciM3-K)"""
    return QUDT_UNIT["GM-PER-DECIM3-K"]


def get_qudt_unit_gram_per_hour_bar() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Hour Bar (http://qudt.org/vocab/unit/GM-PER-HR-BAR)"""
    return QUDT_UNIT["GM-PER-HR-BAR"]


def get_qudt_unit_gram_per_hour_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Hour Kelvin (http://qudt.org/vocab/unit/GM-PER-HR-K)"""
    return QUDT_UNIT["GM-PER-HR-K"]


def get_qudt_unit_gram_per_hertz() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Hertz (http://qudt.org/vocab/unit/GM-PER-HZ)"""
    return QUDT_UNIT["GM-PER-HZ"]


def get_qudt_unit_gram_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Kelvin (http://qudt.org/vocab/unit/GM-PER-K)"""
    return QUDT_UNIT["GM-PER-K"]


def get_qudt_unit_gram_per_litre_centipoise() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Litre Centipoise (http://qudt.org/vocab/unit/GM-PER-L-CentiPOISE)"""
    return QUDT_UNIT["GM-PER-L-CENTIPOISE"]


def get_qudt_unit_gram_per_litre_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Litre Kelvin (http://qudt.org/vocab/unit/GM-PER-L-K)"""
    return QUDT_UNIT["GM-PER-L-K"]


def get_qudt_unit_gram_per_litre_millipascal_second() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Litre Millipascal Second (http://qudt.org/vocab/unit/GM-PER-L-MilliPA-SEC)"""
    return QUDT_UNIT["GM-PER-L-MILLIPA-SEC"]


def get_qudt_unit_gram_per_litre_pascal_second() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Litre Pascal Second (http://qudt.org/vocab/unit/GM-PER-L-PA-SEC)"""
    return QUDT_UNIT["GM-PER-L-PA-SEC"]


def get_qudt_unit_gram_per_litre_poise() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Litre Poise (http://qudt.org/vocab/unit/GM-PER-L-POISE)"""
    return QUDT_UNIT["GM-PER-L-POISE"]


def get_qudt_unit_gram_per_cubic_metre_centipoise() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Cubic Metre Centipoise (http://qudt.org/vocab/unit/GM-PER-M3-CentiPOISE)"""
    return QUDT_UNIT["GM-PER-M3-CENTIPOISE"]


def get_qudt_unit_gram_per_cubic_metre_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Cubic Metre Kelvin (http://qudt.org/vocab/unit/GM-PER-M3-K)"""
    return QUDT_UNIT["GM-PER-M3-K"]


def get_qudt_unit_gram_per_cubic_metre_millipascal_second() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Cubic Metre Millipascal Second (http://qudt.org/vocab/unit/GM-PER-M3-MilliPA-SEC)"""
    return QUDT_UNIT["GM-PER-M3-MILLIPA-SEC"]


def get_qudt_unit_gram_per_cubic_metre_pascal_second() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Cubic Metre Pascal Second (http://qudt.org/vocab/unit/GM-PER-M3-PA-SEC)"""
    return QUDT_UNIT["GM-PER-M3-PA-SEC"]


def get_qudt_unit_gram_per_cubic_metre_poise() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Cubic Metre Poise (http://qudt.org/vocab/unit/GM-PER-M3-POISE)"""
    return QUDT_UNIT["GM-PER-M3-POISE"]


def get_qudt_unit_gram_per_minute_bar() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Minute Bar (http://qudt.org/vocab/unit/GM-PER-MIN-BAR)"""
    return QUDT_UNIT["GM-PER-MIN-BAR"]


def get_qudt_unit_gram_per_minute_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Minute Kelvin (http://qudt.org/vocab/unit/GM-PER-MIN-K)"""
    return QUDT_UNIT["GM-PER-MIN-K"]


def get_qudt_unit_gram_per_millilitre_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Millilitre Kelvin (http://qudt.org/vocab/unit/GM-PER-MilliL-K)"""
    return QUDT_UNIT["GM-PER-MILLIL-K"]


def get_qudt_unit_gram_per_second_bar() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Second Bar (http://qudt.org/vocab/unit/GM-PER-SEC-BAR)"""
    return QUDT_UNIT["GM-PER-SEC-BAR"]


def get_qudt_unit_gram_per_second_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Gram per Second Kelvin (http://qudt.org/vocab/unit/GM-PER-SEC-K)"""
    return QUDT_UNIT["GM-PER-SEC-K"]


def get_qudt_unit_gram_second_per_litre_cubic_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Gram Second per Litre Cubic Centimetre (http://qudt.org/vocab/unit/GM-SEC-PER-L-CentiM3)"""
    return QUDT_UNIT["GM-SEC-PER-L-CENTIM3"]


def get_qudt_unit_gram_second_per_litre_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Gram Second per Litre Cubic Metre (http://qudt.org/vocab/unit/GM-SEC-PER-L-M3)"""
    return QUDT_UNIT["GM-SEC-PER-L-M3"]


def get_qudt_unit_gram_second_per_square_litre() -> URIRef:
    """Returns the URI for QUDT unit: Gram Second per Square Litre (http://qudt.org/vocab/unit/GM-SEC-PER-L2)"""
    return QUDT_UNIT["GM-SEC-PER-L2"]


def get_qudt_unit_gram_second_per_cubic_metre_cubic_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Gram Second per Cubic Metre Cubic Centimetre (http://qudt.org/vocab/unit/GM-SEC-PER-M3-CentiM3)"""
    return QUDT_UNIT["GM-SEC-PER-M3-CENTIM3"]


def get_qudt_unit_gram_second_per_cubic_metre_litre() -> URIRef:
    """Returns the URI for QUDT unit: Gram Second per Cubic Metre Litre (http://qudt.org/vocab/unit/GM-SEC-PER-M3-L)"""
    return QUDT_UNIT["GM-SEC-PER-M3-L"]


def get_qudt_unit_gram_second_per_sextic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Gram Second per Sextic Metre (http://qudt.org/vocab/unit/GM-SEC-PER-M6)"""
    return QUDT_UNIT["GM-SEC-PER-M6"]


def get_qudt_unit_hour_per_square_foot() -> URIRef:
    """Returns the URI for QUDT unit: Hour per Square Foot (http://qudt.org/vocab/unit/HR-PER-FT2)"""
    return QUDT_UNIT["HR-PER-FT2"]


def get_qudt_unit_inch_per_psi() -> URIRef:
    """Returns the URI for QUDT unit: Inch per Psi (http://qudt.org/vocab/unit/IN-PER-PSI)"""
    return QUDT_UNIT["IN-PER-PSI"]


def get_qudt_unit_inch_per_second_degree_fahrenheit() -> URIRef:
    """Returns the URI for QUDT unit: Inch per Second Degree Fahrenheit (http://qudt.org/vocab/unit/IN-PER-SEC-DEG_F)"""
    return QUDT_UNIT["IN-PER-SEC-DEG_F"]


def get_qudt_unit_inch_per_second_psi() -> URIRef:
    """Returns the URI for QUDT unit: Inch per Second Psi (http://qudt.org/vocab/unit/IN-PER-SEC-PSI)"""
    return QUDT_UNIT["IN-PER-SEC-PSI"]


def get_qudt_unit_kelvin_metre_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Kelvin Metre per Second (http://qudt.org/vocab/unit/K-M-PER-SEC)"""
    return QUDT_UNIT["K-M-PER-SEC"]


def get_qudt_unit_kelvin_square_metre_per_kilogram_second() -> URIRef:
    """Returns the URI for QUDT unit: Kelvin Square Metre per Kilogram Second (http://qudt.org/vocab/unit/K-M2-PER-KiloGM-SEC)"""
    return QUDT_UNIT["K-M2-PER-KILOGM-SEC"]


def get_qudt_unit_kelvin_pascal_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Kelvin Pascal per Second (http://qudt.org/vocab/unit/K-PA-PER-SEC)"""
    return QUDT_UNIT["K-PA-PER-SEC"]


def get_qudt_unit_kelvin_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Kelvin per Bar (http://qudt.org/vocab/unit/K-PER-BAR)"""
    return QUDT_UNIT["K-PER-BAR"]


def get_qudt_unit_kelvin_per_pascal() -> URIRef:
    """Returns the URI for QUDT unit: Kelvin per Pascal (http://qudt.org/vocab/unit/K-PER-PA)"""
    return QUDT_UNIT["K-PER-PA"]


def get_qudt_unit_square_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Square Kelvin (http://qudt.org/vocab/unit/K2)"""
    return QUDT_UNIT["K2"]


def get_qudt_unit_kilogram_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Bar (http://qudt.org/vocab/unit/KiloGM-PER-BAR)"""
    return QUDT_UNIT["KILOGM-PER-BAR"]


def get_qudt_unit_kilogram_per_cubic_centimetre_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Cubic Centimetre Kelvin (http://qudt.org/vocab/unit/KiloGM-PER-CentiM3-K)"""
    return QUDT_UNIT["KILOGM-PER-CENTIM3-K"]


def get_qudt_unit_kilogram_per_day_bar() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Day Bar (http://qudt.org/vocab/unit/KiloGM-PER-DAY-BAR)"""
    return QUDT_UNIT["KILOGM-PER-DAY-BAR"]


def get_qudt_unit_kilogram_per_day_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Day Kelvin (http://qudt.org/vocab/unit/KiloGM-PER-DAY-K)"""
    return QUDT_UNIT["KILOGM-PER-DAY-K"]


def get_qudt_unit_kilogram_per_cubic_decimetre_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Cubic Decimetre Kelvin (http://qudt.org/vocab/unit/KiloGM-PER-DeciM3-K)"""
    return QUDT_UNIT["KILOGM-PER-DECIM3-K"]


def get_qudt_unit_kilogram_per_hour_bar() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Hour Bar (http://qudt.org/vocab/unit/KiloGM-PER-HR-BAR)"""
    return QUDT_UNIT["KILOGM-PER-HR-BAR"]


def get_qudt_unit_kilogram_per_hour_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Hour Kelvin (http://qudt.org/vocab/unit/KiloGM-PER-HR-K)"""
    return QUDT_UNIT["KILOGM-PER-HR-K"]


def get_qudt_unit_kilogram_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Kelvin (http://qudt.org/vocab/unit/KiloGM-PER-K)"""
    return QUDT_UNIT["KILOGM-PER-K"]


def get_qudt_unit_kilogram_per_litre_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Litre Kelvin (http://qudt.org/vocab/unit/KiloGM-PER-L-K)"""
    return QUDT_UNIT["KILOGM-PER-L-K"]


def get_qudt_unit_kilogram_per_cubic_metre_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Cubic Metre Kelvin (http://qudt.org/vocab/unit/KiloGM-PER-M3-K)"""
    return QUDT_UNIT["KILOGM-PER-M3-K"]


def get_qudt_unit_kilogram_per_cubic_metre_second() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Cubic Metre Second (http://qudt.org/vocab/unit/KiloGM-PER-M3-SEC)"""
    return QUDT_UNIT["KILOGM-PER-M3-SEC"]


def get_qudt_unit_kilogram_per_minute_bar() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Minute Bar (http://qudt.org/vocab/unit/KiloGM-PER-MIN-BAR)"""
    return QUDT_UNIT["KILOGM-PER-MIN-BAR"]


def get_qudt_unit_kilogram_per_minute_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Minute Kelvin (http://qudt.org/vocab/unit/KiloGM-PER-MIN-K)"""
    return QUDT_UNIT["KILOGM-PER-MIN-K"]


def get_qudt_unit_kilogram_per_pascal() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Pascal (http://qudt.org/vocab/unit/KiloGM-PER-PA)"""
    return QUDT_UNIT["KILOGM-PER-PA"]


def get_qudt_unit_kilogram_per_second_bar() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Second Bar (http://qudt.org/vocab/unit/KiloGM-PER-SEC-BAR)"""
    return QUDT_UNIT["KILOGM-PER-SEC-BAR"]


def get_qudt_unit_kilogram_per_second_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Second Kelvin (http://qudt.org/vocab/unit/KiloGM-PER-SEC-K)"""
    return QUDT_UNIT["KILOGM-PER-SEC-K"]


def get_qudt_unit_kilogram_per_second_pascal() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Second Pascal (http://qudt.org/vocab/unit/KiloGM-PER-SEC-PA)"""
    return QUDT_UNIT["KILOGM-PER-SEC-PA"]


def get_qudt_unit_kilogram_square_second() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram Square Second (http://qudt.org/vocab/unit/KiloGM-SEC2)"""
    return QUDT_UNIT["KILOGM-SEC2"]


def get_qudt_unit_square_kilogram_per_square_second() -> URIRef:
    """Returns the URI for QUDT unit: Square Kilogram per Square Second (http://qudt.org/vocab/unit/KiloGM2-PER-SEC2)"""
    return QUDT_UNIT["KILOGM2-PER-SEC2"]


def get_qudt_unit_kilometre_per_second_bar() -> URIRef:
    """Returns the URI for QUDT unit: Kilometre per Second Bar (http://qudt.org/vocab/unit/KiloM-PER-SEC-BAR)"""
    return QUDT_UNIT["KILOM-PER-SEC-BAR"]


def get_qudt_unit_kilomole_per_cubic_metre_bar() -> URIRef:
    """Returns the URI for QUDT unit: Kilomole per Cubic Metre Bar (http://qudt.org/vocab/unit/KiloMOL-PER-M3-BAR)"""
    return QUDT_UNIT["KILOMOL-PER-M3-BAR"]


def get_qudt_unit_kilomole_per_cubic_metre_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Kilomole per Cubic Metre Kelvin (http://qudt.org/vocab/unit/KiloMOL-PER-M3-K)"""
    return QUDT_UNIT["KILOMOL-PER-M3-K"]


def get_qudt_unit_kiloohm_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Kiloohm per Bar (http://qudt.org/vocab/unit/KiloOHM-PER-BAR)"""
    return QUDT_UNIT["KILOOHM-PER-BAR"]


def get_qudt_unit_kiloohm_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Kiloohm per Kelvin (http://qudt.org/vocab/unit/KiloOHM-PER-K)"""
    return QUDT_UNIT["KILOOHM-PER-K"]


def get_qudt_unit_kilo_volt_ampere_reactive_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Kilo Volt Ampere Reactive per Kelvin (http://qudt.org/vocab/unit/KiloVAR-PER-K)"""
    return QUDT_UNIT["KILOVAR-PER-K"]


def get_qudt_unit_litre_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Litre per Bar (http://qudt.org/vocab/unit/L-PER-BAR)"""
    return QUDT_UNIT["L-PER-BAR"]


def get_qudt_unit_litre_per_day_bar() -> URIRef:
    """Returns the URI for QUDT unit: Litre per Day Bar (http://qudt.org/vocab/unit/L-PER-DAY-BAR)"""
    return QUDT_UNIT["L-PER-DAY-BAR"]


def get_qudt_unit_litre_per_day_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Litre per Day Kelvin (http://qudt.org/vocab/unit/L-PER-DAY-K)"""
    return QUDT_UNIT["L-PER-DAY-K"]


def get_qudt_unit_litre_per_hour_bar() -> URIRef:
    """Returns the URI for QUDT unit: Litre per Hour Bar (http://qudt.org/vocab/unit/L-PER-HR-BAR)"""
    return QUDT_UNIT["L-PER-HR-BAR"]


def get_qudt_unit_litre_per_hour_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Litre per Hour Kelvin (http://qudt.org/vocab/unit/L-PER-HR-K)"""
    return QUDT_UNIT["L-PER-HR-K"]


def get_qudt_unit_litre_per_minute_bar() -> URIRef:
    """Returns the URI for QUDT unit: Litre per Minute Bar (http://qudt.org/vocab/unit/L-PER-MIN-BAR)"""
    return QUDT_UNIT["L-PER-MIN-BAR"]


def get_qudt_unit_litre_per_minute_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Litre per Minute Kelvin (http://qudt.org/vocab/unit/L-PER-MIN-K)"""
    return QUDT_UNIT["L-PER-MIN-K"]


def get_qudt_unit_litre_per_second_bar() -> URIRef:
    """Returns the URI for QUDT unit: Litre per Second Bar (http://qudt.org/vocab/unit/L-PER-SEC-BAR)"""
    return QUDT_UNIT["L-PER-SEC-BAR"]


def get_qudt_unit_litre_per_second_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Litre per Second Kelvin (http://qudt.org/vocab/unit/L-PER-SEC-K)"""
    return QUDT_UNIT["L-PER-SEC-K"]


def get_qudt_unit_pound_mass_square_foot_per_gallon_uk_pound_force_second() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Square Foot per Gallon (UK) Pound Force Second (http://qudt.org/vocab/unit/LB-FT2-PER-GAL_UK-LB_F-SEC)"""
    return QUDT_UNIT["LB-FT2-PER-GAL_UK-LB_F-SEC"]


def get_qudt_unit_pound_mass_square_foot_per_us_gallon_pound_force_second() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Square Foot per Us Gallon Pound Force Second (http://qudt.org/vocab/unit/LB-FT2-PER-GAL_US-LB_F-SEC)"""
    return QUDT_UNIT["LB-FT2-PER-GAL_US-LB_F-SEC"]


def get_qudt_unit_pound_mass_square_foot_per_cubic_inch_pound_force_second() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Square Foot per Cubic Inch Pound Force Second (http://qudt.org/vocab/unit/LB-FT2-PER-IN3-LB_F-SEC)"""
    return QUDT_UNIT["LB-FT2-PER-IN3-LB_F-SEC"]


def get_qudt_unit_pound_mass_hour_per_cubic_foot_gallon_uk() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Hour per Cubic Foot Gallon (UK) (http://qudt.org/vocab/unit/LB-HR-PER-FT3-GAL_UK)"""
    return QUDT_UNIT["LB-HR-PER-FT3-GAL_UK"]


def get_qudt_unit_pound_mass_hour_per_cubic_foot_us_gallon() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Hour per Cubic Foot Us Gallon (http://qudt.org/vocab/unit/LB-HR-PER-FT3-GAL_US)"""
    return QUDT_UNIT["LB-HR-PER-FT3-GAL_US"]


def get_qudt_unit_pound_mass_hour_per_cubic_foot_cubic_inch() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Hour per Cubic Foot Cubic Inch (http://qudt.org/vocab/unit/LB-HR-PER-FT3-IN3)"""
    return QUDT_UNIT["LB-HR-PER-FT3-IN3"]


def get_qudt_unit_pound_mass_hour_per_cubic_foot_cubic_yard() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Hour per Cubic Foot Cubic Yard (http://qudt.org/vocab/unit/LB-HR-PER-FT3-YD3)"""
    return QUDT_UNIT["LB-HR-PER-FT3-YD3"]


def get_qudt_unit_pound_mass_hour_per_sextic_foot() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Hour per Sextic Foot (http://qudt.org/vocab/unit/LB-HR-PER-FT6)"""
    return QUDT_UNIT["LB-HR-PER-FT6"]


def get_qudt_unit_pound_mass_hour_per_gallon_uk_cubic_foot() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Hour per Gallon (UK) Cubic Foot (http://qudt.org/vocab/unit/LB-HR-PER-GAL_UK-FT3)"""
    return QUDT_UNIT["LB-HR-PER-GAL_UK-FT3"]


def get_qudt_unit_pound_mass_hour_per_gallon_uk_cubic_inch() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Hour per Gallon (UK) Cubic Inch (http://qudt.org/vocab/unit/LB-HR-PER-GAL_UK-IN3)"""
    return QUDT_UNIT["LB-HR-PER-GAL_UK-IN3"]


def get_qudt_unit_pound_mass_hour_per_gallon_uk_cubic_yard() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Hour per Gallon (UK) Cubic Yard (http://qudt.org/vocab/unit/LB-HR-PER-GAL_UK-YD3)"""
    return QUDT_UNIT["LB-HR-PER-GAL_UK-YD3"]


def get_qudt_unit_pound_mass_hour_per_square_gallon_uk() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Hour per Square Gallon (UK) (http://qudt.org/vocab/unit/LB-HR-PER-GAL_UK2)"""
    return QUDT_UNIT["LB-HR-PER-GAL_UK2"]


def get_qudt_unit_pound_mass_hour_per_us_gallon_cubic_foot() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Hour per Us Gallon Cubic Foot (http://qudt.org/vocab/unit/LB-HR-PER-GAL_US-FT3)"""
    return QUDT_UNIT["LB-HR-PER-GAL_US-FT3"]


def get_qudt_unit_pound_mass_hour_per_us_gallon_cubic_inch() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Hour per Us Gallon Cubic Inch (http://qudt.org/vocab/unit/LB-HR-PER-GAL_US-IN3)"""
    return QUDT_UNIT["LB-HR-PER-GAL_US-IN3"]


def get_qudt_unit_pound_mass_hour_per_us_gallon_cubic_yard() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Hour per Us Gallon Cubic Yard (http://qudt.org/vocab/unit/LB-HR-PER-GAL_US-YD3)"""
    return QUDT_UNIT["LB-HR-PER-GAL_US-YD3"]


def get_qudt_unit_pound_mass_hour_per_square_us_gallon() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Hour per Square Us Gallon (http://qudt.org/vocab/unit/LB-HR-PER-GAL_US2)"""
    return QUDT_UNIT["LB-HR-PER-GAL_US2"]


def get_qudt_unit_pound_mass_hour_per_cubic_inch_cubic_foot() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Hour per Cubic Inch Cubic Foot (http://qudt.org/vocab/unit/LB-HR-PER-IN3-FT3)"""
    return QUDT_UNIT["LB-HR-PER-IN3-FT3"]


def get_qudt_unit_pound_mass_hour_per_cubic_inch_gallon_uk() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Hour per Cubic Inch Gallon (UK) (http://qudt.org/vocab/unit/LB-HR-PER-IN3-GAL_UK)"""
    return QUDT_UNIT["LB-HR-PER-IN3-GAL_UK"]


def get_qudt_unit_pound_mass_hour_per_cubic_inch_us_gallon() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Hour per Cubic Inch Us Gallon (http://qudt.org/vocab/unit/LB-HR-PER-IN3-GAL_US)"""
    return QUDT_UNIT["LB-HR-PER-IN3-GAL_US"]


def get_qudt_unit_pound_mass_hour_per_cubic_inch_cubic_yard() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Hour per Cubic Inch Cubic Yard (http://qudt.org/vocab/unit/LB-HR-PER-IN3-YD3)"""
    return QUDT_UNIT["LB-HR-PER-IN3-YD3"]


def get_qudt_unit_pound_mass_hour_per_sextic_inch() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Hour per Sextic Inch (http://qudt.org/vocab/unit/LB-HR-PER-IN6)"""
    return QUDT_UNIT["LB-HR-PER-IN6"]


def get_qudt_unit_pound_mass_square_inch_per_cubic_foot_pound_force_second() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Square Inch per Cubic Foot Pound Force Second (http://qudt.org/vocab/unit/LB-IN2-PER-FT3-LB_F-SEC)"""
    return QUDT_UNIT["LB-IN2-PER-FT3-LB_F-SEC"]


def get_qudt_unit_pound_mass_square_inch_per_gallon_uk_pound_force_second() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Square Inch per Gallon (UK) Pound Force Second (http://qudt.org/vocab/unit/LB-IN2-PER-GAL_UK-LB_F-SEC)"""
    return QUDT_UNIT["LB-IN2-PER-GAL_UK-LB_F-SEC"]


def get_qudt_unit_pound_mass_square_inch_per_us_gallon_pound_force_second() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Square Inch per Us Gallon Pound Force Second (http://qudt.org/vocab/unit/LB-IN2-PER-GAL_US-LB_F-SEC)"""
    return QUDT_UNIT["LB-IN2-PER-GAL_US-LB_F-SEC"]


def get_qudt_unit_pound_mass_square_inch_per_cubic_inch_pound_force_second() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Square Inch per Cubic Inch Pound Force Second (http://qudt.org/vocab/unit/LB-IN2-PER-IN3-LB_F-SEC)"""
    return QUDT_UNIT["LB-IN2-PER-IN3-LB_F-SEC"]


def get_qudt_unit_pound_mass_minute_per_cubic_foot_gallon_uk() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Minute per Cubic Foot Gallon (UK) (http://qudt.org/vocab/unit/LB-MIN-PER-FT3-GAL_UK)"""
    return QUDT_UNIT["LB-MIN-PER-FT3-GAL_UK"]


def get_qudt_unit_pound_mass_minute_per_cubic_foot_us_gallon() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Minute per Cubic Foot Us Gallon (http://qudt.org/vocab/unit/LB-MIN-PER-FT3-GAL_US)"""
    return QUDT_UNIT["LB-MIN-PER-FT3-GAL_US"]


def get_qudt_unit_pound_mass_minute_per_cubic_foot_cubic_inch() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Minute per Cubic Foot Cubic Inch (http://qudt.org/vocab/unit/LB-MIN-PER-FT3-IN3)"""
    return QUDT_UNIT["LB-MIN-PER-FT3-IN3"]


def get_qudt_unit_pound_mass_minute_per_cubic_foot_cubic_yard() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Minute per Cubic Foot Cubic Yard (http://qudt.org/vocab/unit/LB-MIN-PER-FT3-YD3)"""
    return QUDT_UNIT["LB-MIN-PER-FT3-YD3"]


def get_qudt_unit_pound_mass_minute_per_sextic_foot() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Minute per Sextic Foot (http://qudt.org/vocab/unit/LB-MIN-PER-FT6)"""
    return QUDT_UNIT["LB-MIN-PER-FT6"]


def get_qudt_unit_pound_mass_minute_per_gallon_uk_cubic_foot() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Minute per Gallon (UK) Cubic Foot (http://qudt.org/vocab/unit/LB-MIN-PER-GAL_UK-FT3)"""
    return QUDT_UNIT["LB-MIN-PER-GAL_UK-FT3"]


def get_qudt_unit_pound_mass_minute_per_gallon_uk_cubic_inch() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Minute per Gallon (UK) Cubic Inch (http://qudt.org/vocab/unit/LB-MIN-PER-GAL_UK-IN3)"""
    return QUDT_UNIT["LB-MIN-PER-GAL_UK-IN3"]


def get_qudt_unit_pound_mass_minute_per_gallon_uk_cubic_yard() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Minute per Gallon (UK) Cubic Yard (http://qudt.org/vocab/unit/LB-MIN-PER-GAL_UK-YD3)"""
    return QUDT_UNIT["LB-MIN-PER-GAL_UK-YD3"]


def get_qudt_unit_pound_mass_minute_per_square_gallon_uk() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Minute per Square Gallon (UK) (http://qudt.org/vocab/unit/LB-MIN-PER-GAL_UK2)"""
    return QUDT_UNIT["LB-MIN-PER-GAL_UK2"]


def get_qudt_unit_pound_mass_minute_per_us_gallon_cubic_foot() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Minute per Us Gallon Cubic Foot (http://qudt.org/vocab/unit/LB-MIN-PER-GAL_US-FT3)"""
    return QUDT_UNIT["LB-MIN-PER-GAL_US-FT3"]


def get_qudt_unit_pound_mass_minute_per_us_gallon_cubic_inch() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Minute per Us Gallon Cubic Inch (http://qudt.org/vocab/unit/LB-MIN-PER-GAL_US-IN3)"""
    return QUDT_UNIT["LB-MIN-PER-GAL_US-IN3"]


def get_qudt_unit_pound_mass_minute_per_us_gallon_cubic_yard() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Minute per Us Gallon Cubic Yard (http://qudt.org/vocab/unit/LB-MIN-PER-GAL_US-YD3)"""
    return QUDT_UNIT["LB-MIN-PER-GAL_US-YD3"]


def get_qudt_unit_pound_mass_minute_per_square_us_gallon() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Minute per Square Us Gallon (http://qudt.org/vocab/unit/LB-MIN-PER-GAL_US2)"""
    return QUDT_UNIT["LB-MIN-PER-GAL_US2"]


def get_qudt_unit_pound_mass_minute_per_cubic_inch_cubic_foot() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Minute per Cubic Inch Cubic Foot (http://qudt.org/vocab/unit/LB-MIN-PER-IN3-FT3)"""
    return QUDT_UNIT["LB-MIN-PER-IN3-FT3"]


def get_qudt_unit_pound_mass_minute_per_cubic_inch_gallon_uk() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Minute per Cubic Inch Gallon (UK) (http://qudt.org/vocab/unit/LB-MIN-PER-IN3-GAL_UK)"""
    return QUDT_UNIT["LB-MIN-PER-IN3-GAL_UK"]


def get_qudt_unit_pound_mass_minute_per_cubic_inch_us_gallon() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Minute per Cubic Inch Us Gallon (http://qudt.org/vocab/unit/LB-MIN-PER-IN3-GAL_US)"""
    return QUDT_UNIT["LB-MIN-PER-IN3-GAL_US"]


def get_qudt_unit_pound_mass_minute_per_cubic_inch_cubic_yard() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Minute per Cubic Inch Cubic Yard (http://qudt.org/vocab/unit/LB-MIN-PER-IN3-YD3)"""
    return QUDT_UNIT["LB-MIN-PER-IN3-YD3"]


def get_qudt_unit_pound_mass_minute_per_sextic_inch() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Minute per Sextic Inch (http://qudt.org/vocab/unit/LB-MIN-PER-IN6)"""
    return QUDT_UNIT["LB-MIN-PER-IN6"]


def get_qudt_unit_pound_mass_per_degree_fahrenheit() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Degree Fahrenheit (http://qudt.org/vocab/unit/LB-PER-DEG_F)"""
    return QUDT_UNIT["LB-PER-DEG_F"]


def get_qudt_unit_pound_mass_per_foot_pound_force_second() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Foot Pound Force Second (http://qudt.org/vocab/unit/LB-PER-FT-LB_F-SEC)"""
    return QUDT_UNIT["LB-PER-FT-LB_F-SEC"]


def get_qudt_unit_pound_mass_per_cubic_foot_degree_fahrenheit() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Cubic Foot Degree Fahrenheit (http://qudt.org/vocab/unit/LB-PER-FT3-DEG_F)"""
    return QUDT_UNIT["LB-PER-FT3-DEG_F"]


def get_qudt_unit_pound_mass_per_hour_degree_fahrenheit() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Hour Degree Fahrenheit (http://qudt.org/vocab/unit/LB-PER-HR-DEG_F)"""
    return QUDT_UNIT["LB-PER-HR-DEG_F"]


def get_qudt_unit_pound_mass_per_cubic_inch_degree_fahrenheit() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Cubic Inch Degree Fahrenheit (http://qudt.org/vocab/unit/LB-PER-IN3-DEG_F)"""
    return QUDT_UNIT["LB-PER-IN3-DEG_F"]


def get_qudt_unit_pound_mass_per_minute_degree_fahrenheit() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Minute Degree Fahrenheit (http://qudt.org/vocab/unit/LB-PER-MIN-DEG_F)"""
    return QUDT_UNIT["LB-PER-MIN-DEG_F"]


def get_qudt_unit_pound_mass_per_psi() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Psi (http://qudt.org/vocab/unit/LB-PER-PSI)"""
    return QUDT_UNIT["LB-PER-PSI"]


def get_qudt_unit_pound_mass_per_second_degree_fahrenheit() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass per Second Degree Fahrenheit (http://qudt.org/vocab/unit/LB-PER-SEC-DEG_F)"""
    return QUDT_UNIT["LB-PER-SEC-DEG_F"]


def get_qudt_unit_pound_mass_second_per_cubic_foot_gallon_uk() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Second per Cubic Foot Gallon (UK) (http://qudt.org/vocab/unit/LB-SEC-PER-FT3-GAL_UK)"""
    return QUDT_UNIT["LB-SEC-PER-FT3-GAL_UK"]


def get_qudt_unit_pound_mass_second_per_cubic_foot_us_gallon() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Second per Cubic Foot Us Gallon (http://qudt.org/vocab/unit/LB-SEC-PER-FT3-GAL_US)"""
    return QUDT_UNIT["LB-SEC-PER-FT3-GAL_US"]


def get_qudt_unit_pound_mass_second_per_cubic_foot_cubic_inch() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Second per Cubic Foot Cubic Inch (http://qudt.org/vocab/unit/LB-SEC-PER-FT3-IN3)"""
    return QUDT_UNIT["LB-SEC-PER-FT3-IN3"]


def get_qudt_unit_pound_mass_second_per_cubic_foot_cubic_yard() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Second per Cubic Foot Cubic Yard (http://qudt.org/vocab/unit/LB-SEC-PER-FT3-YD3)"""
    return QUDT_UNIT["LB-SEC-PER-FT3-YD3"]


def get_qudt_unit_pound_mass_second_per_sextic_foot() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Second per Sextic Foot (http://qudt.org/vocab/unit/LB-SEC-PER-FT6)"""
    return QUDT_UNIT["LB-SEC-PER-FT6"]


def get_qudt_unit_pound_mass_second_per_gallon_uk_cubic_foot() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Second per Gallon (UK) Cubic Foot (http://qudt.org/vocab/unit/LB-SEC-PER-GAL_UK-FT3)"""
    return QUDT_UNIT["LB-SEC-PER-GAL_UK-FT3"]


def get_qudt_unit_pound_mass_second_per_gallon_uk_cubic_inch() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Second per Gallon (UK) Cubic Inch (http://qudt.org/vocab/unit/LB-SEC-PER-GAL_UK-IN3)"""
    return QUDT_UNIT["LB-SEC-PER-GAL_UK-IN3"]


def get_qudt_unit_pound_mass_second_per_gallon_uk_cubic_yard() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Second per Gallon (UK) Cubic Yard (http://qudt.org/vocab/unit/LB-SEC-PER-GAL_UK-YD3)"""
    return QUDT_UNIT["LB-SEC-PER-GAL_UK-YD3"]


def get_qudt_unit_pound_mass_second_per_square_gallon_uk() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Second per Square Gallon (UK) (http://qudt.org/vocab/unit/LB-SEC-PER-GAL_UK2)"""
    return QUDT_UNIT["LB-SEC-PER-GAL_UK2"]


def get_qudt_unit_pound_mass_second_per_us_gallon_cubic_foot() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Second per Us Gallon Cubic Foot (http://qudt.org/vocab/unit/LB-SEC-PER-GAL_US-FT3)"""
    return QUDT_UNIT["LB-SEC-PER-GAL_US-FT3"]


def get_qudt_unit_pound_mass_second_per_us_gallon_cubic_inch() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Second per Us Gallon Cubic Inch (http://qudt.org/vocab/unit/LB-SEC-PER-GAL_US-IN3)"""
    return QUDT_UNIT["LB-SEC-PER-GAL_US-IN3"]


def get_qudt_unit_pound_mass_second_per_us_gallon_cubic_yard() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Second per Us Gallon Cubic Yard (http://qudt.org/vocab/unit/LB-SEC-PER-GAL_US-YD3)"""
    return QUDT_UNIT["LB-SEC-PER-GAL_US-YD3"]


def get_qudt_unit_pound_mass_second_per_square_us_gallon() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Second per Square Us Gallon (http://qudt.org/vocab/unit/LB-SEC-PER-GAL_US2)"""
    return QUDT_UNIT["LB-SEC-PER-GAL_US2"]


def get_qudt_unit_pound_mass_second_per_cubic_inch_cubic_foot() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Second per Cubic Inch Cubic Foot (http://qudt.org/vocab/unit/LB-SEC-PER-IN3-FT3)"""
    return QUDT_UNIT["LB-SEC-PER-IN3-FT3"]


def get_qudt_unit_pound_mass_second_per_cubic_inch_gallon_uk() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Second per Cubic Inch Gallon (UK) (http://qudt.org/vocab/unit/LB-SEC-PER-IN3-GAL_UK)"""
    return QUDT_UNIT["LB-SEC-PER-IN3-GAL_UK"]


def get_qudt_unit_pound_mass_second_per_cubic_inch_us_gallon() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Second per Cubic Inch Us Gallon (http://qudt.org/vocab/unit/LB-SEC-PER-IN3-GAL_US)"""
    return QUDT_UNIT["LB-SEC-PER-IN3-GAL_US"]


def get_qudt_unit_pound_mass_second_per_cubic_inch_cubic_yard() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Second per Cubic Inch Cubic Yard (http://qudt.org/vocab/unit/LB-SEC-PER-IN3-YD3)"""
    return QUDT_UNIT["LB-SEC-PER-IN3-YD3"]


def get_qudt_unit_pound_mass_second_per_sextic_inch() -> URIRef:
    """Returns the URI for QUDT unit: Pound Mass Second per Sextic Inch (http://qudt.org/vocab/unit/LB-SEC-PER-IN6)"""
    return QUDT_UNIT["LB-SEC-PER-IN6"]


def get_qudt_unit_metre_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Metre per Bar (http://qudt.org/vocab/unit/M-PER-BAR)"""
    return QUDT_UNIT["M-PER-BAR"]


def get_qudt_unit_metre_per_pascal() -> URIRef:
    """Returns the URI for QUDT unit: Metre per Pascal (http://qudt.org/vocab/unit/M-PER-PA)"""
    return QUDT_UNIT["M-PER-PA"]


def get_qudt_unit_metre_per_second_bar() -> URIRef:
    """Returns the URI for QUDT unit: Metre per Second Bar (http://qudt.org/vocab/unit/M-PER-SEC-BAR)"""
    return QUDT_UNIT["M-PER-SEC-BAR"]


def get_qudt_unit_metre_per_second_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Metre per Second Kelvin (http://qudt.org/vocab/unit/M-PER-SEC-K)"""
    return QUDT_UNIT["M-PER-SEC-K"]


def get_qudt_unit_metre_per_second_pascal() -> URIRef:
    """Returns the URI for QUDT unit: Metre per Second Pascal (http://qudt.org/vocab/unit/M-PER-SEC-PA)"""
    return QUDT_UNIT["M-PER-SEC-PA"]


def get_qudt_unit_metre_second() -> URIRef:
    """Returns the URI for QUDT unit: Metre Second (http://qudt.org/vocab/unit/M-SEC)"""
    return QUDT_UNIT["M-SEC"]


def get_qudt_unit_metre_square_second() -> URIRef:
    """Returns the URI for QUDT unit: Metre Square Second (http://qudt.org/vocab/unit/M-SEC2)"""
    return QUDT_UNIT["M-SEC2"]


def get_qudt_unit_placeholder() -> URIRef:
    """Returns the URI for QUDT unit: Placeholder (http://qudt.org/vocab/unit/M0dot)"""
    return QUDT_UNIT["M0DOT"]


def get_qudt_unit_square_metre_square_hertz() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre Square Hertz (http://qudt.org/vocab/unit/M2-HZ2)"""
    return QUDT_UNIT["M2-HZ2"]


def get_qudt_unit_square_metre_cubic_hertz() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre Cubic Hertz (http://qudt.org/vocab/unit/M2-HZ3)"""
    return QUDT_UNIT["M2-HZ3"]


def get_qudt_unit_square_metre_quartic_hertz() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre Quartic Hertz (http://qudt.org/vocab/unit/M2-HZ4)"""
    return QUDT_UNIT["M2-HZ4"]


def get_qudt_unit_square_metre_per_hectare_year() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre per Hectare Year (http://qudt.org/vocab/unit/M2-PER-HA-YR)"""
    return QUDT_UNIT["M2-PER-HA-YR"]


def get_qudt_unit_square_metre_per_hertz() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre per Hertz (http://qudt.org/vocab/unit/M2-PER-HZ)"""
    return QUDT_UNIT["M2-PER-HZ"]


def get_qudt_unit_square_metre_per_hertz_degree() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre per Hertz Degree (http://qudt.org/vocab/unit/M2-PER-HZ-DEG)"""
    return QUDT_UNIT["M2-PER-HZ-DEG"]


def get_qudt_unit_square_metre_per_square_hertz() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre per Square Hertz (http://qudt.org/vocab/unit/M2-PER-HZ2)"""
    return QUDT_UNIT["M2-PER-HZ2"]


def get_qudt_unit_square_metre_per_second_bar() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre per Second Bar (http://qudt.org/vocab/unit/M2-PER-SEC-BAR)"""
    return QUDT_UNIT["M2-PER-SEC-BAR"]


def get_qudt_unit_square_metre_per_second_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre per Second Kelvin (http://qudt.org/vocab/unit/M2-PER-SEC-K)"""
    return QUDT_UNIT["M2-PER-SEC-K"]


def get_qudt_unit_square_metre_per_second_pascal() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre per Second Pascal (http://qudt.org/vocab/unit/M2-PER-SEC-PA)"""
    return QUDT_UNIT["M2-PER-SEC-PA"]


def get_qudt_unit_square_metre_second_per_radian() -> URIRef:
    """Returns the URI for QUDT unit: Square Metre Second per Radian (http://qudt.org/vocab/unit/M2-SEC-PER-RAD)"""
    return QUDT_UNIT["M2-SEC-PER-RAD"]


def get_qudt_unit_cubic_metre_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Metre per Bar (http://qudt.org/vocab/unit/M3-PER-BAR)"""
    return QUDT_UNIT["M3-PER-BAR"]


def get_qudt_unit_cubic_metre_per_day_bar() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Metre per Day Bar (http://qudt.org/vocab/unit/M3-PER-DAY-BAR)"""
    return QUDT_UNIT["M3-PER-DAY-BAR"]


def get_qudt_unit_cubic_metre_per_day_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Metre per Day Kelvin (http://qudt.org/vocab/unit/M3-PER-DAY-K)"""
    return QUDT_UNIT["M3-PER-DAY-K"]


def get_qudt_unit_cubic_metre_per_hour_bar() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Metre per Hour Bar (http://qudt.org/vocab/unit/M3-PER-HR-BAR)"""
    return QUDT_UNIT["M3-PER-HR-BAR"]


def get_qudt_unit_cubic_metre_per_hour_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Metre per Hour Kelvin (http://qudt.org/vocab/unit/M3-PER-HR-K)"""
    return QUDT_UNIT["M3-PER-HR-K"]


def get_qudt_unit_cubic_metre_per_minute_bar() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Metre per Minute Bar (http://qudt.org/vocab/unit/M3-PER-MIN-BAR)"""
    return QUDT_UNIT["M3-PER-MIN-BAR"]


def get_qudt_unit_cubic_metre_per_minute_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Metre per Minute Kelvin (http://qudt.org/vocab/unit/M3-PER-MIN-K)"""
    return QUDT_UNIT["M3-PER-MIN-K"]


def get_qudt_unit_cubic_metre_per_pascal() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Metre per Pascal (http://qudt.org/vocab/unit/M3-PER-PA)"""
    return QUDT_UNIT["M3-PER-PA"]


def get_qudt_unit_cubic_metre_per_second_bar() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Metre per Second Bar (http://qudt.org/vocab/unit/M3-PER-SEC-BAR)"""
    return QUDT_UNIT["M3-PER-SEC-BAR"]


def get_qudt_unit_cubic_metre_per_second_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Metre per Second Kelvin (http://qudt.org/vocab/unit/M3-PER-SEC-K)"""
    return QUDT_UNIT["M3-PER-SEC-K"]


def get_qudt_unit_cubic_metre_per_second_pascal() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Metre per Second Pascal (http://qudt.org/vocab/unit/M3-PER-SEC-PA)"""
    return QUDT_UNIT["M3-PER-SEC-PA"]


def get_qudt_unit_quartic_metre_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Quartic Metre per Second (http://qudt.org/vocab/unit/M4-PER-SEC)"""
    return QUDT_UNIT["M4-PER-SEC"]


def get_qudt_unit_mole_per_gram_hour() -> URIRef:
    """Returns the URI for QUDT unit: Mole per Gram Hour (http://qudt.org/vocab/unit/MOL-PER-GM-HR)"""
    return QUDT_UNIT["MOL-PER-GM-HR"]


def get_qudt_unit_mole_per_kilogram_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Mole per Kilogram Kelvin (http://qudt.org/vocab/unit/MOL-PER-KiloGM-K)"""
    return QUDT_UNIT["MOL-PER-KILOGM-K"]


def get_qudt_unit_mole_per_litre_bar() -> URIRef:
    """Returns the URI for QUDT unit: Mole per Litre Bar (http://qudt.org/vocab/unit/MOL-PER-L-BAR)"""
    return QUDT_UNIT["MOL-PER-L-BAR"]


def get_qudt_unit_mole_per_litre_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Mole per Litre Kelvin (http://qudt.org/vocab/unit/MOL-PER-L-K)"""
    return QUDT_UNIT["MOL-PER-L-K"]


def get_qudt_unit_mole_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Mole per Square Metre (http://qudt.org/vocab/unit/MOL-PER-M2)"""
    return QUDT_UNIT["MOL-PER-M2"]


def get_qudt_unit_mole_per_square_metre_second_metre_steradian() -> URIRef:
    """Returns the URI for QUDT unit: Mole per Square Metre Second Metre Steradian (http://qudt.org/vocab/unit/MOL-PER-M2-SEC-M-SR)"""
    return QUDT_UNIT["MOL-PER-M2-SEC-M-SR"]


def get_qudt_unit_mole_per_square_metre_second_steradian() -> URIRef:
    """Returns the URI for QUDT unit: Mole per Square Metre Second Steradian (http://qudt.org/vocab/unit/MOL-PER-M2-SEC-SR)"""
    return QUDT_UNIT["MOL-PER-M2-SEC-SR"]


def get_qudt_unit_mole_per_cubic_metre_bar() -> URIRef:
    """Returns the URI for QUDT unit: Mole per Cubic Metre Bar (http://qudt.org/vocab/unit/MOL-PER-M3-BAR)"""
    return QUDT_UNIT["MOL-PER-M3-BAR"]


def get_qudt_unit_mole_per_cubic_metre_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Mole per Cubic Metre Kelvin (http://qudt.org/vocab/unit/MOL-PER-M3-K)"""
    return QUDT_UNIT["MOL-PER-M3-K"]


def get_qudt_unit_mole_per_cubic_metre_pascal() -> URIRef:
    """Returns the URI for QUDT unit: Mole per Cubic Metre Pascal (http://qudt.org/vocab/unit/MOL-PER-M3-PA)"""
    return QUDT_UNIT["MOL-PER-M3-PA"]


def get_qudt_unit_mole_per_mole() -> URIRef:
    """Returns the URI for QUDT unit: Mole per Mole (http://qudt.org/vocab/unit/MOL-PER-MOL)"""
    return QUDT_UNIT["MOL-PER-MOL"]


def get_qudt_unit_mega_us_dollar_per_year() -> URIRef:
    """Returns the URI for QUDT unit: Mega Us Dollar per Year (http://qudt.org/vocab/unit/MegaCCY_USD-PER-YR)"""
    return QUDT_UNIT["MEGACCY_USD-PER-YR"]


def get_qudt_unit_megahertz_kilometre() -> URIRef:
    """Returns the URI for QUDT unit: Megahertz Kilometre (http://qudt.org/vocab/unit/MegaHZ-KiloM)"""
    return QUDT_UNIT["MEGAHZ-KILOM"]


def get_qudt_unit_megaohm_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Megaohm per Bar (http://qudt.org/vocab/unit/MegaOHM-PER-BAR)"""
    return QUDT_UNIT["MEGAOHM-PER-BAR"]


def get_qudt_unit_megaohm_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Megaohm per Kelvin (http://qudt.org/vocab/unit/MegaOHM-PER-K)"""
    return QUDT_UNIT["MEGAOHM-PER-K"]


def get_qudt_unit_microgalileo_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Microgalileo per Metre (http://qudt.org/vocab/unit/MicroGALILEO-PER-M)"""
    return QUDT_UNIT["MICROGALILEO-PER-M"]


def get_qudt_unit_microgram_per_litre_hour() -> URIRef:
    """Returns the URI for QUDT unit: Microgram per Litre Hour (http://qudt.org/vocab/unit/MicroGM-PER-L-HR)"""
    return QUDT_UNIT["MICROGM-PER-L-HR"]


def get_qudt_unit_microgram_per_cubic_metre_hour() -> URIRef:
    """Returns the URI for QUDT unit: Microgram per Cubic Metre Hour (http://qudt.org/vocab/unit/MicroGM-PER-M3-HR)"""
    return QUDT_UNIT["MICROGM-PER-M3-HR"]


def get_qudt_unit_microgram_per_cubic_metre_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Microgram per Cubic Metre Kelvin (http://qudt.org/vocab/unit/MicroGM-PER-M3-K)"""
    return QUDT_UNIT["MICROGM-PER-M3-K"]


def get_qudt_unit_micrometre_per_millilitre() -> URIRef:
    """Returns the URI for QUDT unit: Micrometre per Millilitre (http://qudt.org/vocab/unit/MicroM-PER-MilliL)"""
    return QUDT_UNIT["MICROM-PER-MILLIL"]


def get_qudt_unit_micromole_per_gram_hour() -> URIRef:
    """Returns the URI for QUDT unit: Micromole per Gram Hour (http://qudt.org/vocab/unit/MicroMOL-PER-GM-HR)"""
    return QUDT_UNIT["MICROMOL-PER-GM-HR"]


def get_qudt_unit_micromole_per_gram_second() -> URIRef:
    """Returns the URI for QUDT unit: Micromole per Gram Second (http://qudt.org/vocab/unit/MicroMOL-PER-GM-SEC)"""
    return QUDT_UNIT["MICROMOL-PER-GM-SEC"]


def get_qudt_unit_micromole_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Micromole per Square Metre (http://qudt.org/vocab/unit/MicroMOL-PER-M2)"""
    return QUDT_UNIT["MICROMOL-PER-M2"]


def get_qudt_unit_micromole_per_square_metre_square_second() -> URIRef:
    """Returns the URI for QUDT unit: Micromole per Square Metre Square Second (http://qudt.org/vocab/unit/MicroMOL-PER-M2-SEC2)"""
    return QUDT_UNIT["MICROMOL-PER-M2-SEC2"]


def get_qudt_unit_micromole_per_mole() -> URIRef:
    """Returns the URI for QUDT unit: Micromole per Mole (http://qudt.org/vocab/unit/MicroMOL-PER-MOL)"""
    return QUDT_UNIT["MICROMOL-PER-MOL"]


def get_qudt_unit_micromole_per_micromole_day() -> URIRef:
    """Returns the URI for QUDT unit: Micromole per Micromole Day (http://qudt.org/vocab/unit/MicroMOL-PER-MicroMOL-DAY)"""
    return QUDT_UNIT["MICROMOL-PER-MICROMOL-DAY"]


def get_qudt_unit_micro_volt_ampere_reactive_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Micro Volt Ampere Reactive per Kelvin (http://qudt.org/vocab/unit/MicroVAR-PER-K)"""
    return QUDT_UNIT["MICROVAR-PER-K"]


def get_qudt_unit_milliampere_square_inch_per_pound_force() -> URIRef:
    """Returns the URI for QUDT unit: Milliampere Square Inch per Pound Force (http://qudt.org/vocab/unit/MilliA-IN2-PER-LB_F)"""
    return QUDT_UNIT["MILLIA-IN2-PER-LB_F"]


def get_qudt_unit_milliampere_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Milliampere per Bar (http://qudt.org/vocab/unit/MilliA-PER-BAR)"""
    return QUDT_UNIT["MILLIA-PER-BAR"]


def get_qudt_unit_milliampere_per_litre_minute() -> URIRef:
    """Returns the URI for QUDT unit: Milliampere per Litre Minute (http://qudt.org/vocab/unit/MilliA-PER-L-MIN)"""
    return QUDT_UNIT["MILLIA-PER-L-MIN"]


def get_qudt_unit_milliampere_per_pound_force_square_inch() -> URIRef:
    """Returns the URI for QUDT unit: Milliampere per Pound Force Square Inch (http://qudt.org/vocab/unit/MilliA-PER-LB_F-IN2)"""
    return QUDT_UNIT["MILLIA-PER-LB_F-IN2"]


def get_qudt_unit_millibecquerel_per_square_metre_day() -> URIRef:
    """Returns the URI for QUDT unit: Millibecquerel per Square Metre Day (http://qudt.org/vocab/unit/MilliBQ-PER-M2-DAY)"""
    return QUDT_UNIT["MILLIBQ-PER-M2-DAY"]


def get_qudt_unit_milligalileo_per_month() -> URIRef:
    """Returns the URI for QUDT unit: Milligalileo per Month (http://qudt.org/vocab/unit/MilliGALILEO-PER-MO)"""
    return QUDT_UNIT["MILLIGALILEO-PER-MO"]


def get_qudt_unit_milligram_hour_per_litre_cubic_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Milligram Hour per Litre Cubic Centimetre (http://qudt.org/vocab/unit/MilliGM-HR-PER-L-CentiM3)"""
    return QUDT_UNIT["MILLIGM-HR-PER-L-CENTIM3"]


def get_qudt_unit_milligram_hour_per_litre_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Milligram Hour per Litre Cubic Metre (http://qudt.org/vocab/unit/MilliGM-HR-PER-L-M3)"""
    return QUDT_UNIT["MILLIGM-HR-PER-L-M3"]


def get_qudt_unit_milligram_hour_per_square_litre() -> URIRef:
    """Returns the URI for QUDT unit: Milligram Hour per Square Litre (http://qudt.org/vocab/unit/MilliGM-HR-PER-L2)"""
    return QUDT_UNIT["MILLIGM-HR-PER-L2"]


def get_qudt_unit_milligram_hour_per_cubic_metre_cubic_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Milligram Hour per Cubic Metre Cubic Centimetre (http://qudt.org/vocab/unit/MilliGM-HR-PER-M3-CentiM3)"""
    return QUDT_UNIT["MILLIGM-HR-PER-M3-CENTIM3"]


def get_qudt_unit_milligram_hour_per_cubic_metre_litre() -> URIRef:
    """Returns the URI for QUDT unit: Milligram Hour per Cubic Metre Litre (http://qudt.org/vocab/unit/MilliGM-HR-PER-M3-L)"""
    return QUDT_UNIT["MILLIGM-HR-PER-M3-L"]


def get_qudt_unit_milligram_hour_per_sextic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Milligram Hour per Sextic Metre (http://qudt.org/vocab/unit/MilliGM-HR-PER-M6)"""
    return QUDT_UNIT["MILLIGM-HR-PER-M6"]


def get_qudt_unit_milligram_minute_per_litre_cubic_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Milligram Minute per Litre Cubic Centimetre (http://qudt.org/vocab/unit/MilliGM-MIN-PER-L-CentiM3)"""
    return QUDT_UNIT["MILLIGM-MIN-PER-L-CENTIM3"]


def get_qudt_unit_milligram_minute_per_litre_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Milligram Minute per Litre Cubic Metre (http://qudt.org/vocab/unit/MilliGM-MIN-PER-L-M3)"""
    return QUDT_UNIT["MILLIGM-MIN-PER-L-M3"]


def get_qudt_unit_milligram_minute_per_square_litre() -> URIRef:
    """Returns the URI for QUDT unit: Milligram Minute per Square Litre (http://qudt.org/vocab/unit/MilliGM-MIN-PER-L2)"""
    return QUDT_UNIT["MILLIGM-MIN-PER-L2"]


def get_qudt_unit_milligram_minute_per_cubic_metre_cubic_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Milligram Minute per Cubic Metre Cubic Centimetre (http://qudt.org/vocab/unit/MilliGM-MIN-PER-M3-CentiM3)"""
    return QUDT_UNIT["MILLIGM-MIN-PER-M3-CENTIM3"]


def get_qudt_unit_milligram_minute_per_cubic_metre_litre() -> URIRef:
    """Returns the URI for QUDT unit: Milligram Minute per Cubic Metre Litre (http://qudt.org/vocab/unit/MilliGM-MIN-PER-M3-L)"""
    return QUDT_UNIT["MILLIGM-MIN-PER-M3-L"]


def get_qudt_unit_milligram_minute_per_sextic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Milligram Minute per Sextic Metre (http://qudt.org/vocab/unit/MilliGM-MIN-PER-M6)"""
    return QUDT_UNIT["MILLIGM-MIN-PER-M6"]


def get_qudt_unit_milligram_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Bar (http://qudt.org/vocab/unit/MilliGM-PER-BAR)"""
    return QUDT_UNIT["MILLIGM-PER-BAR"]


def get_qudt_unit_milligram_per_day_bar() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Day Bar (http://qudt.org/vocab/unit/MilliGM-PER-DAY-BAR)"""
    return QUDT_UNIT["MILLIGM-PER-DAY-BAR"]


def get_qudt_unit_milligram_per_day_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Day Kelvin (http://qudt.org/vocab/unit/MilliGM-PER-DAY-K)"""
    return QUDT_UNIT["MILLIGM-PER-DAY-K"]


def get_qudt_unit_milligram_per_hour_bar() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Hour Bar (http://qudt.org/vocab/unit/MilliGM-PER-HR-BAR)"""
    return QUDT_UNIT["MILLIGM-PER-HR-BAR"]


def get_qudt_unit_milligram_per_hour_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Hour Kelvin (http://qudt.org/vocab/unit/MilliGM-PER-HR-K)"""
    return QUDT_UNIT["MILLIGM-PER-HR-K"]


def get_qudt_unit_milligram_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Kelvin (http://qudt.org/vocab/unit/MilliGM-PER-K)"""
    return QUDT_UNIT["MILLIGM-PER-K"]


def get_qudt_unit_milligram_per_litre_centipoise() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Litre Centipoise (http://qudt.org/vocab/unit/MilliGM-PER-L-CentiPOISE)"""
    return QUDT_UNIT["MILLIGM-PER-L-CENTIPOISE"]


def get_qudt_unit_milligram_per_litre_millipascal_second() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Litre Millipascal Second (http://qudt.org/vocab/unit/MilliGM-PER-L-MilliPA-SEC)"""
    return QUDT_UNIT["MILLIGM-PER-L-MILLIPA-SEC"]


def get_qudt_unit_milligram_per_litre_pascal_second() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Litre Pascal Second (http://qudt.org/vocab/unit/MilliGM-PER-L-PA-SEC)"""
    return QUDT_UNIT["MILLIGM-PER-L-PA-SEC"]


def get_qudt_unit_milligram_per_litre_poise() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Litre Poise (http://qudt.org/vocab/unit/MilliGM-PER-L-POISE)"""
    return QUDT_UNIT["MILLIGM-PER-L-POISE"]


def get_qudt_unit_milligram_per_cubic_metre_centipoise() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Cubic Metre Centipoise (http://qudt.org/vocab/unit/MilliGM-PER-M3-CentiPOISE)"""
    return QUDT_UNIT["MILLIGM-PER-M3-CENTIPOISE"]


def get_qudt_unit_milligram_per_cubic_metre_day() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Cubic Metre Day (http://qudt.org/vocab/unit/MilliGM-PER-M3-DAY)"""
    return QUDT_UNIT["MILLIGM-PER-M3-DAY"]


def get_qudt_unit_milligram_per_cubic_metre_hour() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Cubic Metre Hour (http://qudt.org/vocab/unit/MilliGM-PER-M3-HR)"""
    return QUDT_UNIT["MILLIGM-PER-M3-HR"]


def get_qudt_unit_milligram_per_cubic_metre_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Cubic Metre Kelvin (http://qudt.org/vocab/unit/MilliGM-PER-M3-K)"""
    return QUDT_UNIT["MILLIGM-PER-M3-K"]


def get_qudt_unit_milligram_per_cubic_metre_millipascal_second() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Cubic Metre Millipascal Second (http://qudt.org/vocab/unit/MilliGM-PER-M3-MilliPA-SEC)"""
    return QUDT_UNIT["MILLIGM-PER-M3-MILLIPA-SEC"]


def get_qudt_unit_milligram_per_cubic_metre_pascal_second() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Cubic Metre Pascal Second (http://qudt.org/vocab/unit/MilliGM-PER-M3-PA-SEC)"""
    return QUDT_UNIT["MILLIGM-PER-M3-PA-SEC"]


def get_qudt_unit_milligram_per_cubic_metre_poise() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Cubic Metre Poise (http://qudt.org/vocab/unit/MilliGM-PER-M3-POISE)"""
    return QUDT_UNIT["MILLIGM-PER-M3-POISE"]


def get_qudt_unit_milligram_per_cubic_metre_second() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Cubic Metre Second (http://qudt.org/vocab/unit/MilliGM-PER-M3-SEC)"""
    return QUDT_UNIT["MILLIGM-PER-M3-SEC"]


def get_qudt_unit_milligram_per_minute_bar() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Minute Bar (http://qudt.org/vocab/unit/MilliGM-PER-MIN-BAR)"""
    return QUDT_UNIT["MILLIGM-PER-MIN-BAR"]


def get_qudt_unit_milligram_per_minute_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Minute Kelvin (http://qudt.org/vocab/unit/MilliGM-PER-MIN-K)"""
    return QUDT_UNIT["MILLIGM-PER-MIN-K"]


def get_qudt_unit_milligram_per_second_bar() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Second Bar (http://qudt.org/vocab/unit/MilliGM-PER-SEC-BAR)"""
    return QUDT_UNIT["MILLIGM-PER-SEC-BAR"]


def get_qudt_unit_milligram_per_second_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Milligram per Second Kelvin (http://qudt.org/vocab/unit/MilliGM-PER-SEC-K)"""
    return QUDT_UNIT["MILLIGM-PER-SEC-K"]


def get_qudt_unit_milligram_second_per_litre_cubic_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Milligram Second per Litre Cubic Centimetre (http://qudt.org/vocab/unit/MilliGM-SEC-PER-L-CentiM3)"""
    return QUDT_UNIT["MILLIGM-SEC-PER-L-CENTIM3"]


def get_qudt_unit_milligram_second_per_litre_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Milligram Second per Litre Cubic Metre (http://qudt.org/vocab/unit/MilliGM-SEC-PER-L-M3)"""
    return QUDT_UNIT["MILLIGM-SEC-PER-L-M3"]


def get_qudt_unit_milligram_second_per_square_litre() -> URIRef:
    """Returns the URI for QUDT unit: Milligram Second per Square Litre (http://qudt.org/vocab/unit/MilliGM-SEC-PER-L2)"""
    return QUDT_UNIT["MILLIGM-SEC-PER-L2"]


def get_qudt_unit_milligram_second_per_cubic_metre_cubic_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Milligram Second per Cubic Metre Cubic Centimetre (http://qudt.org/vocab/unit/MilliGM-SEC-PER-M3-CentiM3)"""
    return QUDT_UNIT["MILLIGM-SEC-PER-M3-CENTIM3"]


def get_qudt_unit_milligram_second_per_cubic_metre_litre() -> URIRef:
    """Returns the URI for QUDT unit: Milligram Second per Cubic Metre Litre (http://qudt.org/vocab/unit/MilliGM-SEC-PER-M3-L)"""
    return QUDT_UNIT["MILLIGM-SEC-PER-M3-L"]


def get_qudt_unit_milligram_second_per_sextic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Milligram Second per Sextic Metre (http://qudt.org/vocab/unit/MilliGM-SEC-PER-M6)"""
    return QUDT_UNIT["MILLIGM-SEC-PER-M6"]


def get_qudt_unit_millikelvin_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Millikelvin per Bar (http://qudt.org/vocab/unit/MilliK-PER-BAR)"""
    return QUDT_UNIT["MILLIK-PER-BAR"]


def get_qudt_unit_millilitre_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Millilitre per Bar (http://qudt.org/vocab/unit/MilliL-PER-BAR)"""
    return QUDT_UNIT["MILLIL-PER-BAR"]


def get_qudt_unit_millilitre_per_day_bar() -> URIRef:
    """Returns the URI for QUDT unit: Millilitre per Day Bar (http://qudt.org/vocab/unit/MilliL-PER-DAY-BAR)"""
    return QUDT_UNIT["MILLIL-PER-DAY-BAR"]


def get_qudt_unit_millilitre_per_day_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Millilitre per Day Kelvin (http://qudt.org/vocab/unit/MilliL-PER-DAY-K)"""
    return QUDT_UNIT["MILLIL-PER-DAY-K"]


def get_qudt_unit_millilitre_per_hour_bar() -> URIRef:
    """Returns the URI for QUDT unit: Millilitre per Hour Bar (http://qudt.org/vocab/unit/MilliL-PER-HR-BAR)"""
    return QUDT_UNIT["MILLIL-PER-HR-BAR"]


def get_qudt_unit_millilitre_per_hour_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Millilitre per Hour Kelvin (http://qudt.org/vocab/unit/MilliL-PER-HR-K)"""
    return QUDT_UNIT["MILLIL-PER-HR-K"]


def get_qudt_unit_millilitre_per_square_metre_day() -> URIRef:
    """Returns the URI for QUDT unit: Millilitre per Square Metre Day (http://qudt.org/vocab/unit/MilliL-PER-M2-DAY)"""
    return QUDT_UNIT["MILLIL-PER-M2-DAY"]


def get_qudt_unit_millilitre_per_minute_bar() -> URIRef:
    """Returns the URI for QUDT unit: Millilitre per Minute Bar (http://qudt.org/vocab/unit/MilliL-PER-MIN-BAR)"""
    return QUDT_UNIT["MILLIL-PER-MIN-BAR"]


def get_qudt_unit_millilitre_per_minute_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Millilitre per Minute Kelvin (http://qudt.org/vocab/unit/MilliL-PER-MIN-K)"""
    return QUDT_UNIT["MILLIL-PER-MIN-K"]


def get_qudt_unit_millilitre_per_second_bar() -> URIRef:
    """Returns the URI for QUDT unit: Millilitre per Second Bar (http://qudt.org/vocab/unit/MilliL-PER-SEC-BAR)"""
    return QUDT_UNIT["MILLIL-PER-SEC-BAR"]


def get_qudt_unit_millilitre_per_second_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Millilitre per Second Kelvin (http://qudt.org/vocab/unit/MilliL-PER-SEC-K)"""
    return QUDT_UNIT["MILLIL-PER-SEC-K"]


def get_qudt_unit_millimetre_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Millimetre per Bar (http://qudt.org/vocab/unit/MilliM-PER-BAR)"""
    return QUDT_UNIT["MILLIM-PER-BAR"]


def get_qudt_unit_millimetre_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Millimetre per Square Metre (http://qudt.org/vocab/unit/MilliM-PER-M2)"""
    return QUDT_UNIT["MILLIM-PER-M2"]


def get_qudt_unit_millimole_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Millimole per Square Metre (http://qudt.org/vocab/unit/MilliMOL-PER-M2)"""
    return QUDT_UNIT["MILLIMOL-PER-M2"]


def get_qudt_unit_millimole_per_mole() -> URIRef:
    """Returns the URI for QUDT unit: Millimole per Mole (http://qudt.org/vocab/unit/MilliMOL-PER-MOL)"""
    return QUDT_UNIT["MILLIMOL-PER-MOL"]


def get_qudt_unit_milliohm_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Milliohm per Bar (http://qudt.org/vocab/unit/MilliOHM-PER-BAR)"""
    return QUDT_UNIT["MILLIOHM-PER-BAR"]


def get_qudt_unit_milliohm_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Milliohm per Kelvin (http://qudt.org/vocab/unit/MilliOHM-PER-K)"""
    return QUDT_UNIT["MILLIOHM-PER-K"]


def get_qudt_unit_millipascal_second_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Millipascal Second per Kelvin (http://qudt.org/vocab/unit/MilliPA-SEC-PER-K)"""
    return QUDT_UNIT["MILLIPA-SEC-PER-K"]


def get_qudt_unit_millivolt_per_volt() -> URIRef:
    """Returns the URI for QUDT unit: Millivolt per Volt (http://qudt.org/vocab/unit/MilliV-PER-V)"""
    return QUDT_UNIT["MILLIV-PER-V"]


def get_qudt_unit_milli_volt_ampere_reactive_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Milli Volt Ampere Reactive per Kelvin (http://qudt.org/vocab/unit/MilliVAR-PER-K)"""
    return QUDT_UNIT["MILLIVAR-PER-K"]


def get_qudt_unit_milliwatt_per_square_centimetre_micrometre_steradian() -> URIRef:
    """Returns the URI for QUDT unit: Milliwatt per Square Centimetre Micrometre Steradian (http://qudt.org/vocab/unit/MilliW-PER-CentiM2-MicroM-SR)"""
    return QUDT_UNIT["MILLIW-PER-CENTIM2-MICROM-SR"]


def get_qudt_unit_newton_metre_per_quintic_placeholder() -> URIRef:
    """Returns the URI for QUDT unit: Newton Metre per Quintic Placeholder (http://qudt.org/vocab/unit/N-M-PER-W0dot5)"""
    return QUDT_UNIT["N-M-PER-W0DOT5"]


def get_qudt_unit_neper_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Neper per Second (http://qudt.org/vocab/unit/NP-PER-SEC)"""
    return QUDT_UNIT["NP-PER-SEC"]


def get_qudt_unit_number_per_centimetre_kiloyear() -> URIRef:
    """Returns the URI for QUDT unit: Number per Centimetre Kiloyear (http://qudt.org/vocab/unit/NUM-PER-CentiM-KiloYR)"""
    return QUDT_UNIT["NUM-PER-CENTIM-KILOYR"]


def get_qudt_unit_number_per_gram() -> URIRef:
    """Returns the URI for QUDT unit: Number per Gram (http://qudt.org/vocab/unit/NUM-PER-GM)"""
    return QUDT_UNIT["NUM-PER-GM"]


def get_qudt_unit_number_per_hectogram() -> URIRef:
    """Returns the URI for QUDT unit: Number per Hectogram (http://qudt.org/vocab/unit/NUM-PER-HectoGM)"""
    return QUDT_UNIT["NUM-PER-HECTOGM"]


def get_qudt_unit_number_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Number per Kilogram (http://qudt.org/vocab/unit/NUM-PER-KiloGM)"""
    return QUDT_UNIT["NUM-PER-KILOGM"]


def get_qudt_unit_number_per_milligram() -> URIRef:
    """Returns the URI for QUDT unit: Number per Milligram (http://qudt.org/vocab/unit/NUM-PER-MilliGM)"""
    return QUDT_UNIT["NUM-PER-MILLIGM"]


def get_qudt_unit_nanomole_per_gram_hour() -> URIRef:
    """Returns the URI for QUDT unit: Nanomole per Gram Hour (http://qudt.org/vocab/unit/NanoMOL-PER-GM-HR)"""
    return QUDT_UNIT["NANOMOL-PER-GM-HR"]


def get_qudt_unit_nanomole_per_gram_second() -> URIRef:
    """Returns the URI for QUDT unit: Nanomole per Gram Second (http://qudt.org/vocab/unit/NanoMOL-PER-GM-SEC)"""
    return QUDT_UNIT["NANOMOL-PER-GM-SEC"]


def get_qudt_unit_nanomole_per_microgram_hour() -> URIRef:
    """Returns the URI for QUDT unit: Nanomole per Microgram Hour (http://qudt.org/vocab/unit/NanoMOL-PER-MicroGM-HR)"""
    return QUDT_UNIT["NANOMOL-PER-MICROGM-HR"]


def get_qudt_unit_nanomole_per_micromole() -> URIRef:
    """Returns the URI for QUDT unit: Nanomole per Micromole (http://qudt.org/vocab/unit/NanoMOL-PER-MicroMOL)"""
    return QUDT_UNIT["NANOMOL-PER-MICROMOL"]


def get_qudt_unit_nanomole_per_micromole_day() -> URIRef:
    """Returns the URI for QUDT unit: Nanomole per Micromole Day (http://qudt.org/vocab/unit/NanoMOL-PER-MicroMOL-DAY)"""
    return QUDT_UNIT["NANOMOL-PER-MICROMOL-DAY"]


def get_qudt_unit_ohm_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Ohm per Bar (http://qudt.org/vocab/unit/OHM-PER-BAR)"""
    return QUDT_UNIT["OHM-PER-BAR"]


def get_qudt_unit_ohm_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Ohm per Kelvin (http://qudt.org/vocab/unit/OHM-PER-K)"""
    return QUDT_UNIT["OHM-PER-K"]


def get_qudt_unit_ounce_mass_foot_hour_per_cubic_inch_pound_mass() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass Foot Hour per Cubic Inch Pound Mass (http://qudt.org/vocab/unit/OZ-FT-HR-PER-IN3-LB)"""
    return QUDT_UNIT["OZ-FT-HR-PER-IN3-LB"]


def get_qudt_unit_ounce_mass_foot_second_per_cubic_inch_pound_mass() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass Foot Second per Cubic Inch Pound Mass (http://qudt.org/vocab/unit/OZ-FT-SEC-PER-IN3-LB)"""
    return QUDT_UNIT["OZ-FT-SEC-PER-IN3-LB"]


def get_qudt_unit_ounce_mass_square_foot_per_cubic_inch_pound_force_second() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass Square Foot per Cubic Inch Pound Force Second (http://qudt.org/vocab/unit/OZ-FT2-PER-IN3-LB_F-SEC)"""
    return QUDT_UNIT["OZ-FT2-PER-IN3-LB_F-SEC"]


def get_qudt_unit_ounce_mass_hour_per_cubic_inch_cubic_foot() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass Hour per Cubic Inch Cubic Foot (http://qudt.org/vocab/unit/OZ-HR-PER-IN3-FT3)"""
    return QUDT_UNIT["OZ-HR-PER-IN3-FT3"]


def get_qudt_unit_ounce_mass_hour_per_cubic_inch_gallon_uk() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass Hour per Cubic Inch Gallon (UK) (http://qudt.org/vocab/unit/OZ-HR-PER-IN3-GAL_UK)"""
    return QUDT_UNIT["OZ-HR-PER-IN3-GAL_UK"]


def get_qudt_unit_ounce_mass_hour_per_cubic_inch_us_gallon() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass Hour per Cubic Inch Us Gallon (http://qudt.org/vocab/unit/OZ-HR-PER-IN3-GAL_US)"""
    return QUDT_UNIT["OZ-HR-PER-IN3-GAL_US"]


def get_qudt_unit_ounce_mass_hour_per_cubic_inch_cubic_yard() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass Hour per Cubic Inch Cubic Yard (http://qudt.org/vocab/unit/OZ-HR-PER-IN3-YD3)"""
    return QUDT_UNIT["OZ-HR-PER-IN3-YD3"]


def get_qudt_unit_ounce_mass_hour_per_sextic_inch() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass Hour per Sextic Inch (http://qudt.org/vocab/unit/OZ-HR-PER-IN6)"""
    return QUDT_UNIT["OZ-HR-PER-IN6"]


def get_qudt_unit_ounce_mass_square_inch_per_cubic_inch_pound_force_second() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass Square Inch per Cubic Inch Pound Force Second (http://qudt.org/vocab/unit/OZ-IN2-PER-IN3-LB_F-SEC)"""
    return QUDT_UNIT["OZ-IN2-PER-IN3-LB_F-SEC"]


def get_qudt_unit_ounce_mass_minute_per_cubic_inch_cubic_foot() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass Minute per Cubic Inch Cubic Foot (http://qudt.org/vocab/unit/OZ-MIN-PER-IN3-FT3)"""
    return QUDT_UNIT["OZ-MIN-PER-IN3-FT3"]


def get_qudt_unit_ounce_mass_minute_per_cubic_inch_gallon_uk() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass Minute per Cubic Inch Gallon (UK) (http://qudt.org/vocab/unit/OZ-MIN-PER-IN3-GAL_UK)"""
    return QUDT_UNIT["OZ-MIN-PER-IN3-GAL_UK"]


def get_qudt_unit_ounce_mass_minute_per_cubic_inch_us_gallon() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass Minute per Cubic Inch Us Gallon (http://qudt.org/vocab/unit/OZ-MIN-PER-IN3-GAL_US)"""
    return QUDT_UNIT["OZ-MIN-PER-IN3-GAL_US"]


def get_qudt_unit_ounce_mass_minute_per_cubic_inch_cubic_yard() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass Minute per Cubic Inch Cubic Yard (http://qudt.org/vocab/unit/OZ-MIN-PER-IN3-YD3)"""
    return QUDT_UNIT["OZ-MIN-PER-IN3-YD3"]


def get_qudt_unit_ounce_mass_minute_per_sextic_inch() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass Minute per Sextic Inch (http://qudt.org/vocab/unit/OZ-MIN-PER-IN6)"""
    return QUDT_UNIT["OZ-MIN-PER-IN6"]


def get_qudt_unit_ounce_mass_second_per_cubic_inch_cubic_foot() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass Second per Cubic Inch Cubic Foot (http://qudt.org/vocab/unit/OZ-SEC-PER-IN3-FT3)"""
    return QUDT_UNIT["OZ-SEC-PER-IN3-FT3"]


def get_qudt_unit_ounce_mass_second_per_cubic_inch_gallon_uk() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass Second per Cubic Inch Gallon (UK) (http://qudt.org/vocab/unit/OZ-SEC-PER-IN3-GAL_UK)"""
    return QUDT_UNIT["OZ-SEC-PER-IN3-GAL_UK"]


def get_qudt_unit_ounce_mass_second_per_cubic_inch_us_gallon() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass Second per Cubic Inch Us Gallon (http://qudt.org/vocab/unit/OZ-SEC-PER-IN3-GAL_US)"""
    return QUDT_UNIT["OZ-SEC-PER-IN3-GAL_US"]


def get_qudt_unit_ounce_mass_second_per_cubic_inch_cubic_yard() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass Second per Cubic Inch Cubic Yard (http://qudt.org/vocab/unit/OZ-SEC-PER-IN3-YD3)"""
    return QUDT_UNIT["OZ-SEC-PER-IN3-YD3"]


def get_qudt_unit_ounce_mass_second_per_sextic_inch() -> URIRef:
    """Returns the URI for QUDT unit: Ounce Mass Second per Sextic Inch (http://qudt.org/vocab/unit/OZ-SEC-PER-IN6)"""
    return QUDT_UNIT["OZ-SEC-PER-IN6"]


def get_qudt_unit_pascal_metre() -> URIRef:
    """Returns the URI for QUDT unit: Pascal Metre (http://qudt.org/vocab/unit/PA-M)"""
    return QUDT_UNIT["PA-M"]


def get_qudt_unit_pascal_metre_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Pascal Metre per Second (http://qudt.org/vocab/unit/PA-M-PER-SEC)"""
    return QUDT_UNIT["PA-M-PER-SEC"]


def get_qudt_unit_pascal_metre_per_square_second() -> URIRef:
    """Returns the URI for QUDT unit: Pascal Metre per Square Second (http://qudt.org/vocab/unit/PA-M-PER-SEC2)"""
    return QUDT_UNIT["PA-M-PER-SEC2"]


def get_qudt_unit_pascal_second_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Pascal Second per Kelvin (http://qudt.org/vocab/unit/PA-SEC-PER-K)"""
    return QUDT_UNIT["PA-SEC-PER-K"]


def get_qudt_unit_square_pascal_per_square_second() -> URIRef:
    """Returns the URI for QUDT unit: Square Pascal per Square Second (http://qudt.org/vocab/unit/PA2-PER-SEC2)"""
    return QUDT_UNIT["PA2-PER-SEC2"]


def get_qudt_unit_reciprocal_kilogram_second() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Kilogram Second (http://qudt.org/vocab/unit/PER-KiloGM-SEC)"""
    return QUDT_UNIT["PER-KILOGM-SEC"]


def get_qudt_unit_reciprocal_metre_nanometre_steradian() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Metre Nanometre Steradian (http://qudt.org/vocab/unit/PER-M-NanoM-SR)"""
    return QUDT_UNIT["PER-M-NANOM-SR"]


def get_qudt_unit_reciprocal_metre_second() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Metre Second (http://qudt.org/vocab/unit/PER-M-SEC)"""
    return QUDT_UNIT["PER-M-SEC"]


def get_qudt_unit_reciprocal_metre_steradian() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Metre Steradian (http://qudt.org/vocab/unit/PER-M-SR)"""
    return QUDT_UNIT["PER-M-SR"]


def get_qudt_unit_reciprocal_micromole_litre() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Micromole Litre (http://qudt.org/vocab/unit/PER-MicroMOL-L)"""
    return QUDT_UNIT["PER-MICROMOL-L"]


def get_qudt_unit_reciprocal_pascal_second() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Pascal Second (http://qudt.org/vocab/unit/PER-PA-SEC)"""
    return QUDT_UNIT["PER-PA-SEC"]


def get_qudt_unit_reciprocal_percent() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Percent (http://qudt.org/vocab/unit/PER-PERCENT)"""
    return QUDT_UNIT["PER-PERCENT"]


def get_qudt_unit_reciprocal_radian() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Radian (http://qudt.org/vocab/unit/PER-RAD)"""
    return QUDT_UNIT["PER-RAD"]


def get_qudt_unit_reciprocal_second_steradian_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Second Steradian Square Metre (http://qudt.org/vocab/unit/PER-SEC-SR-M2)"""
    return QUDT_UNIT["PER-SEC-SR-M2"]


def get_qudt_unit_reciprocal_steradian() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Steradian (http://qudt.org/vocab/unit/PER-SR)"""
    return QUDT_UNIT["PER-SR"]


def get_qudt_unit_percent_foot_hour_per_pound_mass() -> URIRef:
    """Returns the URI for QUDT unit: Percent Foot Hour per Pound Mass (http://qudt.org/vocab/unit/PERCENT-FT-HR-PER-LB)"""
    return QUDT_UNIT["PERCENT-FT-HR-PER-LB"]


def get_qudt_unit_percent_foot_second_per_pound_mass() -> URIRef:
    """Returns the URI for QUDT unit: Percent Foot Second per Pound Mass (http://qudt.org/vocab/unit/PERCENT-FT-SEC-PER-LB)"""
    return QUDT_UNIT["PERCENT-FT-SEC-PER-LB"]


def get_qudt_unit_percent_hour_per_cubic_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Percent Hour per Cubic Centimetre (http://qudt.org/vocab/unit/PERCENT-HR-PER-CentiM3)"""
    return QUDT_UNIT["PERCENT-HR-PER-CENTIM3"]


def get_qudt_unit_percent_hour_per_cubic_foot() -> URIRef:
    """Returns the URI for QUDT unit: Percent Hour per Cubic Foot (http://qudt.org/vocab/unit/PERCENT-HR-PER-FT3)"""
    return QUDT_UNIT["PERCENT-HR-PER-FT3"]


def get_qudt_unit_percent_hour_per_gallon_uk() -> URIRef:
    """Returns the URI for QUDT unit: Percent Hour per Gallon (UK) (http://qudt.org/vocab/unit/PERCENT-HR-PER-GAL_UK)"""
    return QUDT_UNIT["PERCENT-HR-PER-GAL_UK"]


def get_qudt_unit_percent_hour_per_us_gallon() -> URIRef:
    """Returns the URI for QUDT unit: Percent Hour per Us Gallon (http://qudt.org/vocab/unit/PERCENT-HR-PER-GAL_US)"""
    return QUDT_UNIT["PERCENT-HR-PER-GAL_US"]


def get_qudt_unit_percent_hour_per_cubic_inch() -> URIRef:
    """Returns the URI for QUDT unit: Percent Hour per Cubic Inch (http://qudt.org/vocab/unit/PERCENT-HR-PER-IN3)"""
    return QUDT_UNIT["PERCENT-HR-PER-IN3"]


def get_qudt_unit_percent_hour_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: Percent Hour per Litre (http://qudt.org/vocab/unit/PERCENT-HR-PER-L)"""
    return QUDT_UNIT["PERCENT-HR-PER-L"]


def get_qudt_unit_percent_hour_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Percent Hour per Cubic Metre (http://qudt.org/vocab/unit/PERCENT-HR-PER-M3)"""
    return QUDT_UNIT["PERCENT-HR-PER-M3"]


def get_qudt_unit_percent_hour_per_cubic_yard() -> URIRef:
    """Returns the URI for QUDT unit: Percent Hour per Cubic Yard (http://qudt.org/vocab/unit/PERCENT-HR-PER-YD3)"""
    return QUDT_UNIT["PERCENT-HR-PER-YD3"]


def get_qudt_unit_percent_minute_per_cubic_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Percent Minute per Cubic Centimetre (http://qudt.org/vocab/unit/PERCENT-MIN-PER-CentiM3)"""
    return QUDT_UNIT["PERCENT-MIN-PER-CENTIM3"]


def get_qudt_unit_percent_minute_per_cubic_foot() -> URIRef:
    """Returns the URI for QUDT unit: Percent Minute per Cubic Foot (http://qudt.org/vocab/unit/PERCENT-MIN-PER-FT3)"""
    return QUDT_UNIT["PERCENT-MIN-PER-FT3"]


def get_qudt_unit_percent_minute_per_gallon_uk() -> URIRef:
    """Returns the URI for QUDT unit: Percent Minute per Gallon (UK) (http://qudt.org/vocab/unit/PERCENT-MIN-PER-GAL_UK)"""
    return QUDT_UNIT["PERCENT-MIN-PER-GAL_UK"]


def get_qudt_unit_percent_minute_per_us_gallon() -> URIRef:
    """Returns the URI for QUDT unit: Percent Minute per Us Gallon (http://qudt.org/vocab/unit/PERCENT-MIN-PER-GAL_US)"""
    return QUDT_UNIT["PERCENT-MIN-PER-GAL_US"]


def get_qudt_unit_percent_minute_per_cubic_inch() -> URIRef:
    """Returns the URI for QUDT unit: Percent Minute per Cubic Inch (http://qudt.org/vocab/unit/PERCENT-MIN-PER-IN3)"""
    return QUDT_UNIT["PERCENT-MIN-PER-IN3"]


def get_qudt_unit_percent_minute_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: Percent Minute per Litre (http://qudt.org/vocab/unit/PERCENT-MIN-PER-L)"""
    return QUDT_UNIT["PERCENT-MIN-PER-L"]


def get_qudt_unit_percent_minute_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Percent Minute per Cubic Metre (http://qudt.org/vocab/unit/PERCENT-MIN-PER-M3)"""
    return QUDT_UNIT["PERCENT-MIN-PER-M3"]


def get_qudt_unit_percent_minute_per_cubic_yard() -> URIRef:
    """Returns the URI for QUDT unit: Percent Minute per Cubic Yard (http://qudt.org/vocab/unit/PERCENT-MIN-PER-YD3)"""
    return QUDT_UNIT["PERCENT-MIN-PER-YD3"]


def get_qudt_unit_percent_per_centipoise() -> URIRef:
    """Returns the URI for QUDT unit: Percent per Centipoise (http://qudt.org/vocab/unit/PERCENT-PER-CentiPOISE)"""
    return QUDT_UNIT["PERCENT-PER-CENTIPOISE"]


def get_qudt_unit_percent_per_degree() -> URIRef:
    """Returns the URI for QUDT unit: Percent per Degree (http://qudt.org/vocab/unit/PERCENT-PER-DEG)"""
    return QUDT_UNIT["PERCENT-PER-DEG"]


def get_qudt_unit_percent_per_hundred() -> URIRef:
    """Returns the URI for QUDT unit: Percent per Hundred (http://qudt.org/vocab/unit/PERCENT-PER-HUNDRED)"""
    return QUDT_UNIT["PERCENT-PER-HUNDRED"]


def get_qudt_unit_percent_per_hundred_thousand() -> URIRef:
    """Returns the URI for QUDT unit: Percent per Hundred Thousand (http://qudt.org/vocab/unit/PERCENT-PER-HUNDRED-THOUSAND)"""
    return QUDT_UNIT["PERCENT-PER-HUNDRED-THOUSAND"]


def get_qudt_unit_percent_per_millipascal_second() -> URIRef:
    """Returns the URI for QUDT unit: Percent per Millipascal Second (http://qudt.org/vocab/unit/PERCENT-PER-MilliPA-SEC)"""
    return QUDT_UNIT["PERCENT-PER-MILLIPA-SEC"]


def get_qudt_unit_percent_per_ohm() -> URIRef:
    """Returns the URI for QUDT unit: Percent per Ohm (http://qudt.org/vocab/unit/PERCENT-PER-OHM)"""
    return QUDT_UNIT["PERCENT-PER-OHM"]


def get_qudt_unit_percent_per_pascal_second() -> URIRef:
    """Returns the URI for QUDT unit: Percent per Pascal Second (http://qudt.org/vocab/unit/PERCENT-PER-PA-SEC)"""
    return QUDT_UNIT["PERCENT-PER-PA-SEC"]


def get_qudt_unit_percent_per_percent() -> URIRef:
    """Returns the URI for QUDT unit: Percent per Percent (http://qudt.org/vocab/unit/PERCENT-PER-PERCENT)"""
    return QUDT_UNIT["PERCENT-PER-PERCENT"]


def get_qudt_unit_percent_per_poise() -> URIRef:
    """Returns the URI for QUDT unit: Percent per Poise (http://qudt.org/vocab/unit/PERCENT-PER-POISE)"""
    return QUDT_UNIT["PERCENT-PER-POISE"]


def get_qudt_unit_percent_per_ten_thousand() -> URIRef:
    """Returns the URI for QUDT unit: Percent per Ten Thousand (http://qudt.org/vocab/unit/PERCENT-PER-TEN-THOUSAND)"""
    return QUDT_UNIT["PERCENT-PER-TEN-THOUSAND"]


def get_qudt_unit_percent_per_thousand() -> URIRef:
    """Returns the URI for QUDT unit: Percent per Thousand (http://qudt.org/vocab/unit/PERCENT-PER-THOUSAND)"""
    return QUDT_UNIT["PERCENT-PER-THOUSAND"]


def get_qudt_unit_percent_per_volt() -> URIRef:
    """Returns the URI for QUDT unit: Percent per Volt (http://qudt.org/vocab/unit/PERCENT-PER-V)"""
    return QUDT_UNIT["PERCENT-PER-V"]


def get_qudt_unit_percent_second_per_cubic_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Percent Second per Cubic Centimetre (http://qudt.org/vocab/unit/PERCENT-SEC-PER-CentiM3)"""
    return QUDT_UNIT["PERCENT-SEC-PER-CENTIM3"]


def get_qudt_unit_percent_second_per_cubic_foot() -> URIRef:
    """Returns the URI for QUDT unit: Percent Second per Cubic Foot (http://qudt.org/vocab/unit/PERCENT-SEC-PER-FT3)"""
    return QUDT_UNIT["PERCENT-SEC-PER-FT3"]


def get_qudt_unit_percent_second_per_gallon_uk() -> URIRef:
    """Returns the URI for QUDT unit: Percent Second per Gallon (UK) (http://qudt.org/vocab/unit/PERCENT-SEC-PER-GAL_UK)"""
    return QUDT_UNIT["PERCENT-SEC-PER-GAL_UK"]


def get_qudt_unit_percent_second_per_us_gallon() -> URIRef:
    """Returns the URI for QUDT unit: Percent Second per Us Gallon (http://qudt.org/vocab/unit/PERCENT-SEC-PER-GAL_US)"""
    return QUDT_UNIT["PERCENT-SEC-PER-GAL_US"]


def get_qudt_unit_percent_second_per_cubic_inch() -> URIRef:
    """Returns the URI for QUDT unit: Percent Second per Cubic Inch (http://qudt.org/vocab/unit/PERCENT-SEC-PER-IN3)"""
    return QUDT_UNIT["PERCENT-SEC-PER-IN3"]


def get_qudt_unit_percent_second_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: Percent Second per Litre (http://qudt.org/vocab/unit/PERCENT-SEC-PER-L)"""
    return QUDT_UNIT["PERCENT-SEC-PER-L"]


def get_qudt_unit_percent_second_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Percent Second per Cubic Metre (http://qudt.org/vocab/unit/PERCENT-SEC-PER-M3)"""
    return QUDT_UNIT["PERCENT-SEC-PER-M3"]


def get_qudt_unit_percent_second_per_cubic_yard() -> URIRef:
    """Returns the URI for QUDT unit: Percent Second per Cubic Yard (http://qudt.org/vocab/unit/PERCENT-SEC-PER-YD3)"""
    return QUDT_UNIT["PERCENT-SEC-PER-YD3"]


def get_qudt_unit_poise_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Poise per Kelvin (http://qudt.org/vocab/unit/POISE-PER-K)"""
    return QUDT_UNIT["POISE-PER-K"]


def get_qudt_unit_parts_per_trillion_by_volume() -> URIRef:
    """Returns the URI for QUDT unit: Parts per Trillion by Volume (http://qudt.org/vocab/unit/PPT_VOL)"""
    return QUDT_UNIT["PPT_VOL"]


def get_qudt_unit_picoampere_per_hectopascal() -> URIRef:
    """Returns the URI for QUDT unit: Picoampere per Hectopascal (http://qudt.org/vocab/unit/PicoA-PER-HectoPA)"""
    return QUDT_UNIT["PICOA-PER-HECTOPA"]


def get_qudt_unit_picoampere_per_micromole_litre() -> URIRef:
    """Returns the URI for QUDT unit: Picoampere per Micromole Litre (http://qudt.org/vocab/unit/PicoA-PER-MicroMOL-L)"""
    return QUDT_UNIT["PICOA-PER-MICROMOL-L"]


def get_qudt_unit_picomole_per_metre_watt_second() -> URIRef:
    """Returns the URI for QUDT unit: Picomole per Metre Watt Second (http://qudt.org/vocab/unit/PicoMOL-PER-M-W-SEC)"""
    return QUDT_UNIT["PICOMOL-PER-M-W-SEC"]


def get_qudt_unit_picowatt_per_square_centimetre_litre() -> URIRef:
    """Returns the URI for QUDT unit: Picowatt per Square Centimetre Litre (http://qudt.org/vocab/unit/PicoW-PER-CentiM2-L)"""
    return QUDT_UNIT["PICOW-PER-CENTIM2-L"]


def get_qudt_unit_second_per_square_foot() -> URIRef:
    """Returns the URI for QUDT unit: Second per Square Foot (http://qudt.org/vocab/unit/SEC-PER-FT2)"""
    return QUDT_UNIT["SEC-PER-FT2"]


def get_qudt_unit_second_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: Second per Metre (http://qudt.org/vocab/unit/SEC-PER-M)"""
    return QUDT_UNIT["SEC-PER-M"]


def get_qudt_unit_sone() -> URIRef:
    """Returns the URI for QUDT unit: Sone (http://qudt.org/vocab/unit/SON)"""
    return QUDT_UNIT["SON"]


def get_qudt_unit_spin_quantum_number() -> URIRef:
    """Returns the URI for QUDT unit: Spin Quantum Number (http://qudt.org/vocab/unit/SPIN_QUANTUM_NUMBER)"""
    return QUDT_UNIT["SPIN_QUANTUM_NUMBER"]


def get_qudt_unit_stokes_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Stokes per Bar (http://qudt.org/vocab/unit/ST-PER-BAR)"""
    return QUDT_UNIT["ST-PER-BAR"]


def get_qudt_unit_stokes_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Stokes per Kelvin (http://qudt.org/vocab/unit/ST-PER-K)"""
    return QUDT_UNIT["ST-PER-K"]


def get_qudt_unit_stokes_per_pascal() -> URIRef:
    """Returns the URI for QUDT unit: Stokes per Pascal (http://qudt.org/vocab/unit/ST-PER-PA)"""
    return QUDT_UNIT["ST-PER-PA"]


def get_qudt_unit_tonne_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Tonne per Bar (http://qudt.org/vocab/unit/TONNE-PER-BAR)"""
    return QUDT_UNIT["TONNE-PER-BAR"]


def get_qudt_unit_tonne_per_day_bar() -> URIRef:
    """Returns the URI for QUDT unit: Tonne per Day Bar (http://qudt.org/vocab/unit/TONNE-PER-DAY-BAR)"""
    return QUDT_UNIT["TONNE-PER-DAY-BAR"]


def get_qudt_unit_tonne_per_day_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Tonne per Day Kelvin (http://qudt.org/vocab/unit/TONNE-PER-DAY-K)"""
    return QUDT_UNIT["TONNE-PER-DAY-K"]


def get_qudt_unit_tonne_per_hour_bar() -> URIRef:
    """Returns the URI for QUDT unit: Tonne per Hour Bar (http://qudt.org/vocab/unit/TONNE-PER-HR-BAR)"""
    return QUDT_UNIT["TONNE-PER-HR-BAR"]


def get_qudt_unit_tonne_per_hour_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Tonne per Hour Kelvin (http://qudt.org/vocab/unit/TONNE-PER-HR-K)"""
    return QUDT_UNIT["TONNE-PER-HR-K"]


def get_qudt_unit_tonne_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Tonne per Kelvin (http://qudt.org/vocab/unit/TONNE-PER-K)"""
    return QUDT_UNIT["TONNE-PER-K"]


def get_qudt_unit_tonne_per_cubic_metre_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Tonne per Cubic Metre Kelvin (http://qudt.org/vocab/unit/TONNE-PER-M3-K)"""
    return QUDT_UNIT["TONNE-PER-M3-K"]


def get_qudt_unit_tonne_per_minute_bar() -> URIRef:
    """Returns the URI for QUDT unit: Tonne per Minute Bar (http://qudt.org/vocab/unit/TONNE-PER-MIN-BAR)"""
    return QUDT_UNIT["TONNE-PER-MIN-BAR"]


def get_qudt_unit_tonne_per_minute_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Tonne per Minute Kelvin (http://qudt.org/vocab/unit/TONNE-PER-MIN-K)"""
    return QUDT_UNIT["TONNE-PER-MIN-K"]


def get_qudt_unit_tonne_per_second_bar() -> URIRef:
    """Returns the URI for QUDT unit: Tonne per Second Bar (http://qudt.org/vocab/unit/TONNE-PER-SEC-BAR)"""
    return QUDT_UNIT["TONNE-PER-SEC-BAR"]


def get_qudt_unit_tonne_per_second_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Tonne per Second Kelvin (http://qudt.org/vocab/unit/TONNE-PER-SEC-K)"""
    return QUDT_UNIT["TONNE-PER-SEC-K"]


def get_qudt_unit_metric_ton_per_bar() -> URIRef:
    """Returns the URI for QUDT unit: Metric Ton per Bar (http://qudt.org/vocab/unit/TON_Metric-PER-BAR)"""
    return QUDT_UNIT["TON_METRIC-PER-BAR"]


def get_qudt_unit_metric_ton_per_day_bar() -> URIRef:
    """Returns the URI for QUDT unit: Metric Ton per Day Bar (http://qudt.org/vocab/unit/TON_Metric-PER-DAY-BAR)"""
    return QUDT_UNIT["TON_METRIC-PER-DAY-BAR"]


def get_qudt_unit_metric_ton_per_day_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Metric Ton per Day Kelvin (http://qudt.org/vocab/unit/TON_Metric-PER-DAY-K)"""
    return QUDT_UNIT["TON_METRIC-PER-DAY-K"]


def get_qudt_unit_metric_ton_per_hour_bar() -> URIRef:
    """Returns the URI for QUDT unit: Metric Ton per Hour Bar (http://qudt.org/vocab/unit/TON_Metric-PER-HR-BAR)"""
    return QUDT_UNIT["TON_METRIC-PER-HR-BAR"]


def get_qudt_unit_metric_ton_per_hour_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Metric Ton per Hour Kelvin (http://qudt.org/vocab/unit/TON_Metric-PER-HR-K)"""
    return QUDT_UNIT["TON_METRIC-PER-HR-K"]


def get_qudt_unit_metric_ton_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Metric Ton per Kelvin (http://qudt.org/vocab/unit/TON_Metric-PER-K)"""
    return QUDT_UNIT["TON_METRIC-PER-K"]


def get_qudt_unit_metric_ton_per_cubic_metre_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Metric Ton per Cubic Metre Kelvin (http://qudt.org/vocab/unit/TON_Metric-PER-M3-K)"""
    return QUDT_UNIT["TON_METRIC-PER-M3-K"]


def get_qudt_unit_metric_ton_per_minute_bar() -> URIRef:
    """Returns the URI for QUDT unit: Metric Ton per Minute Bar (http://qudt.org/vocab/unit/TON_Metric-PER-MIN-BAR)"""
    return QUDT_UNIT["TON_METRIC-PER-MIN-BAR"]


def get_qudt_unit_metric_ton_per_minute_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Metric Ton per Minute Kelvin (http://qudt.org/vocab/unit/TON_Metric-PER-MIN-K)"""
    return QUDT_UNIT["TON_METRIC-PER-MIN-K"]


def get_qudt_unit_metric_ton_per_second_bar() -> URIRef:
    """Returns the URI for QUDT unit: Metric Ton per Second Bar (http://qudt.org/vocab/unit/TON_Metric-PER-SEC-BAR)"""
    return QUDT_UNIT["TON_METRIC-PER-SEC-BAR"]


def get_qudt_unit_metric_ton_per_second_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Metric Ton per Second Kelvin (http://qudt.org/vocab/unit/TON_Metric-PER-SEC-K)"""
    return QUDT_UNIT["TON_METRIC-PER-SEC-K"]


def get_qudt_unit_short_ton_per_degree_fahrenheit() -> URIRef:
    """Returns the URI for QUDT unit: Short Ton per Degree Fahrenheit (http://qudt.org/vocab/unit/TON_SHORT-PER-DEG_F)"""
    return QUDT_UNIT["TON_SHORT-PER-DEG_F"]


def get_qudt_unit_short_ton_per_hour_degree_fahrenheit() -> URIRef:
    """Returns the URI for QUDT unit: Short Ton per Hour Degree Fahrenheit (http://qudt.org/vocab/unit/TON_SHORT-PER-HR-DEG_F)"""
    return QUDT_UNIT["TON_SHORT-PER-HR-DEG_F"]


def get_qudt_unit_short_ton_per_hour_psi() -> URIRef:
    """Returns the URI for QUDT unit: Short Ton per Hour Psi (http://qudt.org/vocab/unit/TON_SHORT-PER-HR-PSI)"""
    return QUDT_UNIT["TON_SHORT-PER-HR-PSI"]


def get_qudt_unit_short_ton_per_psi() -> URIRef:
    """Returns the URI for QUDT unit: Short Ton per Psi (http://qudt.org/vocab/unit/TON_SHORT-PER-PSI)"""
    return QUDT_UNIT["TON_SHORT-PER-PSI"]


def get_qudt_unit_unknown() -> URIRef:
    """Returns the URI for QUDT unit: Unknown (http://qudt.org/vocab/unit/UNKNOWN)"""
    return QUDT_UNIT["UNKNOWN"]


def get_qudt_unit_volt_per_litre_minute() -> URIRef:
    """Returns the URI for QUDT unit: Volt per Litre Minute (http://qudt.org/vocab/unit/V-PER-L-MIN)"""
    return QUDT_UNIT["V-PER-L-MIN"]


def get_qudt_unit_volt_per_volt() -> URIRef:
    """Returns the URI for QUDT unit: Volt per Volt (http://qudt.org/vocab/unit/V-PER-V)"""
    return QUDT_UNIT["V-PER-V"]


def get_qudt_unit_volt_ampere_reactive_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Volt Ampere Reactive per Kelvin (http://qudt.org/vocab/unit/VAR-PER-K)"""
    return QUDT_UNIT["VAR-PER-K"]


def get_qudt_unit_watt_hour_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: Watt Hour per Litre (http://qudt.org/vocab/unit/W-HR-PER-L)"""
    return QUDT_UNIT["W-HR-PER-L"]


def get_qudt_unit_watt_metre_per_square_metre_steradian() -> URIRef:
    """Returns the URI for QUDT unit: Watt Metre per Square Metre Steradian (http://qudt.org/vocab/unit/W-M-PER-M2-SR)"""
    return QUDT_UNIT["W-M-PER-M2-SR"]


def get_qudt_unit_watt_per_square_metre_metre() -> URIRef:
    """Returns the URI for QUDT unit: Watt per Square Metre Metre (http://qudt.org/vocab/unit/W-PER-M2-M)"""
    return QUDT_UNIT["W-PER-M2-M"]


def get_qudt_unit_watt_per_square_metre_metre_steradian() -> URIRef:
    """Returns the URI for QUDT unit: Watt per Square Metre Metre Steradian (http://qudt.org/vocab/unit/W-PER-M2-M-SR)"""
    return QUDT_UNIT["W-PER-M2-M-SR"]


def get_qudt_unit_watt_per_square_metre_nanometre() -> URIRef:
    """Returns the URI for QUDT unit: Watt per Square Metre Nanometre (http://qudt.org/vocab/unit/W-PER-M2-NanoM)"""
    return QUDT_UNIT["W-PER-M2-NANOM"]


def get_qudt_unit_yard_per_psi() -> URIRef:
    """Returns the URI for QUDT unit: Yard per Psi (http://qudt.org/vocab/unit/YD-PER-PSI)"""
    return QUDT_UNIT["YD-PER-PSI"]


def get_qudt_unit_cubic_yard_per_psi() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Yard per Psi (http://qudt.org/vocab/unit/YD3-PER-PSI)"""
    return QUDT_UNIT["YD3-PER-PSI"]


def get_qudt_unit_kilogram_per_pascal_second_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Pascal Second Metre (http://qudt.org/vocab/unit/KiloGM-PER-PA-SEC-M)"""
    return QUDT_UNIT["KILOGM-PER-PA-SEC-M"]


def get_qudt_unit_kilogram_per_square_metre_pascal_second() -> URIRef:
    """Returns the URI for QUDT unit: Kilogram per Square Metre Pascal Second (http://qudt.org/vocab/unit/KiloGM-PER-M2-PA-SEC)"""
    return QUDT_UNIT["KILOGM-PER-M2-PA-SEC"]


def get_qudt_unit_nanogram_per_square_metre_pascal_second() -> URIRef:
    """Returns the URI for QUDT unit: Nanogram per Square Metre Pascal Second (http://qudt.org/vocab/unit/NanoGM-PER-M2-PA-SEC)"""
    return QUDT_UNIT["NANOGM-PER-M2-PA-SEC"]


def get_qudt_unit_metric_perm() -> URIRef:
    """Returns the URI for QUDT unit: Metric Perm (http://qudt.org/vocab/unit/PERM_Metric)"""
    return QUDT_UNIT["PERM_METRIC"]


def get_qudt_unit_u_s_perm() -> URIRef:
    """Returns the URI for QUDT unit: U.s. Perm (http://qudt.org/vocab/unit/PERM_US)"""
    return QUDT_UNIT["PERM_US"]


def get_qudt_unit_litre_per_second_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Litre per Second Square Metre (http://qudt.org/vocab/unit/L-PER-SEC-M2)"""
    return QUDT_UNIT["L-PER-SEC-M2"]


def get_qudt_unit_second_per_radian_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Second per Radian Cubic Metre (http://qudt.org/vocab/unit/SEC-PER-RAD-M3)"""
    return QUDT_UNIT["SEC-PER-RAD-M3"]


def get_qudt_unit_frame_per_second() -> URIRef:
    """Returns the URI for QUDT unit: Frame per Second (http://qudt.org/vocab/unit/FRAME-PER-SEC)"""
    return QUDT_UNIT["FRAME-PER-SEC"]


def get_qudt_unit_cubic_centimetre_per_cubic_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Centimetre per Cubic Centimetre (http://qudt.org/vocab/unit/CentiM3-PER-CentiM3)"""
    return QUDT_UNIT["CENTIM3-PER-CENTIM3"]


def get_qudt_unit_cubic_centimetre_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Centimetre per Cubic Metre (http://qudt.org/vocab/unit/CentiM3-PER-M3)"""
    return QUDT_UNIT["CENTIM3-PER-M3"]


def get_qudt_unit_cubic_decimetre_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Decimetre per Cubic Metre (http://qudt.org/vocab/unit/DeciM3-PER-M3)"""
    return QUDT_UNIT["DECIM3-PER-M3"]


def get_qudt_unit_litre_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: Litre per Litre (http://qudt.org/vocab/unit/L-PER-L)"""
    return QUDT_UNIT["L-PER-L"]


def get_qudt_unit_cubic_metre_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Metre per Cubic Metre (http://qudt.org/vocab/unit/M3-PER-M3)"""
    return QUDT_UNIT["M3-PER-M3"]


def get_qudt_unit_microlitre_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: Microlitre per Litre (http://qudt.org/vocab/unit/MicroL-PER-L)"""
    return QUDT_UNIT["MICROL-PER-L"]


def get_qudt_unit_cubic_micrometre_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Micrometre per Cubic Metre (http://qudt.org/vocab/unit/MicroM3-PER-M3)"""
    return QUDT_UNIT["MICROM3-PER-M3"]


def get_qudt_unit_cubic_micrometre_per_millilitre() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Micrometre per Millilitre (http://qudt.org/vocab/unit/MicroM3-PER-MilliL)"""
    return QUDT_UNIT["MICROM3-PER-MILLIL"]


def get_qudt_unit_millilitre_per_litre() -> URIRef:
    """Returns the URI for QUDT unit: Millilitre per Litre (http://qudt.org/vocab/unit/MilliL-PER-L)"""
    return QUDT_UNIT["MILLIL-PER-L"]


def get_qudt_unit_millilitre_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Millilitre per Cubic Metre (http://qudt.org/vocab/unit/MilliL-PER-M3)"""
    return QUDT_UNIT["MILLIL-PER-M3"]


def get_qudt_unit_cubic_millimetre_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Millimetre per Cubic Metre (http://qudt.org/vocab/unit/MilliM3-PER-M3)"""
    return QUDT_UNIT["MILLIM3-PER-M3"]


def get_qudt_unit_cubic_metre_per_hectare() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Metre per Hectare (http://qudt.org/vocab/unit/M3-PER-HA)"""
    return QUDT_UNIT["M3-PER-HA"]


def get_qudt_unit_cubic_metre_per_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Metre per Square Metre (http://qudt.org/vocab/unit/M3-PER-M2)"""
    return QUDT_UNIT["M3-PER-M2"]


def get_qudt_unit_cubic_centimetre_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Centimetre per Kelvin (http://qudt.org/vocab/unit/CentiM3-PER-K)"""
    return QUDT_UNIT["CENTIM3-PER-K"]


def get_qudt_unit_cubic_foot_per_degree_fahrenheit() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Foot per Degree Fahrenheit (http://qudt.org/vocab/unit/FT3-PER-DEG_F)"""
    return QUDT_UNIT["FT3-PER-DEG_F"]


def get_qudt_unit_litre_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Litre per Kelvin (http://qudt.org/vocab/unit/L-PER-K)"""
    return QUDT_UNIT["L-PER-K"]


def get_qudt_unit_cubic_metre_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Metre per Kelvin (http://qudt.org/vocab/unit/M3-PER-K)"""
    return QUDT_UNIT["M3-PER-K"]


def get_qudt_unit_millilitre_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Millilitre per Kelvin (http://qudt.org/vocab/unit/MilliL-PER-K)"""
    return QUDT_UNIT["MILLIL-PER-K"]


def get_qudt_unit_cubic_yard_per_degree_fahrenheit() -> URIRef:
    """Returns the URI for QUDT unit: Cubic Yard per Degree Fahrenheit (http://qudt.org/vocab/unit/YD3-PER-DEG_F)"""
    return QUDT_UNIT["YD3-PER-DEG_F"]


def get_qudt_unit_bit_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Bit per Cubic Metre (http://qudt.org/vocab/unit/BIT-PER-M3)"""
    return QUDT_UNIT["BIT-PER-M3"]


def get_qudt_unit_exbibit_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Exbibit per Cubic Metre (http://qudt.org/vocab/unit/ExbiBIT-PER-M3)"""
    return QUDT_UNIT["EXBIBIT-PER-M3"]


def get_qudt_unit_gibibit_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Gibibit per Cubic Metre (http://qudt.org/vocab/unit/GibiBIT-PER-M3)"""
    return QUDT_UNIT["GIBIBIT-PER-M3"]


def get_qudt_unit_kibibit_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kibibit per Cubic Metre (http://qudt.org/vocab/unit/KibiBIT-PER-M3)"""
    return QUDT_UNIT["KIBIBIT-PER-M3"]


def get_qudt_unit_mebibit_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Mebibit per Cubic Metre (http://qudt.org/vocab/unit/MebiBIT-PER-M3)"""
    return QUDT_UNIT["MEBIBIT-PER-M3"]


def get_qudt_unit_pebibit_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Pebibit per Cubic Metre (http://qudt.org/vocab/unit/PebiBIT-PER-M3)"""
    return QUDT_UNIT["PEBIBIT-PER-M3"]


def get_qudt_unit_tebibit_per_cubic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Tebibit per Cubic Metre (http://qudt.org/vocab/unit/TebiBIT-PER-M3)"""
    return QUDT_UNIT["TEBIBIT-PER-M3"]


def get_qudt_unit_millilitre_per_square_centimetre_minute() -> URIRef:
    """Returns the URI for QUDT unit: Millilitre per Square Centimetre Minute (http://qudt.org/vocab/unit/MilliL-PER-CentiM2-MIN)"""
    return QUDT_UNIT["MILLIL-PER-CENTIM2-MIN"]


def get_qudt_unit_millilitre_per_square_centimetre_second() -> URIRef:
    """Returns the URI for QUDT unit: Millilitre per Square Centimetre Second (http://qudt.org/vocab/unit/MilliL-PER-CentiM2-SEC)"""
    return QUDT_UNIT["MILLIL-PER-CENTIM2-SEC"]


def get_qudt_unit_thermochemical_calorie_per_cubic_centimetre_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Thermochemical Calorie per Cubic Centimetre Kelvin (http://qudt.org/vocab/unit/CAL_TH-PER-CentiM3-K)"""
    return QUDT_UNIT["CAL_TH-PER-CENTIM3-K"]


def get_qudt_unit_joule_per_cubic_centimetre_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Joule per Cubic Centimetre Kelvin (http://qudt.org/vocab/unit/J-PER-CentiM3-K)"""
    return QUDT_UNIT["J-PER-CENTIM3-K"]


def get_qudt_unit_joule_per_cubic_metre_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Joule per Cubic Metre Kelvin (http://qudt.org/vocab/unit/J-PER-M3-K)"""
    return QUDT_UNIT["J-PER-M3-K"]


def get_qudt_unit_pound_force_per_square_inch_degree_fahrenheit() -> URIRef:
    """Returns the URI for QUDT unit: Pound Force per Square Inch Degree Fahrenheit (http://qudt.org/vocab/unit/LB_F-PER-IN2-DEG_F)"""
    return QUDT_UNIT["LB_F-PER-IN2-DEG_F"]


def get_qudt_unit_millibar_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Millibar per Kelvin (http://qudt.org/vocab/unit/MilliBAR-PER-K)"""
    return QUDT_UNIT["MILLIBAR-PER-K"]


def get_qudt_unit_sextic_centimetre() -> URIRef:
    """Returns the URI for QUDT unit: Sextic Centimetre (http://qudt.org/vocab/unit/CentiM6)"""
    return QUDT_UNIT["CENTIM6"]


def get_qudt_unit_sextic_metre() -> URIRef:
    """Returns the URI for QUDT unit: Sextic Metre (http://qudt.org/vocab/unit/M6)"""
    return QUDT_UNIT["M6"]


def get_qudt_unit_kilonewton_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Kilonewton Square Metre (http://qudt.org/vocab/unit/KiloN-M2)"""
    return QUDT_UNIT["KILON-M2"]


def get_qudt_unit_newton_square_metre() -> URIRef:
    """Returns the URI for QUDT unit: Newton Square Metre (http://qudt.org/vocab/unit/N-M2)"""
    return QUDT_UNIT["N-M2"]


def get_qudt_unit__2pirad() -> URIRef:
    """Returns the URI for QUDT unit: 2pirad (http://qudt.org/vocab/unit/2PiRAD)"""
    return QUDT_UNIT["2PIRAD"]


def get_qudt_unit_swiss_francs_per_kilogram() -> URIRef:
    """Returns the URI for QUDT unit: Swiss Francs per KiloGram (http://qudt.org/vocab/unit/CHF-PER-KiloGM)"""
    return QUDT_UNIT["CHF-PER-KILOGM"]


def get_qudt_unit_centimetre_of_water() -> URIRef:
    """Returns the URI for QUDT unit: Centimetre of Water (http://qudt.org/vocab/unit/CM_H2O)"""
    return QUDT_UNIT["CM_H2O"]


def get_qudt_unit_exavolt_ampere() -> URIRef:
    """Returns the URI for QUDT unit: Exavolt Ampere (http://qudt.org/vocab/unit/ExaV-A)"""
    return QUDT_UNIT["EXAV-A"]


def get_qudt_unit_long_furlong() -> URIRef:
    """Returns the URI for QUDT unit: Long Furlong (http://qudt.org/vocab/unit/FUR_Long)"""
    return QUDT_UNIT["FUR_LONG"]


def get_qudt_unit_gigavolt_ampere() -> URIRef:
    """Returns the URI for QUDT unit: Gigavolt Ampere (http://qudt.org/vocab/unit/GigaV-A)"""
    return QUDT_UNIT["GIGAV-A"]


def get_qudt_unit_gigavolt_ampere_reactive() -> URIRef:
    """Returns the URI for QUDT unit: GigaVolt Ampere Reactive (http://qudt.org/vocab/unit/GigaV-A_Reactive)"""
    return QUDT_UNIT["GIGAV-A_REACTIVE"]


def get_qudt_unit_gs() -> URIRef:
    """Returns the URI for QUDT unit: Gs (http://qudt.org/vocab/unit/Gs)"""
    return QUDT_UNIT["GS"]


def get_qudt_unit_heart_beat() -> URIRef:
    """Returns the URI for QUDT unit: Heart Beat (http://qudt.org/vocab/unit/HeartBeat)"""
    return QUDT_UNIT["HEARTBEAT"]


def get_qudt_unit_inch_per_2pirad() -> URIRef:
    """Returns the URI for QUDT unit: Inch per 2pirad (http://qudt.org/vocab/unit/IN-PER-2PiRAD)"""
    return QUDT_UNIT["IN-PER-2PIRAD"]


def get_qudt_unit_kilovolt_ampere() -> URIRef:
    """Returns the URI for QUDT unit: Kilovolt Ampere (http://qudt.org/vocab/unit/KiloV-A)"""
    return QUDT_UNIT["KILOV-A"]


def get_qudt_unit_kilovolt_ampere_hour() -> URIRef:
    """Returns the URI for QUDT unit: Kilovolt Ampere Hour (http://qudt.org/vocab/unit/KiloV-A-HR)"""
    return QUDT_UNIT["KILOV-A-HR"]


def get_qudt_unit_kilovolt_ampere_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Kilovolt Ampere per Kelvin (http://qudt.org/vocab/unit/KiloV-A-PER-K)"""
    return QUDT_UNIT["KILOV-A-PER-K"]


def get_qudt_unit_kilovolt_ampere_reactive() -> URIRef:
    """Returns the URI for QUDT unit: KiloVolt Ampere Reactive (http://qudt.org/vocab/unit/KiloV-A_Reactive)"""
    return QUDT_UNIT["KILOV-A_REACTIVE"]


def get_qudt_unit_kilovolt_ampere_reactive_hour() -> URIRef:
    """Returns the URI for QUDT unit: KiloVolt Ampere Reactive Hour (http://qudt.org/vocab/unit/KiloV-A_Reactive-HR)"""
    return QUDT_UNIT["KILOV-A_REACTIVE-HR"]


def get_qudt_unit_kilovolt_ampere_reactive_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: KiloVolt Ampere Reactive per Kelvin (http://qudt.org/vocab/unit/KiloV-A_Reactive-PER-K)"""
    return QUDT_UNIT["KILOV-A_REACTIVE-PER-K"]


def get_qudt_unit_pound_per_gallon() -> URIRef:
    """Returns the URI for QUDT unit: Pound per Gallon (http://qudt.org/vocab/unit/LB-PER-GAL)"""
    return QUDT_UNIT["LB-PER-GAL"]


def get_qudt_unit_mil_angle_nato() -> URIRef:
    """Returns the URI for QUDT unit: Mil Angle (nato) (http://qudt.org/vocab/unit/MIL)"""
    return QUDT_UNIT["MIL"]


def get_qudt_unit_million_us_dollars_per_flight() -> URIRef:
    """Returns the URI for QUDT unit: Million Us Dollars per Flight (http://qudt.org/vocab/unit/MegaDOLLAR_US-PER-FLIGHT)"""
    return QUDT_UNIT["MEGADOLLAR_US-PER-FLIGHT"]


def get_qudt_unit_megavolt_ampere() -> URIRef:
    """Returns the URI for QUDT unit: Megavolt Ampere (http://qudt.org/vocab/unit/MegaV-A)"""
    return QUDT_UNIT["MEGAV-A"]


def get_qudt_unit_megavolt_ampere_hour() -> URIRef:
    """Returns the URI for QUDT unit: Megavolt Ampere Hour (http://qudt.org/vocab/unit/MegaV-A-HR)"""
    return QUDT_UNIT["MEGAV-A-HR"]


def get_qudt_unit_megavolt_ampere_reactive() -> URIRef:
    """Returns the URI for QUDT unit: MegaVolt Ampere Reactive (http://qudt.org/vocab/unit/MegaV-A_Reactive)"""
    return QUDT_UNIT["MEGAV-A_REACTIVE"]


def get_qudt_unit_megavolt_ampere_reactive_hour() -> URIRef:
    """Returns the URI for QUDT unit: MegaVolt Ampere Reactive Hour (http://qudt.org/vocab/unit/MegaV-A_Reactive-HR)"""
    return QUDT_UNIT["MEGAV-A_REACTIVE-HR"]


def get_qudt_unit_microgals_per_metre() -> URIRef:
    """Returns the URI for QUDT unit: MicroGals per Metre (http://qudt.org/vocab/unit/MicroGAL-PER-M)"""
    return QUDT_UNIT["MICROGAL-PER-M"]


def get_qudt_unit_microvolt_ampere() -> URIRef:
    """Returns the URI for QUDT unit: Microvolt Ampere (http://qudt.org/vocab/unit/MicroV-A)"""
    return QUDT_UNIT["MICROV-A"]


def get_qudt_unit_microvolt_ampere_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Microvolt Ampere per Kelvin (http://qudt.org/vocab/unit/MicroV-A-PER-K)"""
    return QUDT_UNIT["MICROV-A-PER-K"]


def get_qudt_unit_microvolt_ampere_reactive() -> URIRef:
    """Returns the URI for QUDT unit: MicroVolt Ampere Reactive (http://qudt.org/vocab/unit/MicroV-A_Reactive)"""
    return QUDT_UNIT["MICROV-A_REACTIVE"]


def get_qudt_unit_microvolt_ampere_reactive_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: MicroVolt Ampere Reactive per Kelvin (http://qudt.org/vocab/unit/MicroV-A_Reactive-PER-K)"""
    return QUDT_UNIT["MICROV-A_REACTIVE-PER-K"]


def get_qudt_unit_millivolt_ampere() -> URIRef:
    """Returns the URI for QUDT unit: Millivolt Ampere (http://qudt.org/vocab/unit/MilliV-A)"""
    return QUDT_UNIT["MILLIV-A"]


def get_qudt_unit_millivolt_ampere_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: Millivolt Ampere per Kelvin (http://qudt.org/vocab/unit/MilliV-A-PER-K)"""
    return QUDT_UNIT["MILLIV-A-PER-K"]


def get_qudt_unit_millivolt_ampere_reactive() -> URIRef:
    """Returns the URI for QUDT unit: MilliVolt Ampere Reactive (http://qudt.org/vocab/unit/MilliV-A_Reactive)"""
    return QUDT_UNIT["MILLIV-A_REACTIVE"]


def get_qudt_unit_millivolt_ampere_reactive_per_kelvin() -> URIRef:
    """Returns the URI for QUDT unit: MilliVolt Ampere Reactive per Kelvin (http://qudt.org/vocab/unit/MilliV-A_Reactive-PER-K)"""
    return QUDT_UNIT["MILLIV-A_REACTIVE-PER-K"]


def get_qudt_unit_million_us_dollars_per_year() -> URIRef:
    """Returns the URI for QUDT unit: Million Us Dollars per Year (http://qudt.org/vocab/unit/MillionUSD-PER-YR)"""
    return QUDT_UNIT["MILLIONUSD-PER-YR"]


def get_qudt_unit_nanovolt_ampere() -> URIRef:
    """Returns the URI for QUDT unit: Nanovolt Ampere (http://qudt.org/vocab/unit/NanoV-A)"""
    return QUDT_UNIT["NANOV-A"]


def get_qudt_unit_nanovolt_ampere_reactive() -> URIRef:
    """Returns the URI for QUDT unit: NanoVolt Ampere Reactive (http://qudt.org/vocab/unit/NanoV-A_Reactive)"""
    return QUDT_UNIT["NANOV-A_REACTIVE"]


def get_qudt_unit_reciprocal_kilovolt_ampere_hour() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Kilovolt Ampere Hour (http://qudt.org/vocab/unit/PER-KiloV-A-HR)"""
    return QUDT_UNIT["PER-KILOV-A-HR"]


def get_qudt_unit_reciprocal_mille_psi() -> URIRef:
    """Returns the URI for QUDT unit: Reciprocal Mille Psi (http://qudt.org/vocab/unit/PER-MILLE-PSI)"""
    return QUDT_UNIT["PER-MILLE-PSI"]


def get_qudt_unit_percent_per_one_hundred_thousand() -> URIRef:
    """Returns the URI for QUDT unit: Percent per One Hundred Thousand (http://qudt.org/vocab/unit/PERCENT-PER-100KiloCount)"""
    return QUDT_UNIT["PERCENT-PER-100KILOCOUNT"]


def get_qudt_unit_perm_0_c() -> URIRef:
    """Returns the URI for QUDT unit: Perm (0 °C) (http://qudt.org/vocab/unit/PERM_0DEG_C)"""
    return QUDT_UNIT["PERM_0DEG_C"]


def get_qudt_unit_perm_23_c() -> URIRef:
    """Returns the URI for QUDT unit: Perm (23 °C) (http://qudt.org/vocab/unit/PERM_23DEG_C)"""
    return QUDT_UNIT["PERM_23DEG_C"]


def get_qudt_unit_pixel() -> URIRef:
    """Returns the URI for QUDT unit: Pixel (http://qudt.org/vocab/unit/PIXEL)"""
    return QUDT_UNIT["PIXEL"]


def get_qudt_unit_petavolt_ampere() -> URIRef:
    """Returns the URI for QUDT unit: Petavolt Ampere (http://qudt.org/vocab/unit/PetaV-A)"""
    return QUDT_UNIT["PETAV-A"]


def get_qudt_unit_picovolt_ampere() -> URIRef:
    """Returns the URI for QUDT unit: Picovolt Ampere (http://qudt.org/vocab/unit/PicoV-A)"""
    return QUDT_UNIT["PICOV-A"]


def get_qudt_unit_picovolt_ampere_reactive() -> URIRef:
    """Returns the URI for QUDT unit: PicoVolt Ampere Reactive (http://qudt.org/vocab/unit/PicoV-A_Reactive)"""
    return QUDT_UNIT["PICOV-A_REACTIVE"]


def get_qudt_unit_teravolt_ampere() -> URIRef:
    """Returns the URI for QUDT unit: Teravolt Ampere (http://qudt.org/vocab/unit/TeraV-A)"""
    return QUDT_UNIT["TERAV-A"]


def get_qudt_unit_teravolt_ampere_reactive() -> URIRef:
    """Returns the URI for QUDT unit: TeraVolt Ampere Reactive (http://qudt.org/vocab/unit/TeraV-A_Reactive)"""
    return QUDT_UNIT["TERAV-A_REACTIVE"]


def get_qudt_unit_failures_in_time() -> URIRef:
    """Returns the URI for QUDT unit: Failures in Time (http://qudt.org/vocab/unit/failures-in-time)"""
    return QUDT_UNIT["FAILURES-IN-TIME"]
