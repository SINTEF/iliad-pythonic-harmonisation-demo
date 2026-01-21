"""This module contains functions for the quantity kinds in QUDT."""

from rdflib import URIRef
from ontology_library.constants import QUDT_QUANTITY_KIND


def get_qudt_quantity_kind_dimensionless_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Dimensionless Ratio (http://qudt.org/vocab/quantitykind/DimensionlessRatio)"""
    return QUDT_QUANTITY_KIND["DIMENSIONLESSRATIO"]


def get_qudt_quantity_kind_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: mass (http://qudt.org/vocab/quantitykind/Mass)"""
    return QUDT_QUANTITY_KIND["MASS"]


def get_qudt_quantity_kind_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: energy (http://qudt.org/vocab/quantitykind/Energy)"""
    return QUDT_QUANTITY_KIND["ENERGY"]


def get_qudt_quantity_kind_molar_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: molar mass (http://qudt.org/vocab/quantitykind/MolarMass)"""
    return QUDT_QUANTITY_KIND["MOLARMASS"]


def get_qudt_quantity_kind_length() -> URIRef:
    """Returns the URI for QUDT quantity kind: length (http://qudt.org/vocab/quantitykind/Length)"""
    return QUDT_QUANTITY_KIND["LENGTH"]


def get_qudt_quantity_kind_frequency() -> URIRef:
    """Returns the URI for QUDT quantity kind: frequency (http://qudt.org/vocab/quantitykind/Frequency)"""
    return QUDT_QUANTITY_KIND["FREQUENCY"]


def get_qudt_quantity_kind_inverse_length() -> URIRef:
    """Returns the URI for QUDT quantity kind: Inverse Length (http://qudt.org/vocab/quantitykind/InverseLength)"""
    return QUDT_QUANTITY_KIND["INVERSELENGTH"]


def get_qudt_quantity_kind_thermodynamic_temperature() -> URIRef:
    """Returns the URI for QUDT quantity kind: thermodynamic temperature (http://qudt.org/vocab/quantitykind/ThermodynamicTemperature)"""
    return QUDT_QUANTITY_KIND["THERMODYNAMICTEMPERATURE"]


def get_qudt_quantity_kind_cubic_electric_dipole_moment_per_square_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Cubic Electric Dipole Moment per Square Energy (http://qudt.org/vocab/quantitykind/CubicElectricDipoleMomentPerSquareEnergy)"""
    return QUDT_QUANTITY_KIND["CUBICELECTRICDIPOLEMOMENTPERSQUAREENERGY"]


def get_qudt_quantity_kind_quartic_electric_dipole_moment_per_cubic_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Quartic Electric Dipole Moment per Cubic Energy (http://qudt.org/vocab/quantitykind/QuarticElectricDipoleMomentPerCubicEnergy)"""
    return QUDT_QUANTITY_KIND["QUARTICELECTRICDIPOLEMOMENTPERCUBICENERGY"]


def get_qudt_quantity_kind_action() -> URIRef:
    """Returns the URI for QUDT quantity kind: Action (http://qudt.org/vocab/quantitykind/Action)"""
    return QUDT_QUANTITY_KIND["ACTION"]


def get_qudt_quantity_kind_electric_charge() -> URIRef:
    """Returns the URI for QUDT quantity kind: electric charge (http://qudt.org/vocab/quantitykind/ElectricCharge)"""
    return QUDT_QUANTITY_KIND["ELECTRICCHARGE"]


def get_qudt_quantity_kind_electric_charge_volume_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Electric Charge Volume Density (http://qudt.org/vocab/quantitykind/ElectricChargeVolumeDensity)"""
    return QUDT_QUANTITY_KIND["ELECTRICCHARGEVOLUMEDENSITY"]


def get_qudt_quantity_kind_electric_current() -> URIRef:
    """Returns the URI for QUDT quantity kind: electric current (http://qudt.org/vocab/quantitykind/ElectricCurrent)"""
    return QUDT_QUANTITY_KIND["ELECTRICCURRENT"]


def get_qudt_quantity_kind_electric_dipole_moment() -> URIRef:
    """Returns the URI for QUDT quantity kind: electric dipole moment (http://qudt.org/vocab/quantitykind/ElectricDipoleMoment)"""
    return QUDT_QUANTITY_KIND["ELECTRICDIPOLEMOMENT"]


def get_qudt_quantity_kind_electric_field_strength() -> URIRef:
    """Returns the URI for QUDT quantity kind: electric field strength (http://qudt.org/vocab/quantitykind/ElectricFieldStrength)"""
    return QUDT_QUANTITY_KIND["ELECTRICFIELDSTRENGTH"]


def get_qudt_quantity_kind_energy_per_area_electric_charge() -> URIRef:
    """Returns the URI for QUDT quantity kind: Energy Per Area Electric Charge (http://qudt.org/vocab/quantitykind/EnergyPerAreaElectricCharge)"""
    return QUDT_QUANTITY_KIND["ENERGYPERAREAELECTRICCHARGE"]


def get_qudt_quantity_kind_polarisability() -> URIRef:
    """Returns the URI for QUDT quantity kind: polarisability (http://qudt.org/vocab/quantitykind/Polarizability)"""
    return QUDT_QUANTITY_KIND["POLARIZABILITY"]


def get_qudt_quantity_kind_energy_per_electric_charge() -> URIRef:
    """Returns the URI for QUDT quantity kind: Energy per electric charge (http://qudt.org/vocab/quantitykind/EnergyPerElectricCharge)"""
    return QUDT_QUANTITY_KIND["ENERGYPERELECTRICCHARGE"]


def get_qudt_quantity_kind_electric_quadrupole_moment() -> URIRef:
    """Returns the URI for QUDT quantity kind: electric quadrupole moment (http://qudt.org/vocab/quantitykind/ElectricQuadrupoleMoment)"""
    return QUDT_QUANTITY_KIND["ELECTRICQUADRUPOLEMOMENT"]


def get_qudt_quantity_kind_force() -> URIRef:
    """Returns the URI for QUDT quantity kind: force (http://qudt.org/vocab/quantitykind/Force)"""
    return QUDT_QUANTITY_KIND["FORCE"]


def get_qudt_quantity_kind_magnetic_dipole_moment() -> URIRef:
    """Returns the URI for QUDT quantity kind: Magnetic Dipole Moment (http://qudt.org/vocab/quantitykind/MagneticDipoleMoment)"""
    return QUDT_QUANTITY_KIND["MAGNETICDIPOLEMOMENT"]


def get_qudt_quantity_kind_magnetic_flux_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: magnetic flux density (http://qudt.org/vocab/quantitykind/MagneticFluxDensity)"""
    return QUDT_QUANTITY_KIND["MAGNETICFLUXDENSITY"]


def get_qudt_quantity_kind_energy_per_square_magnetic_flux_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Energy Per Square Magnetic Flux Density (http://qudt.org/vocab/quantitykind/EnergyPerSquareMagneticFluxDensity)"""
    return QUDT_QUANTITY_KIND["ENERGYPERSQUAREMAGNETICFLUXDENSITY"]


def get_qudt_quantity_kind_linear_momentum() -> URIRef:
    """Returns the URI for QUDT quantity kind: Linear Momentum (http://qudt.org/vocab/quantitykind/LinearMomentum)"""
    return QUDT_QUANTITY_KIND["LINEARMOMENTUM"]


def get_qudt_quantity_kind_permittivity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Permittivity (http://qudt.org/vocab/quantitykind/Permittivity)"""
    return QUDT_QUANTITY_KIND["PERMITTIVITY"]


def get_qudt_quantity_kind_time() -> URIRef:
    """Returns the URI for QUDT quantity kind: time (http://qudt.org/vocab/quantitykind/Time)"""
    return QUDT_QUANTITY_KIND["TIME"]


def get_qudt_quantity_kind_linear_velocity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Linear Velocity (http://qudt.org/vocab/quantitykind/LinearVelocity)"""
    return QUDT_QUANTITY_KIND["LINEARVELOCITY"]


def get_qudt_quantity_kind_inverse_amount_of_substance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Inverse amount of substance (http://qudt.org/vocab/quantitykind/InverseAmountOfSubstance)"""
    return QUDT_QUANTITY_KIND["INVERSEAMOUNTOFSUBSTANCE"]


def get_qudt_quantity_kind_electric_charge_per_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: Electric Charge Per Mass (http://qudt.org/vocab/quantitykind/ElectricChargePerMass)"""
    return QUDT_QUANTITY_KIND["ELECTRICCHARGEPERMASS"]


def get_qudt_quantity_kind_magnetic_reluctivity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Magnetic Reluctivity (http://qudt.org/vocab/quantitykind/MagneticReluctivity)"""
    return QUDT_QUANTITY_KIND["MAGNETICRELUCTIVITY"]


def get_qudt_quantity_kind_temperature_per_magnetic_flux_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Temperature per Magnetic Flux Density (http://qudt.org/vocab/quantitykind/TemperaturePerMagneticFluxDensity)"""
    return QUDT_QUANTITY_KIND["TEMPERATUREPERMAGNETICFLUXDENSITY"]


def get_qudt_quantity_kind_heat_capacity() -> URIRef:
    """Returns the URI for QUDT quantity kind: heat capacity (http://qudt.org/vocab/quantitykind/HeatCapacity)"""
    return QUDT_QUANTITY_KIND["HEATCAPACITY"]


def get_qudt_quantity_kind_inverse_time_temperature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Inverse Time Temperature (http://qudt.org/vocab/quantitykind/InverseTimeTemperature)"""
    return QUDT_QUANTITY_KIND["INVERSETIMETEMPERATURE"]


def get_qudt_quantity_kind_inverse_length_temperature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Inverse Length Temperature (http://qudt.org/vocab/quantitykind/InverseLengthTemperature)"""
    return QUDT_QUANTITY_KIND["INVERSELENGTHTEMPERATURE"]


def get_qudt_quantity_kind_resistance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Resistance (http://qudt.org/vocab/quantitykind/Resistance)"""
    return QUDT_QUANTITY_KIND["RESISTANCE"]


def get_qudt_quantity_kind_electric_conductivity() -> URIRef:
    """Returns the URI for QUDT quantity kind: electric conductivity (http://qudt.org/vocab/quantitykind/ElectricConductivity)"""
    return QUDT_QUANTITY_KIND["ELECTRICCONDUCTIVITY"]


def get_qudt_quantity_kind_inverse_magnetic_flux() -> URIRef:
    """Returns the URI for QUDT quantity kind: Inverse Magnetic Flux (http://qudt.org/vocab/quantitykind/InverseMagneticFlux)"""
    return QUDT_QUANTITY_KIND["INVERSEMAGNETICFLUX"]


def get_qudt_quantity_kind_gyromagnetic_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Gyromagnetic Ratio (http://qudt.org/vocab/quantitykind/GyromagneticRatio)"""
    return QUDT_QUANTITY_KIND["GYROMAGNETICRATIO"]


def get_qudt_quantity_kind_electric_current_per_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Electric Current per Energy (http://qudt.org/vocab/quantitykind/ElectricCurrentPerEnergy)"""
    return QUDT_QUANTITY_KIND["ELECTRICCURRENTPERENERGY"]


def get_qudt_quantity_kind_electric_charge_per_amount_of_substance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Electric charge per amount of substance (http://qudt.org/vocab/quantitykind/ElectricChargePerAmountOfSubstance)"""
    return QUDT_QUANTITY_KIND["ELECTRICCHARGEPERAMOUNTOFSUBSTANCE"]


def get_qudt_quantity_kind_inverse_square_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Inverse Square Energy (http://qudt.org/vocab/quantitykind/InverseSquareEnergy)"""
    return QUDT_QUANTITY_KIND["INVERSESQUAREENERGY"]


def get_qudt_quantity_kind_power_area() -> URIRef:
    """Returns the URI for QUDT quantity kind: Power Area (http://qudt.org/vocab/quantitykind/PowerArea)"""
    return QUDT_QUANTITY_KIND["POWERAREA"]


def get_qudt_quantity_kind_power_area_per_solid_angle() -> URIRef:
    """Returns the URI for QUDT quantity kind: Power Area per Solid Angle (http://qudt.org/vocab/quantitykind/PowerAreaPerSolidAngle)"""
    return QUDT_QUANTITY_KIND["POWERAREAPERSOLIDANGLE"]


def get_qudt_quantity_kind_gravitational_attraction() -> URIRef:
    """Returns the URI for QUDT quantity kind: Gravitational Attraction (http://qudt.org/vocab/quantitykind/GravitationalAttraction)"""
    return QUDT_QUANTITY_KIND["GRAVITATIONALATTRACTION"]


def get_qudt_quantity_kind_number_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Number Density (http://qudt.org/vocab/quantitykind/NumberDensity)"""
    return QUDT_QUANTITY_KIND["NUMBERDENSITY"]


def get_qudt_quantity_kind_magnetic_flux() -> URIRef:
    """Returns the URI for QUDT quantity kind: magnetic flux (http://qudt.org/vocab/quantitykind/MagneticFlux)"""
    return QUDT_QUANTITY_KIND["MAGNETICFLUX"]


def get_qudt_quantity_kind_molar_heat_capacity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Molar Heat Capacity (http://qudt.org/vocab/quantitykind/MolarHeatCapacity)"""
    return QUDT_QUANTITY_KIND["MOLARHEATCAPACITY"]


def get_qudt_quantity_kind_molar_angular_momentum() -> URIRef:
    """Returns the URI for QUDT quantity kind: Molar Angular Momentum (http://qudt.org/vocab/quantitykind/MolarAngularMomentum)"""
    return QUDT_QUANTITY_KIND["MOLARANGULARMOMENTUM"]


def get_qudt_quantity_kind_length_molar_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Length Molar Energy (http://qudt.org/vocab/quantitykind/LengthMolarEnergy)"""
    return QUDT_QUANTITY_KIND["LENGTHMOLARENERGY"]


def get_qudt_quantity_kind_molar_volume() -> URIRef:
    """Returns the URI for QUDT quantity kind: molar volume (http://qudt.org/vocab/quantitykind/MolarVolume)"""
    return QUDT_QUANTITY_KIND["MOLARVOLUME"]


def get_qudt_quantity_kind_electric_flux_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: electric flux density (http://qudt.org/vocab/quantitykind/ElectricFluxDensity)"""
    return QUDT_QUANTITY_KIND["ELECTRICFLUXDENSITY"]


def get_qudt_quantity_kind_angle() -> URIRef:
    """Returns the URI for QUDT quantity kind: Angle (http://qudt.org/vocab/quantitykind/Angle)"""
    return QUDT_QUANTITY_KIND["ANGLE"]


def get_qudt_quantity_kind_length_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Length Energy (http://qudt.org/vocab/quantitykind/LengthEnergy)"""
    return QUDT_QUANTITY_KIND["LENGTHENERGY"]


def get_qudt_quantity_kind_circulation() -> URIRef:
    """Returns the URI for QUDT quantity kind: Circulation (http://qudt.org/vocab/quantitykind/Circulation)"""
    return QUDT_QUANTITY_KIND["CIRCULATION"]


def get_qudt_quantity_kind_length_temperature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Length Temperature (http://qudt.org/vocab/quantitykind/LengthTemperature)"""
    return QUDT_QUANTITY_KIND["LENGTHTEMPERATURE"]


def get_qudt_quantity_kind_speed() -> URIRef:
    """Returns the URI for QUDT quantity kind: Speed (http://qudt.org/vocab/quantitykind/Speed)"""
    return QUDT_QUANTITY_KIND["SPEED"]


def get_qudt_quantity_kind_linear_acceleration() -> URIRef:
    """Returns the URI for QUDT quantity kind: Linear Acceleration (http://qudt.org/vocab/quantitykind/LinearAcceleration)"""
    return QUDT_QUANTITY_KIND["LINEARACCELERATION"]


def get_qudt_quantity_kind_pressure() -> URIRef:
    """Returns the URI for QUDT quantity kind: pressure (http://qudt.org/vocab/quantitykind/Pressure)"""
    return QUDT_QUANTITY_KIND["PRESSURE"]


def get_qudt_quantity_kind_power_per_area_quartic_temperature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Power per area quartic temperature (http://qudt.org/vocab/quantitykind/PowerPerAreaQuarticTemperature)"""
    return QUDT_QUANTITY_KIND["POWERPERAREAQUARTICTEMPERATURE"]


def get_qudt_quantity_kind_area() -> URIRef:
    """Returns the URI for QUDT quantity kind: area (http://qudt.org/vocab/quantitykind/Area)"""
    return QUDT_QUANTITY_KIND["AREA"]


def get_qudt_quantity_kind_currency() -> URIRef:
    """Returns the URI for QUDT quantity kind: Currency (http://qudt.org/vocab/quantitykind/Currency)"""
    return QUDT_QUANTITY_KIND["CURRENCY"]


def get_qudt_quantity_kind_molar_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Molar Energy (http://qudt.org/vocab/quantitykind/MolarEnergy)"""
    return QUDT_QUANTITY_KIND["MOLARENERGY"]


def get_qudt_quantity_kind_reaction_rate_constant() -> URIRef:
    """Returns the URI for QUDT quantity kind: Reaction Rate Constant (http://qudt.org/vocab/quantitykind/SecondOrderReactionRateConstant)"""
    return QUDT_QUANTITY_KIND["SECONDORDERREACTIONRATECONSTANT"]


def get_qudt_quantity_kind_mass_per_electric_charge() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass per Electric Charge (http://qudt.org/vocab/quantitykind/MassPerElectricCharge)"""
    return QUDT_QUANTITY_KIND["MASSPERELECTRICCHARGE"]


def get_qudt_quantity_kind_length_per_electric_current() -> URIRef:
    """Returns the URI for QUDT quantity kind: Length per Electric Current (http://qudt.org/vocab/quantitykind/LengthPerElectricCurrent)"""
    return QUDT_QUANTITY_KIND["LENGTHPERELECTRICCURRENT"]


def get_qudt_quantity_kind_magnetic_flux_per_length() -> URIRef:
    """Returns the URI for QUDT quantity kind: Magnetic flux per length (http://qudt.org/vocab/quantitykind/MagneticFluxPerLength)"""
    return QUDT_QUANTITY_KIND["MAGNETICFLUXPERLENGTH"]


def get_qudt_quantity_kind_power_per_electric_charge() -> URIRef:
    """Returns the URI for QUDT quantity kind: Power Per Electric Charge (http://qudt.org/vocab/quantitykind/PowerPerElectricCharge)"""
    return QUDT_QUANTITY_KIND["POWERPERELECTRICCHARGE"]


def get_qudt_quantity_kind_electric_flux() -> URIRef:
    """Returns the URI for QUDT quantity kind: Electric Flux (http://qudt.org/vocab/quantitykind/ElectricFlux)"""
    return QUDT_QUANTITY_KIND["ELECTRICFLUX"]


def get_qudt_quantity_kind_permeability() -> URIRef:
    """Returns the URI for QUDT quantity kind: Permeability (http://qudt.org/vocab/quantitykind/ElectromagneticPermeability)"""
    return QUDT_QUANTITY_KIND["ELECTROMAGNETICPERMEABILITY"]


def get_qudt_quantity_kind_measurement_unit_of_thermal_inertia() -> URIRef:
    """Returns the URI for QUDT quantity kind: Measurement Unit of Thermal Inertia (http://qudt.org/vocab/quantitykind/ThermalInertia)"""
    return QUDT_QUANTITY_KIND["THERMALINERTIA"]


def get_qudt_quantity_kind_inductance() -> URIRef:
    """Returns the URI for QUDT quantity kind: inductance (http://qudt.org/vocab/quantitykind/Inductance)"""
    return QUDT_QUANTITY_KIND["INDUCTANCE"]


def get_qudt_quantity_kind_inverse_permittivity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Inverse Permittivity (http://qudt.org/vocab/quantitykind/InversePermittivity)"""
    return QUDT_QUANTITY_KIND["INVERSEPERMITTIVITY"]


def get_qudt_quantity_kind_stress_intensity_factor() -> URIRef:
    """Returns the URI for QUDT quantity kind: Stress Intensity Factor (http://qudt.org/vocab/quantitykind/StressIntensityFactor)"""
    return QUDT_QUANTITY_KIND["STRESSINTENSITYFACTOR"]


def get_qudt_quantity_kind_thermal_resistivity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Thermal Resistivity (http://qudt.org/vocab/quantitykind/ThermalResistivity)"""
    return QUDT_QUANTITY_KIND["THERMALRESISTIVITY"]


def get_qudt_quantity_kind_specific_heat_volume() -> URIRef:
    """Returns the URI for QUDT quantity kind: Specific Heat Volume (http://qudt.org/vocab/quantitykind/SpecificHeatVolume)"""
    return QUDT_QUANTITY_KIND["SPECIFICHEATVOLUME"]


def get_qudt_quantity_kind_curvature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Curvature (http://qudt.org/vocab/quantitykind/Curvature)"""
    return QUDT_QUANTITY_KIND["CURVATURE"]


def get_qudt_quantity_kind_volumetric_heat_capacity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Volumetric Heat Capacity (http://qudt.org/vocab/quantitykind/VolumetricHeatCapacity)"""
    return QUDT_QUANTITY_KIND["VOLUMETRICHEATCAPACITY"]


def get_qudt_quantity_kind_dynamic_viscosity() -> URIRef:
    """Returns the URI for QUDT quantity kind: dynamic viscosity (http://qudt.org/vocab/quantitykind/DynamicViscosity)"""
    return QUDT_QUANTITY_KIND["DYNAMICVISCOSITY"]


def get_qudt_quantity_kind_energy_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Energy Density (http://qudt.org/vocab/quantitykind/EnergyDensity)"""
    return QUDT_QUANTITY_KIND["ENERGYDENSITY"]


def get_qudt_quantity_kind_force_per_area() -> URIRef:
    """Returns the URI for QUDT quantity kind: Force Per Area (http://qudt.org/vocab/quantitykind/ForcePerArea)"""
    return QUDT_QUANTITY_KIND["FORCEPERAREA"]


def get_qudt_quantity_kind_force_per_area_time() -> URIRef:
    """Returns the URI for QUDT quantity kind: Force Per Area Time (http://qudt.org/vocab/quantitykind/ForcePerAreaTime)"""
    return QUDT_QUANTITY_KIND["FORCEPERAREATIME"]


def get_qudt_quantity_kind_mass_per_length() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass per Length (http://qudt.org/vocab/quantitykind/MassPerLength)"""
    return QUDT_QUANTITY_KIND["MASSPERLENGTH"]


def get_qudt_quantity_kind_inverse_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Inverse Energy (http://qudt.org/vocab/quantitykind/InverseEnergy)"""
    return QUDT_QUANTITY_KIND["INVERSEENERGY"]


def get_qudt_quantity_kind_thermal_resistance() -> URIRef:
    """Returns the URI for QUDT quantity kind: thermal resistance (http://qudt.org/vocab/quantitykind/ThermalResistance)"""
    return QUDT_QUANTITY_KIND["THERMALRESISTANCE"]


def get_qudt_quantity_kind_mass_per_area_time() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass per Area Time (http://qudt.org/vocab/quantitykind/MassPerAreaTime)"""
    return QUDT_QUANTITY_KIND["MASSPERAREATIME"]


def get_qudt_quantity_kind_spectral_radiant_energy_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Spectral Radiant Energy Density (http://qudt.org/vocab/quantitykind/SpectralRadiantEnergyDensity)"""
    return QUDT_QUANTITY_KIND["SPECTRALRADIANTENERGYDENSITY"]


def get_qudt_quantity_kind_radiant_intensity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Radiant Intensity (http://qudt.org/vocab/quantitykind/RadiantIntensity)"""
    return QUDT_QUANTITY_KIND["RADIANTINTENSITY"]


def get_qudt_quantity_kind_mass_per_area() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass per Area (http://qudt.org/vocab/quantitykind/MassPerArea)"""
    return QUDT_QUANTITY_KIND["MASSPERAREA"]


def get_qudt_quantity_kind_luminance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Luminance (http://qudt.org/vocab/quantitykind/Luminance)"""
    return QUDT_QUANTITY_KIND["LUMINANCE"]


def get_qudt_quantity_kind_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Density (http://qudt.org/vocab/quantitykind/Density)"""
    return QUDT_QUANTITY_KIND["DENSITY"]


def get_qudt_quantity_kind_measurement_unit_of_spectral_emittance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Measurement Unit of Spectral Emittance (http://qudt.org/vocab/quantitykind/SpectralEmittance)"""
    return QUDT_QUANTITY_KIND["SPECTRALEMITTANCE"]


def get_qudt_quantity_kind_measurement_unit_of_spectral_irradiance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Measurement Unit of Spectral Irradiance (http://qudt.org/vocab/quantitykind/SpectralIrradiance)"""
    return QUDT_QUANTITY_KIND["SPECTRALIRRADIANCE"]


def get_qudt_quantity_kind_thermal_insulance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Thermal Insulance (http://qudt.org/vocab/quantitykind/ThermalInsulance)"""
    return QUDT_QUANTITY_KIND["THERMALINSULANCE"]


def get_qudt_quantity_kind_measurement_unit_for_a_quantity_approximately_proportional_to_thermal_inertia() -> (
    URIRef
):
    """Returns the URI for QUDT quantity kind: Measurement Unit for a quantity approximately proportional to Thermal Inertia (http://qudt.org/vocab/quantitykind/ApparentThermalInertia)"""
    return QUDT_QUANTITY_KIND["APPARENTTHERMALINERTIA"]


def get_qudt_quantity_kind_angular_acceleration() -> URIRef:
    """Returns the URI for QUDT quantity kind: angular acceleration (http://qudt.org/vocab/quantitykind/AngularAcceleration)"""
    return QUDT_QUANTITY_KIND["ANGULARACCELERATION"]


def get_qudt_quantity_kind_dimensionless() -> URIRef:
    """Returns the URI for QUDT quantity kind: Dimensionless (http://qudt.org/vocab/quantitykind/Dimensionless)"""
    return QUDT_QUANTITY_KIND["DIMENSIONLESS"]


def get_qudt_quantity_kind_square_time() -> URIRef:
    """Returns the URI for QUDT quantity kind: Square Time (http://qudt.org/vocab/quantitykind/SquareTime)"""
    return QUDT_QUANTITY_KIND["SQUARETIME"]


def get_qudt_quantity_kind_temperature_per_time() -> URIRef:
    """Returns the URI for QUDT quantity kind: Temperature per Time (http://qudt.org/vocab/quantitykind/TemperaturePerTime)"""
    return QUDT_QUANTITY_KIND["TEMPERATUREPERTIME"]


def get_qudt_quantity_kind_temperature_per_square_time() -> URIRef:
    """Returns the URI for QUDT quantity kind: Temperature per Square Time (http://qudt.org/vocab/quantitykind/TemperaturePerSquareTime)"""
    return QUDT_QUANTITY_KIND["TEMPERATUREPERSQUARETIME"]


def get_qudt_quantity_kind_time_temperature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Time Temperature (http://qudt.org/vocab/quantitykind/TimeTemperature)"""
    return QUDT_QUANTITY_KIND["TIMETEMPERATURE"]


def get_qudt_quantity_kind_coefficient_of_heat_transfer() -> URIRef:
    """Returns the URI for QUDT quantity kind: Coefficient of heat transfer (http://qudt.org/vocab/quantitykind/CoefficientOfHeatTransfer)"""
    return QUDT_QUANTITY_KIND["COEFFICIENTOFHEATTRANSFER"]


def get_qudt_quantity_kind_mass_flow_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass Flow Rate (http://qudt.org/vocab/quantitykind/MassFlowRate)"""
    return QUDT_QUANTITY_KIND["MASSFLOWRATE"]


def get_qudt_quantity_kind_energy_per_area() -> URIRef:
    """Returns the URI for QUDT quantity kind: Energy per Area (http://qudt.org/vocab/quantitykind/EnergyPerArea)"""
    return QUDT_QUANTITY_KIND["ENERGYPERAREA"]


def get_qudt_quantity_kind_force_per_length() -> URIRef:
    """Returns the URI for QUDT quantity kind: Force per Length (http://qudt.org/vocab/quantitykind/ForcePerLength)"""
    return QUDT_QUANTITY_KIND["FORCEPERLENGTH"]


def get_qudt_quantity_kind_power_per_area() -> URIRef:
    """Returns the URI for QUDT quantity kind: Power Per Area (http://qudt.org/vocab/quantitykind/PowerPerArea)"""
    return QUDT_QUANTITY_KIND["POWERPERAREA"]


def get_qudt_quantity_kind_mass_temperature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass Temperature (http://qudt.org/vocab/quantitykind/MassTemperature)"""
    return QUDT_QUANTITY_KIND["MASSTEMPERATURE"]


def get_qudt_quantity_kind_luminous_intensity() -> URIRef:
    """Returns the URI for QUDT quantity kind: luminous intensity (http://qudt.org/vocab/quantitykind/LuminousIntensity)"""
    return QUDT_QUANTITY_KIND["LUMINOUSINTENSITY"]


def get_qudt_quantity_kind_inverse_pressure() -> URIRef:
    """Returns the URI for QUDT quantity kind: Inverse Pressure (http://qudt.org/vocab/quantitykind/InversePressure)"""
    return QUDT_QUANTITY_KIND["INVERSEPRESSURE"]


def get_qudt_quantity_kind_linear_thermal_expansion() -> URIRef:
    """Returns the URI for QUDT quantity kind: Linear Thermal Expansion (http://qudt.org/vocab/quantitykind/LinearThermalExpansion)"""
    return QUDT_QUANTITY_KIND["LINEARTHERMALEXPANSION"]


def get_qudt_quantity_kind_thrust_to_mass_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Thrust To Mass Ratio (http://qudt.org/vocab/quantitykind/ThrustToMassRatio)"""
    return QUDT_QUANTITY_KIND["THRUSTTOMASSRATIO"]


def get_qudt_quantity_kind_thermal_conductivity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Thermal Conductivity (http://qudt.org/vocab/quantitykind/ThermalConductivity)"""
    return QUDT_QUANTITY_KIND["THERMALCONDUCTIVITY"]


def get_qudt_quantity_kind_length_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: Length Mass (http://qudt.org/vocab/quantitykind/LengthMass)"""
    return QUDT_QUANTITY_KIND["LENGTHMASS"]


def get_qudt_quantity_kind_specific_heat_capacity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Specific Heat Capacity (http://qudt.org/vocab/quantitykind/SpecificHeatCapacity)"""
    return QUDT_QUANTITY_KIND["SPECIFICHEATCAPACITY"]


def get_qudt_quantity_kind_area_thermal_expansion() -> URIRef:
    """Returns the URI for QUDT quantity kind: Area Thermal Expansion (http://qudt.org/vocab/quantitykind/AreaThermalExpansion)"""
    return QUDT_QUANTITY_KIND["AREATHERMALEXPANSION"]


def get_qudt_quantity_kind_area_per_time() -> URIRef:
    """Returns the URI for QUDT quantity kind: Area per Time (http://qudt.org/vocab/quantitykind/AreaPerTime)"""
    return QUDT_QUANTITY_KIND["AREAPERTIME"]


def get_qudt_quantity_kind_specific_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Specific Energy (http://qudt.org/vocab/quantitykind/SpecificEnergy)"""
    return QUDT_QUANTITY_KIND["SPECIFICENERGY"]


def get_qudt_quantity_kind_absorbed_dose_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: Absorbed Dose Rate (http://qudt.org/vocab/quantitykind/AbsorbedDoseRate)"""
    return QUDT_QUANTITY_KIND["ABSORBEDDOSERATE"]


def get_qudt_quantity_kind_area_time() -> URIRef:
    """Returns the URI for QUDT quantity kind: Area Time (http://qudt.org/vocab/quantitykind/AreaTime)"""
    return QUDT_QUANTITY_KIND["AREATIME"]


def get_qudt_quantity_kind_area_temperature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Area Temperature (http://qudt.org/vocab/quantitykind/AreaTemperature)"""
    return QUDT_QUANTITY_KIND["AREATEMPERATURE"]


def get_qudt_quantity_kind_area_time_temperature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Area Time Temperature (http://qudt.org/vocab/quantitykind/AreaTimeTemperature)"""
    return QUDT_QUANTITY_KIND["AREATIMETEMPERATURE"]


def get_qudt_quantity_kind_energy_per_temperature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Energy per temperature (http://qudt.org/vocab/quantitykind/EnergyPerTemperature)"""
    return QUDT_QUANTITY_KIND["ENERGYPERTEMPERATURE"]


def get_qudt_quantity_kind_angular_momentum() -> URIRef:
    """Returns the URI for QUDT quantity kind: Angular Momentum (http://qudt.org/vocab/quantitykind/AngularMomentum)"""
    return QUDT_QUANTITY_KIND["ANGULARMOMENTUM"]


def get_qudt_quantity_kind_torque() -> URIRef:
    """Returns the URI for QUDT quantity kind: torque (http://qudt.org/vocab/quantitykind/Torque)"""
    return QUDT_QUANTITY_KIND["TORQUE"]


def get_qudt_quantity_kind_power() -> URIRef:
    """Returns the URI for QUDT quantity kind: power (http://qudt.org/vocab/quantitykind/Power)"""
    return QUDT_QUANTITY_KIND["POWER"]


def get_qudt_quantity_kind_moment_of_inertia() -> URIRef:
    """Returns the URI for QUDT quantity kind: moment of inertia (http://qudt.org/vocab/quantitykind/MomentOfInertia)"""
    return QUDT_QUANTITY_KIND["MOMENTOFINERTIA"]


def get_qudt_quantity_kind_specific_heat_pressure() -> URIRef:
    """Returns the URI for QUDT quantity kind: Specific Heat Pressure (http://qudt.org/vocab/quantitykind/SpecificHeatPressure)"""
    return QUDT_QUANTITY_KIND["SPECIFICHEATPRESSURE"]


def get_qudt_quantity_kind_specific_volume() -> URIRef:
    """Returns the URI for QUDT quantity kind: Specific Volume (http://qudt.org/vocab/quantitykind/SpecificVolume)"""
    return QUDT_QUANTITY_KIND["SPECIFICVOLUME"]


def get_qudt_quantity_kind_volume_thermal_expansion() -> URIRef:
    """Returns the URI for QUDT quantity kind: Volume Thermal Expansion (http://qudt.org/vocab/quantitykind/VolumeThermalExpansion)"""
    return QUDT_QUANTITY_KIND["VOLUMETHERMALEXPANSION"]


def get_qudt_quantity_kind_volume_flow_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: Volume Flow Rate (http://qudt.org/vocab/quantitykind/VolumeFlowRate)"""
    return QUDT_QUANTITY_KIND["VOLUMEFLOWRATE"]


def get_qudt_quantity_kind_standard_gravitational_parameter() -> URIRef:
    """Returns the URI for QUDT quantity kind: Standard Gravitational Parameter (http://qudt.org/vocab/quantitykind/StandardGravitationalParameter)"""
    return QUDT_QUANTITY_KIND["STANDARDGRAVITATIONALPARAMETER"]


def get_qudt_quantity_kind_volume() -> URIRef:
    """Returns the URI for QUDT quantity kind: Volume (http://qudt.org/vocab/quantitykind/Volume)"""
    return QUDT_QUANTITY_KIND["VOLUME"]


def get_qudt_quantity_kind_moment_of_force() -> URIRef:
    """Returns the URI for QUDT quantity kind: Moment of Force (http://qudt.org/vocab/quantitykind/MomentOfForce)"""
    return QUDT_QUANTITY_KIND["MOMENTOFFORCE"]


def get_qudt_quantity_kind_thermal_energy_length() -> URIRef:
    """Returns the URI for QUDT quantity kind: Thermal Energy Length (http://qudt.org/vocab/quantitykind/ThermalEnergyLength)"""
    return QUDT_QUANTITY_KIND["THERMALENERGYLENGTH"]


def get_qudt_quantity_kind_second_axial_moment_of_area() -> URIRef:
    """Returns the URI for QUDT quantity kind: Second Axial Moment of Area (http://qudt.org/vocab/quantitykind/SecondAxialMomentOfArea)"""
    return QUDT_QUANTITY_KIND["SECONDAXIALMOMENTOFAREA"]


def get_qudt_quantity_kind_square_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Square Energy (http://qudt.org/vocab/quantitykind/SquareEnergy)"""
    return QUDT_QUANTITY_KIND["SQUAREENERGY"]


def get_qudt_quantity_kind_electric_charge_line_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Electric Charge Line Density (http://qudt.org/vocab/quantitykind/ElectricChargeLineDensity)"""
    return QUDT_QUANTITY_KIND["ELECTRICCHARGELINEDENSITY"]


def get_qudt_quantity_kind_electric_current_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: electric current density (http://qudt.org/vocab/quantitykind/ElectricCurrentDensity)"""
    return QUDT_QUANTITY_KIND["ELECTRICCURRENTDENSITY"]


def get_qudt_quantity_kind_electric_charge_per_area() -> URIRef:
    """Returns the URI for QUDT quantity kind: Electric charge per area (http://qudt.org/vocab/quantitykind/ElectricChargePerArea)"""
    return QUDT_QUANTITY_KIND["ELECTRICCHARGEPERAREA"]


def get_qudt_quantity_kind_exposure_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: Exposure Rate (http://qudt.org/vocab/quantitykind/ExposureRate)"""
    return QUDT_QUANTITY_KIND["EXPOSURERATE"]


def get_qudt_quantity_kind_specific_electrical_current() -> URIRef:
    """Returns the URI for QUDT quantity kind: Specific Electrical Current (http://qudt.org/vocab/quantitykind/SpecificElectricCurrent)"""
    return QUDT_QUANTITY_KIND["SPECIFICELECTRICCURRENT"]


def get_qudt_quantity_kind_specific_electric_charge() -> URIRef:
    """Returns the URI for QUDT quantity kind: Specific Electric Charge (http://qudt.org/vocab/quantitykind/SpecificElectricCharge)"""
    return QUDT_QUANTITY_KIND["SPECIFICELECTRICCHARGE"]


def get_qudt_quantity_kind_electric_current_per_temperature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Electric Current per Temperature (http://qudt.org/vocab/quantitykind/ElectricCurrentPerTemperature)"""
    return QUDT_QUANTITY_KIND["ELECTRICCURRENTPERTEMPERATURE"]


def get_qudt_quantity_kind_capacitance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Capacitance (http://qudt.org/vocab/quantitykind/Capacitance)"""
    return QUDT_QUANTITY_KIND["CAPACITANCE"]


def get_qudt_quantity_kind_molar_flux_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Molar Flux Density (http://qudt.org/vocab/quantitykind/MolarFluxDensity)"""
    return QUDT_QUANTITY_KIND["MOLARFLUXDENSITY"]


def get_qudt_quantity_kind_amount_of_substance_per_volume() -> URIRef:
    """Returns the URI for QUDT quantity kind: Amount of Substance per Volume (http://qudt.org/vocab/quantitykind/AmountOfSubstancePerVolume)"""
    return QUDT_QUANTITY_KIND["AMOUNTOFSUBSTANCEPERVOLUME"]


def get_qudt_quantity_kind_amount_of_substance_per_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: Amount of Substance per Mass (http://qudt.org/vocab/quantitykind/AmountOfSubstancePerMass)"""
    return QUDT_QUANTITY_KIND["AMOUNTOFSUBSTANCEPERMASS"]


def get_qudt_quantity_kind_catalytic_activity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Catalytic Activity (http://qudt.org/vocab/quantitykind/CatalyticActivity)"""
    return QUDT_QUANTITY_KIND["CATALYTICACTIVITY"]


def get_qudt_quantity_kind_amount_of_substance() -> URIRef:
    """Returns the URI for QUDT quantity kind: amount of substance (http://qudt.org/vocab/quantitykind/AmountOfSubstance)"""
    return QUDT_QUANTITY_KIND["AMOUNTOFSUBSTANCE"]


def get_qudt_quantity_kind_temperature_amount_of_substance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Temperature Amount of Substance (http://qudt.org/vocab/quantitykind/TemperatureAmountOfSubstance)"""
    return QUDT_QUANTITY_KIND["TEMPERATUREAMOUNTOFSUBSTANCE"]


def get_qudt_quantity_kind_mass_amount_of_substance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass Amount of Substance (http://qudt.org/vocab/quantitykind/MassAmountOfSubstance)"""
    return QUDT_QUANTITY_KIND["MASSAMOUNTOFSUBSTANCE"]


def get_qudt_quantity_kind_molar_mass_variation_due_to_pressure() -> URIRef:
    """Returns the URI for QUDT quantity kind: Molar Mass variation due to Pressure (http://qudt.org/vocab/quantitykind/AmountOfSubstancePerMassPressure)"""
    return QUDT_QUANTITY_KIND["AMOUNTOFSUBSTANCEPERMASSPRESSURE"]


def get_qudt_quantity_kind_api_gravity() -> URIRef:
    """Returns the URI for QUDT quantity kind: API Gravity (http://qudt.org/vocab/quantitykind/APIGravity)"""
    return QUDT_QUANTITY_KIND["APIGRAVITY"]


def get_qudt_quantity_kind_absolute_activity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Absolute Activity (http://qudt.org/vocab/quantitykind/AbsoluteActivity)"""
    return QUDT_QUANTITY_KIND["ABSOLUTEACTIVITY"]


def get_qudt_quantity_kind_inverse_volume() -> URIRef:
    """Returns the URI for QUDT quantity kind: Inverse Volume (http://qudt.org/vocab/quantitykind/InverseVolume)"""
    return QUDT_QUANTITY_KIND["INVERSEVOLUME"]


def get_qudt_quantity_kind_absolute_humidity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Absolute Humidity (http://qudt.org/vocab/quantitykind/AbsoluteHumidity)"""
    return QUDT_QUANTITY_KIND["ABSOLUTEHUMIDITY"]


def get_qudt_quantity_kind_relative_humidity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Relative Humidity (http://qudt.org/vocab/quantitykind/RelativeHumidity)"""
    return QUDT_QUANTITY_KIND["RELATIVEHUMIDITY"]


def get_qudt_quantity_kind_absolute_typographic_measurement() -> URIRef:
    """Returns the URI for QUDT quantity kind: absolute typographic measurement (http://qudt.org/vocab/quantitykind/AbsoluteTypographicMeasurement)"""
    return QUDT_QUANTITY_KIND["ABSOLUTETYPOGRAPHICMEASUREMENT"]


def get_qudt_quantity_kind_absorbed_dose() -> URIRef:
    """Returns the URI for QUDT quantity kind: Absorbed Dose (http://qudt.org/vocab/quantitykind/AbsorbedDose)"""
    return QUDT_QUANTITY_KIND["ABSORBEDDOSE"]


def get_qudt_quantity_kind_absorptance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Absorptance (http://qudt.org/vocab/quantitykind/Absorptance)"""
    return QUDT_QUANTITY_KIND["ABSORPTANCE"]


def get_qudt_quantity_kind_acceleration() -> URIRef:
    """Returns the URI for QUDT quantity kind: acceleration (http://qudt.org/vocab/quantitykind/Acceleration)"""
    return QUDT_QUANTITY_KIND["ACCELERATION"]


def get_qudt_quantity_kind_acceleration_of_gravity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Acceleration Of Gravity (http://qudt.org/vocab/quantitykind/AccelerationOfGravity)"""
    return QUDT_QUANTITY_KIND["ACCELERATIONOFGRAVITY"]


def get_qudt_quantity_kind_acceptor_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Acceptor Density (http://qudt.org/vocab/quantitykind/AcceptorDensity)"""
    return QUDT_QUANTITY_KIND["ACCEPTORDENSITY"]


def get_qudt_quantity_kind_acceptor_ionization_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Acceptor Ionization Energy (http://qudt.org/vocab/quantitykind/AcceptorIonizationEnergy)"""
    return QUDT_QUANTITY_KIND["ACCEPTORIONIZATIONENERGY"]


def get_qudt_quantity_kind_ionization_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Ionization Energy (http://qudt.org/vocab/quantitykind/IonizationEnergy)"""
    return QUDT_QUANTITY_KIND["IONIZATIONENERGY"]


def get_qudt_quantity_kind_donor_ionization_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Donor Ionization Energy (http://qudt.org/vocab/quantitykind/DonorIonizationEnergy)"""
    return QUDT_QUANTITY_KIND["DONORIONIZATIONENERGY"]


def get_qudt_quantity_kind_acidity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Acidity (http://qudt.org/vocab/quantitykind/Acidity)"""
    return QUDT_QUANTITY_KIND["ACIDITY"]


def get_qudt_quantity_kind_basicity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Basicity (http://qudt.org/vocab/quantitykind/Basicity)"""
    return QUDT_QUANTITY_KIND["BASICITY"]


def get_qudt_quantity_kind_acoustic_impediance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Acoustic Impediance (http://qudt.org/vocab/quantitykind/AcousticImpedance)"""
    return QUDT_QUANTITY_KIND["ACOUSTICIMPEDANCE"]


def get_qudt_quantity_kind_action_time() -> URIRef:
    """Returns the URI for QUDT quantity kind: Action Time (http://qudt.org/vocab/quantitykind/ActionTime)"""
    return QUDT_QUANTITY_KIND["ACTIONTIME"]


def get_qudt_quantity_kind_active_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Active Energy (http://qudt.org/vocab/quantitykind/ActiveEnergy)"""
    return QUDT_QUANTITY_KIND["ACTIVEENERGY"]


def get_qudt_quantity_kind_instantaneous_power() -> URIRef:
    """Returns the URI for QUDT quantity kind: Instantaneous Power (http://qudt.org/vocab/quantitykind/InstantaneousPower)"""
    return QUDT_QUANTITY_KIND["INSTANTANEOUSPOWER"]


def get_qudt_quantity_kind_active_power() -> URIRef:
    """Returns the URI for QUDT quantity kind: Active Power (http://qudt.org/vocab/quantitykind/ActivePower)"""
    return QUDT_QUANTITY_KIND["ACTIVEPOWER"]


def get_qudt_quantity_kind_electric_power() -> URIRef:
    """Returns the URI for QUDT quantity kind: electric power (http://qudt.org/vocab/quantitykind/ElectricPower)"""
    return QUDT_QUANTITY_KIND["ELECTRICPOWER"]


def get_qudt_quantity_kind_activity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Activity (http://qudt.org/vocab/quantitykind/Activity)"""
    return QUDT_QUANTITY_KIND["ACTIVITY"]


def get_qudt_quantity_kind_stochastic_process() -> URIRef:
    """Returns the URI for QUDT quantity kind: Stochastic Process (http://qudt.org/vocab/quantitykind/StochasticProcess)"""
    return QUDT_QUANTITY_KIND["STOCHASTICPROCESS"]


def get_qudt_quantity_kind_activity_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Activity Coefficient (http://qudt.org/vocab/quantitykind/ActivityCoefficient)"""
    return QUDT_QUANTITY_KIND["ACTIVITYCOEFFICIENT"]


def get_qudt_quantity_kind_activity_concentration() -> URIRef:
    """Returns the URI for QUDT quantity kind: Activity Concentration (http://qudt.org/vocab/quantitykind/ActivityConcentration)"""
    return QUDT_QUANTITY_KIND["ACTIVITYCONCENTRATION"]


def get_qudt_quantity_kind_massic_activity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Massic Activity (http://qudt.org/vocab/quantitykind/MassicActivity)"""
    return QUDT_QUANTITY_KIND["MASSICACTIVITY"]


def get_qudt_quantity_kind_activity_thresholds() -> URIRef:
    """Returns the URI for QUDT quantity kind: Activity Thresholds (http://qudt.org/vocab/quantitykind/ActivityThresholds)"""
    return QUDT_QUANTITY_KIND["ACTIVITYTHRESHOLDS"]


def get_qudt_quantity_kind_adaptation() -> URIRef:
    """Returns the URI for QUDT quantity kind: Adaptation (http://qudt.org/vocab/quantitykind/Adaptation)"""
    return QUDT_QUANTITY_KIND["ADAPTATION"]


def get_qudt_quantity_kind_admittance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Admittance (http://qudt.org/vocab/quantitykind/Admittance)"""
    return QUDT_QUANTITY_KIND["ADMITTANCE"]


def get_qudt_quantity_kind_impedance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Impedance (http://qudt.org/vocab/quantitykind/Impedance)"""
    return QUDT_QUANTITY_KIND["IMPEDANCE"]


def get_qudt_quantity_kind_alpha_disintegration_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Alpha Disintegration Energy (http://qudt.org/vocab/quantitykind/AlphaDisintegrationEnergy)"""
    return QUDT_QUANTITY_KIND["ALPHADISINTEGRATIONENERGY"]


def get_qudt_quantity_kind_altitude() -> URIRef:
    """Returns the URI for QUDT quantity kind: Altitude (http://qudt.org/vocab/quantitykind/Altitude)"""
    return QUDT_QUANTITY_KIND["ALTITUDE"]


def get_qudt_quantity_kind_ambient_pressure() -> URIRef:
    """Returns the URI for QUDT quantity kind: Ambient Pressure (http://qudt.org/vocab/quantitykind/AmbientPressure)"""
    return QUDT_QUANTITY_KIND["AMBIENTPRESSURE"]


def get_qudt_quantity_kind_amount_of_biologically_active_substance() -> URIRef:
    """Returns the URI for QUDT quantity kind: amount of biologically active substance (http://qudt.org/vocab/quantitykind/AmountOfBiologicallyActiveSubstance)"""
    return QUDT_QUANTITY_KIND["AMOUNTOFBIOLOGICALLYACTIVESUBSTANCE"]


def get_qudt_quantity_kind_amount_of_cloud_cover() -> URIRef:
    """Returns the URI for QUDT quantity kind: Amount of cloud cover (http://qudt.org/vocab/quantitykind/AmountOfCloudCover)"""
    return QUDT_QUANTITY_KIND["AMOUNTOFCLOUDCOVER"]


def get_qudt_quantity_kind_amount_of_substance_of_concentration() -> URIRef:
    """Returns the URI for QUDT quantity kind: Amount of Substance of Concentration (http://qudt.org/vocab/quantitykind/AmountOfSubstanceConcentration)"""
    return QUDT_QUANTITY_KIND["AMOUNTOFSUBSTANCECONCENTRATION"]


def get_qudt_quantity_kind_concentration() -> URIRef:
    """Returns the URI for QUDT quantity kind: Concentration (http://qudt.org/vocab/quantitykind/Concentration)"""
    return QUDT_QUANTITY_KIND["CONCENTRATION"]


def get_qudt_quantity_kind_fractional_amount_of_substance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Fractional Amount of Substance (http://qudt.org/vocab/quantitykind/AmountOfSubstanceFraction)"""
    return QUDT_QUANTITY_KIND["AMOUNTOFSUBSTANCEFRACTION"]


def get_qudt_quantity_kind_ion_concentration() -> URIRef:
    """Returns the URI for QUDT quantity kind: Ion Concentration (http://qudt.org/vocab/quantitykind/AmountOfSubstanceIonConcentration)"""
    return QUDT_QUANTITY_KIND["AMOUNTOFSUBSTANCEIONCONCENTRATION"]


def get_qudt_quantity_kind_plane_angle() -> URIRef:
    """Returns the URI for QUDT quantity kind: plane angle (http://qudt.org/vocab/quantitykind/PlaneAngle)"""
    return QUDT_QUANTITY_KIND["PLANEANGLE"]


def get_qudt_quantity_kind_angle_of_attack() -> URIRef:
    """Returns the URI for QUDT quantity kind: Angle Of Attack (http://qudt.org/vocab/quantitykind/AngleOfAttack)"""
    return QUDT_QUANTITY_KIND["ANGLEOFATTACK"]


def get_qudt_quantity_kind_angle_of_optical_rotation() -> URIRef:
    """Returns the URI for QUDT quantity kind: Angle of Optical Rotation (http://qudt.org/vocab/quantitykind/AngleOfOpticalRotation)"""
    return QUDT_QUANTITY_KIND["ANGLEOFOPTICALROTATION"]


def get_qudt_quantity_kind_inverse_square_time() -> URIRef:
    """Returns the URI for QUDT quantity kind: Inverse Square Time (http://qudt.org/vocab/quantitykind/InverseSquareTime)"""
    return QUDT_QUANTITY_KIND["INVERSESQUARETIME"]


def get_qudt_quantity_kind_angular_cross_section() -> URIRef:
    """Returns the URI for QUDT quantity kind: Angular Cross-section (http://qudt.org/vocab/quantitykind/AngularCrossSection)"""
    return QUDT_QUANTITY_KIND["ANGULARCROSSSECTION"]


def get_qudt_quantity_kind_spectral_cross_section() -> URIRef:
    """Returns the URI for QUDT quantity kind: Spectral Cross-section (http://qudt.org/vocab/quantitykind/SpectralCrossSection)"""
    return QUDT_QUANTITY_KIND["SPECTRALCROSSSECTION"]


def get_qudt_quantity_kind_angular_distance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Angular Distance (http://qudt.org/vocab/quantitykind/AngularDistance)"""
    return QUDT_QUANTITY_KIND["ANGULARDISTANCE"]


def get_qudt_quantity_kind_angular_frequency() -> URIRef:
    """Returns the URI for QUDT quantity kind: angular frequency (http://qudt.org/vocab/quantitykind/AngularFrequency)"""
    return QUDT_QUANTITY_KIND["ANGULARFREQUENCY"]


def get_qudt_quantity_kind_angular_velocity() -> URIRef:
    """Returns the URI for QUDT quantity kind: angular velocity (http://qudt.org/vocab/quantitykind/AngularVelocity)"""
    return QUDT_QUANTITY_KIND["ANGULARVELOCITY"]


def get_qudt_quantity_kind_rotationalfrequency() -> URIRef:
    """Returns the URI for QUDT quantity kind: RotationalFrequency (http://qudt.org/vocab/quantitykind/RotationalFrequency)"""
    return QUDT_QUANTITY_KIND["ROTATIONALFREQUENCY"]


def get_qudt_quantity_kind_rotationalfrequency() -> URIRef:
    """Returns the URI for QUDT quantity kind: RotationalFrequency (http://qudt.org/vocab/quantitykind/RotationalVelocity)"""
    return QUDT_QUANTITY_KIND["ROTATIONALVELOCITY"]


def get_qudt_quantity_kind_angular_impulse() -> URIRef:
    """Returns the URI for QUDT quantity kind: angular impulse (http://qudt.org/vocab/quantitykind/AngularImpulse)"""
    return QUDT_QUANTITY_KIND["ANGULARIMPULSE"]


def get_qudt_quantity_kind_angular_momentum_per_angle() -> URIRef:
    """Returns the URI for QUDT quantity kind: Angular Momentum per Angle (http://qudt.org/vocab/quantitykind/AngularMomentumPerAngle)"""
    return QUDT_QUANTITY_KIND["ANGULARMOMENTUMPERANGLE"]


def get_qudt_quantity_kind_angular_reciprocal_lattice_vector() -> URIRef:
    """Returns the URI for QUDT quantity kind: Angular Reciprocal Lattice Vector (http://qudt.org/vocab/quantitykind/AngularReciprocalLatticeVector)"""
    return QUDT_QUANTITY_KIND["ANGULARRECIPROCALLATTICEVECTOR"]


def get_qudt_quantity_kind_angular_wavenumber() -> URIRef:
    """Returns the URI for QUDT quantity kind: angular wavenumber (http://qudt.org/vocab/quantitykind/AngularWavenumber)"""
    return QUDT_QUANTITY_KIND["ANGULARWAVENUMBER"]


def get_qudt_quantity_kind_apogee_radius() -> URIRef:
    """Returns the URI for QUDT quantity kind: Apogee Radius (http://qudt.org/vocab/quantitykind/ApogeeRadius)"""
    return QUDT_QUANTITY_KIND["APOGEERADIUS"]


def get_qudt_quantity_kind_radius() -> URIRef:
    """Returns the URI for QUDT quantity kind: Radius (http://qudt.org/vocab/quantitykind/Radius)"""
    return QUDT_QUANTITY_KIND["RADIUS"]


def get_qudt_quantity_kind_apparent_power() -> URIRef:
    """Returns the URI for QUDT quantity kind: apparent power (http://qudt.org/vocab/quantitykind/ApparentPower)"""
    return QUDT_QUANTITY_KIND["APPARENTPOWER"]


def get_qudt_quantity_kind_voltage() -> URIRef:
    """Returns the URI for QUDT quantity kind: Voltage (http://qudt.org/vocab/quantitykind/Voltage)"""
    return QUDT_QUANTITY_KIND["VOLTAGE"]


def get_qudt_quantity_kind_area_angle() -> URIRef:
    """Returns the URI for QUDT quantity kind: Area Angle (http://qudt.org/vocab/quantitykind/AreaAngle)"""
    return QUDT_QUANTITY_KIND["AREAANGLE"]


def get_qudt_quantity_kind_areic_bit_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: areic bit density (http://qudt.org/vocab/quantitykind/AreaBitDensity)"""
    return QUDT_QUANTITY_KIND["AREABITDENSITY"]


def get_qudt_quantity_kind_areic_charge_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: areic charge density (http://qudt.org/vocab/quantitykind/AreaChargeDensity)"""
    return QUDT_QUANTITY_KIND["AREACHARGEDENSITY"]


def get_qudt_quantity_kind_areic_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: areic mass (http://qudt.org/vocab/quantitykind/AreaMass)"""
    return QUDT_QUANTITY_KIND["AREAMASS"]


def get_qudt_quantity_kind_area_per_length() -> URIRef:
    """Returns the URI for QUDT quantity kind: area per length (http://qudt.org/vocab/quantitykind/AreaPerLength)"""
    return QUDT_QUANTITY_KIND["AREAPERLENGTH"]


def get_qudt_quantity_kind_area_per_heating_load() -> URIRef:
    """Returns the URI for QUDT quantity kind: area per heating load (http://qudt.org/vocab/quantitykind/AreaPerPower)"""
    return QUDT_QUANTITY_KIND["AREAPERPOWER"]


def get_qudt_quantity_kind_area_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Area Ratio (http://qudt.org/vocab/quantitykind/AreaRatio)"""
    return QUDT_QUANTITY_KIND["AREARATIO"]


def get_qudt_quantity_kind_aeric_heat_flow_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: Aeric Heat Flow Rate (http://qudt.org/vocab/quantitykind/AreicHeatFlowRate)"""
    return QUDT_QUANTITY_KIND["AREICHEATFLOWRATE"]


def get_qudt_quantity_kind_asset() -> URIRef:
    """Returns the URI for QUDT quantity kind: Asset (http://qudt.org/vocab/quantitykind/Asset)"""
    return QUDT_QUANTITY_KIND["ASSET"]


def get_qudt_quantity_kind_atmospheric_hydroxylation_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: Atmospheric Hydroxylation Rate (http://qudt.org/vocab/quantitykind/AtmosphericHydroxylationRate)"""
    return QUDT_QUANTITY_KIND["ATMOSPHERICHYDROXYLATIONRATE"]


def get_qudt_quantity_kind_atmospheric_pressure() -> URIRef:
    """Returns the URI for QUDT quantity kind: Atmospheric Pressure (http://qudt.org/vocab/quantitykind/AtmosphericPressure)"""
    return QUDT_QUANTITY_KIND["ATMOSPHERICPRESSURE"]


def get_qudt_quantity_kind_atom_scattering_factor() -> URIRef:
    """Returns the URI for QUDT quantity kind: Atom Scattering Factor (http://qudt.org/vocab/quantitykind/AtomScatteringFactor)"""
    return QUDT_QUANTITY_KIND["ATOMSCATTERINGFACTOR"]


def get_qudt_quantity_kind_atomic_attenuation_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Atomic Attenuation Coefficient (http://qudt.org/vocab/quantitykind/AtomicAttenuationCoefficient)"""
    return QUDT_QUANTITY_KIND["ATOMICATTENUATIONCOEFFICIENT"]


def get_qudt_quantity_kind_molar_attenuation_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Molar Attenuation Coefficient (http://qudt.org/vocab/quantitykind/MolarAttenuationCoefficient)"""
    return QUDT_QUANTITY_KIND["MOLARATTENUATIONCOEFFICIENT"]


def get_qudt_quantity_kind_atomic_charge() -> URIRef:
    """Returns the URI for QUDT quantity kind: Atomic Charge (http://qudt.org/vocab/quantitykind/AtomicCharge)"""
    return QUDT_QUANTITY_KIND["ATOMICCHARGE"]


def get_qudt_quantity_kind_atomic_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: Atomic Mass (http://qudt.org/vocab/quantitykind/AtomicMass)"""
    return QUDT_QUANTITY_KIND["ATOMICMASS"]


def get_qudt_quantity_kind_atomic_number() -> URIRef:
    """Returns the URI for QUDT quantity kind: Atomic Number (http://qudt.org/vocab/quantitykind/AtomicNumber)"""
    return QUDT_QUANTITY_KIND["ATOMICNUMBER"]


def get_qudt_quantity_kind_count() -> URIRef:
    """Returns the URI for QUDT quantity kind: Count (http://qudt.org/vocab/quantitykind/Count)"""
    return QUDT_QUANTITY_KIND["COUNT"]


def get_qudt_quantity_kind_attenuation_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Attenuation Coefficient (http://qudt.org/vocab/quantitykind/AttenuationCoefficient)"""
    return QUDT_QUANTITY_KIND["ATTENUATIONCOEFFICIENT"]


def get_qudt_quantity_kind_auditory_thresholds() -> URIRef:
    """Returns the URI for QUDT quantity kind: Auditory Thresholds (http://qudt.org/vocab/quantitykind/AuditoryThresholds)"""
    return QUDT_QUANTITY_KIND["AUDITORYTHRESHOLDS"]


def get_qudt_quantity_kind_sound_power_level() -> URIRef:
    """Returns the URI for QUDT quantity kind: Sound power level (http://qudt.org/vocab/quantitykind/SoundPowerLevel)"""
    return QUDT_QUANTITY_KIND["SOUNDPOWERLEVEL"]


def get_qudt_quantity_kind_auxillary_magnetic_field() -> URIRef:
    """Returns the URI for QUDT quantity kind: Auxillary Magnetic Field (http://qudt.org/vocab/quantitykind/AuxillaryMagneticField)"""
    return QUDT_QUANTITY_KIND["AUXILLARYMAGNETICFIELD"]


def get_qudt_quantity_kind_magnetic_field_strength() -> URIRef:
    """Returns the URI for QUDT quantity kind: magnetic field strength (http://qudt.org/vocab/quantitykind/MagneticFieldStrength)"""
    return QUDT_QUANTITY_KIND["MAGNETICFIELDSTRENGTH"]


def get_qudt_quantity_kind_average_energy_loss_per_elementary_charge_produced() -> (
    URIRef
):
    """Returns the URI for QUDT quantity kind: Average Energy Loss per Elementary Charge Produced (http://qudt.org/vocab/quantitykind/AverageEnergyLossPerElementaryChargeProduced)"""
    return QUDT_QUANTITY_KIND["AVERAGEENERGYLOSSPERELEMENTARYCHARGEPRODUCED"]


def get_qudt_quantity_kind_average_head_end_pressure() -> URIRef:
    """Returns the URI for QUDT quantity kind: Average Head End Pressure (http://qudt.org/vocab/quantitykind/AverageHeadEndPressure)"""
    return QUDT_QUANTITY_KIND["AVERAGEHEADENDPRESSURE"]


def get_qudt_quantity_kind_head_end_pressure() -> URIRef:
    """Returns the URI for QUDT quantity kind: Head End Pressure (http://qudt.org/vocab/quantitykind/HeadEndPressure)"""
    return QUDT_QUANTITY_KIND["HEADENDPRESSURE"]


def get_qudt_quantity_kind_average_logarithmic_energy_decrement() -> URIRef:
    """Returns the URI for QUDT quantity kind: Average Logarithmic Energy Decrement (http://qudt.org/vocab/quantitykind/AverageLogarithmicEnergyDecrement)"""
    return QUDT_QUANTITY_KIND["AVERAGELOGARITHMICENERGYDECREMENT"]


def get_qudt_quantity_kind_average_specific_impulse() -> URIRef:
    """Returns the URI for QUDT quantity kind: Average Specific Impulse (http://qudt.org/vocab/quantitykind/AverageSpecificImpulse)"""
    return QUDT_QUANTITY_KIND["AVERAGESPECIFICIMPULSE"]


def get_qudt_quantity_kind_specific_impulse() -> URIRef:
    """Returns the URI for QUDT quantity kind: Specific Impulse (http://qudt.org/vocab/quantitykind/SpecificImpulse)"""
    return QUDT_QUANTITY_KIND["SPECIFICIMPULSE"]


def get_qudt_quantity_kind_average_vacuum_thrust() -> URIRef:
    """Returns the URI for QUDT quantity kind: Average Vacuum Thrust (http://qudt.org/vocab/quantitykind/AverageVacuumThrust)"""
    return QUDT_QUANTITY_KIND["AVERAGEVACUUMTHRUST"]


def get_qudt_quantity_kind_vacuum_thrust() -> URIRef:
    """Returns the URI for QUDT quantity kind: Vacuum Thrust (http://qudt.org/vocab/quantitykind/VacuumThrust)"""
    return QUDT_QUANTITY_KIND["VACUUMTHRUST"]


def get_qudt_quantity_kind_azimuth() -> URIRef:
    """Returns the URI for QUDT quantity kind: Azimuth (http://qudt.org/vocab/quantitykind/Azimuth)"""
    return QUDT_QUANTITY_KIND["AZIMUTH"]


def get_qudt_quantity_kind_bandwidth_distance_product() -> URIRef:
    """Returns the URI for QUDT quantity kind: bandwidth distance product (http://qudt.org/vocab/quantitykind/BandwidthDistanceProduct)"""
    return QUDT_QUANTITY_KIND["BANDWIDTHDISTANCEPRODUCT"]


def get_qudt_quantity_kind_battery_capacity() -> URIRef:
    """Returns the URI for QUDT quantity kind: battery capacity (http://qudt.org/vocab/quantitykind/BatteryCapacity)"""
    return QUDT_QUANTITY_KIND["BATTERYCAPACITY"]


def get_qudt_quantity_kind_bending_moment_of_force() -> URIRef:
    """Returns the URI for QUDT quantity kind: Bending Moment of Force (http://qudt.org/vocab/quantitykind/BendingMomentOfForce)"""
    return QUDT_QUANTITY_KIND["BENDINGMOMENTOFFORCE"]


def get_qudt_quantity_kind_beta_disintegration_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Beta Disintegration Energy (http://qudt.org/vocab/quantitykind/BetaDisintegrationEnergy)"""
    return QUDT_QUANTITY_KIND["BETADISINTEGRATIONENERGY"]


def get_qudt_quantity_kind_bevel_gear_pitch_angle() -> URIRef:
    """Returns the URI for QUDT quantity kind: Bevel Gear Pitch Angle (http://qudt.org/vocab/quantitykind/BevelGearPitchAngle)"""
    return QUDT_QUANTITY_KIND["BEVELGEARPITCHANGLE"]


def get_qudt_quantity_kind_binding_fraction() -> URIRef:
    """Returns the URI for QUDT quantity kind: Binding Fraction (http://qudt.org/vocab/quantitykind/BindingFraction)"""
    return QUDT_QUANTITY_KIND["BINDINGFRACTION"]


def get_qudt_quantity_kind_bioconcentration_factor() -> URIRef:
    """Returns the URI for QUDT quantity kind: Bioconcentration Factor (http://qudt.org/vocab/quantitykind/BioconcentrationFactor)"""
    return QUDT_QUANTITY_KIND["BIOCONCENTRATIONFACTOR"]


def get_qudt_quantity_kind_biodegredation_half_life() -> URIRef:
    """Returns the URI for QUDT quantity kind: Biodegredation Half Life (http://qudt.org/vocab/quantitykind/BiodegredationHalfLife)"""
    return QUDT_QUANTITY_KIND["BIODEGREDATIONHALFLIFE"]


def get_qudt_quantity_kind_biogeochemical_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: Biogeochemical Rate (http://qudt.org/vocab/quantitykind/BiogeochemicalRate)"""
    return QUDT_QUANTITY_KIND["BIOGEOCHEMICALRATE"]


def get_qudt_quantity_kind_bit_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: bit rate (http://qudt.org/vocab/quantitykind/BitRate)"""
    return QUDT_QUANTITY_KIND["BITRATE"]


def get_qudt_quantity_kind_blood_glucose_level() -> URIRef:
    """Returns the URI for QUDT quantity kind: Blood Glucose Level (http://qudt.org/vocab/quantitykind/BloodGlucoseLevel)"""
    return QUDT_QUANTITY_KIND["BLOODGLUCOSELEVEL"]


def get_qudt_quantity_kind_blood_glucose_level_by_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: Blood Glucose Level by Mass (http://qudt.org/vocab/quantitykind/MassBasedBloodGlucoseLevel)"""
    return QUDT_QUANTITY_KIND["MASSBASEDBLOODGLUCOSELEVEL"]


def get_qudt_quantity_kind_blood_glucose_level_by_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: Blood Glucose Level by Mass (http://qudt.org/vocab/quantitykind/BloodGlucoseLevel_Mass)"""
    return QUDT_QUANTITY_KIND["BLOODGLUCOSELEVEL_MASS"]


def get_qudt_quantity_kind_body_mass_index() -> URIRef:
    """Returns the URI for QUDT quantity kind: Body Mass Index (http://qudt.org/vocab/quantitykind/BodyMassIndex)"""
    return QUDT_QUANTITY_KIND["BODYMASSINDEX"]


def get_qudt_quantity_kind_boiling_point_temperature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Boiling Point Temperature (http://qudt.org/vocab/quantitykind/BoilingPoint)"""
    return QUDT_QUANTITY_KIND["BOILINGPOINT"]


def get_qudt_quantity_kind_temperature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Temperature (http://qudt.org/vocab/quantitykind/Temperature)"""
    return QUDT_QUANTITY_KIND["TEMPERATURE"]


def get_qudt_quantity_kind_bragg_angle() -> URIRef:
    """Returns the URI for QUDT quantity kind: Bragg Angle (http://qudt.org/vocab/quantitykind/BraggAngle)"""
    return QUDT_QUANTITY_KIND["BRAGGANGLE"]


def get_qudt_quantity_kind_breadth() -> URIRef:
    """Returns the URI for QUDT quantity kind: breadth (http://qudt.org/vocab/quantitykind/Breadth)"""
    return QUDT_QUANTITY_KIND["BREADTH"]


def get_qudt_quantity_kind_buckling_factor() -> URIRef:
    """Returns the URI for QUDT quantity kind: Buckling Factor (http://qudt.org/vocab/quantitykind/BucklingFactor)"""
    return QUDT_QUANTITY_KIND["BUCKLINGFACTOR"]


def get_qudt_quantity_kind_bulk_modulus() -> URIRef:
    """Returns the URI for QUDT quantity kind: Bulk Modulus (http://qudt.org/vocab/quantitykind/BulkModulus)"""
    return QUDT_QUANTITY_KIND["BULKMODULUS"]


def get_qudt_quantity_kind_burgers_vector() -> URIRef:
    """Returns the URI for QUDT quantity kind: Burgers Vector (http://qudt.org/vocab/quantitykind/BurgersVector)"""
    return QUDT_QUANTITY_KIND["BURGERSVECTOR"]


def get_qudt_quantity_kind_burn_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: Burn Rate (http://qudt.org/vocab/quantitykind/BurnRate)"""
    return QUDT_QUANTITY_KIND["BURNRATE"]


def get_qudt_quantity_kind_velocity() -> URIRef:
    """Returns the URI for QUDT quantity kind: velocity (http://qudt.org/vocab/quantitykind/Velocity)"""
    return QUDT_QUANTITY_KIND["VELOCITY"]


def get_qudt_quantity_kind_burn_time() -> URIRef:
    """Returns the URI for QUDT quantity kind: Burn Time (http://qudt.org/vocab/quantitykind/BurnTime)"""
    return QUDT_QUANTITY_KIND["BURNTIME"]


def get_qudt_quantity_kind_burst_factor() -> URIRef:
    """Returns the URI for QUDT quantity kind: burst factor (http://qudt.org/vocab/quantitykind/BurstFactor)"""
    return QUDT_QUANTITY_KIND["BURSTFACTOR"]


def get_qudt_quantity_kind_byte_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: byte rate (http://qudt.org/vocab/quantitykind/ByteRate)"""
    return QUDT_QUANTITY_KIND["BYTERATE"]


def get_qudt_quantity_kind_center_of_gravity_in_the_x_axis() -> URIRef:
    """Returns the URI for QUDT quantity kind: Center of Gravity in the X axis (http://qudt.org/vocab/quantitykind/CENTER-OF-GRAVITY_X)"""
    return QUDT_QUANTITY_KIND["CENTER-OF-GRAVITY_X"]


def get_qudt_quantity_kind_center_of_gravity_in_the_x_axis() -> URIRef:
    """Returns the URI for QUDT quantity kind: Center of Gravity in the X axis (http://qudt.org/vocab/quantitykind/CenterOfGravity_X)"""
    return QUDT_QUANTITY_KIND["CENTEROFGRAVITY_X"]


def get_qudt_quantity_kind_center_of_gravity_in_the_y_axis() -> URIRef:
    """Returns the URI for QUDT quantity kind: Center of Gravity in the Y axis (http://qudt.org/vocab/quantitykind/CENTER-OF-GRAVITY_Y)"""
    return QUDT_QUANTITY_KIND["CENTER-OF-GRAVITY_Y"]


def get_qudt_quantity_kind_center_of_gravity_in_the_y_axis() -> URIRef:
    """Returns the URI for QUDT quantity kind: Center of Gravity in the Y axis (http://qudt.org/vocab/quantitykind/CenterOfGravity_Y)"""
    return QUDT_QUANTITY_KIND["CENTEROFGRAVITY_Y"]


def get_qudt_quantity_kind_center_of_gravity_in_the_z_axis() -> URIRef:
    """Returns the URI for QUDT quantity kind: Center of Gravity in the Z axis (http://qudt.org/vocab/quantitykind/CENTER-OF-GRAVITY_Z)"""
    return QUDT_QUANTITY_KIND["CENTER-OF-GRAVITY_Z"]


def get_qudt_quantity_kind_center_of_gravity_in_the_z_axis() -> URIRef:
    """Returns the URI for QUDT quantity kind: Center of Gravity in the Z axis (http://qudt.org/vocab/quantitykind/CenterOfGravity_Z)"""
    return QUDT_QUANTITY_KIND["CENTEROFGRAVITY_Z"]


def get_qudt_quantity_kind_center_of_mass_com() -> URIRef:
    """Returns the URI for QUDT quantity kind: Center of Mass (CoM) (http://qudt.org/vocab/quantitykind/CENTER-OF-MASS)"""
    return QUDT_QUANTITY_KIND["CENTER-OF-MASS"]


def get_qudt_quantity_kind_position_vector() -> URIRef:
    """Returns the URI for QUDT quantity kind: Position Vector (http://qudt.org/vocab/quantitykind/PositionVector)"""
    return QUDT_QUANTITY_KIND["POSITIONVECTOR"]


def get_qudt_quantity_kind_co2equivalent() -> URIRef:
    """Returns the URI for QUDT quantity kind: CO2Equivalent (http://qudt.org/vocab/quantitykind/CO2Equivalent)"""
    return QUDT_QUANTITY_KIND["CO2EQUIVALENT"]


def get_qudt_quantity_kind_mass_equivalent() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass Equivalent (http://qudt.org/vocab/quantitykind/MassEquivalent)"""
    return QUDT_QUANTITY_KIND["MASSEQUIVALENT"]


def get_qudt_quantity_kind_contract_end_item_cei_specification_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: Contract End Item (CEI) Specification Mass. (http://qudt.org/vocab/quantitykind/CONTRACT-END-ITEM-SPECIFICATION-MASS)"""
    return QUDT_QUANTITY_KIND["CONTRACT-END-ITEM-SPECIFICATION-MASS"]


def get_qudt_quantity_kind_control_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: Control Mass. (http://qudt.org/vocab/quantitykind/CONTROL-MASS)"""
    return QUDT_QUANTITY_KIND["CONTROL-MASS"]


def get_qudt_quantity_kind_canonical_partition_function() -> URIRef:
    """Returns the URI for QUDT quantity kind: Canonical Partition Function (http://qudt.org/vocab/quantitykind/CanonicalPartitionFunction)"""
    return QUDT_QUANTITY_KIND["CANONICALPARTITIONFUNCTION"]


def get_qudt_quantity_kind_capacity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Capacity (http://qudt.org/vocab/quantitykind/Capacity)"""
    return QUDT_QUANTITY_KIND["CAPACITY"]


def get_qudt_quantity_kind_carrier_lifetime() -> URIRef:
    """Returns the URI for QUDT quantity kind: Carrier LifetIme (http://qudt.org/vocab/quantitykind/CarrierLifetime)"""
    return QUDT_QUANTITY_KIND["CARRIERLIFETIME"]


def get_qudt_quantity_kind_cartesian_area() -> URIRef:
    """Returns the URI for QUDT quantity kind: Cartesian Area (http://qudt.org/vocab/quantitykind/CartesianArea)"""
    return QUDT_QUANTITY_KIND["CARTESIANAREA"]


def get_qudt_quantity_kind_cartesian_coordinates() -> URIRef:
    """Returns the URI for QUDT quantity kind: Cartesian coordinates (http://qudt.org/vocab/quantitykind/CartesianCoordinates)"""
    return QUDT_QUANTITY_KIND["CARTESIANCOORDINATES"]


def get_qudt_quantity_kind_volume() -> URIRef:
    """Returns the URI for QUDT quantity kind: volume (http://qudt.org/vocab/quantitykind/CartesianVolume)"""
    return QUDT_QUANTITY_KIND["CARTESIANVOLUME"]


def get_qudt_quantity_kind_catalytic_activity_concentration() -> URIRef:
    """Returns the URI for QUDT quantity kind: Catalytic Activity Concentration (http://qudt.org/vocab/quantitykind/CatalyticActivityConcentration)"""
    return QUDT_QUANTITY_KIND["CATALYTICACTIVITYCONCENTRATION"]


def get_qudt_quantity_kind_cation_exchange_capacity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Cation Exchange Capacity (http://qudt.org/vocab/quantitykind/CationExchangeCapacity)"""
    return QUDT_QUANTITY_KIND["CATIONEXCHANGECAPACITY"]


def get_qudt_quantity_kind_reactive_charge_per_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: Reactive Charge per Mass (http://qudt.org/vocab/quantitykind/ReactiveChargePerMass)"""
    return QUDT_QUANTITY_KIND["REACTIVECHARGEPERMASS"]


def get_qudt_quantity_kind_celsius_temperature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Celsius temperature (http://qudt.org/vocab/quantitykind/CelsiusTemperature)"""
    return QUDT_QUANTITY_KIND["CELSIUSTEMPERATURE"]


def get_qudt_quantity_kind_characteristic_acoustic_impedance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Characteristic Acoustic Impedance (http://qudt.org/vocab/quantitykind/CharacteristicAcousticImpedance)"""
    return QUDT_QUANTITY_KIND["CHARACTERISTICACOUSTICIMPEDANCE"]


def get_qudt_quantity_kind_characteristic_velocity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Characteristic Velocity (http://qudt.org/vocab/quantitykind/CharacteristicVelocity)"""
    return QUDT_QUANTITY_KIND["CHARACTERISTICVELOCITY"]


def get_qudt_quantity_kind_charge_number() -> URIRef:
    """Returns the URI for QUDT quantity kind: Charge Number (http://qudt.org/vocab/quantitykind/ChargeNumber)"""
    return QUDT_QUANTITY_KIND["CHARGENUMBER"]


def get_qudt_quantity_kind_chemical_affinity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Chemical Affinity (http://qudt.org/vocab/quantitykind/ChemicalAffinity)"""
    return QUDT_QUANTITY_KIND["CHEMICALAFFINITY"]


def get_qudt_quantity_kind_chemical_consumption_per_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: Chemical Consumption per Mass (http://qudt.org/vocab/quantitykind/ChemicalConsumptionPerMass)"""
    return QUDT_QUANTITY_KIND["CHEMICALCONSUMPTIONPERMASS"]


def get_qudt_quantity_kind_chemical_potential() -> URIRef:
    """Returns the URI for QUDT quantity kind: chemical potential (http://qudt.org/vocab/quantitykind/ChemicalPotential)"""
    return QUDT_QUANTITY_KIND["CHEMICALPOTENTIAL"]


def get_qudt_quantity_kind_chromaticity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Chromaticity (http://qudt.org/vocab/quantitykind/Chromaticity)"""
    return QUDT_QUANTITY_KIND["CHROMATICITY"]


def get_qudt_quantity_kind_closest_approach_radius() -> URIRef:
    """Returns the URI for QUDT quantity kind: Closest Approach Radius (http://qudt.org/vocab/quantitykind/ClosestApproachRadius)"""
    return QUDT_QUANTITY_KIND["CLOSESTAPPROACHRADIUS"]


def get_qudt_quantity_kind_coefficientofperformance() -> URIRef:
    """Returns the URI for QUDT quantity kind: CoefficientOfPerformance (http://qudt.org/vocab/quantitykind/CoefficientOfPerformance)"""
    return QUDT_QUANTITY_KIND["COEFFICIENTOFPERFORMANCE"]


def get_qudt_quantity_kind_coercivity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Coercivity (http://qudt.org/vocab/quantitykind/Coercivity)"""
    return QUDT_QUANTITY_KIND["COERCIVITY"]


def get_qudt_quantity_kind_coherence_length() -> URIRef:
    """Returns the URI for QUDT quantity kind: Coherence Length (http://qudt.org/vocab/quantitykind/CoherenceLength)"""
    return QUDT_QUANTITY_KIND["COHERENCELENGTH"]


def get_qudt_quantity_kind_cold_receptor_threshold() -> URIRef:
    """Returns the URI for QUDT quantity kind: Cold Receptor Threshold (http://qudt.org/vocab/quantitykind/ColdReceptorThreshold)"""
    return QUDT_QUANTITY_KIND["COLDRECEPTORTHRESHOLD"]


def get_qudt_quantity_kind_combined_non_evaporative_heat_transfer_coefficient() -> (
    URIRef
):
    """Returns the URI for QUDT quantity kind: Combined Non Evaporative Heat Transfer Coefficient (http://qudt.org/vocab/quantitykind/CombinedNonEvaporativeHeatTransferCoefficient)"""
    return QUDT_QUANTITY_KIND["COMBINEDNONEVAPORATIVEHEATTRANSFERCOEFFICIENT"]


def get_qudt_quantity_kind_combustion_chamber_temperature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Combustion Chamber Temperature (http://qudt.org/vocab/quantitykind/CombustionChamberTemperature)"""
    return QUDT_QUANTITY_KIND["COMBUSTIONCHAMBERTEMPERATURE"]


def get_qudt_quantity_kind_imaginary_part_of_complex_frequency() -> URIRef:
    """Returns the URI for QUDT quantity kind: imaginary part of complex frequency (http://qudt.org/vocab/quantitykind/ComplexFrequency_Imaginary)"""
    return QUDT_QUANTITY_KIND["COMPLEXFREQUENCY_IMAGINARY"]


def get_qudt_quantity_kind_real_part_of_complex_frequency() -> URIRef:
    """Returns the URI for QUDT quantity kind: real part of complex frequency (http://qudt.org/vocab/quantitykind/ComplexFrequency_Real)"""
    return QUDT_QUANTITY_KIND["COMPLEXFREQUENCY_REAL"]


def get_qudt_quantity_kind_complex_power() -> URIRef:
    """Returns the URI for QUDT quantity kind: Complex Power (http://qudt.org/vocab/quantitykind/ComplexPower)"""
    return QUDT_QUANTITY_KIND["COMPLEXPOWER"]


def get_qudt_quantity_kind_electric_current_phasor() -> URIRef:
    """Returns the URI for QUDT quantity kind: Electric Current Phasor (http://qudt.org/vocab/quantitykind/ElectricCurrentPhasor)"""
    return QUDT_QUANTITY_KIND["ELECTRICCURRENTPHASOR"]


def get_qudt_quantity_kind_voltage_phasor() -> URIRef:
    """Returns the URI for QUDT quantity kind: Voltage Phasor (http://qudt.org/vocab/quantitykind/VoltagePhasor)"""
    return QUDT_QUANTITY_KIND["VOLTAGEPHASOR"]


def get_qudt_quantity_kind_compound_plane_angle() -> URIRef:
    """Returns the URI for QUDT quantity kind: Compound Plane Angle (http://qudt.org/vocab/quantitykind/CompoundPlaneAngle)"""
    return QUDT_QUANTITY_KIND["COMPOUNDPLANEANGLE"]


def get_qudt_quantity_kind_compressibility() -> URIRef:
    """Returns the URI for QUDT quantity kind: Compressibility (http://qudt.org/vocab/quantitykind/Compressibility)"""
    return QUDT_QUANTITY_KIND["COMPRESSIBILITY"]


def get_qudt_quantity_kind_compressibility_factor() -> URIRef:
    """Returns the URI for QUDT quantity kind: Compressibility Factor (http://qudt.org/vocab/quantitykind/CompressibilityFactor)"""
    return QUDT_QUANTITY_KIND["COMPRESSIBILITYFACTOR"]


def get_qudt_quantity_kind_conductance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Conductance (http://qudt.org/vocab/quantitykind/Conductance)"""
    return QUDT_QUANTITY_KIND["CONDUCTANCE"]


def get_qudt_quantity_kind_conduction_speed() -> URIRef:
    """Returns the URI for QUDT quantity kind: Conduction Speed (http://qudt.org/vocab/quantitykind/ConductionSpeed)"""
    return QUDT_QUANTITY_KIND["CONDUCTIONSPEED"]


def get_qudt_quantity_kind_conductive_heat_transfer_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: Conductive Heat Transfer Rate (http://qudt.org/vocab/quantitykind/ConductiveHeatTransferRate)"""
    return QUDT_QUANTITY_KIND["CONDUCTIVEHEATTRANSFERRATE"]


def get_qudt_quantity_kind_heat_flow_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: Heat Flow Rate (http://qudt.org/vocab/quantitykind/HeatFlowRate)"""
    return QUDT_QUANTITY_KIND["HEATFLOWRATE"]


def get_qudt_quantity_kind_conductivity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Conductivity (http://qudt.org/vocab/quantitykind/Conductivity)"""
    return QUDT_QUANTITY_KIND["CONDUCTIVITY"]


def get_qudt_quantity_kind_conductivity_variance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Conductivity Variance (http://qudt.org/vocab/quantitykind/ConductivityVariance)"""
    return QUDT_QUANTITY_KIND["CONDUCTIVITYVARIANCE"]


def get_qudt_quantity_kind_conductivity_variance_neon() -> URIRef:
    """Returns the URI for QUDT quantity kind: Conductivity Variance, NEON (http://qudt.org/vocab/quantitykind/ConductivityVariance_NEON)"""
    return QUDT_QUANTITY_KIND["CONDUCTIVITYVARIANCE_NEON"]


def get_qudt_quantity_kind_constringence() -> URIRef:
    """Returns the URI for QUDT quantity kind: Constringence (http://qudt.org/vocab/quantitykind/Constringence)"""
    return QUDT_QUANTITY_KIND["CONSTRINGENCE"]


def get_qudt_quantity_kind_convective_heat_transfer() -> URIRef:
    """Returns the URI for QUDT quantity kind: Convective Heat Transfer (http://qudt.org/vocab/quantitykind/ConvectiveHeatTransfer)"""
    return QUDT_QUANTITY_KIND["CONVECTIVEHEATTRANSFER"]


def get_qudt_quantity_kind_cooling_performance_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Cooling Performance Ratio (http://qudt.org/vocab/quantitykind/CoolingPerformanceRatio)"""
    return QUDT_QUANTITY_KIND["COOLINGPERFORMANCERATIO"]


def get_qudt_quantity_kind_correlated_colour_temperature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Correlated Colour Temperature (http://qudt.org/vocab/quantitykind/CorrelatedColorTemperature)"""
    return QUDT_QUANTITY_KIND["CORRELATEDCOLORTEMPERATURE"]


def get_qudt_quantity_kind_delta_u_v() -> URIRef:
    """Returns the URI for QUDT quantity kind: Delta u,v (http://qudt.org/vocab/quantitykind/Duv)"""
    return QUDT_QUANTITY_KIND["DUV"]


def get_qudt_quantity_kind_cost_per_area() -> URIRef:
    """Returns the URI for QUDT quantity kind: cost per area (http://qudt.org/vocab/quantitykind/CostPerArea)"""
    return QUDT_QUANTITY_KIND["COSTPERAREA"]


def get_qudt_quantity_kind_energy_cost() -> URIRef:
    """Returns the URI for QUDT quantity kind: energy cost (http://qudt.org/vocab/quantitykind/CostPerEnergy)"""
    return QUDT_QUANTITY_KIND["COSTPERENERGY"]


def get_qudt_quantity_kind_cost_per_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: cost per mass (http://qudt.org/vocab/quantitykind/CostPerMass)"""
    return QUDT_QUANTITY_KIND["COSTPERMASS"]


def get_qudt_quantity_kind_cost_per_power() -> URIRef:
    """Returns the URI for QUDT quantity kind: cost per power (http://qudt.org/vocab/quantitykind/CostPerPower)"""
    return QUDT_QUANTITY_KIND["COSTPERPOWER"]


def get_qudt_quantity_kind_countrate() -> URIRef:
    """Returns the URI for QUDT quantity kind: CountRate (http://qudt.org/vocab/quantitykind/CountRate)"""
    return QUDT_QUANTITY_KIND["COUNTRATE"]


def get_qudt_quantity_kind_coupling_factor() -> URIRef:
    """Returns the URI for QUDT quantity kind: coupling factor (http://qudt.org/vocab/quantitykind/CouplingFactor)"""
    return QUDT_QUANTITY_KIND["COUPLINGFACTOR"]


def get_qudt_quantity_kind_cross_section() -> URIRef:
    """Returns the URI for QUDT quantity kind: Cross-section (http://qudt.org/vocab/quantitykind/CrossSection)"""
    return QUDT_QUANTITY_KIND["CROSSSECTION"]


def get_qudt_quantity_kind_cross_sectional_area() -> URIRef:
    """Returns the URI for QUDT quantity kind: Cross-sectional Area (http://qudt.org/vocab/quantitykind/CrossSectionalArea)"""
    return QUDT_QUANTITY_KIND["CROSSSECTIONALAREA"]


def get_qudt_quantity_kind_cubic_expansion_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: cubic expansion coefficient (http://qudt.org/vocab/quantitykind/CubicExpansionCoefficient)"""
    return QUDT_QUANTITY_KIND["CUBICEXPANSIONCOEFFICIENT"]


def get_qudt_quantity_kind_expansion_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Expansion Ratio (http://qudt.org/vocab/quantitykind/ExpansionRatio)"""
    return QUDT_QUANTITY_KIND["EXPANSIONRATIO"]


def get_qudt_quantity_kind_curie_temperature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Curie temperature (http://qudt.org/vocab/quantitykind/CurieTemperature)"""
    return QUDT_QUANTITY_KIND["CURIETEMPERATURE"]


def get_qudt_quantity_kind_neel_temperature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Neel Temperature (http://qudt.org/vocab/quantitykind/NeelTemperature)"""
    return QUDT_QUANTITY_KIND["NEELTEMPERATURE"]


def get_qudt_quantity_kind_superconduction_transition_temperature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Superconduction Transition Temperature (http://qudt.org/vocab/quantitykind/SuperconductionTransitionTemperature)"""
    return QUDT_QUANTITY_KIND["SUPERCONDUCTIONTRANSITIONTEMPERATURE"]


def get_qudt_quantity_kind_currency_per_flight() -> URIRef:
    """Returns the URI for QUDT quantity kind: Currency Per Flight (http://qudt.org/vocab/quantitykind/CurrencyPerFlight)"""
    return QUDT_QUANTITY_KIND["CURRENCYPERFLIGHT"]


def get_qudt_quantity_kind_current_linkage() -> URIRef:
    """Returns the URI for QUDT quantity kind: Current Linkage (http://qudt.org/vocab/quantitykind/CurrentLinkage)"""
    return QUDT_QUANTITY_KIND["CURRENTLINKAGE"]


def get_qudt_quantity_kind_curvature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Curvature (http://qudt.org/vocab/quantitykind/CurvatureFromRadius)"""
    return QUDT_QUANTITY_KIND["CURVATUREFROMRADIUS"]


def get_qudt_quantity_kind_larmor_angular_frequency() -> URIRef:
    """Returns the URI for QUDT quantity kind: Larmor Angular Frequency (http://qudt.org/vocab/quantitykind/CyclotronAngularFrequency)"""
    return QUDT_QUANTITY_KIND["CYCLOTRONANGULARFREQUENCY"]


def get_qudt_quantity_kind_delta_v() -> URIRef:
    """Returns the URI for QUDT quantity kind: Delta-V (http://qudt.org/vocab/quantitykind/DELTA-V)"""
    return QUDT_QUANTITY_KIND["DELTA-V"]


def get_qudt_quantity_kind_dry_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: Dry Mass (http://qudt.org/vocab/quantitykind/DRY-MASS)"""
    return QUDT_QUANTITY_KIND["DRY-MASS"]


def get_qudt_quantity_kind_data_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: Data Rate (http://qudt.org/vocab/quantitykind/DataRate)"""
    return QUDT_QUANTITY_KIND["DATARATE"]


def get_qudt_quantity_kind_information_flow_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: Information flow rate (http://qudt.org/vocab/quantitykind/InformationFlowRate)"""
    return QUDT_QUANTITY_KIND["INFORMATIONFLOWRATE"]


def get_qudt_quantity_kind_dataset_of_bits() -> URIRef:
    """Returns the URI for QUDT quantity kind: dataset of bits (http://qudt.org/vocab/quantitykind/DatasetOfBits)"""
    return QUDT_QUANTITY_KIND["DATASETOFBITS"]


def get_qudt_quantity_kind_dataset_of_bytes() -> URIRef:
    """Returns the URI for QUDT quantity kind: dataset of bytes (http://qudt.org/vocab/quantitykind/DatasetOfBytes)"""
    return QUDT_QUANTITY_KIND["DATASETOFBYTES"]


def get_qudt_quantity_kind_debye_waller_factor() -> URIRef:
    """Returns the URI for QUDT quantity kind: Debye-Waller Factor (http://qudt.org/vocab/quantitykind/Debye-WallerFactor)"""
    return QUDT_QUANTITY_KIND["DEBYE-WALLERFACTOR"]


def get_qudt_quantity_kind_debye_angular_frequency() -> URIRef:
    """Returns the URI for QUDT quantity kind: Debye Angular Frequency (http://qudt.org/vocab/quantitykind/DebyeAngularFrequency)"""
    return QUDT_QUANTITY_KIND["DEBYEANGULARFREQUENCY"]


def get_qudt_quantity_kind_debye_angular_wavenumber() -> URIRef:
    """Returns the URI for QUDT quantity kind: Debye Angular Wavenumber (http://qudt.org/vocab/quantitykind/DebyeAngularWavenumber)"""
    return QUDT_QUANTITY_KIND["DEBYEANGULARWAVENUMBER"]


def get_qudt_quantity_kind_debye_temperature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Debye Temperature (http://qudt.org/vocab/quantitykind/DebyeTemperature)"""
    return QUDT_QUANTITY_KIND["DEBYETEMPERATURE"]


def get_qudt_quantity_kind_decay_constant() -> URIRef:
    """Returns the URI for QUDT quantity kind: Decay Constant (http://qudt.org/vocab/quantitykind/DecayConstant)"""
    return QUDT_QUANTITY_KIND["DECAYCONSTANT"]


def get_qudt_quantity_kind_inverse_time() -> URIRef:
    """Returns the URI for QUDT quantity kind: Inverse Time (http://qudt.org/vocab/quantitykind/InverseTime)"""
    return QUDT_QUANTITY_KIND["INVERSETIME"]


def get_qudt_quantity_kind_degree_of_dissociation() -> URIRef:
    """Returns the URI for QUDT quantity kind: Degree of Dissociation (http://qudt.org/vocab/quantitykind/DegreeOfDissociation)"""
    return QUDT_QUANTITY_KIND["DEGREEOFDISSOCIATION"]


def get_qudt_quantity_kind_mass_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: mass density (http://qudt.org/vocab/quantitykind/MassDensity)"""
    return QUDT_QUANTITY_KIND["MASSDENSITY"]


def get_qudt_quantity_kind_density_in_combustion_chamber() -> URIRef:
    """Returns the URI for QUDT quantity kind: Density In Combustion Chamber (http://qudt.org/vocab/quantitykind/DensityInCombustionChamber)"""
    return QUDT_QUANTITY_KIND["DENSITYINCOMBUSTIONCHAMBER"]


def get_qudt_quantity_kind_density_of_states() -> URIRef:
    """Returns the URI for QUDT quantity kind: Density of states (http://qudt.org/vocab/quantitykind/DensityOfStates)"""
    return QUDT_QUANTITY_KIND["DENSITYOFSTATES"]


def get_qudt_quantity_kind_vibrational_density_of_states() -> URIRef:
    """Returns the URI for QUDT quantity kind: Vibrational density of states (http://qudt.org/vocab/quantitykind/VibrationalDensityOfStates)"""
    return QUDT_QUANTITY_KIND["VIBRATIONALDENSITYOFSTATES"]


def get_qudt_quantity_kind_density_of_the_exhaust_gases() -> URIRef:
    """Returns the URI for QUDT quantity kind: Density Of The Exhaust Gases (http://qudt.org/vocab/quantitykind/DensityOfTheExhaustGases)"""
    return QUDT_QUANTITY_KIND["DENSITYOFTHEEXHAUSTGASES"]


def get_qudt_quantity_kind_depth() -> URIRef:
    """Returns the URI for QUDT quantity kind: Depth (http://qudt.org/vocab/quantitykind/Depth)"""
    return QUDT_QUANTITY_KIND["DEPTH"]


def get_qudt_quantity_kind_dew_point_temperature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Dew Point Temperature (http://qudt.org/vocab/quantitykind/DewPointTemperature)"""
    return QUDT_QUANTITY_KIND["DEWPOINTTEMPERATURE"]


def get_qudt_quantity_kind_diameter() -> URIRef:
    """Returns the URI for QUDT quantity kind: diameter (http://qudt.org/vocab/quantitykind/Diameter)"""
    return QUDT_QUANTITY_KIND["DIAMETER"]


def get_qudt_quantity_kind_diastolic_blood_pressure() -> URIRef:
    """Returns the URI for QUDT quantity kind: Diastolic Blood Pressure (http://qudt.org/vocab/quantitykind/DiastolicBloodPressure)"""
    return QUDT_QUANTITY_KIND["DIASTOLICBLOODPRESSURE"]


def get_qudt_quantity_kind_systolic_blood_pressure() -> URIRef:
    """Returns the URI for QUDT quantity kind: Systolic Blood Pressure (http://qudt.org/vocab/quantitykind/SystolicBloodPressure)"""
    return QUDT_QUANTITY_KIND["SYSTOLICBLOODPRESSURE"]


def get_qudt_quantity_kind_diffusion_area() -> URIRef:
    """Returns the URI for QUDT quantity kind: Diffusion Area (http://qudt.org/vocab/quantitykind/DiffusionArea)"""
    return QUDT_QUANTITY_KIND["DIFFUSIONAREA"]


def get_qudt_quantity_kind_diffusion_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: diffusion coefficient (http://qudt.org/vocab/quantitykind/DiffusionCoefficient)"""
    return QUDT_QUANTITY_KIND["DIFFUSIONCOEFFICIENT"]


def get_qudt_quantity_kind_diffusion_coefficient_for_fluence_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: Diffusion Coefficient for Fluence Rate (http://qudt.org/vocab/quantitykind/DiffusionCoefficientForFluenceRate)"""
    return QUDT_QUANTITY_KIND["DIFFUSIONCOEFFICIENTFORFLUENCERATE"]


def get_qudt_quantity_kind_diffusion_length() -> URIRef:
    """Returns the URI for QUDT quantity kind: Diffusion Length (http://qudt.org/vocab/quantitykind/DiffusionLength)"""
    return QUDT_QUANTITY_KIND["DIFFUSIONLENGTH"]


def get_qudt_quantity_kind_digit_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: digit rate (http://qudt.org/vocab/quantitykind/DigitRate)"""
    return QUDT_QUANTITY_KIND["DIGITRATE"]


def get_qudt_quantity_kind_displacement() -> URIRef:
    """Returns the URI for QUDT quantity kind: Displacement (http://qudt.org/vocab/quantitykind/Displacement)"""
    return QUDT_QUANTITY_KIND["DISPLACEMENT"]


def get_qudt_quantity_kind_displacement_current() -> URIRef:
    """Returns the URI for QUDT quantity kind: Displacement Current (http://qudt.org/vocab/quantitykind/DisplacementCurrent)"""
    return QUDT_QUANTITY_KIND["DISPLACEMENTCURRENT"]


def get_qudt_quantity_kind_displacement_current_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Displacement Current Density (http://qudt.org/vocab/quantitykind/DisplacementCurrentDensity)"""
    return QUDT_QUANTITY_KIND["DISPLACEMENTCURRENTDENSITY"]


def get_qudt_quantity_kind_displacement_vector_of_ion() -> URIRef:
    """Returns the URI for QUDT quantity kind: Displacement Vector of Ion (http://qudt.org/vocab/quantitykind/DisplacementVectorOfIon)"""
    return QUDT_QUANTITY_KIND["DISPLACEMENTVECTOROFION"]


def get_qudt_quantity_kind_dissipance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Dissipance (http://qudt.org/vocab/quantitykind/Dissipance)"""
    return QUDT_QUANTITY_KIND["DISSIPANCE"]


def get_qudt_quantity_kind_distance() -> URIRef:
    """Returns the URI for QUDT quantity kind: distance (http://qudt.org/vocab/quantitykind/Distance)"""
    return QUDT_QUANTITY_KIND["DISTANCE"]


def get_qudt_quantity_kind_distance_traveled_during_a_burn() -> URIRef:
    """Returns the URI for QUDT quantity kind: Distance Traveled During a Burn (http://qudt.org/vocab/quantitykind/DistanceTraveledDuringBurn)"""
    return QUDT_QUANTITY_KIND["DISTANCETRAVELEDDURINGBURN"]


def get_qudt_quantity_kind_donor_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Donor Density (http://qudt.org/vocab/quantitykind/DonorDensity)"""
    return QUDT_QUANTITY_KIND["DONORDENSITY"]


def get_qudt_quantity_kind_dose_equivalent() -> URIRef:
    """Returns the URI for QUDT quantity kind: Dose Equivalent (http://qudt.org/vocab/quantitykind/DoseEquivalent)"""
    return QUDT_QUANTITY_KIND["DOSEEQUIVALENT"]


def get_qudt_quantity_kind_dose_equivalent_quality_factor() -> URIRef:
    """Returns the URI for QUDT quantity kind: Dose Equivalent Quality Factor (http://qudt.org/vocab/quantitykind/DoseEquivalentQualityFactor)"""
    return QUDT_QUANTITY_KIND["DOSEEQUIVALENTQUALITYFACTOR"]


def get_qudt_quantity_kind_dose_equivalent_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: dose equivalent rate (http://qudt.org/vocab/quantitykind/DoseEquivalentRate)"""
    return QUDT_QUANTITY_KIND["DOSEEQUIVALENTRATE"]


def get_qudt_quantity_kind_dots_per_inch() -> URIRef:
    """Returns the URI for QUDT quantity kind: dots per inch (http://qudt.org/vocab/quantitykind/DotsPerInch)"""
    return QUDT_QUANTITY_KIND["DOTSPERINCH"]


def get_qudt_quantity_kind_drag_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Drag Coefficient (http://qudt.org/vocab/quantitykind/DragCoefficient)"""
    return QUDT_QUANTITY_KIND["DRAGCOEFFICIENT"]


def get_qudt_quantity_kind_drag_force() -> URIRef:
    """Returns the URI for QUDT quantity kind: Drag Force (http://qudt.org/vocab/quantitykind/DragForce)"""
    return QUDT_QUANTITY_KIND["DRAGFORCE"]


def get_qudt_quantity_kind_dry_bulb_temperature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Dry Bulb Temperature (http://qudt.org/vocab/quantitykind/DryBulbTemperature)"""
    return QUDT_QUANTITY_KIND["DRYBULBTEMPERATURE"]


def get_qudt_quantity_kind_dry_volume() -> URIRef:
    """Returns the URI for QUDT quantity kind: Dry Volume (http://qudt.org/vocab/quantitykind/DryVolume)"""
    return QUDT_QUANTITY_KIND["DRYVOLUME"]


def get_qudt_quantity_kind_duty_cycle() -> URIRef:
    """Returns the URI for QUDT quantity kind: Duty Cycle (http://qudt.org/vocab/quantitykind/DutyCycle)"""
    return QUDT_QUANTITY_KIND["DUTYCYCLE"]


def get_qudt_quantity_kind_dynamic_friction() -> URIRef:
    """Returns the URI for QUDT quantity kind: Dynamic Friction (http://qudt.org/vocab/quantitykind/DynamicFriction)"""
    return QUDT_QUANTITY_KIND["DYNAMICFRICTION"]


def get_qudt_quantity_kind_friction() -> URIRef:
    """Returns the URI for QUDT quantity kind: Friction (http://qudt.org/vocab/quantitykind/Friction)"""
    return QUDT_QUANTITY_KIND["FRICTION"]


def get_qudt_quantity_kind_dynamic_friction_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Dynamic Friction Coefficient (http://qudt.org/vocab/quantitykind/DynamicFrictionCoefficient)"""
    return QUDT_QUANTITY_KIND["DYNAMICFRICTIONCOEFFICIENT"]


def get_qudt_quantity_kind_friction_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Friction Coefficient (http://qudt.org/vocab/quantitykind/FrictionCoefficient)"""
    return QUDT_QUANTITY_KIND["FRICTIONCOEFFICIENT"]


def get_qudt_quantity_kind_dynamic_pressure() -> URIRef:
    """Returns the URI for QUDT quantity kind: Dynamic Pressure (http://qudt.org/vocab/quantitykind/DynamicPressure)"""
    return QUDT_QUANTITY_KIND["DYNAMICPRESSURE"]


def get_qudt_quantity_kind_viscosity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Viscosity (http://qudt.org/vocab/quantitykind/Viscosity)"""
    return QUDT_QUANTITY_KIND["VISCOSITY"]


def get_qudt_quantity_kind_earth_closest_approach_vehicle_velocity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Earth Closest Approach Vehicle Velocity (http://qudt.org/vocab/quantitykind/EarthClosestApproachVehicleVelocity)"""
    return QUDT_QUANTITY_KIND["EARTHCLOSESTAPPROACHVEHICLEVELOCITY"]


def get_qudt_quantity_kind_vehicle_velocity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Vehicle Velocity (http://qudt.org/vocab/quantitykind/VehicleVelocity)"""
    return QUDT_QUANTITY_KIND["VEHICLEVELOCITY"]


def get_qudt_quantity_kind_earthquake_magnitude() -> URIRef:
    """Returns the URI for QUDT quantity kind: earthquake magnitude (http://qudt.org/vocab/quantitykind/EarthquakeMagnitude)"""
    return QUDT_QUANTITY_KIND["EARTHQUAKEMAGNITUDE"]


def get_qudt_quantity_kind_eccentricity_of_orbit() -> URIRef:
    """Returns the URI for QUDT quantity kind: Eccentricity Of Orbit (http://qudt.org/vocab/quantitykind/EccentricityOfOrbit)"""
    return QUDT_QUANTITY_KIND["ECCENTRICITYOFORBIT"]


def get_qudt_quantity_kind_effective_exhaustvelocity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Effective Exhaustvelocity (http://qudt.org/vocab/quantitykind/EffectiveExhaustVelocity)"""
    return QUDT_QUANTITY_KIND["EFFECTIVEEXHAUSTVELOCITY"]


def get_qudt_quantity_kind_effective_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: Effective Mass (http://qudt.org/vocab/quantitykind/EffectiveMass)"""
    return QUDT_QUANTITY_KIND["EFFECTIVEMASS"]


def get_qudt_quantity_kind_effective_multiplication_factor() -> URIRef:
    """Returns the URI for QUDT quantity kind: Effective Multiplication Factor (http://qudt.org/vocab/quantitykind/EffectiveMultiplicationFactor)"""
    return QUDT_QUANTITY_KIND["EFFECTIVEMULTIPLICATIONFACTOR"]


def get_qudt_quantity_kind_multiplication_factor() -> URIRef:
    """Returns the URI for QUDT quantity kind: Multiplication Factor (http://qudt.org/vocab/quantitykind/MultiplicationFactor)"""
    return QUDT_QUANTITY_KIND["MULTIPLICATIONFACTOR"]


def get_qudt_quantity_kind_infinite_multiplication_factor() -> URIRef:
    """Returns the URI for QUDT quantity kind: Infinite Multiplication Factor (http://qudt.org/vocab/quantitykind/InfiniteMultiplicationFactor)"""
    return QUDT_QUANTITY_KIND["INFINITEMULTIPLICATIONFACTOR"]


def get_qudt_quantity_kind_efficiency() -> URIRef:
    """Returns the URI for QUDT quantity kind: efficiency (http://qudt.org/vocab/quantitykind/Efficiency)"""
    return QUDT_QUANTITY_KIND["EFFICIENCY"]


def get_qudt_quantity_kind_einstein_coefficients() -> URIRef:
    """Returns the URI for QUDT quantity kind: Einstein coefficients (http://qudt.org/vocab/quantitykind/EinsteinCoefficients)"""
    return QUDT_QUANTITY_KIND["EINSTEINCOEFFICIENTS"]


def get_qudt_quantity_kind_einstein_transition_probability() -> URIRef:
    """Returns the URI for QUDT quantity kind: Einstein Transition Probability (http://qudt.org/vocab/quantitykind/EinsteinTransitionProbability)"""
    return QUDT_QUANTITY_KIND["EINSTEINTRANSITIONPROBABILITY"]


def get_qudt_quantity_kind_electric_charge_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Electric Charge Density (http://qudt.org/vocab/quantitykind/ElectricChargeDensity)"""
    return QUDT_QUANTITY_KIND["ELECTRICCHARGEDENSITY"]


def get_qudt_quantity_kind_electric_charge_surface_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Electric Charge Surface Density (http://qudt.org/vocab/quantitykind/ElectricChargeSurfaceDensity)"""
    return QUDT_QUANTITY_KIND["ELECTRICCHARGESURFACEDENSITY"]


def get_qudt_quantity_kind_electric_charge_linear_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Electric Charge Linear Density (http://qudt.org/vocab/quantitykind/ElectricChargeLinearDensity)"""
    return QUDT_QUANTITY_KIND["ELECTRICCHARGELINEARDENSITY"]


def get_qudt_quantity_kind_electric_current_per_angle() -> URIRef:
    """Returns the URI for QUDT quantity kind: Electric Current per Angle (http://qudt.org/vocab/quantitykind/ElectricCurrentPerAngle)"""
    return QUDT_QUANTITY_KIND["ELECTRICCURRENTPERANGLE"]


def get_qudt_quantity_kind_electric_current_per_length() -> URIRef:
    """Returns the URI for QUDT quantity kind: Electric Current per Length (http://qudt.org/vocab/quantitykind/ElectricCurrentPerLength)"""
    return QUDT_QUANTITY_KIND["ELECTRICCURRENTPERLENGTH"]


def get_qudt_quantity_kind_linear_electric_current_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Linear Electric Current Density (http://qudt.org/vocab/quantitykind/LinearElectricCurrentDensity)"""
    return QUDT_QUANTITY_KIND["LINEARELECTRICCURRENTDENSITY"]


def get_qudt_quantity_kind_cubic_electric_dipole_moment_per_square_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Cubic Electric Dipole Moment per Square Energy (http://qudt.org/vocab/quantitykind/ElectricDipoleMoment_CubicPerEnergy_Squared)"""
    return QUDT_QUANTITY_KIND["ELECTRICDIPOLEMOMENT_CUBICPERENERGY_SQUARED"]


def get_qudt_quantity_kind_quartic_electric_dipole_moment_per_cubic_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Quartic Electric Dipole Moment per Cubic Energy (http://qudt.org/vocab/quantitykind/ElectricDipoleMoment_QuarticPerEnergy_Cubic)"""
    return QUDT_QUANTITY_KIND["ELECTRICDIPOLEMOMENT_QUARTICPERENERGY_CUBIC"]


def get_qudt_quantity_kind_electric_displacement() -> URIRef:
    """Returns the URI for QUDT quantity kind: Electric Displacement (http://qudt.org/vocab/quantitykind/ElectricDisplacement)"""
    return QUDT_QUANTITY_KIND["ELECTRICDISPLACEMENT"]


def get_qudt_quantity_kind_electric_displacement_field() -> URIRef:
    """Returns the URI for QUDT quantity kind: Electric Displacement Field (http://qudt.org/vocab/quantitykind/ElectricDisplacementField)"""
    return QUDT_QUANTITY_KIND["ELECTRICDISPLACEMENTFIELD"]


def get_qudt_quantity_kind_electric_field() -> URIRef:
    """Returns the URI for QUDT quantity kind: Electric Field (http://qudt.org/vocab/quantitykind/ElectricField)"""
    return QUDT_QUANTITY_KIND["ELECTRICFIELD"]


def get_qudt_quantity_kind_electric_polarizability() -> URIRef:
    """Returns the URI for QUDT quantity kind: electric polarizability (http://qudt.org/vocab/quantitykind/ElectricPolarizability)"""
    return QUDT_QUANTITY_KIND["ELECTRICPOLARIZABILITY"]


def get_qudt_quantity_kind_electric_polarization() -> URIRef:
    """Returns the URI for QUDT quantity kind: electric polarization (http://qudt.org/vocab/quantitykind/ElectricPolarization)"""
    return QUDT_QUANTITY_KIND["ELECTRICPOLARIZATION"]


def get_qudt_quantity_kind_electric_potential() -> URIRef:
    """Returns the URI for QUDT quantity kind: electric potential (http://qudt.org/vocab/quantitykind/ElectricPotential)"""
    return QUDT_QUANTITY_KIND["ELECTRICPOTENTIAL"]


def get_qudt_quantity_kind_electric_potential_difference() -> URIRef:
    """Returns the URI for QUDT quantity kind: electric potential difference (http://qudt.org/vocab/quantitykind/ElectricPotentialDifference)"""
    return QUDT_QUANTITY_KIND["ELECTRICPOTENTIALDIFFERENCE"]


def get_qudt_quantity_kind_electric_propulsion_propellant_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: Electric Propulsion Propellant Mass (http://qudt.org/vocab/quantitykind/ElectricPropulsionPropellantMass)"""
    return QUDT_QUANTITY_KIND["ELECTRICPROPULSIONPROPELLANTMASS"]


def get_qudt_quantity_kind_propellant_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: Propellant Mass (http://qudt.org/vocab/quantitykind/PropellantMass)"""
    return QUDT_QUANTITY_KIND["PROPELLANTMASS"]


def get_qudt_quantity_kind_electric_susceptibility() -> URIRef:
    """Returns the URI for QUDT quantity kind: electric susceptibility (http://qudt.org/vocab/quantitykind/ElectricSusceptibility)"""
    return QUDT_QUANTITY_KIND["ELECTRICSUSCEPTIBILITY"]


def get_qudt_quantity_kind_electrical_conductance() -> URIRef:
    """Returns the URI for QUDT quantity kind: electrical conductance (http://qudt.org/vocab/quantitykind/ElectricalConductance)"""
    return QUDT_QUANTITY_KIND["ELECTRICALCONDUCTANCE"]


def get_qudt_quantity_kind_electrical_power_to_mass_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Electrical Power To Mass Ratio (http://qudt.org/vocab/quantitykind/ElectricalPowerToMassRatio)"""
    return QUDT_QUANTITY_KIND["ELECTRICALPOWERTOMASSRATIO"]


def get_qudt_quantity_kind_specific_power() -> URIRef:
    """Returns the URI for QUDT quantity kind: Specific Power (http://qudt.org/vocab/quantitykind/SpecificPower)"""
    return QUDT_QUANTITY_KIND["SPECIFICPOWER"]


def get_qudt_quantity_kind_electrolytic_conductivity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Electrolytic Conductivity (http://qudt.org/vocab/quantitykind/ElectrolyticConductivity)"""
    return QUDT_QUANTITY_KIND["ELECTROLYTICCONDUCTIVITY"]


def get_qudt_quantity_kind_electromagnetic_energy_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Electromagnetic Energy Density (http://qudt.org/vocab/quantitykind/ElectromagneticEnergyDensity)"""
    return QUDT_QUANTITY_KIND["ELECTROMAGNETICENERGYDENSITY"]


def get_qudt_quantity_kind_volumic_electromagnetic_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Volumic Electromagnetic Energy (http://qudt.org/vocab/quantitykind/VolumicElectromagneticEnergy)"""
    return QUDT_QUANTITY_KIND["VOLUMICELECTROMAGNETICENERGY"]


def get_qudt_quantity_kind_permeability() -> URIRef:
    """Returns the URI for QUDT quantity kind: Permeability (http://qudt.org/vocab/quantitykind/Permeability)"""
    return QUDT_QUANTITY_KIND["PERMEABILITY"]


def get_qudt_quantity_kind_electromagnetic_permeability_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Electromagnetic Permeability Ratio (http://qudt.org/vocab/quantitykind/ElectromagneticPermeabilityRatio)"""
    return QUDT_QUANTITY_KIND["ELECTROMAGNETICPERMEABILITYRATIO"]


def get_qudt_quantity_kind_electromagnetic_wave_phase_speed() -> URIRef:
    """Returns the URI for QUDT quantity kind: Electromagnetic Wave Phase Speed (http://qudt.org/vocab/quantitykind/ElectromagneticWavePhaseSpeed)"""
    return QUDT_QUANTITY_KIND["ELECTROMAGNETICWAVEPHASESPEED"]


def get_qudt_quantity_kind_electromotive_force() -> URIRef:
    """Returns the URI for QUDT quantity kind: electromotive force (http://qudt.org/vocab/quantitykind/ElectromotiveForce)"""
    return QUDT_QUANTITY_KIND["ELECTROMOTIVEFORCE"]


def get_qudt_quantity_kind_electron_affinity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Electron Affinity (http://qudt.org/vocab/quantitykind/ElectronAffinity)"""
    return QUDT_QUANTITY_KIND["ELECTRONAFFINITY"]


def get_qudt_quantity_kind_electron_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Electron Density (http://qudt.org/vocab/quantitykind/ElectronDensity)"""
    return QUDT_QUANTITY_KIND["ELECTRONDENSITY"]


def get_qudt_quantity_kind_electron_mean_free_path() -> URIRef:
    """Returns the URI for QUDT quantity kind: Electron Mean Free Path (http://qudt.org/vocab/quantitykind/ElectronMeanFreePath)"""
    return QUDT_QUANTITY_KIND["ELECTRONMEANFREEPATH"]


def get_qudt_quantity_kind_electron_mobility() -> URIRef:
    """Returns the URI for QUDT quantity kind: electron mobility (http://qudt.org/vocab/quantitykind/ElectronMobility)"""
    return QUDT_QUANTITY_KIND["ELECTRONMOBILITY"]


def get_qudt_quantity_kind_mobility() -> URIRef:
    """Returns the URI for QUDT quantity kind: mobility (http://qudt.org/vocab/quantitykind/Mobility)"""
    return QUDT_QUANTITY_KIND["MOBILITY"]


def get_qudt_quantity_kind_electron_radius() -> URIRef:
    """Returns the URI for QUDT quantity kind: Electron Radius (http://qudt.org/vocab/quantitykind/ElectronRadius)"""
    return QUDT_QUANTITY_KIND["ELECTRONRADIUS"]


def get_qudt_quantity_kind_elevation_relative_to_nap() -> URIRef:
    """Returns the URI for QUDT quantity kind: Elevation relative to NAP (http://qudt.org/vocab/quantitykind/ElevationRelativeToNAP)"""
    return QUDT_QUANTITY_KIND["ELEVATIONRELATIVETONAP"]


def get_qudt_quantity_kind_elliptical_orbit_apogee_velocity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Elliptical Orbit Apogee Velocity (http://qudt.org/vocab/quantitykind/EllipticalOrbitApogeeVelocity)"""
    return QUDT_QUANTITY_KIND["ELLIPTICALORBITAPOGEEVELOCITY"]


def get_qudt_quantity_kind_elliptical_orbit_perigee_velocity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Elliptical Orbit Perigee Velocity (http://qudt.org/vocab/quantitykind/EllipticalOrbitPerigeeVelocity)"""
    return QUDT_QUANTITY_KIND["ELLIPTICALORBITPERIGEEVELOCITY"]


def get_qudt_quantity_kind_emissivity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Emissivity (http://qudt.org/vocab/quantitykind/Emissivity)"""
    return QUDT_QUANTITY_KIND["EMISSIVITY"]


def get_qudt_quantity_kind_enthalpy() -> URIRef:
    """Returns the URI for QUDT quantity kind: enthalpy (http://qudt.org/vocab/quantitykind/Enthalpy)"""
    return QUDT_QUANTITY_KIND["ENTHALPY"]


def get_qudt_quantity_kind_entropy() -> URIRef:
    """Returns the URI for QUDT quantity kind: entropy (http://qudt.org/vocab/quantitykind/Entropy)"""
    return QUDT_QUANTITY_KIND["ENTROPY"]


def get_qudt_quantity_kind_gibbs_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Gibbs energy (http://qudt.org/vocab/quantitykind/GibbsEnergy)"""
    return QUDT_QUANTITY_KIND["GIBBSENERGY"]


def get_qudt_quantity_kind_helmholtz_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Helmholtz energy (http://qudt.org/vocab/quantitykind/HelmholtzEnergy)"""
    return QUDT_QUANTITY_KIND["HELMHOLTZENERGY"]


def get_qudt_quantity_kind_internal_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Internal Energy (http://qudt.org/vocab/quantitykind/InternalEnergy)"""
    return QUDT_QUANTITY_KIND["INTERNALENERGY"]


def get_qudt_quantity_kind_work() -> URIRef:
    """Returns the URI for QUDT quantity kind: work (http://qudt.org/vocab/quantitykind/Work)"""
    return QUDT_QUANTITY_KIND["WORK"]


def get_qudt_quantity_kind_energy_content() -> URIRef:
    """Returns the URI for QUDT quantity kind: energy content (http://qudt.org/vocab/quantitykind/EnergyContent)"""
    return QUDT_QUANTITY_KIND["ENERGYCONTENT"]


def get_qudt_quantity_kind_energy_density_of_states() -> URIRef:
    """Returns the URI for QUDT quantity kind: Energy Density of States (http://qudt.org/vocab/quantitykind/EnergyDensityOfStates)"""
    return QUDT_QUANTITY_KIND["ENERGYDENSITYOFSTATES"]


def get_qudt_quantity_kind_energy_expenditure() -> URIRef:
    """Returns the URI for QUDT quantity kind: Energy Expenditure (http://qudt.org/vocab/quantitykind/EnergyExpenditure)"""
    return QUDT_QUANTITY_KIND["ENERGYEXPENDITURE"]


def get_qudt_quantity_kind_energy_fluence() -> URIRef:
    """Returns the URI for QUDT quantity kind: Energy Fluence (http://qudt.org/vocab/quantitykind/EnergyFluence)"""
    return QUDT_QUANTITY_KIND["ENERGYFLUENCE"]


def get_qudt_quantity_kind_energy_fluence_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: Energy Fluence Rate (http://qudt.org/vocab/quantitykind/EnergyFluenceRate)"""
    return QUDT_QUANTITY_KIND["ENERGYFLUENCERATE"]


def get_qudt_quantity_kind_energy_imparted() -> URIRef:
    """Returns the URI for QUDT quantity kind: Energy Imparted (http://qudt.org/vocab/quantitykind/EnergyImparted)"""
    return QUDT_QUANTITY_KIND["ENERGYIMPARTED"]


def get_qudt_quantity_kind_internal_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: internal energy (http://qudt.org/vocab/quantitykind/EnergyInternal)"""
    return QUDT_QUANTITY_KIND["ENERGYINTERNAL"]


def get_qudt_quantity_kind_thermodynamic_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Thermodynamic Energy (http://qudt.org/vocab/quantitykind/ThermodynamicEnergy)"""
    return QUDT_QUANTITY_KIND["THERMODYNAMICENERGY"]


def get_qudt_quantity_kind_kinetic_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: kinetic energy (http://qudt.org/vocab/quantitykind/EnergyKinetic)"""
    return QUDT_QUANTITY_KIND["ENERGYKINETIC"]


def get_qudt_quantity_kind_energy_level() -> URIRef:
    """Returns the URI for QUDT quantity kind: Energy Level (http://qudt.org/vocab/quantitykind/EnergyLevel)"""
    return QUDT_QUANTITY_KIND["ENERGYLEVEL"]


def get_qudt_quantity_kind_energy_per_square_magnetic_flux_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Energy Per Square Magnetic Flux Density (http://qudt.org/vocab/quantitykind/EnergyPerMagneticFluxDensity_Squared)"""
    return QUDT_QUANTITY_KIND["ENERGYPERMAGNETICFLUXDENSITY_SQUARED"]


def get_qudt_quantity_kind_energy_and_work_per_mass_amount_of_substance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Energy and work per mass amount of substance (http://qudt.org/vocab/quantitykind/EnergyPerMassAmountOfSubstance)"""
    return QUDT_QUANTITY_KIND["ENERGYPERMASSAMOUNTOFSUBSTANCE"]


def get_qudt_quantity_kind_square_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Square Energy (http://qudt.org/vocab/quantitykind/Energy_Squared)"""
    return QUDT_QUANTITY_KIND["ENERGY_SQUARED"]


def get_qudt_quantity_kind_equilibrium_constant() -> URIRef:
    """Returns the URI for QUDT quantity kind: Equilibrium Constant (http://qudt.org/vocab/quantitykind/EquilibriumConstant)"""
    return QUDT_QUANTITY_KIND["EQUILIBRIUMCONSTANT"]


def get_qudt_quantity_kind_equilibrium_constant_on_concentration_basis() -> URIRef:
    """Returns the URI for QUDT quantity kind: Equilibrium Constant on Concentration Basis (http://qudt.org/vocab/quantitykind/EquilibriumConstantOnConcentrationBasis)"""
    return QUDT_QUANTITY_KIND["EQUILIBRIUMCONSTANTONCONCENTRATIONBASIS"]


def get_qudt_quantity_kind_equilibrium_constant_on_pressure_basis() -> URIRef:
    """Returns the URI for QUDT quantity kind: Equilibrium Constant on Pressure Basis (http://qudt.org/vocab/quantitykind/EquilibriumConstantOnPressureBasis)"""
    return QUDT_QUANTITY_KIND["EQUILIBRIUMCONSTANTONPRESSUREBASIS"]


def get_qudt_quantity_kind_equilibrium_position_vector_of_ion() -> URIRef:
    """Returns the URI for QUDT quantity kind: Equilibrium Position Vector of Ion (http://qudt.org/vocab/quantitykind/EquilibriumPositionVectorOfIon)"""
    return QUDT_QUANTITY_KIND["EQUILIBRIUMPOSITIONVECTOROFION"]


def get_qudt_quantity_kind_equivalent_absorption_area() -> URIRef:
    """Returns the URI for QUDT quantity kind: Equivalent absorption area (http://qudt.org/vocab/quantitykind/EquivalentAbsorptionArea)"""
    return QUDT_QUANTITY_KIND["EQUIVALENTABSORPTIONAREA"]


def get_qudt_quantity_kind_equivalent_concentration() -> URIRef:
    """Returns the URI for QUDT quantity kind: Equivalent Concentration (http://qudt.org/vocab/quantitykind/EquivalentConcentration)"""
    return QUDT_QUANTITY_KIND["EQUIVALENTCONCENTRATION"]


def get_qudt_quantity_kind_equivalent_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Equivalent Density (http://qudt.org/vocab/quantitykind/EquivalentDensity)"""
    return QUDT_QUANTITY_KIND["EQUIVALENTDENSITY"]


def get_qudt_quantity_kind_mass_equivalent() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass Equivalent (http://qudt.org/vocab/quantitykind/Equivalent_Mass)"""
    return QUDT_QUANTITY_KIND["EQUIVALENT_MASS"]


def get_qudt_quantity_kind_molar_equivalent() -> URIRef:
    """Returns the URI for QUDT quantity kind: Molar Equivalent (http://qudt.org/vocab/quantitykind/Equivalent_Molar)"""
    return QUDT_QUANTITY_KIND["EQUIVALENT_MOLAR"]


def get_qudt_quantity_kind_molar_equivalent() -> URIRef:
    """Returns the URI for QUDT quantity kind: Molar Equivalent (http://qudt.org/vocab/quantitykind/MolarEquivalent)"""
    return QUDT_QUANTITY_KIND["MOLAREQUIVALENT"]


def get_qudt_quantity_kind_evaporative_heat_transfer() -> URIRef:
    """Returns the URI for QUDT quantity kind: Evaporative Heat Transfer (http://qudt.org/vocab/quantitykind/EvaporativeHeatTransfer)"""
    return QUDT_QUANTITY_KIND["EVAPORATIVEHEATTRANSFER"]


def get_qudt_quantity_kind_combined_non_evaporative_heat_transfer_coefficient() -> (
    URIRef
):
    """Returns the URI for QUDT quantity kind: Combined Non Evaporative Heat Transfer Coefficient (http://qudt.org/vocab/quantitykind/EvaporativeHeatTransferCoefficient)"""
    return QUDT_QUANTITY_KIND["EVAPORATIVEHEATTRANSFERCOEFFICIENT"]


def get_qudt_quantity_kind_exchange_integral() -> URIRef:
    """Returns the URI for QUDT quantity kind: Exchange Integral (http://qudt.org/vocab/quantitykind/ExchangeIntegral)"""
    return QUDT_QUANTITY_KIND["EXCHANGEINTEGRAL"]


def get_qudt_quantity_kind_exhaust_gas_mean_molecular_weight() -> URIRef:
    """Returns the URI for QUDT quantity kind: Exhaust Gas Mean Molecular Weight (http://qudt.org/vocab/quantitykind/ExhaustGasMeanMolecularWeight)"""
    return QUDT_QUANTITY_KIND["EXHAUSTGASMEANMOLECULARWEIGHT"]


def get_qudt_quantity_kind_exhaust_gases_specific_heat() -> URIRef:
    """Returns the URI for QUDT quantity kind: Exhaust Gases Specific Heat (http://qudt.org/vocab/quantitykind/ExhaustGasesSpecificHeat)"""
    return QUDT_QUANTITY_KIND["EXHAUSTGASESSPECIFICHEAT"]


def get_qudt_quantity_kind_exhaust_stream_power() -> URIRef:
    """Returns the URI for QUDT quantity kind: Exhaust Stream Power (http://qudt.org/vocab/quantitykind/ExhaustStreamPower)"""
    return QUDT_QUANTITY_KIND["EXHAUSTSTREAMPOWER"]


def get_qudt_quantity_kind_exit_plane_cross_sectional_area() -> URIRef:
    """Returns the URI for QUDT quantity kind: Exit Plane Cross-sectional Area (http://qudt.org/vocab/quantitykind/ExitPlaneCrossSectionalArea)"""
    return QUDT_QUANTITY_KIND["EXITPLANECROSSSECTIONALAREA"]


def get_qudt_quantity_kind_exit_plane_pressure() -> URIRef:
    """Returns the URI for QUDT quantity kind: Exit Plane Pressure (http://qudt.org/vocab/quantitykind/ExitPlanePressure)"""
    return QUDT_QUANTITY_KIND["EXITPLANEPRESSURE"]


def get_qudt_quantity_kind_exit_plane_temperature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Exit Plane Temperature (http://qudt.org/vocab/quantitykind/ExitPlaneTemperature)"""
    return QUDT_QUANTITY_KIND["EXITPLANETEMPERATURE"]


def get_qudt_quantity_kind_exposure() -> URIRef:
    """Returns the URI for QUDT quantity kind: Exposure (http://qudt.org/vocab/quantitykind/Exposure)"""
    return QUDT_QUANTITY_KIND["EXPOSURE"]


def get_qudt_quantity_kind_extent_of_reaction() -> URIRef:
    """Returns the URI for QUDT quantity kind: Extent of Reaction (http://qudt.org/vocab/quantitykind/ExtentOfReaction)"""
    return QUDT_QUANTITY_KIND["EXTENTOFREACTION"]


def get_qudt_quantity_kind_flight_performance_reserve_propellant_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: Flight Performance Reserve Propellant Mass (http://qudt.org/vocab/quantitykind/FLIGHT-PERFORMANCE-RESERVE-PROPELLANT-MASS)"""
    return QUDT_QUANTITY_KIND["FLIGHT-PERFORMANCE-RESERVE-PROPELLANT-MASS"]


def get_qudt_quantity_kind_fuel_bias() -> URIRef:
    """Returns the URI for QUDT quantity kind: Fuel Bias (http://qudt.org/vocab/quantitykind/FUEL-BIAS)"""
    return QUDT_QUANTITY_KIND["FUEL-BIAS"]


def get_qudt_quantity_kind_fahrenheit_temperature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Fahrenheit temperature (http://qudt.org/vocab/quantitykind/FahrenheitTemperature)"""
    return QUDT_QUANTITY_KIND["FAHRENHEITTEMPERATURE"]


def get_qudt_quantity_kind_failure_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: failure rate (http://qudt.org/vocab/quantitykind/FailureRate)"""
    return QUDT_QUANTITY_KIND["FAILURERATE"]


def get_qudt_quantity_kind_incidence() -> URIRef:
    """Returns the URI for QUDT quantity kind: Incidence (http://qudt.org/vocab/quantitykind/Incidence)"""
    return QUDT_QUANTITY_KIND["INCIDENCE"]


def get_qudt_quantity_kind_fast_fission_factor() -> URIRef:
    """Returns the URI for QUDT quantity kind: Fast Fission Factor (http://qudt.org/vocab/quantitykind/FastFissionFactor)"""
    return QUDT_QUANTITY_KIND["FASTFISSIONFACTOR"]


def get_qudt_quantity_kind_fermi_angular_wavenumber() -> URIRef:
    """Returns the URI for QUDT quantity kind: Fermi Angular Wavenumber (http://qudt.org/vocab/quantitykind/FermiAngularWavenumber)"""
    return QUDT_QUANTITY_KIND["FERMIANGULARWAVENUMBER"]


def get_qudt_quantity_kind_fermi_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Fermi Energy (http://qudt.org/vocab/quantitykind/FermiEnergy)"""
    return QUDT_QUANTITY_KIND["FERMIENERGY"]


def get_qudt_quantity_kind_fermi_temperature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Fermi Temperature (http://qudt.org/vocab/quantitykind/FermiTemperature)"""
    return QUDT_QUANTITY_KIND["FERMITEMPERATURE"]


def get_qudt_quantity_kind_final_or_current_vehicle_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: Final Or Current Vehicle Mass (http://qudt.org/vocab/quantitykind/FinalOrCurrentVehicleMass)"""
    return QUDT_QUANTITY_KIND["FINALORCURRENTVEHICLEMASS"]


def get_qudt_quantity_kind_first_moment_of_area() -> URIRef:
    """Returns the URI for QUDT quantity kind: First Moment of Area (http://qudt.org/vocab/quantitykind/FirstMomentOfArea)"""
    return QUDT_QUANTITY_KIND["FIRSTMOMENTOFAREA"]


def get_qudt_quantity_kind_first_stage_mass_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: First Stage Mass Ratio (http://qudt.org/vocab/quantitykind/FirstStageMassRatio)"""
    return QUDT_QUANTITY_KIND["FIRSTSTAGEMASSRATIO"]


def get_qudt_quantity_kind_mass_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass Ratio (http://qudt.org/vocab/quantitykind/MassRatio)"""
    return QUDT_QUANTITY_KIND["MASSRATIO"]


def get_qudt_quantity_kind_fish_biotransformation_half_life() -> URIRef:
    """Returns the URI for QUDT quantity kind: Fish Biotransformation Half Life (http://qudt.org/vocab/quantitykind/FishBiotransformationHalfLife)"""
    return QUDT_QUANTITY_KIND["FISHBIOTRANSFORMATIONHALFLIFE"]


def get_qudt_quantity_kind_fission_core_radius_to_height_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Fission Core Radius To Height Ratio (http://qudt.org/vocab/quantitykind/FissionCoreRadiusToHeightRatio)"""
    return QUDT_QUANTITY_KIND["FISSIONCORERADIUSTOHEIGHTRATIO"]


def get_qudt_quantity_kind_fission_fuel_utilization_factor() -> URIRef:
    """Returns the URI for QUDT quantity kind: Fission Fuel Utilization Factor (http://qudt.org/vocab/quantitykind/FissionFuelUtilizationFactor)"""
    return QUDT_QUANTITY_KIND["FISSIONFUELUTILIZATIONFACTOR"]


def get_qudt_quantity_kind_fission_multiplication_factor() -> URIRef:
    """Returns the URI for QUDT quantity kind: Fission Multiplication Factor (http://qudt.org/vocab/quantitykind/FissionMultiplicationFactor)"""
    return QUDT_QUANTITY_KIND["FISSIONMULTIPLICATIONFACTOR"]


def get_qudt_quantity_kind_flash_point_temperature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Flash Point Temperature (http://qudt.org/vocab/quantitykind/FlashPoint)"""
    return QUDT_QUANTITY_KIND["FLASHPOINT"]


def get_qudt_quantity_kind_flight_path_angle() -> URIRef:
    """Returns the URI for QUDT quantity kind: Flight Path Angle (http://qudt.org/vocab/quantitykind/FlightPathAngle)"""
    return QUDT_QUANTITY_KIND["FLIGHTPATHANGLE"]


def get_qudt_quantity_kind_floating_point_calculation_capability() -> URIRef:
    """Returns the URI for QUDT quantity kind: floating point calculation capability (http://qudt.org/vocab/quantitykind/FloatingPointCalculationCapability)"""
    return QUDT_QUANTITY_KIND["FLOATINGPOINTCALCULATIONCAPABILITY"]


def get_qudt_quantity_kind_fluidity() -> URIRef:
    """Returns the URI for QUDT quantity kind: fluidity (http://qudt.org/vocab/quantitykind/Fluidity)"""
    return QUDT_QUANTITY_KIND["FLUIDITY"]


def get_qudt_quantity_kind_flux() -> URIRef:
    """Returns the URI for QUDT quantity kind: Flux (http://qudt.org/vocab/quantitykind/Flux)"""
    return QUDT_QUANTITY_KIND["FLUX"]


def get_qudt_quantity_kind_force_constant() -> URIRef:
    """Returns the URI for QUDT quantity kind: force constant (http://qudt.org/vocab/quantitykind/ForceConstant)"""
    return QUDT_QUANTITY_KIND["FORCECONSTANT"]


def get_qudt_quantity_kind_force_magnitude() -> URIRef:
    """Returns the URI for QUDT quantity kind: Force Magnitude (http://qudt.org/vocab/quantitykind/ForceMagnitude)"""
    return QUDT_QUANTITY_KIND["FORCEMAGNITUDE"]


def get_qudt_quantity_kind_force_per_angle() -> URIRef:
    """Returns the URI for QUDT quantity kind: Force per Angle (http://qudt.org/vocab/quantitykind/ForcePerAngle)"""
    return QUDT_QUANTITY_KIND["FORCEPERANGLE"]


def get_qudt_quantity_kind_force_per_electric_charge() -> URIRef:
    """Returns the URI for QUDT quantity kind: Force per Electric Charge (http://qudt.org/vocab/quantitykind/ForcePerElectricCharge)"""
    return QUDT_QUANTITY_KIND["FORCEPERELECTRICCHARGE"]


def get_qudt_quantity_kind_fugacity() -> URIRef:
    """Returns the URI for QUDT quantity kind: fugacity (http://qudt.org/vocab/quantitykind/Fugacity)"""
    return QUDT_QUANTITY_KIND["FUGACITY"]


def get_qudt_quantity_kind_fundamental_lattice_vector() -> URIRef:
    """Returns the URI for QUDT quantity kind: Fundamental Lattice vector (http://qudt.org/vocab/quantitykind/FundamentalLatticeVector)"""
    return QUDT_QUANTITY_KIND["FUNDAMENTALLATTICEVECTOR"]


def get_qudt_quantity_kind_lattice_vector() -> URIRef:
    """Returns the URI for QUDT quantity kind: Lattice Vector (http://qudt.org/vocab/quantitykind/LatticeVector)"""
    return QUDT_QUANTITY_KIND["LATTICEVECTOR"]


def get_qudt_quantity_kind_fundamental_reciprocal_lattice_vector() -> URIRef:
    """Returns the URI for QUDT quantity kind: Fundamental Reciprocal Lattice Vector (http://qudt.org/vocab/quantitykind/FundamentalReciprocalLatticeVector)"""
    return QUDT_QUANTITY_KIND["FUNDAMENTALRECIPROCALLATTICEVECTOR"]


def get_qudt_quantity_kind_g_factor_of_nucleus() -> URIRef:
    """Returns the URI for QUDT quantity kind: g-Factor of Nucleus (http://qudt.org/vocab/quantitykind/GFactorOfNucleus)"""
    return QUDT_QUANTITY_KIND["GFACTOROFNUCLEUS"]


def get_qudt_quantity_kind_gross_lift_off_weight() -> URIRef:
    """Returns the URI for QUDT quantity kind: Gross Lift-Off Weight (http://qudt.org/vocab/quantitykind/GROSS-LIFT-OFF-WEIGHT)"""
    return QUDT_QUANTITY_KIND["GROSS-LIFT-OFF-WEIGHT"]


def get_qudt_quantity_kind_gain() -> URIRef:
    """Returns the URI for QUDT quantity kind: Gain (http://qudt.org/vocab/quantitykind/Gain)"""
    return QUDT_QUANTITY_KIND["GAIN"]


def get_qudt_quantity_kind_gap_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Gap Energy (http://qudt.org/vocab/quantitykind/GapEnergy)"""
    return QUDT_QUANTITY_KIND["GAPENERGY"]


def get_qudt_quantity_kind_gas_leak_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: gas leak rate (http://qudt.org/vocab/quantitykind/GasLeakRate)"""
    return QUDT_QUANTITY_KIND["GASLEAKRATE"]


def get_qudt_quantity_kind_gauge_pressure() -> URIRef:
    """Returns the URI for QUDT quantity kind: Gauge Pressure (http://qudt.org/vocab/quantitykind/GaugePressure)"""
    return QUDT_QUANTITY_KIND["GAUGEPRESSURE"]


def get_qudt_quantity_kind_gene_family_abundance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Gene Family Abundance (http://qudt.org/vocab/quantitykind/GeneFamilyAbundance)"""
    return QUDT_QUANTITY_KIND["GENEFAMILYABUNDANCE"]


def get_qudt_quantity_kind_generalized_coordinate() -> URIRef:
    """Returns the URI for QUDT quantity kind: Generalized Coordinate (http://qudt.org/vocab/quantitykind/GeneralizedCoordinate)"""
    return QUDT_QUANTITY_KIND["GENERALIZEDCOORDINATE"]


def get_qudt_quantity_kind_generalized_force() -> URIRef:
    """Returns the URI for QUDT quantity kind: Generalized Force (http://qudt.org/vocab/quantitykind/GeneralizedForce)"""
    return QUDT_QUANTITY_KIND["GENERALIZEDFORCE"]


def get_qudt_quantity_kind_generalized_force() -> URIRef:
    """Returns the URI for QUDT quantity kind: Generalized Force (http://qudt.org/vocab/quantitykind/GeneralizedMomentum)"""
    return QUDT_QUANTITY_KIND["GENERALIZEDMOMENTUM"]


def get_qudt_quantity_kind_generalized_velocity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Generalized Velocity (http://qudt.org/vocab/quantitykind/GeneralizedVelocity)"""
    return QUDT_QUANTITY_KIND["GENERALIZEDVELOCITY"]


def get_qudt_quantity_kind_gradient() -> URIRef:
    """Returns the URI for QUDT quantity kind: gradient (http://qudt.org/vocab/quantitykind/Gradient)"""
    return QUDT_QUANTITY_KIND["GRADIENT"]


def get_qudt_quantity_kind_grand_canonical_partition_function() -> URIRef:
    """Returns the URI for QUDT quantity kind: Grand Canonical Partition Function (http://qudt.org/vocab/quantitykind/GrandCanonicalPartitionFunction)"""
    return QUDT_QUANTITY_KIND["GRANDCANONICALPARTITIONFUNCTION"]


def get_qudt_quantity_kind_api_gravity() -> URIRef:
    """Returns the URI for QUDT quantity kind: API Gravity (http://qudt.org/vocab/quantitykind/Gravity_API)"""
    return QUDT_QUANTITY_KIND["GRAVITY_API"]


def get_qudt_quantity_kind_group_speed_of_sound() -> URIRef:
    """Returns the URI for QUDT quantity kind: Group Speed of Sound (http://qudt.org/vocab/quantitykind/GroupSpeedOfSound)"""
    return QUDT_QUANTITY_KIND["GROUPSPEEDOFSOUND"]


def get_qudt_quantity_kind_speed_of_sound() -> URIRef:
    """Returns the URI for QUDT quantity kind: speed of sound (http://qudt.org/vocab/quantitykind/SpeedOfSound)"""
    return QUDT_QUANTITY_KIND["SPEEDOFSOUND"]


def get_qudt_quantity_kind_growing_degree_days_cereals() -> URIRef:
    """Returns the URI for QUDT quantity kind: Growing Degree Days (Cereals) (http://qudt.org/vocab/quantitykind/GrowingDegreeDay)"""
    return QUDT_QUANTITY_KIND["GROWINGDEGREEDAY"]


def get_qudt_quantity_kind_growing_degree_days_cereals() -> URIRef:
    """Returns the URI for QUDT quantity kind: Growing Degree Days (Cereals) (http://qudt.org/vocab/quantitykind/GrowingDegreeDay_Cereal)"""
    return QUDT_QUANTITY_KIND["GROWINGDEGREEDAY_CEREAL"]


def get_qudt_quantity_kind_gruneisen_parameter() -> URIRef:
    """Returns the URI for QUDT quantity kind: Gruneisen Parameter (http://qudt.org/vocab/quantitykind/GruneisenParameter)"""
    return QUDT_QUANTITY_KIND["GRUNEISENPARAMETER"]


def get_qudt_quantity_kind_gustatory_threshold() -> URIRef:
    """Returns the URI for QUDT quantity kind: Gustatory Threshold (http://qudt.org/vocab/quantitykind/GustatoryThreshold)"""
    return QUDT_QUANTITY_KIND["GUSTATORYTHRESHOLD"]


def get_qudt_quantity_kind_half_life() -> URIRef:
    """Returns the URI for QUDT quantity kind: half-life (http://qudt.org/vocab/quantitykind/Half-Life)"""
    return QUDT_QUANTITY_KIND["HALF-LIFE"]


def get_qudt_quantity_kind_half_value_thickness() -> URIRef:
    """Returns the URI for QUDT quantity kind: Half-Value Thickness (http://qudt.org/vocab/quantitykind/Half-ValueThickness)"""
    return QUDT_QUANTITY_KIND["HALF-VALUETHICKNESS"]


def get_qudt_quantity_kind_hall_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Hall Coefficient (http://qudt.org/vocab/quantitykind/HallCoefficient)"""
    return QUDT_QUANTITY_KIND["HALLCOEFFICIENT"]


def get_qudt_quantity_kind_hamilton_function() -> URIRef:
    """Returns the URI for QUDT quantity kind: Hamilton Function (http://qudt.org/vocab/quantitykind/HamiltonFunction)"""
    return QUDT_QUANTITY_KIND["HAMILTONFUNCTION"]


def get_qudt_quantity_kind_heart_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: Heart Rate (http://qudt.org/vocab/quantitykind/HeartRate)"""
    return QUDT_QUANTITY_KIND["HEARTRATE"]


def get_qudt_quantity_kind_heat() -> URIRef:
    """Returns the URI for QUDT quantity kind: heat (http://qudt.org/vocab/quantitykind/Heat)"""
    return QUDT_QUANTITY_KIND["HEAT"]


def get_qudt_quantity_kind_thermal_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Thermal Energy (http://qudt.org/vocab/quantitykind/ThermalEnergy)"""
    return QUDT_QUANTITY_KIND["THERMALENERGY"]


def get_qudt_quantity_kind_heat_capacity_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Heat Capacity Ratio (http://qudt.org/vocab/quantitykind/HeatCapacityRatio)"""
    return QUDT_QUANTITY_KIND["HEATCAPACITYRATIO"]


def get_qudt_quantity_kind_heat_flow_rate_per_unit_area() -> URIRef:
    """Returns the URI for QUDT quantity kind: Heat Flow Rate per Unit Area (http://qudt.org/vocab/quantitykind/HeatFlowRatePerArea)"""
    return QUDT_QUANTITY_KIND["HEATFLOWRATEPERAREA"]


def get_qudt_quantity_kind_heat_flux_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Heat Flux Density (http://qudt.org/vocab/quantitykind/HeatFluxDensity)"""
    return QUDT_QUANTITY_KIND["HEATFLUXDENSITY"]


def get_qudt_quantity_kind_calorific_value() -> URIRef:
    """Returns the URI for QUDT quantity kind: Calorific Value (http://qudt.org/vocab/quantitykind/HeatingValue)"""
    return QUDT_QUANTITY_KIND["HEATINGVALUE"]


def get_qudt_quantity_kind_height() -> URIRef:
    """Returns the URI for QUDT quantity kind: height (http://qudt.org/vocab/quantitykind/Height)"""
    return QUDT_QUANTITY_KIND["HEIGHT"]


def get_qudt_quantity_kind_henry_s_law_volatility_constant() -> URIRef:
    """Returns the URI for QUDT quantity kind: Henry's Law Volatility Constant (http://qudt.org/vocab/quantitykind/HenrysLawVolatilityConstant)"""
    return QUDT_QUANTITY_KIND["HENRYSLAWVOLATILITYCONSTANT"]


def get_qudt_quantity_kind_hole_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Hole Density (http://qudt.org/vocab/quantitykind/HoleDensity)"""
    return QUDT_QUANTITY_KIND["HOLEDENSITY"]


def get_qudt_quantity_kind_horizontal_velocity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Horizontal Velocity (http://qudt.org/vocab/quantitykind/HorizontalVelocity)"""
    return QUDT_QUANTITY_KIND["HORIZONTALVELOCITY"]


def get_qudt_quantity_kind_hydraulic_permeability() -> URIRef:
    """Returns the URI for QUDT quantity kind: Hydraulic Permeability (http://qudt.org/vocab/quantitykind/HydraulicPermeability)"""
    return QUDT_QUANTITY_KIND["HYDRAULICPERMEABILITY"]


def get_qudt_quantity_kind_hyperfine_structure_quantum_number() -> URIRef:
    """Returns the URI for QUDT quantity kind: Hyperfine Structure Quantum Number (http://qudt.org/vocab/quantitykind/HyperfineStructureQuantumNumber)"""
    return QUDT_QUANTITY_KIND["HYPERFINESTRUCTUREQUANTUMNUMBER"]


def get_qudt_quantity_kind_quantum_number() -> URIRef:
    """Returns the URI for QUDT quantity kind: Quantum Number (http://qudt.org/vocab/quantitykind/QuantumNumber)"""
    return QUDT_QUANTITY_KIND["QUANTUMNUMBER"]


def get_qudt_quantity_kind_inert_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: Inert Mass (http://qudt.org/vocab/quantitykind/INERT-MASS)"""
    return QUDT_QUANTITY_KIND["INERT-MASS"]


def get_qudt_quantity_kind_ignition_interval_time() -> URIRef:
    """Returns the URI for QUDT quantity kind: Ignition interval time (http://qudt.org/vocab/quantitykind/IgnitionIntervalTime)"""
    return QUDT_QUANTITY_KIND["IGNITIONINTERVALTIME"]


def get_qudt_quantity_kind_illuminance() -> URIRef:
    """Returns the URI for QUDT quantity kind: illuminance (http://qudt.org/vocab/quantitykind/Illuminance)"""
    return QUDT_QUANTITY_KIND["ILLUMINANCE"]


def get_qudt_quantity_kind_luminous_flux_per_area() -> URIRef:
    """Returns the URI for QUDT quantity kind: Luminous Flux per Area (http://qudt.org/vocab/quantitykind/LuminousFluxPerArea)"""
    return QUDT_QUANTITY_KIND["LUMINOUSFLUXPERAREA"]


def get_qudt_quantity_kind_impulse() -> URIRef:
    """Returns the URI for QUDT quantity kind: impulse (http://qudt.org/vocab/quantitykind/Impulse)"""
    return QUDT_QUANTITY_KIND["IMPULSE"]


def get_qudt_quantity_kind_incidence_proportion() -> URIRef:
    """Returns the URI for QUDT quantity kind: Incidence Proportion (http://qudt.org/vocab/quantitykind/IncidenceProportion)"""
    return QUDT_QUANTITY_KIND["INCIDENCEPROPORTION"]


def get_qudt_quantity_kind_incidence_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: Incidence Rate (http://qudt.org/vocab/quantitykind/IncidenceRate)"""
    return QUDT_QUANTITY_KIND["INCIDENCERATE"]


def get_qudt_quantity_kind_mutual_inductance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mutual Inductance (http://qudt.org/vocab/quantitykind/MutualInductance)"""
    return QUDT_QUANTITY_KIND["MUTUALINDUCTANCE"]


def get_qudt_quantity_kind_inductance_based_time_constant() -> URIRef:
    """Returns the URI for QUDT quantity kind: Inductance based time constant (http://qudt.org/vocab/quantitykind/InductanceBasedTimeConstant)"""
    return QUDT_QUANTITY_KIND["INDUCTANCEBASEDTIMECONSTANT"]


def get_qudt_quantity_kind_information_content() -> URIRef:
    """Returns the URI for QUDT quantity kind: information content (http://qudt.org/vocab/quantitykind/InformationContent)"""
    return QUDT_QUANTITY_KIND["INFORMATIONCONTENT"]


def get_qudt_quantity_kind_information_entropy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Information Entropy (http://qudt.org/vocab/quantitykind/InformationEntropy)"""
    return QUDT_QUANTITY_KIND["INFORMATIONENTROPY"]


def get_qudt_quantity_kind_initial_expansion_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Initial Expansion Ratio (http://qudt.org/vocab/quantitykind/InitialExpansionRatio)"""
    return QUDT_QUANTITY_KIND["INITIALEXPANSIONRATIO"]


def get_qudt_quantity_kind_initial_nozzle_throat_diameter() -> URIRef:
    """Returns the URI for QUDT quantity kind: Initial Nozzle Throat Diameter (http://qudt.org/vocab/quantitykind/InitialNozzleThroatDiameter)"""
    return QUDT_QUANTITY_KIND["INITIALNOZZLETHROATDIAMETER"]


def get_qudt_quantity_kind_nozzle_throat_diameter() -> URIRef:
    """Returns the URI for QUDT quantity kind: Nozzle Throat Diameter (http://qudt.org/vocab/quantitykind/NozzleThroatDiameter)"""
    return QUDT_QUANTITY_KIND["NOZZLETHROATDIAMETER"]


def get_qudt_quantity_kind_initial_vehicle_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: Initial Vehicle Mass (http://qudt.org/vocab/quantitykind/InitialVehicleMass)"""
    return QUDT_QUANTITY_KIND["INITIALVEHICLEMASS"]


def get_qudt_quantity_kind_initial_velocity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Initial Velocity (http://qudt.org/vocab/quantitykind/InitialVelocity)"""
    return QUDT_QUANTITY_KIND["INITIALVELOCITY"]


def get_qudt_quantity_kind_internalconversionfactor() -> URIRef:
    """Returns the URI for QUDT quantity kind: InternalConversionFactor (http://qudt.org/vocab/quantitykind/InternalConversionFactor)"""
    return QUDT_QUANTITY_KIND["INTERNALCONVERSIONFACTOR"]


def get_qudt_quantity_kind_intinsic_carrier_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Intinsic Carrier Density (http://qudt.org/vocab/quantitykind/IntinsicCarrierDensity)"""
    return QUDT_QUANTITY_KIND["INTINSICCARRIERDENSITY"]


def get_qudt_quantity_kind_inverse_square_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Inverse Square Energy (http://qudt.org/vocab/quantitykind/InverseEnergy_Squared)"""
    return QUDT_QUANTITY_KIND["INVERSEENERGY_SQUARED"]


def get_qudt_quantity_kind_reciprocal_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: reciprocal mass (http://qudt.org/vocab/quantitykind/InverseMass)"""
    return QUDT_QUANTITY_KIND["INVERSEMASS"]


def get_qudt_quantity_kind_inverse_square_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: Inverse Square Mass (http://qudt.org/vocab/quantitykind/InverseMass_Squared)"""
    return QUDT_QUANTITY_KIND["INVERSEMASS_SQUARED"]


def get_qudt_quantity_kind_inverse_square_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: Inverse Square Mass (http://qudt.org/vocab/quantitykind/InverseSquareMass)"""
    return QUDT_QUANTITY_KIND["INVERSESQUAREMASS"]


def get_qudt_quantity_kind_isothermal_compressibility() -> URIRef:
    """Returns the URI for QUDT quantity kind: isothermal compressibility (http://qudt.org/vocab/quantitykind/IsothermalCompressibility)"""
    return QUDT_QUANTITY_KIND["ISOTHERMALCOMPRESSIBILITY"]


def get_qudt_quantity_kind_inverse_temperature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Inverse Temperature (http://qudt.org/vocab/quantitykind/InverseTemperature)"""
    return QUDT_QUANTITY_KIND["INVERSETEMPERATURE"]


def get_qudt_quantity_kind_inverse_square_time() -> URIRef:
    """Returns the URI for QUDT quantity kind: Inverse Square Time (http://qudt.org/vocab/quantitykind/InverseTime_Squared)"""
    return QUDT_QUANTITY_KIND["INVERSETIME_SQUARED"]


def get_qudt_quantity_kind_ion_concentration() -> URIRef:
    """Returns the URI for QUDT quantity kind: Ion Concentration (http://qudt.org/vocab/quantitykind/IonConcentration)"""
    return QUDT_QUANTITY_KIND["IONCONCENTRATION"]


def get_qudt_quantity_kind_ion_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Ion Density (http://qudt.org/vocab/quantitykind/IonDensity)"""
    return QUDT_QUANTITY_KIND["IONDENSITY"]


def get_qudt_quantity_kind_ion_current() -> URIRef:
    """Returns the URI for QUDT quantity kind: Ion Current (http://qudt.org/vocab/quantitykind/IonCurrent)"""
    return QUDT_QUANTITY_KIND["IONCURRENT"]


def get_qudt_quantity_kind_ion_transport_number() -> URIRef:
    """Returns the URI for QUDT quantity kind: Ion Transport Number (http://qudt.org/vocab/quantitykind/IonTransportNumber)"""
    return QUDT_QUANTITY_KIND["IONTRANSPORTNUMBER"]


def get_qudt_quantity_kind_ionic_charge() -> URIRef:
    """Returns the URI for QUDT quantity kind: Ionic Charge (http://qudt.org/vocab/quantitykind/IonicCharge)"""
    return QUDT_QUANTITY_KIND["IONICCHARGE"]


def get_qudt_quantity_kind_ionic_strength() -> URIRef:
    """Returns the URI for QUDT quantity kind: Ionic Strength (http://qudt.org/vocab/quantitykind/IonicStrength)"""
    return QUDT_QUANTITY_KIND["IONICSTRENGTH"]


def get_qudt_quantity_kind_irradiance() -> URIRef:
    """Returns the URI for QUDT quantity kind: irradiance (http://qudt.org/vocab/quantitykind/Irradiance)"""
    return QUDT_QUANTITY_KIND["IRRADIANCE"]


def get_qudt_quantity_kind_isentropic_compressibility() -> URIRef:
    """Returns the URI for QUDT quantity kind: Isentropic Compressibility (http://qudt.org/vocab/quantitykind/IsentropicCompressibility)"""
    return QUDT_QUANTITY_KIND["ISENTROPICCOMPRESSIBILITY"]


def get_qudt_quantity_kind_isentropic_exponent() -> URIRef:
    """Returns the URI for QUDT quantity kind: isentropic exponent (http://qudt.org/vocab/quantitykind/IsentropicExponent)"""
    return QUDT_QUANTITY_KIND["ISENTROPICEXPONENT"]


def get_qudt_quantity_kind_isothermal_moisture_capacity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Isothermal Moisture Capacity (http://qudt.org/vocab/quantitykind/IsothermalMoistureCapacity)"""
    return QUDT_QUANTITY_KIND["ISOTHERMALMOISTURECAPACITY"]


def get_qudt_quantity_kind_kerma() -> URIRef:
    """Returns the URI for QUDT quantity kind: Kerma (http://qudt.org/vocab/quantitykind/Kerma)"""
    return QUDT_QUANTITY_KIND["KERMA"]


def get_qudt_quantity_kind_kerma_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: Kerma Rate (http://qudt.org/vocab/quantitykind/KermaRate)"""
    return QUDT_QUANTITY_KIND["KERMARATE"]


def get_qudt_quantity_kind_kinematic_viscosity() -> URIRef:
    """Returns the URI for QUDT quantity kind: kinematic viscosity (http://qudt.org/vocab/quantitykind/KinematicViscosity)"""
    return QUDT_QUANTITY_KIND["KINEMATICVISCOSITY"]


def get_qudt_quantity_kind_molecular_viscosity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Molecular Viscosity (http://qudt.org/vocab/quantitykind/MolecularViscosity)"""
    return QUDT_QUANTITY_KIND["MOLECULARVISCOSITY"]


def get_qudt_quantity_kind_kinetic_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Kinetic Energy (http://qudt.org/vocab/quantitykind/KineticEnergy)"""
    return QUDT_QUANTITY_KIND["KINETICENERGY"]


def get_qudt_quantity_kind_lagrange_function() -> URIRef:
    """Returns the URI for QUDT quantity kind: Lagrange Function (http://qudt.org/vocab/quantitykind/LagrangeFunction)"""
    return QUDT_QUANTITY_KIND["LAGRANGEFUNCTION"]


def get_qudt_quantity_kind_landau_ginzburg_number() -> URIRef:
    """Returns the URI for QUDT quantity kind: Landau-Ginzburg Number (http://qudt.org/vocab/quantitykind/Landau-GinzburgNumber)"""
    return QUDT_QUANTITY_KIND["LANDAU-GINZBURGNUMBER"]


def get_qudt_quantity_kind_lande_g_factor() -> URIRef:
    """Returns the URI for QUDT quantity kind: Lande g-Factor (http://qudt.org/vocab/quantitykind/LandeGFactor)"""
    return QUDT_QUANTITY_KIND["LANDEGFACTOR"]


def get_qudt_quantity_kind_larmor_angular_frequency() -> URIRef:
    """Returns the URI for QUDT quantity kind: Larmor Angular Frequency (http://qudt.org/vocab/quantitykind/LarmorAngularFrequency)"""
    return QUDT_QUANTITY_KIND["LARMORANGULARFREQUENCY"]


def get_qudt_quantity_kind_lattice_plane_spacing() -> URIRef:
    """Returns the URI for QUDT quantity kind: Lattice Plane Spacing (http://qudt.org/vocab/quantitykind/LatticePlaneSpacing)"""
    return QUDT_QUANTITY_KIND["LATTICEPLANESPACING"]


def get_qudt_quantity_kind_leakage_factor() -> URIRef:
    """Returns the URI for QUDT quantity kind: Leakage Factor (http://qudt.org/vocab/quantitykind/LeakageFactor)"""
    return QUDT_QUANTITY_KIND["LEAKAGEFACTOR"]


def get_qudt_quantity_kind_length_force() -> URIRef:
    """Returns the URI for QUDT quantity kind: Length Force (http://qudt.org/vocab/quantitykind/LengthByForce)"""
    return QUDT_QUANTITY_KIND["LENGTHBYFORCE"]


def get_qudt_quantity_kind_length_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Length Ratio (http://qudt.org/vocab/quantitykind/LengthRatio)"""
    return QUDT_QUANTITY_KIND["LENGTHRATIO"]


def get_qudt_quantity_kind_length_temperature_time() -> URIRef:
    """Returns the URI for QUDT quantity kind: Length Temperature Time (http://qudt.org/vocab/quantitykind/LengthTemperatureTime)"""
    return QUDT_QUANTITY_KIND["LENGTHTEMPERATURETIME"]


def get_qudt_quantity_kind_lethargy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Lethargy (http://qudt.org/vocab/quantitykind/Lethargy)"""
    return QUDT_QUANTITY_KIND["LETHARGY"]


def get_qudt_quantity_kind_level_width() -> URIRef:
    """Returns the URI for QUDT quantity kind: Level Width (http://qudt.org/vocab/quantitykind/LevelWidth)"""
    return QUDT_QUANTITY_KIND["LEVELWIDTH"]


def get_qudt_quantity_kind_lift_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Lift Coefficient (http://qudt.org/vocab/quantitykind/LiftCoefficient)"""
    return QUDT_QUANTITY_KIND["LIFTCOEFFICIENT"]


def get_qudt_quantity_kind_lift_force() -> URIRef:
    """Returns the URI for QUDT quantity kind: Lift Force (http://qudt.org/vocab/quantitykind/LiftForce)"""
    return QUDT_QUANTITY_KIND["LIFTFORCE"]


def get_qudt_quantity_kind_linear_absorption_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Linear Absorption Coefficient (http://qudt.org/vocab/quantitykind/LinearAbsorptionCoefficient)"""
    return QUDT_QUANTITY_KIND["LINEARABSORPTIONCOEFFICIENT"]


def get_qudt_quantity_kind_linear_attenuation_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Linear Attenuation Coefficient (http://qudt.org/vocab/quantitykind/LinearAttenuationCoefficient)"""
    return QUDT_QUANTITY_KIND["LINEARATTENUATIONCOEFFICIENT"]


def get_qudt_quantity_kind_lineic_bit_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: lineic bit density (http://qudt.org/vocab/quantitykind/LinearBitDensity)"""
    return QUDT_QUANTITY_KIND["LINEARBITDENSITY"]


def get_qudt_quantity_kind_linear_compressibility() -> URIRef:
    """Returns the URI for QUDT quantity kind: Linear Compressibility (http://qudt.org/vocab/quantitykind/LinearCompressibility)"""
    return QUDT_QUANTITY_KIND["LINEARCOMPRESSIBILITY"]


def get_qudt_quantity_kind_linear_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Linear Density (http://qudt.org/vocab/quantitykind/LinearDensity)"""
    return QUDT_QUANTITY_KIND["LINEARDENSITY"]


def get_qudt_quantity_kind_lineic_electric_charge() -> URIRef:
    """Returns the URI for QUDT quantity kind: lineic electric charge (http://qudt.org/vocab/quantitykind/LinearElectricCharge)"""
    return QUDT_QUANTITY_KIND["LINEARELECTRICCHARGE"]


def get_qudt_quantity_kind_linear_electric_current() -> URIRef:
    """Returns the URI for QUDT quantity kind: Linear Electric Current (http://qudt.org/vocab/quantitykind/LinearElectricCurrent)"""
    return QUDT_QUANTITY_KIND["LINEARELECTRICCURRENT"]


def get_qudt_quantity_kind_linear_energy_transfer() -> URIRef:
    """Returns the URI for QUDT quantity kind: Linear Energy Transfer (http://qudt.org/vocab/quantitykind/LinearEnergyTransfer)"""
    return QUDT_QUANTITY_KIND["LINEARENERGYTRANSFER"]


def get_qudt_quantity_kind_linear_expansion_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: linear expansion coefficient (http://qudt.org/vocab/quantitykind/LinearExpansionCoefficient)"""
    return QUDT_QUANTITY_KIND["LINEAREXPANSIONCOEFFICIENT"]


def get_qudt_quantity_kind_linear_force() -> URIRef:
    """Returns the URI for QUDT quantity kind: Linear Force (http://qudt.org/vocab/quantitykind/LinearForce)"""
    return QUDT_QUANTITY_KIND["LINEARFORCE"]


def get_qudt_quantity_kind_linear_ionization() -> URIRef:
    """Returns the URI for QUDT quantity kind: Linear Ionization (http://qudt.org/vocab/quantitykind/LinearIonization)"""
    return QUDT_QUANTITY_KIND["LINEARIONIZATION"]


def get_qudt_quantity_kind_lineic_logarithmic_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: lineic logarithmic ratio (http://qudt.org/vocab/quantitykind/LinearLogarithmicRatio)"""
    return QUDT_QUANTITY_KIND["LINEARLOGARITHMICRATIO"]


def get_qudt_quantity_kind_lineic_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: lineic mass (http://qudt.org/vocab/quantitykind/LinearMass)"""
    return QUDT_QUANTITY_KIND["LINEARMASS"]


def get_qudt_quantity_kind_momentum() -> URIRef:
    """Returns the URI for QUDT quantity kind: momentum (http://qudt.org/vocab/quantitykind/Momentum)"""
    return QUDT_QUANTITY_KIND["MOMENTUM"]


def get_qudt_quantity_kind_lineic_power() -> URIRef:
    """Returns the URI for QUDT quantity kind: lineic power (http://qudt.org/vocab/quantitykind/LinearPower)"""
    return QUDT_QUANTITY_KIND["LINEARPOWER"]


def get_qudt_quantity_kind_lineic_resistance() -> URIRef:
    """Returns the URI for QUDT quantity kind: lineic resistance (http://qudt.org/vocab/quantitykind/LinearResistance)"""
    return QUDT_QUANTITY_KIND["LINEARRESISTANCE"]


def get_qudt_quantity_kind_linear_force() -> URIRef:
    """Returns the URI for QUDT quantity kind: Linear Force (http://qudt.org/vocab/quantitykind/LinearStiffness)"""
    return QUDT_QUANTITY_KIND["LINEARSTIFFNESS"]


def get_qudt_quantity_kind_linear_strain() -> URIRef:
    """Returns the URI for QUDT quantity kind: Linear Strain (http://qudt.org/vocab/quantitykind/LinearStrain)"""
    return QUDT_QUANTITY_KIND["LINEARSTRAIN"]


def get_qudt_quantity_kind_strain() -> URIRef:
    """Returns the URI for QUDT quantity kind: Strain (http://qudt.org/vocab/quantitykind/Strain)"""
    return QUDT_QUANTITY_KIND["STRAIN"]


def get_qudt_quantity_kind_lineic_torque() -> URIRef:
    """Returns the URI for QUDT quantity kind: lineic torque (http://qudt.org/vocab/quantitykind/LinearTorque)"""
    return QUDT_QUANTITY_KIND["LINEARTORQUE"]


def get_qudt_quantity_kind_linked_flux() -> URIRef:
    """Returns the URI for QUDT quantity kind: Linked Flux (http://qudt.org/vocab/quantitykind/LinkedFlux)"""
    return QUDT_QUANTITY_KIND["LINKEDFLUX"]


def get_qudt_quantity_kind_liquid_volume() -> URIRef:
    """Returns the URI for QUDT quantity kind: Liquid Volume (http://qudt.org/vocab/quantitykind/LiquidVolume)"""
    return QUDT_QUANTITY_KIND["LIQUIDVOLUME"]


def get_qudt_quantity_kind_logarithmic_frequency_interval_to_base_10() -> URIRef:
    """Returns the URI for QUDT quantity kind: logarithmic frequency interval to base 10 (http://qudt.org/vocab/quantitykind/Log10FrequencyInterval)"""
    return QUDT_QUANTITY_KIND["LOG10FREQUENCYINTERVAL"]


def get_qudt_quantity_kind_logarithmic_ratio_to_base_10() -> URIRef:
    """Returns the URI for QUDT quantity kind: logarithmic ratio to base 10 (http://qudt.org/vocab/quantitykind/Log10Ratio)"""
    return QUDT_QUANTITY_KIND["LOG10RATIO"]


def get_qudt_quantity_kind_logarithmic_ratio_to_base_e() -> URIRef:
    """Returns the URI for QUDT quantity kind: logarithmic ratio to base e (http://qudt.org/vocab/quantitykind/LogERatio)"""
    return QUDT_QUANTITY_KIND["LOGERATIO"]


def get_qudt_quantity_kind_octanol_air_partition_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Octanol Air Partition Coefficient (http://qudt.org/vocab/quantitykind/LogOctanolAirPartitionCoefficient)"""
    return QUDT_QUANTITY_KIND["LOGOCTANOLAIRPARTITIONCOEFFICIENT"]


def get_qudt_quantity_kind_logarithm_of_octanol_water_partition_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Logarithm of Octanol Water Partition Coefficient (http://qudt.org/vocab/quantitykind/LogOctanolWaterPartitionCoefficient)"""
    return QUDT_QUANTITY_KIND["LOGOCTANOLWATERPARTITIONCOEFFICIENT"]


def get_qudt_quantity_kind_logarithmic_frequency_interval() -> URIRef:
    """Returns the URI for QUDT quantity kind: logarithmic frequency interval (http://qudt.org/vocab/quantitykind/LogarithmicFrequencyInterval)"""
    return QUDT_QUANTITY_KIND["LOGARITHMICFREQUENCYINTERVAL"]


def get_qudt_quantity_kind_london_penetration_depth() -> URIRef:
    """Returns the URI for QUDT quantity kind: London Penetration Depth (http://qudt.org/vocab/quantitykind/LondonPenetrationDepth)"""
    return QUDT_QUANTITY_KIND["LONDONPENETRATIONDEPTH"]


def get_qudt_quantity_kind_long_range_order_parameter() -> URIRef:
    """Returns the URI for QUDT quantity kind: Long-Range Order Parameter (http://qudt.org/vocab/quantitykind/Long-RangeOrderParameter)"""
    return QUDT_QUANTITY_KIND["LONG-RANGEORDERPARAMETER"]


def get_qudt_quantity_kind_lorenz_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Lorenz Coefficient (http://qudt.org/vocab/quantitykind/LorenzCoefficient)"""
    return QUDT_QUANTITY_KIND["LORENZCOEFFICIENT"]


def get_qudt_quantity_kind_loss_angle() -> URIRef:
    """Returns the URI for QUDT quantity kind: Loss Angle (http://qudt.org/vocab/quantitykind/LossAngle)"""
    return QUDT_QUANTITY_KIND["LOSSANGLE"]


def get_qudt_quantity_kind_loss_factor() -> URIRef:
    """Returns the URI for QUDT quantity kind: Loss Factor (http://qudt.org/vocab/quantitykind/LossFactor)"""
    return QUDT_QUANTITY_KIND["LOSSFACTOR"]


def get_qudt_quantity_kind_quality_factor() -> URIRef:
    """Returns the URI for QUDT quantity kind: Quality Factor (http://qudt.org/vocab/quantitykind/QualityFactor)"""
    return QUDT_QUANTITY_KIND["QUALITYFACTOR"]


def get_qudt_quantity_kind_reactance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Reactance (http://qudt.org/vocab/quantitykind/Reactance)"""
    return QUDT_QUANTITY_KIND["REACTANCE"]


def get_qudt_quantity_kind_loudness() -> URIRef:
    """Returns the URI for QUDT quantity kind: loudness (http://qudt.org/vocab/quantitykind/Loudness)"""
    return QUDT_QUANTITY_KIND["LOUDNESS"]


def get_qudt_quantity_kind_loudness_level() -> URIRef:
    """Returns the URI for QUDT quantity kind: loudness level (http://qudt.org/vocab/quantitykind/LoudnessLevel)"""
    return QUDT_QUANTITY_KIND["LOUDNESSLEVEL"]


def get_qudt_quantity_kind_lower_critical_magnetic_flux_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Lower Critical Magnetic Flux Density (http://qudt.org/vocab/quantitykind/LowerCriticalMagneticFluxDensity)"""
    return QUDT_QUANTITY_KIND["LOWERCRITICALMAGNETICFLUXDENSITY"]


def get_qudt_quantity_kind_upper_critical_magnetic_flux_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Upper Critical Magnetic Flux Density (http://qudt.org/vocab/quantitykind/UpperCriticalMagneticFluxDensity)"""
    return QUDT_QUANTITY_KIND["UPPERCRITICALMAGNETICFLUXDENSITY"]


def get_qudt_quantity_kind_luminous_efficacy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Luminous Efficacy (http://qudt.org/vocab/quantitykind/LuminousEfficacy)"""
    return QUDT_QUANTITY_KIND["LUMINOUSEFFICACY"]


def get_qudt_quantity_kind_luminous_emmitance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Luminous Emmitance (http://qudt.org/vocab/quantitykind/LuminousEmittance)"""
    return QUDT_QUANTITY_KIND["LUMINOUSEMITTANCE"]


def get_qudt_quantity_kind_luminous_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Luminous Energy (http://qudt.org/vocab/quantitykind/LuminousEnergy)"""
    return QUDT_QUANTITY_KIND["LUMINOUSENERGY"]


def get_qudt_quantity_kind_radiant_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: radiant energy (http://qudt.org/vocab/quantitykind/RadiantEnergy)"""
    return QUDT_QUANTITY_KIND["RADIANTENERGY"]


def get_qudt_quantity_kind_luminous_exposure() -> URIRef:
    """Returns the URI for QUDT quantity kind: Luminous Exposure (http://qudt.org/vocab/quantitykind/LuminousExposure)"""
    return QUDT_QUANTITY_KIND["LUMINOUSEXPOSURE"]


def get_qudt_quantity_kind_luminous_flux() -> URIRef:
    """Returns the URI for QUDT quantity kind: luminous flux (http://qudt.org/vocab/quantitykind/LuminousFlux)"""
    return QUDT_QUANTITY_KIND["LUMINOUSFLUX"]


def get_qudt_quantity_kind_luminous_flux_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Luminous Flux Ratio (http://qudt.org/vocab/quantitykind/LuminousFluxRatio)"""
    return QUDT_QUANTITY_KIND["LUMINOUSFLUXRATIO"]


def get_qudt_quantity_kind_ion_concentration() -> URIRef:
    """Returns the URI for QUDT quantity kind: Ion Concentration (http://qudt.org/vocab/quantitykind/LuminousIntensityDistribution)"""
    return QUDT_QUANTITY_KIND["LUMINOUSINTENSITYDISTRIBUTION"]


def get_qudt_quantity_kind_mass_delivered() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass Delivered (http://qudt.org/vocab/quantitykind/MASS-DELIVERED)"""
    return QUDT_QUANTITY_KIND["MASS-DELIVERED"]


def get_qudt_quantity_kind_mass_growth_allowance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass Growth Allowance (http://qudt.org/vocab/quantitykind/MASS-GROWTH-ALLOWANCE)"""
    return QUDT_QUANTITY_KIND["MASS-GROWTH-ALLOWANCE"]


def get_qudt_quantity_kind_mass_margin() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass Margin (http://qudt.org/vocab/quantitykind/MASS-MARGIN)"""
    return QUDT_QUANTITY_KIND["MASS-MARGIN"]


def get_qudt_quantity_kind_mass_property_uncertainty() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass Property Uncertainty (http://qudt.org/vocab/quantitykind/MASS-PROPERTY-UNCERTAINTY)"""
    return QUDT_QUANTITY_KIND["MASS-PROPERTY-UNCERTAINTY"]


def get_qudt_quantity_kind_moment_of_inertia_in_the_y_axis() -> URIRef:
    """Returns the URI for QUDT quantity kind: Moment of Inertia in the Y axis (http://qudt.org/vocab/quantitykind/MOMENT-OF-INERTIA_Y)"""
    return QUDT_QUANTITY_KIND["MOMENT-OF-INERTIA_Y"]


def get_qudt_quantity_kind_moment_of_inertia_in_the_y_axis() -> URIRef:
    """Returns the URI for QUDT quantity kind: Moment of Inertia in the Y axis (http://qudt.org/vocab/quantitykind/MomentOfInertia_Y)"""
    return QUDT_QUANTITY_KIND["MOMENTOFINERTIA_Y"]


def get_qudt_quantity_kind_moment_of_inertia_in_the_z_axis() -> URIRef:
    """Returns the URI for QUDT quantity kind: Moment of Inertia in the Z axis (http://qudt.org/vocab/quantitykind/MOMENT-OF-INERTIA_Z)"""
    return QUDT_QUANTITY_KIND["MOMENT-OF-INERTIA_Z"]


def get_qudt_quantity_kind_moment_of_inertia_in_the_z_axis() -> URIRef:
    """Returns the URI for QUDT quantity kind: Moment of Inertia in the Z axis (http://qudt.org/vocab/quantitykind/MomentOfInertia_Z)"""
    return QUDT_QUANTITY_KIND["MOMENTOFINERTIA_Z"]


def get_qudt_quantity_kind_mach_number() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mach number (http://qudt.org/vocab/quantitykind/MachNumber)"""
    return QUDT_QUANTITY_KIND["MACHNUMBER"]


def get_qudt_quantity_kind_macroscopic_cross_section() -> URIRef:
    """Returns the URI for QUDT quantity kind: Macroscopic Cross-section (http://qudt.org/vocab/quantitykind/MacroscopicCrossSection)"""
    return QUDT_QUANTITY_KIND["MACROSCOPICCROSSSECTION"]


def get_qudt_quantity_kind_macroscopic_total_cross_section() -> URIRef:
    """Returns the URI for QUDT quantity kind: Macroscopic Total Cross-section (http://qudt.org/vocab/quantitykind/MacroscopicTotalCrossSection)"""
    return QUDT_QUANTITY_KIND["MACROSCOPICTOTALCROSSSECTION"]


def get_qudt_quantity_kind_madelung_constant() -> URIRef:
    """Returns the URI for QUDT quantity kind: Madelung constant (http://qudt.org/vocab/quantitykind/MadelungConstant)"""
    return QUDT_QUANTITY_KIND["MADELUNGCONSTANT"]


def get_qudt_quantity_kind_magnetic_area_moment() -> URIRef:
    """Returns the URI for QUDT quantity kind: Magnetic Area Moment (http://qudt.org/vocab/quantitykind/MagneticAreaMoment)"""
    return QUDT_QUANTITY_KIND["MAGNETICAREAMOMENT"]


def get_qudt_quantity_kind_magnetic_moment() -> URIRef:
    """Returns the URI for QUDT quantity kind: magnetic moment (http://qudt.org/vocab/quantitykind/MagneticMoment)"""
    return QUDT_QUANTITY_KIND["MAGNETICMOMENT"]


def get_qudt_quantity_kind_magnetic_field() -> URIRef:
    """Returns the URI for QUDT quantity kind: Magnetic Field (http://qudt.org/vocab/quantitykind/MagneticField)"""
    return QUDT_QUANTITY_KIND["MAGNETICFIELD"]


def get_qudt_quantity_kind_magnetic_field_strength() -> URIRef:
    """Returns the URI for QUDT quantity kind: magnetic field strength (http://qudt.org/vocab/quantitykind/MagneticFieldStrength_H)"""
    return QUDT_QUANTITY_KIND["MAGNETICFIELDSTRENGTH_H"]


def get_qudt_quantity_kind_magnetic_polarization() -> URIRef:
    """Returns the URI for QUDT quantity kind: Magnetic Polarization (http://qudt.org/vocab/quantitykind/MagneticPolarization)"""
    return QUDT_QUANTITY_KIND["MAGNETICPOLARIZATION"]


def get_qudt_quantity_kind_magnetization() -> URIRef:
    """Returns the URI for QUDT quantity kind: magnetization (http://qudt.org/vocab/quantitykind/Magnetization)"""
    return QUDT_QUANTITY_KIND["MAGNETIZATION"]


def get_qudt_quantity_kind_magnetic_quantum_number() -> URIRef:
    """Returns the URI for QUDT quantity kind: Magnetic Quantum Number (http://qudt.org/vocab/quantitykind/MagneticQuantumNumber)"""
    return QUDT_QUANTITY_KIND["MAGNETICQUANTUMNUMBER"]


def get_qudt_quantity_kind_orbital_angular_momentum_quantum_number() -> URIRef:
    """Returns the URI for QUDT quantity kind: Orbital Angular Momentum Quantum Number (http://qudt.org/vocab/quantitykind/OrbitalAngularMomentumQuantumNumber)"""
    return QUDT_QUANTITY_KIND["ORBITALANGULARMOMENTUMQUANTUMNUMBER"]


def get_qudt_quantity_kind_principal_quantum_number() -> URIRef:
    """Returns the URI for QUDT quantity kind: Principal Quantum Number (http://qudt.org/vocab/quantitykind/PrincipalQuantumNumber)"""
    return QUDT_QUANTITY_KIND["PRINCIPALQUANTUMNUMBER"]


def get_qudt_quantity_kind_spin_quantum_number() -> URIRef:
    """Returns the URI for QUDT quantity kind: Spin Quantum Number (http://qudt.org/vocab/quantitykind/SpinQuantumNumber)"""
    return QUDT_QUANTITY_KIND["SPINQUANTUMNUMBER"]


def get_qudt_quantity_kind_magnetic_susceptability() -> URIRef:
    """Returns the URI for QUDT quantity kind: Magnetic Susceptability (http://qudt.org/vocab/quantitykind/MagneticSusceptability)"""
    return QUDT_QUANTITY_KIND["MAGNETICSUSCEPTABILITY"]


def get_qudt_quantity_kind_magnetic_tension() -> URIRef:
    """Returns the URI for QUDT quantity kind: Magnetic Tension (http://qudt.org/vocab/quantitykind/MagneticTension)"""
    return QUDT_QUANTITY_KIND["MAGNETICTENSION"]


def get_qudt_quantity_kind_magnetic_vector_potential() -> URIRef:
    """Returns the URI for QUDT quantity kind: magnetic vector potential (http://qudt.org/vocab/quantitykind/MagneticVectorPotential)"""
    return QUDT_QUANTITY_KIND["MAGNETICVECTORPOTENTIAL"]


def get_qudt_quantity_kind_magnetization_field() -> URIRef:
    """Returns the URI for QUDT quantity kind: Magnetization Field (http://qudt.org/vocab/quantitykind/MagnetizationField)"""
    return QUDT_QUANTITY_KIND["MAGNETIZATIONFIELD"]


def get_qudt_quantity_kind_magnetomotive_force() -> URIRef:
    """Returns the URI for QUDT quantity kind: Magnetomotive Force (http://qudt.org/vocab/quantitykind/MagnetomotiveForce)"""
    return QUDT_QUANTITY_KIND["MAGNETOMOTIVEFORCE"]


def get_qudt_quantity_kind_mass_absorption_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass Absorption Coefficient (http://qudt.org/vocab/quantitykind/MassAbsorptionCoefficient)"""
    return QUDT_QUANTITY_KIND["MASSABSORPTIONCOEFFICIENT"]


def get_qudt_quantity_kind_mass_amount_of_substance_temperature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass Amount of Substance Temperature (http://qudt.org/vocab/quantitykind/MassAmountOfSubstanceTemperature)"""
    return QUDT_QUANTITY_KIND["MASSAMOUNTOFSUBSTANCETEMPERATURE"]


def get_qudt_quantity_kind_mass_attenuation_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass Attenuation Coefficient (http://qudt.org/vocab/quantitykind/MassAttenuationCoefficient)"""
    return QUDT_QUANTITY_KIND["MASSATTENUATIONCOEFFICIENT"]


def get_qudt_quantity_kind_mass_concentration() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass Concentration (http://qudt.org/vocab/quantitykind/MassConcentration)"""
    return QUDT_QUANTITY_KIND["MASSCONCENTRATION"]


def get_qudt_quantity_kind_mass_concentration_of_water() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass Concentration of Water (http://qudt.org/vocab/quantitykind/MassConcentrationOfWater)"""
    return QUDT_QUANTITY_KIND["MASSCONCENTRATIONOFWATER"]


def get_qudt_quantity_kind_mass_concentration_of_water_vapour() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass Concentration of Water Vapour (http://qudt.org/vocab/quantitykind/MassConcentrationOfWaterVapour)"""
    return QUDT_QUANTITY_KIND["MASSCONCENTRATIONOFWATERVAPOUR"]


def get_qudt_quantity_kind_mass_concentration_rate_of_change() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass Concentration Rate Of Change (http://qudt.org/vocab/quantitykind/MassConcentrationRateOfChange)"""
    return QUDT_QUANTITY_KIND["MASSCONCENTRATIONRATEOFCHANGE"]


def get_qudt_quantity_kind_mass_defect() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass Defect (http://qudt.org/vocab/quantitykind/MassDefect)"""
    return QUDT_QUANTITY_KIND["MASSDEFECT"]


def get_qudt_quantity_kind_mass_energy_transfer_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass Energy Transfer Coefficient (http://qudt.org/vocab/quantitykind/MassEnergyTransferCoefficient)"""
    return QUDT_QUANTITY_KIND["MASSENERGYTRANSFERCOEFFICIENT"]


def get_qudt_quantity_kind_mass_excess() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass Excess (http://qudt.org/vocab/quantitykind/MassExcess)"""
    return QUDT_QUANTITY_KIND["MASSEXCESS"]


def get_qudt_quantity_kind_mass_flux_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: mass flux density (http://qudt.org/vocab/quantitykind/MassFluxDensity)"""
    return QUDT_QUANTITY_KIND["MASSFLUXDENSITY"]


def get_qudt_quantity_kind_mass_fraction() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass Fraction (http://qudt.org/vocab/quantitykind/MassFraction)"""
    return QUDT_QUANTITY_KIND["MASSFRACTION"]


def get_qudt_quantity_kind_mass_fraction_of_dry_matter() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass Fraction of Dry Matter (http://qudt.org/vocab/quantitykind/MassFractionOfDryMatter)"""
    return QUDT_QUANTITY_KIND["MASSFRACTIONOFDRYMATTER"]


def get_qudt_quantity_kind_mass_fraction_of_water() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass Fraction of Water (http://qudt.org/vocab/quantitykind/MassFractionOfWater)"""
    return QUDT_QUANTITY_KIND["MASSFRACTIONOFWATER"]


def get_qudt_quantity_kind_mass_number() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass Number (http://qudt.org/vocab/quantitykind/MassNumber)"""
    return QUDT_QUANTITY_KIND["MASSNUMBER"]


def get_qudt_quantity_kind_mass_of_electrical_power_supply() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass Of Electrical Power Supply (http://qudt.org/vocab/quantitykind/MassOfElectricalPowerSupply)"""
    return QUDT_QUANTITY_KIND["MASSOFELECTRICALPOWERSUPPLY"]


def get_qudt_quantity_kind_mass_of_solid_booster() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass Of Solid Booster (http://qudt.org/vocab/quantitykind/MassOfSolidBooster)"""
    return QUDT_QUANTITY_KIND["MASSOFSOLIDBOOSTER"]


def get_qudt_quantity_kind_mass_of_the_earth() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass Of The Earth (http://qudt.org/vocab/quantitykind/MassOfTheEarth)"""
    return QUDT_QUANTITY_KIND["MASSOFTHEEARTH"]


def get_qudt_quantity_kind_mass_per_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass per Energy (http://qudt.org/vocab/quantitykind/MassPerEnergy)"""
    return QUDT_QUANTITY_KIND["MASSPERENERGY"]


def get_qudt_quantity_kind_mass_per_time() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass per Time (http://qudt.org/vocab/quantitykind/MassPerTime)"""
    return QUDT_QUANTITY_KIND["MASSPERTIME"]


def get_qudt_quantity_kind_mass_concentration_of_water_to_dry_matter() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass Concentration of Water To Dry Matter (http://qudt.org/vocab/quantitykind/MassRatioOfWaterToDryMatter)"""
    return QUDT_QUANTITY_KIND["MASSRATIOOFWATERTODRYMATTER"]


def get_qudt_quantity_kind_mass_ratio_of_water_vapour_to_dry_gas() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass Ratio of Water Vapour to Dry Gas (http://qudt.org/vocab/quantitykind/MassRatioOfWaterVapourToDryGas)"""
    return QUDT_QUANTITY_KIND["MASSRATIOOFWATERVAPOURTODRYGAS"]


def get_qudt_quantity_kind_mass_specific_biogeochemical_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mass Specific Biogeochemical Rate (http://qudt.org/vocab/quantitykind/MassSpecificBiogeochemicalRate)"""
    return QUDT_QUANTITY_KIND["MASSSPECIFICBIOGEOCHEMICALRATE"]


def get_qudt_quantity_kind_mass_stopping_power() -> URIRef:
    """Returns the URI for QUDT quantity kind: mass stopping power (http://qudt.org/vocab/quantitykind/MassStoppingPower)"""
    return QUDT_QUANTITY_KIND["MASSSTOPPINGPOWER"]


def get_qudt_quantity_kind_massic_electric_current() -> URIRef:
    """Returns the URI for QUDT quantity kind: massic electric current (http://qudt.org/vocab/quantitykind/MassicElectricCurrent)"""
    return QUDT_QUANTITY_KIND["MASSICELECTRICCURRENT"]


def get_qudt_quantity_kind_massic_heat_capacity() -> URIRef:
    """Returns the URI for QUDT quantity kind: massic heat capacity (http://qudt.org/vocab/quantitykind/MassicHeatCapacity)"""
    return QUDT_QUANTITY_KIND["MASSICHEATCAPACITY"]


def get_qudt_quantity_kind_massic_power() -> URIRef:
    """Returns the URI for QUDT quantity kind: massic power (http://qudt.org/vocab/quantitykind/MassicPower)"""
    return QUDT_QUANTITY_KIND["MASSICPOWER"]


def get_qudt_quantity_kind_massic_torque() -> URIRef:
    """Returns the URI for QUDT quantity kind: massic torque (http://qudt.org/vocab/quantitykind/MassicTorque)"""
    return QUDT_QUANTITY_KIND["MASSICTORQUE"]


def get_qudt_quantity_kind_massieu_function() -> URIRef:
    """Returns the URI for QUDT quantity kind: Massieu Function (http://qudt.org/vocab/quantitykind/MassieuFunction)"""
    return QUDT_QUANTITY_KIND["MASSIEUFUNCTION"]


def get_qudt_quantity_kind_planck_function() -> URIRef:
    """Returns the URI for QUDT quantity kind: Planck Function (http://qudt.org/vocab/quantitykind/PlanckFunction)"""
    return QUDT_QUANTITY_KIND["PLANCKFUNCTION"]


def get_qudt_quantity_kind_specific_enthalpy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Specific Enthalpy (http://qudt.org/vocab/quantitykind/SpecificEnthalpy)"""
    return QUDT_QUANTITY_KIND["SPECIFICENTHALPY"]


def get_qudt_quantity_kind_specific_gibbs_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Specific Gibbs Energy (http://qudt.org/vocab/quantitykind/SpecificGibbsEnergy)"""
    return QUDT_QUANTITY_KIND["SPECIFICGIBBSENERGY"]


def get_qudt_quantity_kind_specific_helmholtz_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Specific Helmholtz Energy (http://qudt.org/vocab/quantitykind/SpecificHelmholtzEnergy)"""
    return QUDT_QUANTITY_KIND["SPECIFICHELMHOLTZENERGY"]


def get_qudt_quantity_kind_specific_internal_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Specific Internal Energy (http://qudt.org/vocab/quantitykind/SpecificInternalEnergy)"""
    return QUDT_QUANTITY_KIND["SPECIFICINTERNALENERGY"]


def get_qudt_quantity_kind_maximum_expected_operating_thrust() -> URIRef:
    """Returns the URI for QUDT quantity kind: Maximum Expected Operating Thrust (http://qudt.org/vocab/quantitykind/MaxExpectedOperatingThrust)"""
    return QUDT_QUANTITY_KIND["MAXEXPECTEDOPERATINGTHRUST"]


def get_qudt_quantity_kind_max_operating_thrust() -> URIRef:
    """Returns the URI for QUDT quantity kind: Max Operating Thrust (http://qudt.org/vocab/quantitykind/MaxOperatingThrust)"""
    return QUDT_QUANTITY_KIND["MAXOPERATINGTHRUST"]


def get_qudt_quantity_kind_thrust() -> URIRef:
    """Returns the URI for QUDT quantity kind: Thrust (http://qudt.org/vocab/quantitykind/Thrust)"""
    return QUDT_QUANTITY_KIND["THRUST"]


def get_qudt_quantity_kind_max_sea_level_thrust() -> URIRef:
    """Returns the URI for QUDT quantity kind: Max Sea Level Thrust (http://qudt.org/vocab/quantitykind/MaxSeaLevelThrust)"""
    return QUDT_QUANTITY_KIND["MAXSEALEVELTHRUST"]


def get_qudt_quantity_kind_maximum_beta_particle_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Maximum Beta-Particle Energy (http://qudt.org/vocab/quantitykind/MaximumBeta-ParticleEnergy)"""
    return QUDT_QUANTITY_KIND["MAXIMUMBETA-PARTICLEENERGY"]


def get_qudt_quantity_kind_maximum_expected_operating_pressure() -> URIRef:
    """Returns the URI for QUDT quantity kind: Maximum Expected Operating Pressure (http://qudt.org/vocab/quantitykind/MaximumExpectedOperatingPressure)"""
    return QUDT_QUANTITY_KIND["MAXIMUMEXPECTEDOPERATINGPRESSURE"]


def get_qudt_quantity_kind_maximum_operating_pressure() -> URIRef:
    """Returns the URI for QUDT quantity kind: Maximum Operating Pressure (http://qudt.org/vocab/quantitykind/MaximumOperatingPressure)"""
    return QUDT_QUANTITY_KIND["MAXIMUMOPERATINGPRESSURE"]


def get_qudt_quantity_kind_mean_energy_imparted() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mean Energy Imparted (http://qudt.org/vocab/quantitykind/MeanEnergyImparted)"""
    return QUDT_QUANTITY_KIND["MEANENERGYIMPARTED"]


def get_qudt_quantity_kind_mean_free_path() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mean Free Path (http://qudt.org/vocab/quantitykind/MeanFreePath)"""
    return QUDT_QUANTITY_KIND["MEANFREEPATH"]


def get_qudt_quantity_kind_mean_lifetime() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mean Lifetime (http://qudt.org/vocab/quantitykind/MeanLifetime)"""
    return QUDT_QUANTITY_KIND["MEANLIFETIME"]


def get_qudt_quantity_kind_mean_linear_range() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mean Linear Range (http://qudt.org/vocab/quantitykind/MeanLinearRange)"""
    return QUDT_QUANTITY_KIND["MEANLINEARRANGE"]


def get_qudt_quantity_kind_mean_mass_range() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mean Mass Range (http://qudt.org/vocab/quantitykind/MeanMassRange)"""
    return QUDT_QUANTITY_KIND["MEANMASSRANGE"]


def get_qudt_quantity_kind_mechanical_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mechanical Energy (http://qudt.org/vocab/quantitykind/MechanicalEnergy)"""
    return QUDT_QUANTITY_KIND["MECHANICALENERGY"]


def get_qudt_quantity_kind_mechanical_impedance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mechanical Impedance (http://qudt.org/vocab/quantitykind/MechanicalImpedance)"""
    return QUDT_QUANTITY_KIND["MECHANICALIMPEDANCE"]


def get_qudt_quantity_kind_mechanical_mobility() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mechanical Mobility (http://qudt.org/vocab/quantitykind/MechanicalMobility)"""
    return QUDT_QUANTITY_KIND["MECHANICALMOBILITY"]


def get_qudt_quantity_kind_mechanical_surface_impedance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mechanical surface impedance (http://qudt.org/vocab/quantitykind/MechanicalSurfaceImpedance)"""
    return QUDT_QUANTITY_KIND["MECHANICALSURFACEIMPEDANCE"]


def get_qudt_quantity_kind_melting_point_temperature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Melting Point Temperature (http://qudt.org/vocab/quantitykind/MeltingPoint)"""
    return QUDT_QUANTITY_KIND["MELTINGPOINT"]


def get_qudt_quantity_kind_micro_canonical_partition_function() -> URIRef:
    """Returns the URI for QUDT quantity kind: Micro Canonical Partition Function (http://qudt.org/vocab/quantitykind/MicroCanonicalPartitionFunction)"""
    return QUDT_QUANTITY_KIND["MICROCANONICALPARTITIONFUNCTION"]


def get_qudt_quantity_kind_microbial_formation() -> URIRef:
    """Returns the URI for QUDT quantity kind: Microbial Formation (http://qudt.org/vocab/quantitykind/MicrobialFormation)"""
    return QUDT_QUANTITY_KIND["MICROBIALFORMATION"]


def get_qudt_quantity_kind_migration_area() -> URIRef:
    """Returns the URI for QUDT quantity kind: Migration Area (http://qudt.org/vocab/quantitykind/MigrationArea)"""
    return QUDT_QUANTITY_KIND["MIGRATIONAREA"]


def get_qudt_quantity_kind_migration_length() -> URIRef:
    """Returns the URI for QUDT quantity kind: Migration Length (http://qudt.org/vocab/quantitykind/MigrationLength)"""
    return QUDT_QUANTITY_KIND["MIGRATIONLENGTH"]


def get_qudt_quantity_kind_mobility_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mobility Ratio (http://qudt.org/vocab/quantitykind/MobilityRatio)"""
    return QUDT_QUANTITY_KIND["MOBILITYRATIO"]


def get_qudt_quantity_kind_modulus_of_admittance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Modulus Of Admittance (http://qudt.org/vocab/quantitykind/ModulusOfAdmittance)"""
    return QUDT_QUANTITY_KIND["MODULUSOFADMITTANCE"]


def get_qudt_quantity_kind_modulus_of_elasticity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Modulus of Elasticity (http://qudt.org/vocab/quantitykind/ModulusOfElasticity)"""
    return QUDT_QUANTITY_KIND["MODULUSOFELASTICITY"]


def get_qudt_quantity_kind_modulus_of_impedance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Modulus Of Impedance (http://qudt.org/vocab/quantitykind/ModulusOfImpedance)"""
    return QUDT_QUANTITY_KIND["MODULUSOFIMPEDANCE"]


def get_qudt_quantity_kind_modulus_of_linear_subgrade_reaction() -> URIRef:
    """Returns the URI for QUDT quantity kind: Modulus of Linear Subgrade Reaction (http://qudt.org/vocab/quantitykind/ModulusOfLinearSubgradeReaction)"""
    return QUDT_QUANTITY_KIND["MODULUSOFLINEARSUBGRADEREACTION"]


def get_qudt_quantity_kind_modulus_of_rotational_subgrade_reaction() -> URIRef:
    """Returns the URI for QUDT quantity kind: Modulus of Rotational Subgrade Reaction (http://qudt.org/vocab/quantitykind/ModulusOfRotationalSubgradeReaction)"""
    return QUDT_QUANTITY_KIND["MODULUSOFROTATIONALSUBGRADEREACTION"]


def get_qudt_quantity_kind_modulus_of_subgrade_reaction() -> URIRef:
    """Returns the URI for QUDT quantity kind: Modulus of Subgrade Reaction (http://qudt.org/vocab/quantitykind/ModulusOfSubgradeReaction)"""
    return QUDT_QUANTITY_KIND["MODULUSOFSUBGRADEREACTION"]


def get_qudt_quantity_kind_moisture_diffusivity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Moisture Diffusivity (http://qudt.org/vocab/quantitykind/MoistureDiffusivity)"""
    return QUDT_QUANTITY_KIND["MOISTUREDIFFUSIVITY"]


def get_qudt_quantity_kind_molality_of_solute() -> URIRef:
    """Returns the URI for QUDT quantity kind: Molality of Solute (http://qudt.org/vocab/quantitykind/MolalityOfSolute)"""
    return QUDT_QUANTITY_KIND["MOLALITYOFSOLUTE"]


def get_qudt_quantity_kind_molar_absorption_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Molar Absorption Coefficient (http://qudt.org/vocab/quantitykind/MolarAbsorptionCoefficient)"""
    return QUDT_QUANTITY_KIND["MOLARABSORPTIONCOEFFICIENT"]


def get_qudt_quantity_kind_molar_conductivity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Molar Conductivity (http://qudt.org/vocab/quantitykind/MolarConductivity)"""
    return QUDT_QUANTITY_KIND["MOLARCONDUCTIVITY"]


def get_qudt_quantity_kind_molar_entropy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Molar Entropy (http://qudt.org/vocab/quantitykind/MolarEntropy)"""
    return QUDT_QUANTITY_KIND["MOLARENTROPY"]


def get_qudt_quantity_kind_molar_flow_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: Molar Flow Rate (http://qudt.org/vocab/quantitykind/MolarFlowRate)"""
    return QUDT_QUANTITY_KIND["MOLARFLOWRATE"]


def get_qudt_quantity_kind_molar_flux_density_variance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Molar Flux Density Variance (http://qudt.org/vocab/quantitykind/MolarFluxDensityVariance)"""
    return QUDT_QUANTITY_KIND["MOLARFLUXDENSITYVARIANCE"]


def get_qudt_quantity_kind_molar_flux_density_variance_neon() -> URIRef:
    """Returns the URI for QUDT quantity kind: Molar Flux Density Variance, NEON (http://qudt.org/vocab/quantitykind/MolarFluxDensityVariance_NEON)"""
    return QUDT_QUANTITY_KIND["MOLARFLUXDENSITYVARIANCE_NEON"]


def get_qudt_quantity_kind_molar_internal_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: molar internal energy (http://qudt.org/vocab/quantitykind/MolarInternalEnergy)"""
    return QUDT_QUANTITY_KIND["MOLARINTERNALENERGY"]


def get_qudt_quantity_kind_molar_optical_rotatory_power() -> URIRef:
    """Returns the URI for QUDT quantity kind: Molar Optical Rotatory Power (http://qudt.org/vocab/quantitykind/MolarOpticalRotatoryPower)"""
    return QUDT_QUANTITY_KIND["MOLAROPTICALROTATORYPOWER"]


def get_qudt_quantity_kind_molar_refractivity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Molar Refractivity (http://qudt.org/vocab/quantitykind/MolarRefractivity)"""
    return QUDT_QUANTITY_KIND["MOLARREFRACTIVITY"]


def get_qudt_quantity_kind_mole_fraction() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mole Fraction (http://qudt.org/vocab/quantitykind/MoleFraction)"""
    return QUDT_QUANTITY_KIND["MOLEFRACTION"]


def get_qudt_quantity_kind_molecular_concentration() -> URIRef:
    """Returns the URI for QUDT quantity kind: Molecular Concentration (http://qudt.org/vocab/quantitykind/MolecularConcentration)"""
    return QUDT_QUANTITY_KIND["MOLECULARCONCENTRATION"]


def get_qudt_quantity_kind_molecular_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: Molecular Mass (http://qudt.org/vocab/quantitykind/MolecularMass)"""
    return QUDT_QUANTITY_KIND["MOLECULARMASS"]


def get_qudt_quantity_kind_rotational_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: Rotational Mass (http://qudt.org/vocab/quantitykind/RotationalMass)"""
    return QUDT_QUANTITY_KIND["ROTATIONALMASS"]


def get_qudt_quantity_kind_momentum_per_angle() -> URIRef:
    """Returns the URI for QUDT quantity kind: Momentum per Angle (http://qudt.org/vocab/quantitykind/MomentumPerAngle)"""
    return QUDT_QUANTITY_KIND["MOMENTUMPERANGLE"]


def get_qudt_quantity_kind_morbidity_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: Morbidity Rate (http://qudt.org/vocab/quantitykind/MorbidityRate)"""
    return QUDT_QUANTITY_KIND["MORBIDITYRATE"]


def get_qudt_quantity_kind_mortality_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: Mortality Rate (http://qudt.org/vocab/quantitykind/MortalityRate)"""
    return QUDT_QUANTITY_KIND["MORTALITYRATE"]


def get_qudt_quantity_kind_motor_constant() -> URIRef:
    """Returns the URI for QUDT quantity kind: motor constant (http://qudt.org/vocab/quantitykind/MotorConstant)"""
    return QUDT_QUANTITY_KIND["MOTORCONSTANT"]


def get_qudt_quantity_kind_nominal_ascent_propellant_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: Nominal Ascent Propellant Mass (http://qudt.org/vocab/quantitykind/NOMINAL-ASCENT-PROPELLANT-MASS)"""
    return QUDT_QUANTITY_KIND["NOMINAL-ASCENT-PROPELLANT-MASS"]


def get_qudt_quantity_kind_napierian_absorbance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Napierian Absorbance (http://qudt.org/vocab/quantitykind/NapierianAbsorbance)"""
    return QUDT_QUANTITY_KIND["NAPIERIANABSORBANCE"]


def get_qudt_quantity_kind_diffusion_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: diffusion coefficient (http://qudt.org/vocab/quantitykind/NeutronDiffusionCoefficient)"""
    return QUDT_QUANTITY_KIND["NEUTRONDIFFUSIONCOEFFICIENT"]


def get_qudt_quantity_kind_neutron_diffusion_length() -> URIRef:
    """Returns the URI for QUDT quantity kind: Neutron Diffusion Length (http://qudt.org/vocab/quantitykind/NeutronDiffusionLength)"""
    return QUDT_QUANTITY_KIND["NEUTRONDIFFUSIONLENGTH"]


def get_qudt_quantity_kind_neutron_number() -> URIRef:
    """Returns the URI for QUDT quantity kind: neutron number (http://qudt.org/vocab/quantitykind/NeutronNumber)"""
    return QUDT_QUANTITY_KIND["NEUTRONNUMBER"]


def get_qudt_quantity_kind_neutron_yield_per_absorption() -> URIRef:
    """Returns the URI for QUDT quantity kind: Neutron Yield per Absorption (http://qudt.org/vocab/quantitykind/NeutronYieldPerAbsorption)"""
    return QUDT_QUANTITY_KIND["NEUTRONYIELDPERABSORPTION"]


def get_qudt_quantity_kind_neutron_yield_per_fission() -> URIRef:
    """Returns the URI for QUDT quantity kind: Neutron Yield per Fission (http://qudt.org/vocab/quantitykind/NeutronYieldPerFission)"""
    return QUDT_QUANTITY_KIND["NEUTRONYIELDPERFISSION"]


def get_qudt_quantity_kind_non_leakage_probability() -> URIRef:
    """Returns the URI for QUDT quantity kind: Non-Leakage Probability (http://qudt.org/vocab/quantitykind/Non-LeakageProbability)"""
    return QUDT_QUANTITY_KIND["NON-LEAKAGEPROBABILITY"]


def get_qudt_quantity_kind_non_active_power() -> URIRef:
    """Returns the URI for QUDT quantity kind: Non-active Power (http://qudt.org/vocab/quantitykind/NonActivePower)"""
    return QUDT_QUANTITY_KIND["NONACTIVEPOWER"]


def get_qudt_quantity_kind_positive_length() -> URIRef:
    """Returns the URI for QUDT quantity kind: Positive Length (http://qudt.org/vocab/quantitykind/NonNegativeLength)"""
    return QUDT_QUANTITY_KIND["NONNEGATIVELENGTH"]


def get_qudt_quantity_kind_normal_stress() -> URIRef:
    """Returns the URI for QUDT quantity kind: Normal Stress (http://qudt.org/vocab/quantitykind/NormalStress)"""
    return QUDT_QUANTITY_KIND["NORMALSTRESS"]


def get_qudt_quantity_kind_stress() -> URIRef:
    """Returns the URI for QUDT quantity kind: Stress (http://qudt.org/vocab/quantitykind/Stress)"""
    return QUDT_QUANTITY_KIND["STRESS"]


def get_qudt_quantity_kind_positive_dimensionless_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Positive Dimensionless Ratio (http://qudt.org/vocab/quantitykind/NormalizedDimensionlessRatio)"""
    return QUDT_QUANTITY_KIND["NORMALIZEDDIMENSIONLESSRATIO"]


def get_qudt_quantity_kind_nozzle_throat_cross_sectional_area() -> URIRef:
    """Returns the URI for QUDT quantity kind: Nozzle Throat Cross-sectional Area (http://qudt.org/vocab/quantitykind/NozzleThroatCrossSectionalArea)"""
    return QUDT_QUANTITY_KIND["NOZZLETHROATCROSSSECTIONALAREA"]


def get_qudt_quantity_kind_nozzle_throat_pressure() -> URIRef:
    """Returns the URI for QUDT quantity kind: Nozzle Throat Pressure (http://qudt.org/vocab/quantitykind/NozzleThroatPressure)"""
    return QUDT_QUANTITY_KIND["NOZZLETHROATPRESSURE"]


def get_qudt_quantity_kind_nozzle_walls_thrust_reaction() -> URIRef:
    """Returns the URI for QUDT quantity kind: Nozzle Walls Thrust Reaction (http://qudt.org/vocab/quantitykind/NozzleWallsThrustReaction)"""
    return QUDT_QUANTITY_KIND["NOZZLEWALLSTHRUSTREACTION"]


def get_qudt_quantity_kind_nuclear_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: nuclear energy (http://qudt.org/vocab/quantitykind/NuclearEnergy)"""
    return QUDT_QUANTITY_KIND["NUCLEARENERGY"]


def get_qudt_quantity_kind_nuclear_quadrupole_moment() -> URIRef:
    """Returns the URI for QUDT quantity kind: Nuclear Quadrupole Moment (http://qudt.org/vocab/quantitykind/NuclearQuadrupoleMoment)"""
    return QUDT_QUANTITY_KIND["NUCLEARQUADRUPOLEMOMENT"]


def get_qudt_quantity_kind_nuclear_radius() -> URIRef:
    """Returns the URI for QUDT quantity kind: Nuclear Radius (http://qudt.org/vocab/quantitykind/NuclearRadius)"""
    return QUDT_QUANTITY_KIND["NUCLEARRADIUS"]


def get_qudt_quantity_kind_spin_quantum_number() -> URIRef:
    """Returns the URI for QUDT quantity kind: Spin Quantum Number (http://qudt.org/vocab/quantitykind/NuclearSpinQuantumNumber)"""
    return QUDT_QUANTITY_KIND["NUCLEARSPINQUANTUMNUMBER"]


def get_qudt_quantity_kind_nucleon_number() -> URIRef:
    """Returns the URI for QUDT quantity kind: nucleon number (http://qudt.org/vocab/quantitykind/NucleonNumber)"""
    return QUDT_QUANTITY_KIND["NUCLEONNUMBER"]


def get_qudt_quantity_kind_number_of_electrical_phases() -> URIRef:
    """Returns the URI for QUDT quantity kind: Number of Electrical Phases (http://qudt.org/vocab/quantitykind/NumberOfElectricalPhases)"""
    return QUDT_QUANTITY_KIND["NUMBEROFELECTRICALPHASES"]


def get_qudt_quantity_kind_number_of_particles() -> URIRef:
    """Returns the URI for QUDT quantity kind: Number of Particles (http://qudt.org/vocab/quantitykind/NumberOfParticles)"""
    return QUDT_QUANTITY_KIND["NUMBEROFPARTICLES"]


def get_qudt_quantity_kind_olfactory_threshold() -> URIRef:
    """Returns the URI for QUDT quantity kind: Olfactory Threshold (http://qudt.org/vocab/quantitykind/OlfactoryThreshold)"""
    return QUDT_QUANTITY_KIND["OLFACTORYTHRESHOLD"]


def get_qudt_quantity_kind_opening_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Opening Ratio (http://qudt.org/vocab/quantitykind/OpeningRatio)"""
    return QUDT_QUANTITY_KIND["OPENINGRATIO"]


def get_qudt_quantity_kind_orbital_angular_momentum_per_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: Orbital Angular Momentum per Mass (http://qudt.org/vocab/quantitykind/OrbitalAngularMomentumPerMass)"""
    return QUDT_QUANTITY_KIND["ORBITALANGULARMOMENTUMPERMASS"]


def get_qudt_quantity_kind_orbital_radial_distance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Orbital Radial Distance (http://qudt.org/vocab/quantitykind/OrbitalRadialDistance)"""
    return QUDT_QUANTITY_KIND["ORBITALRADIALDISTANCE"]


def get_qudt_quantity_kind_order_of_reflection() -> URIRef:
    """Returns the URI for QUDT quantity kind: Order of Reflection (http://qudt.org/vocab/quantitykind/OrderOfReflection)"""
    return QUDT_QUANTITY_KIND["ORDEROFREFLECTION"]


def get_qudt_quantity_kind_osmotic_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Osmotic Coefficient (http://qudt.org/vocab/quantitykind/OsmoticCoefficient)"""
    return QUDT_QUANTITY_KIND["OSMOTICCOEFFICIENT"]


def get_qudt_quantity_kind_osmotic_concentration() -> URIRef:
    """Returns the URI for QUDT quantity kind: Osmotic Concentration (http://qudt.org/vocab/quantitykind/OsmoticConcentration)"""
    return QUDT_QUANTITY_KIND["OSMOTICCONCENTRATION"]


def get_qudt_quantity_kind_osmotic_pressure() -> URIRef:
    """Returns the URI for QUDT quantity kind: osmotic pressure (http://qudt.org/vocab/quantitykind/OsmoticPressure)"""
    return QUDT_QUANTITY_KIND["OSMOTICPRESSURE"]


def get_qudt_quantity_kind_over_range_distance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Over-range distance (http://qudt.org/vocab/quantitykind/OverRangeDistance)"""
    return QUDT_QUANTITY_KIND["OVERRANGEDISTANCE"]


def get_qudt_quantity_kind_predicted_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: Predicted Mass (http://qudt.org/vocab/quantitykind/PREDICTED-MASS)"""
    return QUDT_QUANTITY_KIND["PREDICTED-MASS"]


def get_qudt_quantity_kind_product_of_inertia() -> URIRef:
    """Returns the URI for QUDT quantity kind: Product of Inertia (http://qudt.org/vocab/quantitykind/PRODUCT-OF-INERTIA)"""
    return QUDT_QUANTITY_KIND["PRODUCT-OF-INERTIA"]


def get_qudt_quantity_kind_product_of_inertia_in_the_x_axis() -> URIRef:
    """Returns the URI for QUDT quantity kind: Product of Inertia in the X axis (http://qudt.org/vocab/quantitykind/PRODUCT-OF-INERTIA_X)"""
    return QUDT_QUANTITY_KIND["PRODUCT-OF-INERTIA_X"]


def get_qudt_quantity_kind_product_of_inertia_in_the_x_axis() -> URIRef:
    """Returns the URI for QUDT quantity kind: Product of Inertia in the X axis (http://qudt.org/vocab/quantitykind/ProductOfInertia_X)"""
    return QUDT_QUANTITY_KIND["PRODUCTOFINERTIA_X"]


def get_qudt_quantity_kind_product_of_inertia_in_the_y_axis() -> URIRef:
    """Returns the URI for QUDT quantity kind: Product of Inertia in the Y axis (http://qudt.org/vocab/quantitykind/PRODUCT-OF-INERTIA_Y)"""
    return QUDT_QUANTITY_KIND["PRODUCT-OF-INERTIA_Y"]


def get_qudt_quantity_kind_product_of_inertia_in_the_y_axis() -> URIRef:
    """Returns the URI for QUDT quantity kind: Product of Inertia in the Y axis (http://qudt.org/vocab/quantitykind/ProductOfInertia_Y)"""
    return QUDT_QUANTITY_KIND["PRODUCTOFINERTIA_Y"]


def get_qudt_quantity_kind_product_of_inertia_in_the_z_axis() -> URIRef:
    """Returns the URI for QUDT quantity kind: Product of Inertia in the Z axis (http://qudt.org/vocab/quantitykind/PRODUCT-OF-INERTIA_Z)"""
    return QUDT_QUANTITY_KIND["PRODUCT-OF-INERTIA_Z"]


def get_qudt_quantity_kind_product_of_inertia_in_the_z_axis() -> URIRef:
    """Returns the URI for QUDT quantity kind: Product of Inertia in the Z axis (http://qudt.org/vocab/quantitykind/ProductOfInertia_Z)"""
    return QUDT_QUANTITY_KIND["PRODUCTOFINERTIA_Z"]


def get_qudt_quantity_kind_pace() -> URIRef:
    """Returns the URI for QUDT quantity kind: Pace (http://qudt.org/vocab/quantitykind/Pace)"""
    return QUDT_QUANTITY_KIND["PACE"]


def get_qudt_quantity_kind_packing_fraction() -> URIRef:
    """Returns the URI for QUDT quantity kind: Packing Fraction (http://qudt.org/vocab/quantitykind/PackingFraction)"""
    return QUDT_QUANTITY_KIND["PACKINGFRACTION"]


def get_qudt_quantity_kind_partial_pressure() -> URIRef:
    """Returns the URI for QUDT quantity kind: Partial Pressure (http://qudt.org/vocab/quantitykind/PartialPressure)"""
    return QUDT_QUANTITY_KIND["PARTIALPRESSURE"]


def get_qudt_quantity_kind_particle_current() -> URIRef:
    """Returns the URI for QUDT quantity kind: Particle Current (http://qudt.org/vocab/quantitykind/ParticleCurrent)"""
    return QUDT_QUANTITY_KIND["PARTICLECURRENT"]


def get_qudt_quantity_kind_particle_current_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: particle current density (http://qudt.org/vocab/quantitykind/ParticleCurrentDensity)"""
    return QUDT_QUANTITY_KIND["PARTICLECURRENTDENSITY"]


def get_qudt_quantity_kind_particle_fluence() -> URIRef:
    """Returns the URI for QUDT quantity kind: Particle Fluence (http://qudt.org/vocab/quantitykind/ParticleFluence)"""
    return QUDT_QUANTITY_KIND["PARTICLEFLUENCE"]


def get_qudt_quantity_kind_particle_fluence_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: Particle Fluence Rate (http://qudt.org/vocab/quantitykind/ParticleFluenceRate)"""
    return QUDT_QUANTITY_KIND["PARTICLEFLUENCERATE"]


def get_qudt_quantity_kind_particle_number_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Particle Number Density (http://qudt.org/vocab/quantitykind/ParticleNumberDensity)"""
    return QUDT_QUANTITY_KIND["PARTICLENUMBERDENSITY"]


def get_qudt_quantity_kind_particle_position_vector() -> URIRef:
    """Returns the URI for QUDT quantity kind: Particle Position Vector (http://qudt.org/vocab/quantitykind/ParticlePositionVector)"""
    return QUDT_QUANTITY_KIND["PARTICLEPOSITIONVECTOR"]


def get_qudt_quantity_kind_particle_source_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Particle Source Density (http://qudt.org/vocab/quantitykind/ParticleSourceDensity)"""
    return QUDT_QUANTITY_KIND["PARTICLESOURCEDENSITY"]


def get_qudt_quantity_kind_path_length() -> URIRef:
    """Returns the URI for QUDT quantity kind: Path Length (http://qudt.org/vocab/quantitykind/PathLength)"""
    return QUDT_QUANTITY_KIND["PATHLENGTH"]


def get_qudt_quantity_kind_payload_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: Payload Mass (http://qudt.org/vocab/quantitykind/PayloadMass)"""
    return QUDT_QUANTITY_KIND["PAYLOADMASS"]


def get_qudt_quantity_kind_payload_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Payload Ratio (http://qudt.org/vocab/quantitykind/PayloadRatio)"""
    return QUDT_QUANTITY_KIND["PAYLOADRATIO"]


def get_qudt_quantity_kind_peltier_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Peltier Coefficient (http://qudt.org/vocab/quantitykind/PeltierCoefficient)"""
    return QUDT_QUANTITY_KIND["PELTIERCOEFFICIENT"]


def get_qudt_quantity_kind_period() -> URIRef:
    """Returns the URI for QUDT quantity kind: Period (http://qudt.org/vocab/quantitykind/Period)"""
    return QUDT_QUANTITY_KIND["PERIOD"]


def get_qudt_quantity_kind_permeability_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Permeability Ratio (http://qudt.org/vocab/quantitykind/PermeabilityRatio)"""
    return QUDT_QUANTITY_KIND["PERMEABILITYRATIO"]


def get_qudt_quantity_kind_permeance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Permeance (http://qudt.org/vocab/quantitykind/Permeance)"""
    return QUDT_QUANTITY_KIND["PERMEANCE"]


def get_qudt_quantity_kind_reluctance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Reluctance (http://qudt.org/vocab/quantitykind/Reluctance)"""
    return QUDT_QUANTITY_KIND["RELUCTANCE"]


def get_qudt_quantity_kind_permittivity_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Permittivity Ratio (http://qudt.org/vocab/quantitykind/PermittivityRatio)"""
    return QUDT_QUANTITY_KIND["PERMITTIVITYRATIO"]


def get_qudt_quantity_kind_phase_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Phase coefficient (http://qudt.org/vocab/quantitykind/PhaseCoefficient)"""
    return QUDT_QUANTITY_KIND["PHASECOEFFICIENT"]


def get_qudt_quantity_kind_phase_difference() -> URIRef:
    """Returns the URI for QUDT quantity kind: phase difference (http://qudt.org/vocab/quantitykind/PhaseDifference)"""
    return QUDT_QUANTITY_KIND["PHASEDIFFERENCE"]


def get_qudt_quantity_kind_phase_speed_of_sound() -> URIRef:
    """Returns the URI for QUDT quantity kind: Phase speed of sound (http://qudt.org/vocab/quantitykind/PhaseSpeedOfSound)"""
    return QUDT_QUANTITY_KIND["PHASESPEEDOFSOUND"]


def get_qudt_quantity_kind_phonon_mean_free_path() -> URIRef:
    """Returns the URI for QUDT quantity kind: Phonon Mean Free Path (http://qudt.org/vocab/quantitykind/PhononMeanFreePath)"""
    return QUDT_QUANTITY_KIND["PHONONMEANFREEPATH"]


def get_qudt_quantity_kind_photo_threshold_of_awareness_function() -> URIRef:
    """Returns the URI for QUDT quantity kind: Photo Threshold of Awareness Function (http://qudt.org/vocab/quantitykind/PhotoThresholdOfAwarenessFunction)"""
    return QUDT_QUANTITY_KIND["PHOTOTHRESHOLDOFAWARENESSFUNCTION"]


def get_qudt_quantity_kind_photon_intensity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Photon Intensity (http://qudt.org/vocab/quantitykind/PhotonIntensity)"""
    return QUDT_QUANTITY_KIND["PHOTONINTENSITY"]


def get_qudt_quantity_kind_photon_luminance() -> URIRef:
    """Returns the URI for QUDT quantity kind: photon luminance (http://qudt.org/vocab/quantitykind/PhotonLuminance)"""
    return QUDT_QUANTITY_KIND["PHOTONLUMINANCE"]


def get_qudt_quantity_kind_photon_radiance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Photon Radiance (http://qudt.org/vocab/quantitykind/PhotonRadiance)"""
    return QUDT_QUANTITY_KIND["PHOTONRADIANCE"]


def get_qudt_quantity_kind_photosynthetic_photon_flux() -> URIRef:
    """Returns the URI for QUDT quantity kind: Photosynthetic Photon Flux (http://qudt.org/vocab/quantitykind/PhotosyntheticPhotonFlux)"""
    return QUDT_QUANTITY_KIND["PHOTOSYNTHETICPHOTONFLUX"]


def get_qudt_quantity_kind_photosynthetic_photon_flux_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Photosynthetic Photon Flux Density (http://qudt.org/vocab/quantitykind/PhotosyntheticPhotonFluxDensity)"""
    return QUDT_QUANTITY_KIND["PHOTOSYNTHETICPHOTONFLUXDENSITY"]


def get_qudt_quantity_kind_picture_element() -> URIRef:
    """Returns the URI for QUDT quantity kind: picture element (http://qudt.org/vocab/quantitykind/PictureElement)"""
    return QUDT_QUANTITY_KIND["PICTUREELEMENT"]


def get_qudt_quantity_kind_piece() -> URIRef:
    """Returns the URI for QUDT quantity kind: piece (http://qudt.org/vocab/quantitykind/Piece)"""
    return QUDT_QUANTITY_KIND["PIECE"]


def get_qudt_quantity_kind_planar_force() -> URIRef:
    """Returns the URI for QUDT quantity kind: Planar Force (http://qudt.org/vocab/quantitykind/PlanarForce)"""
    return QUDT_QUANTITY_KIND["PLANARFORCE"]


def get_qudt_quantity_kind_plasma_level() -> URIRef:
    """Returns the URI for QUDT quantity kind: Plasma Level (http://qudt.org/vocab/quantitykind/PlasmaLevel)"""
    return QUDT_QUANTITY_KIND["PLASMALEVEL"]


def get_qudt_quantity_kind_poisson_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Poisson Ratio (http://qudt.org/vocab/quantitykind/PoissonRatio)"""
    return QUDT_QUANTITY_KIND["POISSONRATIO"]


def get_qudt_quantity_kind_polar_moment_of_inertia() -> URIRef:
    """Returns the URI for QUDT quantity kind: Polar moment of inertia (http://qudt.org/vocab/quantitykind/PolarMomentOfInertia)"""
    return QUDT_QUANTITY_KIND["POLARMOMENTOFINERTIA"]


def get_qudt_quantity_kind_polarization_field() -> URIRef:
    """Returns the URI for QUDT quantity kind: Polarization Field (http://qudt.org/vocab/quantitykind/PolarizationField)"""
    return QUDT_QUANTITY_KIND["POLARIZATIONFIELD"]


def get_qudt_quantity_kind_population() -> URIRef:
    """Returns the URI for QUDT quantity kind: Population (http://qudt.org/vocab/quantitykind/Population)"""
    return QUDT_QUANTITY_KIND["POPULATION"]


def get_qudt_quantity_kind_positive_dimensionless_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Positive Dimensionless Ratio (http://qudt.org/vocab/quantitykind/PositiveDimensionlessRatio)"""
    return QUDT_QUANTITY_KIND["POSITIVEDIMENSIONLESSRATIO"]


def get_qudt_quantity_kind_positive_length() -> URIRef:
    """Returns the URI for QUDT quantity kind: Positive Length (http://qudt.org/vocab/quantitykind/PositiveLength)"""
    return QUDT_QUANTITY_KIND["POSITIVELENGTH"]


def get_qudt_quantity_kind_positive_plane_angle() -> URIRef:
    """Returns the URI for QUDT quantity kind: Positive Plane Angle (http://qudt.org/vocab/quantitykind/PositivePlaneAngle)"""
    return QUDT_QUANTITY_KIND["POSITIVEPLANEANGLE"]


def get_qudt_quantity_kind_potential_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: potential energy (http://qudt.org/vocab/quantitykind/PotentialEnergy)"""
    return QUDT_QUANTITY_KIND["POTENTIALENERGY"]


def get_qudt_quantity_kind_powerdensity() -> URIRef:
    """Returns the URI for QUDT quantity kind: PowerDensity (http://qudt.org/vocab/quantitykind/PowerDensity)"""
    return QUDT_QUANTITY_KIND["POWERDENSITY"]


def get_qudt_quantity_kind_power_per_volume() -> URIRef:
    """Returns the URI for QUDT quantity kind: Power per Volume (http://qudt.org/vocab/quantitykind/PowerPerVolume)"""
    return QUDT_QUANTITY_KIND["POWERPERVOLUME"]


def get_qudt_quantity_kind_power_factor() -> URIRef:
    """Returns the URI for QUDT quantity kind: power factor (http://qudt.org/vocab/quantitykind/PowerFactor)"""
    return QUDT_QUANTITY_KIND["POWERFACTOR"]


def get_qudt_quantity_kind_power_per_area_angle() -> URIRef:
    """Returns the URI for QUDT quantity kind: Power per Area Angle (http://qudt.org/vocab/quantitykind/PowerPerAreaAngle)"""
    return QUDT_QUANTITY_KIND["POWERPERAREAANGLE"]


def get_qudt_quantity_kind_poynting_vector() -> URIRef:
    """Returns the URI for QUDT quantity kind: Poynting vector (http://qudt.org/vocab/quantitykind/PoyntingVector)"""
    return QUDT_QUANTITY_KIND["POYNTINGVECTOR"]


def get_qudt_quantity_kind_pressure_burning_rate_constant() -> URIRef:
    """Returns the URI for QUDT quantity kind: Pressure Burning Rate Constant (http://qudt.org/vocab/quantitykind/PressureBurningRateConstant)"""
    return QUDT_QUANTITY_KIND["PRESSUREBURNINGRATECONSTANT"]


def get_qudt_quantity_kind_pressure_burning_rate_index() -> URIRef:
    """Returns the URI for QUDT quantity kind: Pressure Burning Rate Index (http://qudt.org/vocab/quantitykind/PressureBurningRateIndex)"""
    return QUDT_QUANTITY_KIND["PRESSUREBURNINGRATEINDEX"]


def get_qudt_quantity_kind_pressure_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Pressure Coefficient (http://qudt.org/vocab/quantitykind/PressureCoefficient)"""
    return QUDT_QUANTITY_KIND["PRESSURECOEFFICIENT"]


def get_qudt_quantity_kind_pressure_gradient() -> URIRef:
    """Returns the URI for QUDT quantity kind: pressure gradient (http://qudt.org/vocab/quantitykind/PressureGradient)"""
    return QUDT_QUANTITY_KIND["PRESSUREGRADIENT"]


def get_qudt_quantity_kind_pressure_in_relation_to_volume_flow_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: pressure in relation to volume flow rate (http://qudt.org/vocab/quantitykind/PressureInRelationToVolumeFlowRate)"""
    return QUDT_QUANTITY_KIND["PRESSUREINRELATIONTOVOLUMEFLOWRATE"]


def get_qudt_quantity_kind_pressure_loss_per_length() -> URIRef:
    """Returns the URI for QUDT quantity kind: Pressure Loss per Length (http://qudt.org/vocab/quantitykind/PressureLossPerLength)"""
    return QUDT_QUANTITY_KIND["PRESSURELOSSPERLENGTH"]


def get_qudt_quantity_kind_pressure_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Pressure Ratio (http://qudt.org/vocab/quantitykind/PressureRatio)"""
    return QUDT_QUANTITY_KIND["PRESSURERATIO"]


def get_qudt_quantity_kind_prevalence() -> URIRef:
    """Returns the URI for QUDT quantity kind: Prevalence (http://qudt.org/vocab/quantitykind/Prevalence)"""
    return QUDT_QUANTITY_KIND["PREVALENCE"]


def get_qudt_quantity_kind_propagation_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Propagation coefficient (http://qudt.org/vocab/quantitykind/PropagationCoefficient)"""
    return QUDT_QUANTITY_KIND["PROPAGATIONCOEFFICIENT"]


def get_qudt_quantity_kind_propellant_burn_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: Propellant Burn Rate (http://qudt.org/vocab/quantitykind/PropellantBurnRate)"""
    return QUDT_QUANTITY_KIND["PROPELLANTBURNRATE"]


def get_qudt_quantity_kind_propellant_mean_bulk_temperature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Propellant Mean Bulk Temperature (http://qudt.org/vocab/quantitykind/PropellantMeanBulkTemperature)"""
    return QUDT_QUANTITY_KIND["PROPELLANTMEANBULKTEMPERATURE"]


def get_qudt_quantity_kind_propellant_temperature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Propellant Temperature (http://qudt.org/vocab/quantitykind/PropellantTemperature)"""
    return QUDT_QUANTITY_KIND["PROPELLANTTEMPERATURE"]


def get_qudt_quantity_kind_quantity_of_light() -> URIRef:
    """Returns the URI for QUDT quantity kind: quantity of light (http://qudt.org/vocab/quantitykind/QuantityOfLight)"""
    return QUDT_QUANTITY_KIND["QUANTITYOFLIGHT"]


def get_qudt_quantity_kind_reserve_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: Reserve Mass (http://qudt.org/vocab/quantitykind/RESERVE-MASS)"""
    return QUDT_QUANTITY_KIND["RESERVE-MASS"]


def get_qudt_quantity_kind_rf_power_level() -> URIRef:
    """Returns the URI for QUDT quantity kind: RF-Power Level (http://qudt.org/vocab/quantitykind/RF-Power)"""
    return QUDT_QUANTITY_KIND["RF-POWER"]


def get_qudt_quantity_kind_signal_strength() -> URIRef:
    """Returns the URI for QUDT quantity kind: Signal Strength (http://qudt.org/vocab/quantitykind/SignalStrength)"""
    return QUDT_QUANTITY_KIND["SIGNALSTRENGTH"]


def get_qudt_quantity_kind_radial_distance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Radial Distance (http://qudt.org/vocab/quantitykind/RadialDistance)"""
    return QUDT_QUANTITY_KIND["RADIALDISTANCE"]


def get_qudt_quantity_kind_radiance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Radiance (http://qudt.org/vocab/quantitykind/Radiance)"""
    return QUDT_QUANTITY_KIND["RADIANCE"]


def get_qudt_quantity_kind_radiance_factor() -> URIRef:
    """Returns the URI for QUDT quantity kind: Radiance Factor (http://qudt.org/vocab/quantitykind/RadianceFactor)"""
    return QUDT_QUANTITY_KIND["RADIANCEFACTOR"]


def get_qudt_quantity_kind_radiant_emmitance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Radiant Emmitance (http://qudt.org/vocab/quantitykind/RadiantEmmitance)"""
    return QUDT_QUANTITY_KIND["RADIANTEMMITANCE"]


def get_qudt_quantity_kind_radiant_energy_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Radiant Energy Density (http://qudt.org/vocab/quantitykind/RadiantEnergyDensity)"""
    return QUDT_QUANTITY_KIND["RADIANTENERGYDENSITY"]


def get_qudt_quantity_kind_radiant_energy_exposure() -> URIRef:
    """Returns the URI for QUDT quantity kind: radiant energy exposure (http://qudt.org/vocab/quantitykind/RadiantEnergyExposure)"""
    return QUDT_QUANTITY_KIND["RADIANTENERGYEXPOSURE"]


def get_qudt_quantity_kind_radiant_exposure() -> URIRef:
    """Returns the URI for QUDT quantity kind: Radiant Exposure (http://qudt.org/vocab/quantitykind/RadiantExposure)"""
    return QUDT_QUANTITY_KIND["RADIANTEXPOSURE"]


def get_qudt_quantity_kind_radiant_fluence() -> URIRef:
    """Returns the URI for QUDT quantity kind: Radiant Fluence (http://qudt.org/vocab/quantitykind/RadiantFluence)"""
    return QUDT_QUANTITY_KIND["RADIANTFLUENCE"]


def get_qudt_quantity_kind_radiant_fluence_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: Radiant Fluence Rate (http://qudt.org/vocab/quantitykind/RadiantFluenceRate)"""
    return QUDT_QUANTITY_KIND["RADIANTFLUENCERATE"]


def get_qudt_quantity_kind_radiant_flux() -> URIRef:
    """Returns the URI for QUDT quantity kind: radiant flux (http://qudt.org/vocab/quantitykind/RadiantFlux)"""
    return QUDT_QUANTITY_KIND["RADIANTFLUX"]


def get_qudt_quantity_kind_radiative_heat_transfer() -> URIRef:
    """Returns the URI for QUDT quantity kind: Radiative Heat Transfer (http://qudt.org/vocab/quantitykind/RadiativeHeatTransfer)"""
    return QUDT_QUANTITY_KIND["RADIATIVEHEATTRANSFER"]


def get_qudt_quantity_kind_radioactive_decay() -> URIRef:
    """Returns the URI for QUDT quantity kind: radioactive decay (http://qudt.org/vocab/quantitykind/RadioactiveDecay)"""
    return QUDT_QUANTITY_KIND["RADIOACTIVEDECAY"]


def get_qudt_quantity_kind_radiosity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Radiosity (http://qudt.org/vocab/quantitykind/Radiosity)"""
    return QUDT_QUANTITY_KIND["RADIOSITY"]


def get_qudt_quantity_kind_radius_of_curvature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Radius of Curvature (http://qudt.org/vocab/quantitykind/RadiusOfCurvature)"""
    return QUDT_QUANTITY_KIND["RADIUSOFCURVATURE"]


def get_qudt_quantity_kind_rankine_temperature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Rankine temperature (http://qudt.org/vocab/quantitykind/RankineTemperature)"""
    return QUDT_QUANTITY_KIND["RANKINETEMPERATURE"]


def get_qudt_quantity_kind_rate_of_change() -> URIRef:
    """Returns the URI for QUDT quantity kind: Rate of Change (http://qudt.org/vocab/quantitykind/RateOfChange)"""
    return QUDT_QUANTITY_KIND["RATEOFCHANGE"]


def get_qudt_quantity_kind_rate_of_rise_of_voltage() -> URIRef:
    """Returns the URI for QUDT quantity kind: rate of rise of voltage (http://qudt.org/vocab/quantitykind/RateOfRiseOfVoltage)"""
    return QUDT_QUANTITY_KIND["RATEOFRISEOFVOLTAGE"]


def get_qudt_quantity_kind_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: ratio (http://qudt.org/vocab/quantitykind/Ratio)"""
    return QUDT_QUANTITY_KIND["RATIO"]


def get_qudt_quantity_kind_ratio_of_specific_heat_capacities() -> URIRef:
    """Returns the URI for QUDT quantity kind: Ratio of Specific Heat Capacities (http://qudt.org/vocab/quantitykind/RatioOfSpecificHeatCapacities)"""
    return QUDT_QUANTITY_KIND["RATIOOFSPECIFICHEATCAPACITIES"]


def get_qudt_quantity_kind_reaction_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Reaction Energy (http://qudt.org/vocab/quantitykind/ReactionEnergy)"""
    return QUDT_QUANTITY_KIND["REACTIONENERGY"]


def get_qudt_quantity_kind_reactive_charge() -> URIRef:
    """Returns the URI for QUDT quantity kind: Reactive Charge (http://qudt.org/vocab/quantitykind/ReactiveCharge)"""
    return QUDT_QUANTITY_KIND["REACTIVECHARGE"]


def get_qudt_quantity_kind_reactive_power() -> URIRef:
    """Returns the URI for QUDT quantity kind: reactive power (http://qudt.org/vocab/quantitykind/ReactivePower)"""
    return QUDT_QUANTITY_KIND["REACTIVEPOWER"]


def get_qudt_quantity_kind_reactivity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Reactivity (http://qudt.org/vocab/quantitykind/Reactivity)"""
    return QUDT_QUANTITY_KIND["REACTIVITY"]


def get_qudt_quantity_kind_reactor_time_constant() -> URIRef:
    """Returns the URI for QUDT quantity kind: Reactor Time Constant (http://qudt.org/vocab/quantitykind/ReactorTimeConstant)"""
    return QUDT_QUANTITY_KIND["REACTORTIMECONSTANT"]


def get_qudt_quantity_kind_recombination_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Recombination Coefficient (http://qudt.org/vocab/quantitykind/RecombinationCoefficient)"""
    return QUDT_QUANTITY_KIND["RECOMBINATIONCOEFFICIENT"]


def get_qudt_quantity_kind_reflectance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Reflectance (http://qudt.org/vocab/quantitykind/Reflectance)"""
    return QUDT_QUANTITY_KIND["REFLECTANCE"]


def get_qudt_quantity_kind_reflectance_factor() -> URIRef:
    """Returns the URI for QUDT quantity kind: Reflectance Factor (http://qudt.org/vocab/quantitykind/ReflectanceFactor)"""
    return QUDT_QUANTITY_KIND["REFLECTANCEFACTOR"]


def get_qudt_quantity_kind_reflectivity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Reflectivity (http://qudt.org/vocab/quantitykind/Reflectivity)"""
    return QUDT_QUANTITY_KIND["REFLECTIVITY"]


def get_qudt_quantity_kind_refractive_index() -> URIRef:
    """Returns the URI for QUDT quantity kind: refractive index (http://qudt.org/vocab/quantitykind/RefractiveIndex)"""
    return QUDT_QUANTITY_KIND["REFRACTIVEINDEX"]


def get_qudt_quantity_kind_relative_atomic_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: Relative Atomic Mass (http://qudt.org/vocab/quantitykind/RelativeAtomicMass)"""
    return QUDT_QUANTITY_KIND["RELATIVEATOMICMASS"]


def get_qudt_quantity_kind_relative_partial_pressure() -> URIRef:
    """Returns the URI for QUDT quantity kind: Relative Partial Pressure (http://qudt.org/vocab/quantitykind/RelativePartialPressure)"""
    return QUDT_QUANTITY_KIND["RELATIVEPARTIALPRESSURE"]


def get_qudt_quantity_kind_relative_mass_concentration_of_vapour() -> URIRef:
    """Returns the URI for QUDT quantity kind: Relative Mass Concentration of Vapour (http://qudt.org/vocab/quantitykind/RelativeMassConcentrationOfVapour)"""
    return QUDT_QUANTITY_KIND["RELATIVEMASSCONCENTRATIONOFVAPOUR"]


def get_qudt_quantity_kind_relative_mass_defect() -> URIRef:
    """Returns the URI for QUDT quantity kind: Relative Mass Defect (http://qudt.org/vocab/quantitykind/RelativeMassDefect)"""
    return QUDT_QUANTITY_KIND["RELATIVEMASSDEFECT"]


def get_qudt_quantity_kind_relative_mass_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Relative Mass Density (http://qudt.org/vocab/quantitykind/RelativeMassDensity)"""
    return QUDT_QUANTITY_KIND["RELATIVEMASSDENSITY"]


def get_qudt_quantity_kind_relative_mass_excess() -> URIRef:
    """Returns the URI for QUDT quantity kind: Relative Mass Excess (http://qudt.org/vocab/quantitykind/RelativeMassExcess)"""
    return QUDT_QUANTITY_KIND["RELATIVEMASSEXCESS"]


def get_qudt_quantity_kind_relative_mass_ratio_of_vapour() -> URIRef:
    """Returns the URI for QUDT quantity kind: Relative Mass Ratio of Vapour (http://qudt.org/vocab/quantitykind/RelativeMassRatioOfVapour)"""
    return QUDT_QUANTITY_KIND["RELATIVEMASSRATIOOFVAPOUR"]


def get_qudt_quantity_kind_relative_molecular_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: Relative Molecular Mass (http://qudt.org/vocab/quantitykind/RelativeMolecularMass)"""
    return QUDT_QUANTITY_KIND["RELATIVEMOLECULARMASS"]


def get_qudt_quantity_kind_relative_pressure_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Relative Pressure Coefficient (http://qudt.org/vocab/quantitykind/RelativePressureCoefficient)"""
    return QUDT_QUANTITY_KIND["RELATIVEPRESSURECOEFFICIENT"]


def get_qudt_quantity_kind_relaxation_time() -> URIRef:
    """Returns the URI for QUDT quantity kind: Relaxation TIme (http://qudt.org/vocab/quantitykind/RelaxationTIme)"""
    return QUDT_QUANTITY_KIND["RELAXATIONTIME"]


def get_qudt_quantity_kind_repetency() -> URIRef:
    """Returns the URI for QUDT quantity kind: repetency (http://qudt.org/vocab/quantitykind/Repetency)"""
    return QUDT_QUANTITY_KIND["REPETENCY"]


def get_qudt_quantity_kind_residual_resistivity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Residual Resistivity (http://qudt.org/vocab/quantitykind/ResidualResistivity)"""
    return QUDT_QUANTITY_KIND["RESIDUALRESISTIVITY"]


def get_qudt_quantity_kind_resistance_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Resistance Ratio (http://qudt.org/vocab/quantitykind/ResistanceRatio)"""
    return QUDT_QUANTITY_KIND["RESISTANCERATIO"]


def get_qudt_quantity_kind_resistivity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Resistivity (http://qudt.org/vocab/quantitykind/Resistivity)"""
    return QUDT_QUANTITY_KIND["RESISTIVITY"]


def get_qudt_quantity_kind_resonance_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Resonance Energy (http://qudt.org/vocab/quantitykind/ResonanceEnergy)"""
    return QUDT_QUANTITY_KIND["RESONANCEENERGY"]


def get_qudt_quantity_kind_resonance_escape_probability() -> URIRef:
    """Returns the URI for QUDT quantity kind: Resonance Escape Probability (http://qudt.org/vocab/quantitykind/ResonanceEscapeProbability)"""
    return QUDT_QUANTITY_KIND["RESONANCEESCAPEPROBABILITY"]


def get_qudt_quantity_kind_resonance_escape_probability_for_fission() -> URIRef:
    """Returns the URI for QUDT quantity kind: Resonance Escape Probability For Fission (http://qudt.org/vocab/quantitykind/ResonanceEscapeProbabilityForFission)"""
    return QUDT_QUANTITY_KIND["RESONANCEESCAPEPROBABILITYFORFISSION"]


def get_qudt_quantity_kind_respiratory_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: Respiratory Rate (http://qudt.org/vocab/quantitykind/RespiratoryRate)"""
    return QUDT_QUANTITY_KIND["RESPIRATORYRATE"]


def get_qudt_quantity_kind_rest_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Rest Energy (http://qudt.org/vocab/quantitykind/RestEnergy)"""
    return QUDT_QUANTITY_KIND["RESTENERGY"]


def get_qudt_quantity_kind_rest_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: rest mass (http://qudt.org/vocab/quantitykind/RestMass)"""
    return QUDT_QUANTITY_KIND["RESTMASS"]


def get_qudt_quantity_kind_reverberation_time() -> URIRef:
    """Returns the URI for QUDT quantity kind: Reverberation Time (http://qudt.org/vocab/quantitykind/ReverberationTime)"""
    return QUDT_QUANTITY_KIND["REVERBERATIONTIME"]


def get_qudt_quantity_kind_reynolds_number() -> URIRef:
    """Returns the URI for QUDT quantity kind: Reynolds Number (http://qudt.org/vocab/quantitykind/ReynoldsNumber)"""
    return QUDT_QUANTITY_KIND["REYNOLDSNUMBER"]


def get_qudt_quantity_kind_richardson_constant() -> URIRef:
    """Returns the URI for QUDT quantity kind: Richardson Constant (http://qudt.org/vocab/quantitykind/RichardsonConstant)"""
    return QUDT_QUANTITY_KIND["RICHARDSONCONSTANT"]


def get_qudt_quantity_kind_rocket_atmospheric_transverse_force() -> URIRef:
    """Returns the URI for QUDT quantity kind: Rocket Atmospheric Transverse Force (http://qudt.org/vocab/quantitykind/RocketAtmosphericTransverseForce)"""
    return QUDT_QUANTITY_KIND["ROCKETATMOSPHERICTRANSVERSEFORCE"]


def get_qudt_quantity_kind_rotary_translatory_motion_conversion() -> URIRef:
    """Returns the URI for QUDT quantity kind: rotary-translatory motion conversion (http://qudt.org/vocab/quantitykind/Rotary-TranslatoryMotionConversion)"""
    return QUDT_QUANTITY_KIND["ROTARY-TRANSLATORYMOTIONCONVERSION"]


def get_qudt_quantity_kind_rotational_stiffness() -> URIRef:
    """Returns the URI for QUDT quantity kind: Rotational Stiffness (http://qudt.org/vocab/quantitykind/RotationalStiffness)"""
    return QUDT_QUANTITY_KIND["ROTATIONALSTIFFNESS"]


def get_qudt_quantity_kind_torque_per_angle() -> URIRef:
    """Returns the URI for QUDT quantity kind: Torque per Angle (http://qudt.org/vocab/quantitykind/TorquePerAngle)"""
    return QUDT_QUANTITY_KIND["TORQUEPERANGLE"]


def get_qudt_quantity_kind_scalar_magnetic_potential() -> URIRef:
    """Returns the URI for QUDT quantity kind: Scalar Magnetic Potential (http://qudt.org/vocab/quantitykind/ScalarMagneticPotential)"""
    return QUDT_QUANTITY_KIND["SCALARMAGNETICPOTENTIAL"]


def get_qudt_quantity_kind_second_moment_of_area() -> URIRef:
    """Returns the URI for QUDT quantity kind: second moment of area (http://qudt.org/vocab/quantitykind/SecondMomentOfArea)"""
    return QUDT_QUANTITY_KIND["SECONDMOMENTOFAREA"]


def get_qudt_quantity_kind_second_polar_moment_of_area() -> URIRef:
    """Returns the URI for QUDT quantity kind: Second Polar Moment of Area (http://qudt.org/vocab/quantitykind/SecondPolarMomentOfArea)"""
    return QUDT_QUANTITY_KIND["SECONDPOLARMOMENTOFAREA"]


def get_qudt_quantity_kind_second_stage_mass_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Second Stage Mass Ratio (http://qudt.org/vocab/quantitykind/SecondStageMassRatio)"""
    return QUDT_QUANTITY_KIND["SECONDSTAGEMASSRATIO"]


def get_qudt_quantity_kind_section_area_integral() -> URIRef:
    """Returns the URI for QUDT quantity kind: Section Area Integral (http://qudt.org/vocab/quantitykind/SectionAreaIntegral)"""
    return QUDT_QUANTITY_KIND["SECTIONAREAINTEGRAL"]


def get_qudt_quantity_kind_section_modulus() -> URIRef:
    """Returns the URI for QUDT quantity kind: Section Modulus (http://qudt.org/vocab/quantitykind/SectionModulus)"""
    return QUDT_QUANTITY_KIND["SECTIONMODULUS"]


def get_qudt_quantity_kind_seebeck_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Seebeck Coefficient (http://qudt.org/vocab/quantitykind/SeebeckCoefficient)"""
    return QUDT_QUANTITY_KIND["SEEBECKCOEFFICIENT"]


def get_qudt_quantity_kind_serum_level() -> URIRef:
    """Returns the URI for QUDT quantity kind: Serum Level (http://qudt.org/vocab/quantitykind/SerumLevel)"""
    return QUDT_QUANTITY_KIND["SERUMLEVEL"]


def get_qudt_quantity_kind_serum_or_plasma_level() -> URIRef:
    """Returns the URI for QUDT quantity kind: Serum or Plasma Level (http://qudt.org/vocab/quantitykind/SerumOrPlasmaLevel)"""
    return QUDT_QUANTITY_KIND["SERUMORPLASMALEVEL"]


def get_qudt_quantity_kind_service_factor() -> URIRef:
    """Returns the URI for QUDT quantity kind: Service Factor (http://qudt.org/vocab/quantitykind/ServiceFactor)"""
    return QUDT_QUANTITY_KIND["SERVICEFACTOR"]


def get_qudt_quantity_kind_shannon_diversity_index() -> URIRef:
    """Returns the URI for QUDT quantity kind: Shannon Diversity Index (http://qudt.org/vocab/quantitykind/ShannonDiversityIndex)"""
    return QUDT_QUANTITY_KIND["SHANNONDIVERSITYINDEX"]


def get_qudt_quantity_kind_shear_modulus() -> URIRef:
    """Returns the URI for QUDT quantity kind: Shear Modulus (http://qudt.org/vocab/quantitykind/ShearModulus)"""
    return QUDT_QUANTITY_KIND["SHEARMODULUS"]


def get_qudt_quantity_kind_shear_strain() -> URIRef:
    """Returns the URI for QUDT quantity kind: Shear Strain (http://qudt.org/vocab/quantitykind/ShearStrain)"""
    return QUDT_QUANTITY_KIND["SHEARSTRAIN"]


def get_qudt_quantity_kind_shear_stress() -> URIRef:
    """Returns the URI for QUDT quantity kind: Shear Stress (http://qudt.org/vocab/quantitykind/ShearStress)"""
    return QUDT_QUANTITY_KIND["SHEARSTRESS"]


def get_qudt_quantity_kind_short_range_order_parameter() -> URIRef:
    """Returns the URI for QUDT quantity kind: Short-Range Order Parameter (http://qudt.org/vocab/quantitykind/Short-RangeOrderParameter)"""
    return QUDT_QUANTITY_KIND["SHORT-RANGEORDERPARAMETER"]


def get_qudt_quantity_kind_signal_detection_threshold() -> URIRef:
    """Returns the URI for QUDT quantity kind: Signal Detection Threshold (http://qudt.org/vocab/quantitykind/SignalDetectionThreshold)"""
    return QUDT_QUANTITY_KIND["SIGNALDETECTIONTHRESHOLD"]


def get_qudt_quantity_kind_single_stage_launcher_mass_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Single Stage Launcher Mass Ratio (http://qudt.org/vocab/quantitykind/SingleStageLauncherMassRatio)"""
    return QUDT_QUANTITY_KIND["SINGLESTAGELAUNCHERMASSRATIO"]


def get_qudt_quantity_kind_slowing_down_area() -> URIRef:
    """Returns the URI for QUDT quantity kind: Slowing-Down Area (http://qudt.org/vocab/quantitykind/Slowing-DownArea)"""
    return QUDT_QUANTITY_KIND["SLOWING-DOWNAREA"]


def get_qudt_quantity_kind_slowing_down_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Slowing-Down Density (http://qudt.org/vocab/quantitykind/Slowing-DownDensity)"""
    return QUDT_QUANTITY_KIND["SLOWING-DOWNDENSITY"]


def get_qudt_quantity_kind_slowing_down_length() -> URIRef:
    """Returns the URI for QUDT quantity kind: Slowing-Down Length (http://qudt.org/vocab/quantitykind/Slowing-DownLength)"""
    return QUDT_QUANTITY_KIND["SLOWING-DOWNLENGTH"]


def get_qudt_quantity_kind_soil_adsorption_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Soil Adsorption Coefficient (http://qudt.org/vocab/quantitykind/SoilAdsorptionCoefficient)"""
    return QUDT_QUANTITY_KIND["SOILADSORPTIONCOEFFICIENT"]


def get_qudt_quantity_kind_solid_angle() -> URIRef:
    """Returns the URI for QUDT quantity kind: solid angle (http://qudt.org/vocab/quantitykind/SolidAngle)"""
    return QUDT_QUANTITY_KIND["SOLIDANGLE"]


def get_qudt_quantity_kind_diffusion_length_solid_state_physics() -> URIRef:
    """Returns the URI for QUDT quantity kind: Diffusion Length (Solid State Physics) (http://qudt.org/vocab/quantitykind/SolidStateDiffusionLength)"""
    return QUDT_QUANTITY_KIND["SOLIDSTATEDIFFUSIONLENGTH"]


def get_qudt_quantity_kind_water_solubility() -> URIRef:
    """Returns the URI for QUDT quantity kind: Water Solubility (http://qudt.org/vocab/quantitykind/Solubility_Water)"""
    return QUDT_QUANTITY_KIND["SOLUBILITY_WATER"]


def get_qudt_quantity_kind_water_solubility() -> URIRef:
    """Returns the URI for QUDT quantity kind: Water Solubility (http://qudt.org/vocab/quantitykind/WaterSolubility)"""
    return QUDT_QUANTITY_KIND["WATERSOLUBILITY"]


def get_qudt_quantity_kind_sound_energy_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Sound energy density (http://qudt.org/vocab/quantitykind/SoundEnergyDensity)"""
    return QUDT_QUANTITY_KIND["SOUNDENERGYDENSITY"]


def get_qudt_quantity_kind_sound_exposure() -> URIRef:
    """Returns the URI for QUDT quantity kind: Sound exposure (http://qudt.org/vocab/quantitykind/SoundExposure)"""
    return QUDT_QUANTITY_KIND["SOUNDEXPOSURE"]


def get_qudt_quantity_kind_sound_exposure_level() -> URIRef:
    """Returns the URI for QUDT quantity kind: Sound exposure level (http://qudt.org/vocab/quantitykind/SoundExposureLevel)"""
    return QUDT_QUANTITY_KIND["SOUNDEXPOSURELEVEL"]


def get_qudt_quantity_kind_sound_intensity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Sound intensity (http://qudt.org/vocab/quantitykind/SoundIntensity)"""
    return QUDT_QUANTITY_KIND["SOUNDINTENSITY"]


def get_qudt_quantity_kind_sound_particle_acceleration() -> URIRef:
    """Returns the URI for QUDT quantity kind: Sound particle acceleration (http://qudt.org/vocab/quantitykind/SoundParticleAcceleration)"""
    return QUDT_QUANTITY_KIND["SOUNDPARTICLEACCELERATION"]


def get_qudt_quantity_kind_sound_particle_displacement() -> URIRef:
    """Returns the URI for QUDT quantity kind: Sound Particle Displacement (http://qudt.org/vocab/quantitykind/SoundParticleDisplacement)"""
    return QUDT_QUANTITY_KIND["SOUNDPARTICLEDISPLACEMENT"]


def get_qudt_quantity_kind_sound_particle_velocity() -> URIRef:
    """Returns the URI for QUDT quantity kind: sound particle velocity (http://qudt.org/vocab/quantitykind/SoundParticleVelocity)"""
    return QUDT_QUANTITY_KIND["SOUNDPARTICLEVELOCITY"]


def get_qudt_quantity_kind_sound_power() -> URIRef:
    """Returns the URI for QUDT quantity kind: sound power (http://qudt.org/vocab/quantitykind/SoundPower)"""
    return QUDT_QUANTITY_KIND["SOUNDPOWER"]


def get_qudt_quantity_kind_sound_pressure() -> URIRef:
    """Returns the URI for QUDT quantity kind: Sound pressure (http://qudt.org/vocab/quantitykind/SoundPressure)"""
    return QUDT_QUANTITY_KIND["SOUNDPRESSURE"]


def get_qudt_quantity_kind_sound_pressure_level() -> URIRef:
    """Returns the URI for QUDT quantity kind: sound pressure level (http://qudt.org/vocab/quantitykind/SoundPressureLevel)"""
    return QUDT_QUANTITY_KIND["SOUNDPRESSURELEVEL"]


def get_qudt_quantity_kind_sound_reduction_index() -> URIRef:
    """Returns the URI for QUDT quantity kind: Sound reduction index (http://qudt.org/vocab/quantitykind/SoundReductionIndex)"""
    return QUDT_QUANTITY_KIND["SOUNDREDUCTIONINDEX"]


def get_qudt_quantity_kind_sound_volume_velocity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Sound volume velocity (http://qudt.org/vocab/quantitykind/SoundVolumeVelocity)"""
    return QUDT_QUANTITY_KIND["SOUNDVOLUMEVELOCITY"]


def get_qudt_quantity_kind_source_voltage() -> URIRef:
    """Returns the URI for QUDT quantity kind: Source Voltage (http://qudt.org/vocab/quantitykind/SourceVoltage)"""
    return QUDT_QUANTITY_KIND["SOURCEVOLTAGE"]


def get_qudt_quantity_kind_source_voltage_between_substances() -> URIRef:
    """Returns the URI for QUDT quantity kind: Source Voltage Between Substances (http://qudt.org/vocab/quantitykind/SourceVoltageBetweenSubstances)"""
    return QUDT_QUANTITY_KIND["SOURCEVOLTAGEBETWEENSUBSTANCES"]


def get_qudt_quantity_kind_spatial_summation_function() -> URIRef:
    """Returns the URI for QUDT quantity kind: Spatial Summation Function (http://qudt.org/vocab/quantitykind/SpatialSummationFunction)"""
    return QUDT_QUANTITY_KIND["SPATIALSUMMATIONFUNCTION"]


def get_qudt_quantity_kind_specific_acoustic_impedance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Specific Acoustic Impedance (http://qudt.org/vocab/quantitykind/SpecificAcousticImpedance)"""
    return QUDT_QUANTITY_KIND["SPECIFICACOUSTICIMPEDANCE"]


def get_qudt_quantity_kind_specific_activity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Specific Activity (http://qudt.org/vocab/quantitykind/SpecificActivity)"""
    return QUDT_QUANTITY_KIND["SPECIFICACTIVITY"]


def get_qudt_quantity_kind_specific_energy_imparted() -> URIRef:
    """Returns the URI for QUDT quantity kind: Specific Energy Imparted (http://qudt.org/vocab/quantitykind/SpecificEnergyImparted)"""
    return QUDT_QUANTITY_KIND["SPECIFICENERGYIMPARTED"]


def get_qudt_quantity_kind_specific_entropy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Specific Entropy (http://qudt.org/vocab/quantitykind/SpecificEntropy)"""
    return QUDT_QUANTITY_KIND["SPECIFICENTROPY"]


def get_qudt_quantity_kind_specific_heat_capacity_at_constant_pressure() -> URIRef:
    """Returns the URI for QUDT quantity kind: Specific heat capacity at constant pressure (http://qudt.org/vocab/quantitykind/SpecificHeatCapacityAtConstantPressure)"""
    return QUDT_QUANTITY_KIND["SPECIFICHEATCAPACITYATCONSTANTPRESSURE"]


def get_qudt_quantity_kind_specific_heat_capacity_at_constant_volume() -> URIRef:
    """Returns the URI for QUDT quantity kind: Specific heat capacity at constant volume (http://qudt.org/vocab/quantitykind/SpecificHeatCapacityAtConstantVolume)"""
    return QUDT_QUANTITY_KIND["SPECIFICHEATCAPACITYATCONSTANTVOLUME"]


def get_qudt_quantity_kind_specific_heat_capacity_at_saturation() -> URIRef:
    """Returns the URI for QUDT quantity kind: Specific Heat Capacity at Saturation (http://qudt.org/vocab/quantitykind/SpecificHeatCapacityAtSaturation)"""
    return QUDT_QUANTITY_KIND["SPECIFICHEATCAPACITYATSATURATION"]


def get_qudt_quantity_kind_specific_heats_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Specific Heats Ratio (http://qudt.org/vocab/quantitykind/SpecificHeatsRatio)"""
    return QUDT_QUANTITY_KIND["SPECIFICHEATSRATIO"]


def get_qudt_quantity_kind_specific_impulse_by_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: Specific Impulse by Mass (http://qudt.org/vocab/quantitykind/SpecificImpulseByMass)"""
    return QUDT_QUANTITY_KIND["SPECIFICIMPULSEBYMASS"]


def get_qudt_quantity_kind_specific_impulse_by_weight() -> URIRef:
    """Returns the URI for QUDT quantity kind: Specific Impulse by Weight (http://qudt.org/vocab/quantitykind/SpecificImpulseByWeight)"""
    return QUDT_QUANTITY_KIND["SPECIFICIMPULSEBYWEIGHT"]


def get_qudt_quantity_kind_specific_modulus() -> URIRef:
    """Returns the URI for QUDT quantity kind: Specific Modulus (http://qudt.org/vocab/quantitykind/SpecificModulus)"""
    return QUDT_QUANTITY_KIND["SPECIFICMODULUS"]


def get_qudt_quantity_kind_specific_optical_rotational_ability() -> URIRef:
    """Returns the URI for QUDT quantity kind: specific optical rotational ability (http://qudt.org/vocab/quantitykind/SpecificOpticalRotationalAbility)"""
    return QUDT_QUANTITY_KIND["SPECIFICOPTICALROTATIONALABILITY"]


def get_qudt_quantity_kind_specific_optical_rotatory_power() -> URIRef:
    """Returns the URI for QUDT quantity kind: Specific Optical Rotatory Power (http://qudt.org/vocab/quantitykind/SpecificOpticalRotatoryPower)"""
    return QUDT_QUANTITY_KIND["SPECIFICOPTICALROTATORYPOWER"]


def get_qudt_quantity_kind_specific_surface_area() -> URIRef:
    """Returns the URI for QUDT quantity kind: Specific Surface Area (http://qudt.org/vocab/quantitykind/SpecificSurfaceArea)"""
    return QUDT_QUANTITY_KIND["SPECIFICSURFACEAREA"]


def get_qudt_quantity_kind_specific_thrust() -> URIRef:
    """Returns the URI for QUDT quantity kind: Specific thrust (http://qudt.org/vocab/quantitykind/SpecificThrust)"""
    return QUDT_QUANTITY_KIND["SPECIFICTHRUST"]


def get_qudt_quantity_kind_specific_weight() -> URIRef:
    """Returns the URI for QUDT quantity kind: specific weight (http://qudt.org/vocab/quantitykind/SpecificWeight)"""
    return QUDT_QUANTITY_KIND["SPECIFICWEIGHT"]


def get_qudt_quantity_kind_spectral_angular_cross_section() -> URIRef:
    """Returns the URI for QUDT quantity kind: Spectral Angular Cross-section (http://qudt.org/vocab/quantitykind/SpectralAngularCrossSection)"""
    return QUDT_QUANTITY_KIND["SPECTRALANGULARCROSSSECTION"]


def get_qudt_quantity_kind_spectral_density_of_vibrational_modes() -> URIRef:
    """Returns the URI for QUDT quantity kind: spectral density of vibrational modes (http://qudt.org/vocab/quantitykind/SpectralDensityOfVibrationalModes)"""
    return QUDT_QUANTITY_KIND["SPECTRALDENSITYOFVIBRATIONALMODES"]


def get_qudt_quantity_kind_spectral_luminous_efficiency() -> URIRef:
    """Returns the URI for QUDT quantity kind: Spectral Luminous Efficiency (http://qudt.org/vocab/quantitykind/SpectralLuminousEfficiency)"""
    return QUDT_QUANTITY_KIND["SPECTRALLUMINOUSEFFICIENCY"]


def get_qudt_quantity_kind_measurement_unit_of_spectral_radiance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Measurement Unit of Spectral Radiance (http://qudt.org/vocab/quantitykind/SpectralRadiance)"""
    return QUDT_QUANTITY_KIND["SPECTRALRADIANCE"]


def get_qudt_quantity_kind_spectral_radiant_energy_density_in_terms_of_wavelength() -> (
    URIRef
):
    """Returns the URI for QUDT quantity kind: spectral radiant energy density in terms of wavelength (http://qudt.org/vocab/quantitykind/SpectralRadiantEnergyDensityInTermsOfWavelength)"""
    return QUDT_QUANTITY_KIND["SPECTRALRADIANTENERGYDENSITYINTERMSOFWAVELENGTH"]


def get_qudt_quantity_kind_speed_of_light() -> URIRef:
    """Returns the URI for QUDT quantity kind: speed of light (http://qudt.org/vocab/quantitykind/SpeedOfLight)"""
    return QUDT_QUANTITY_KIND["SPEEDOFLIGHT"]


def get_qudt_quantity_kind_speed_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Speed Ratio (http://qudt.org/vocab/quantitykind/SpeedRatio)"""
    return QUDT_QUANTITY_KIND["SPEEDRATIO"]


def get_qudt_quantity_kind_illuminance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Illuminance (http://qudt.org/vocab/quantitykind/SphericalIlluminance)"""
    return QUDT_QUANTITY_KIND["SPHERICALILLUMINANCE"]


def get_qudt_quantity_kind_spin() -> URIRef:
    """Returns the URI for QUDT quantity kind: spin (http://qudt.org/vocab/quantitykind/Spin)"""
    return QUDT_QUANTITY_KIND["SPIN"]


def get_qudt_quantity_kind_stage_propellant_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: Stage Propellant Mass (http://qudt.org/vocab/quantitykind/StagePropellantMass)"""
    return QUDT_QUANTITY_KIND["STAGEPROPELLANTMASS"]


def get_qudt_quantity_kind_stage_structure_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: Stage Structure Mass (http://qudt.org/vocab/quantitykind/StageStructuralMass)"""
    return QUDT_QUANTITY_KIND["STAGESTRUCTURALMASS"]


def get_qudt_quantity_kind_standard_absolute_activity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Standard Absolute Activity (http://qudt.org/vocab/quantitykind/StandardAbsoluteActivity)"""
    return QUDT_QUANTITY_KIND["STANDARDABSOLUTEACTIVITY"]


def get_qudt_quantity_kind_standard_chemical_potential() -> URIRef:
    """Returns the URI for QUDT quantity kind: Standard Chemical Potential (http://qudt.org/vocab/quantitykind/StandardChemicalPotential)"""
    return QUDT_QUANTITY_KIND["STANDARDCHEMICALPOTENTIAL"]


def get_qudt_quantity_kind_state_density_as_expression_of_angular_frequency() -> URIRef:
    """Returns the URI for QUDT quantity kind: state density as expression of angular frequency) (http://qudt.org/vocab/quantitykind/StateDensityAsExpressionOfAngularFrequency)"""
    return QUDT_QUANTITY_KIND["STATEDENSITYASEXPRESSIONOFANGULARFREQUENCY"]


def get_qudt_quantity_kind_state_of_charge() -> URIRef:
    """Returns the URI for QUDT quantity kind: State of charge (http://qudt.org/vocab/quantitykind/StateOfCharge)"""
    return QUDT_QUANTITY_KIND["STATEOFCHARGE"]


def get_qudt_quantity_kind_static_friction() -> URIRef:
    """Returns the URI for QUDT quantity kind: Static Friction (http://qudt.org/vocab/quantitykind/StaticFriction)"""
    return QUDT_QUANTITY_KIND["STATICFRICTION"]


def get_qudt_quantity_kind_static_friction_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Static Friction Coefficient (http://qudt.org/vocab/quantitykind/StaticFrictionCoefficient)"""
    return QUDT_QUANTITY_KIND["STATICFRICTIONCOEFFICIENT"]


def get_qudt_quantity_kind_static_pressure() -> URIRef:
    """Returns the URI for QUDT quantity kind: Static pressure (http://qudt.org/vocab/quantitykind/StaticPressure)"""
    return QUDT_QUANTITY_KIND["STATICPRESSURE"]


def get_qudt_quantity_kind_statistical_weight() -> URIRef:
    """Returns the URI for QUDT quantity kind: Statistical Weight (http://qudt.org/vocab/quantitykind/StatisticalWeight)"""
    return QUDT_QUANTITY_KIND["STATISTICALWEIGHT"]


def get_qudt_quantity_kind_stoichiometric_number() -> URIRef:
    """Returns the URI for QUDT quantity kind: Stoichiometric Number (http://qudt.org/vocab/quantitykind/StoichiometricNumber)"""
    return QUDT_QUANTITY_KIND["STOICHIOMETRICNUMBER"]


def get_qudt_quantity_kind_strain_energy_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Strain Energy Density (http://qudt.org/vocab/quantitykind/StrainEnergyDensity)"""
    return QUDT_QUANTITY_KIND["STRAINENERGYDENSITY"]


def get_qudt_quantity_kind_strain_energy_release_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: Strain Energy Release Rate (http://qudt.org/vocab/quantitykind/StrainEnergyReleaseRate)"""
    return QUDT_QUANTITY_KIND["STRAINENERGYRELEASERATE"]


def get_qudt_quantity_kind_stress_optic_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Stress-Optic Coefficient (http://qudt.org/vocab/quantitykind/StressOpticCoefficient)"""
    return QUDT_QUANTITY_KIND["STRESSOPTICCOEFFICIENT"]


def get_qudt_quantity_kind_structural_efficiency() -> URIRef:
    """Returns the URI for QUDT quantity kind: Structural Efficiency (http://qudt.org/vocab/quantitykind/StructuralEfficiency)"""
    return QUDT_QUANTITY_KIND["STRUCTURALEFFICIENCY"]


def get_qudt_quantity_kind_structure_factor() -> URIRef:
    """Returns the URI for QUDT quantity kind: Structure Factor (http://qudt.org/vocab/quantitykind/StructureFactor)"""
    return QUDT_QUANTITY_KIND["STRUCTUREFACTOR"]


def get_qudt_quantity_kind_sun_protection_factor_of_a_product() -> URIRef:
    """Returns the URI for QUDT quantity kind: sun protection factor of a product (http://qudt.org/vocab/quantitykind/SunProtectionFactorOfAProduct)"""
    return QUDT_QUANTITY_KIND["SUNPROTECTIONFACTOROFAPRODUCT"]


def get_qudt_quantity_kind_superconductor_energy_gap() -> URIRef:
    """Returns the URI for QUDT quantity kind: Superconductor Energy Gap (http://qudt.org/vocab/quantitykind/SuperconductorEnergyGap)"""
    return QUDT_QUANTITY_KIND["SUPERCONDUCTORENERGYGAP"]


def get_qudt_quantity_kind_surface_activity_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Surface Activity Density (http://qudt.org/vocab/quantitykind/SurfaceActivityDensity)"""
    return QUDT_QUANTITY_KIND["SURFACEACTIVITYDENSITY"]


def get_qudt_quantity_kind_surface_coefficient_of_heat_transfer() -> URIRef:
    """Returns the URI for QUDT quantity kind: Surface Coefficient of Heat Transfer (http://qudt.org/vocab/quantitykind/SurfaceCoefficientOfHeatTransfer)"""
    return QUDT_QUANTITY_KIND["SURFACECOEFFICIENTOFHEATTRANSFER"]


def get_qudt_quantity_kind_surface_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Surface Density (http://qudt.org/vocab/quantitykind/SurfaceDensity)"""
    return QUDT_QUANTITY_KIND["SURFACEDENSITY"]


def get_qudt_quantity_kind_surface_related_volume_flow_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: surface‑related volume flow rate (http://qudt.org/vocab/quantitykind/SurfaceRelatedVolumeFlowRate)"""
    return QUDT_QUANTITY_KIND["SURFACERELATEDVOLUMEFLOWRATE"]


def get_qudt_quantity_kind_surface_tension() -> URIRef:
    """Returns the URI for QUDT quantity kind: surface tension (http://qudt.org/vocab/quantitykind/SurfaceTension)"""
    return QUDT_QUANTITY_KIND["SURFACETENSION"]


def get_qudt_quantity_kind_surge_impedance_of_the_medium() -> URIRef:
    """Returns the URI for QUDT quantity kind: surge impedance of the medium (http://qudt.org/vocab/quantitykind/SurgeImpedanceOfTheMedium)"""
    return QUDT_QUANTITY_KIND["SURGEIMPEDANCEOFTHEMEDIUM"]


def get_qudt_quantity_kind_susceptance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Susceptance (http://qudt.org/vocab/quantitykind/Susceptance)"""
    return QUDT_QUANTITY_KIND["SUSCEPTANCE"]


def get_qudt_quantity_kind_target_bogie_mass() -> URIRef:
    """Returns the URI for QUDT quantity kind: Target Bogie Mass (http://qudt.org/vocab/quantitykind/TARGET-BOGIE-MASS)"""
    return QUDT_QUANTITY_KIND["TARGET-BOGIE-MASS"]


def get_qudt_quantity_kind_temperature_difference() -> URIRef:
    """Returns the URI for QUDT quantity kind: temperature difference (http://qudt.org/vocab/quantitykind/TemperatureDifference)"""
    return QUDT_QUANTITY_KIND["TEMPERATUREDIFFERENCE"]


def get_qudt_quantity_kind_temperature_gradient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Temperature Gradient (http://qudt.org/vocab/quantitykind/TemperatureGradient)"""
    return QUDT_QUANTITY_KIND["TEMPERATUREGRADIENT"]


def get_qudt_quantity_kind_temperature_per_time_squared() -> URIRef:
    """Returns the URI for QUDT quantity kind: Temperature per Time Squared (http://qudt.org/vocab/quantitykind/TemperaturePerTime_Squared)"""
    return QUDT_QUANTITY_KIND["TEMPERATUREPERTIME_SQUARED"]


def get_qudt_quantity_kind_temperature_rate_of_change() -> URIRef:
    """Returns the URI for QUDT quantity kind: Temperature Rate of Change (http://qudt.org/vocab/quantitykind/TemperatureRateOfChange)"""
    return QUDT_QUANTITY_KIND["TEMPERATURERATEOFCHANGE"]


def get_qudt_quantity_kind_temperature_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Temperature Ratio (http://qudt.org/vocab/quantitykind/TemperatureRatio)"""
    return QUDT_QUANTITY_KIND["TEMPERATURERATIO"]


def get_qudt_quantity_kind_temperature_variance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Temperature Variance (http://qudt.org/vocab/quantitykind/TemperatureVariance)"""
    return QUDT_QUANTITY_KIND["TEMPERATUREVARIANCE"]


def get_qudt_quantity_kind_temperature_variance_neon() -> URIRef:
    """Returns the URI for QUDT quantity kind: Temperature Variance, NEON (http://qudt.org/vocab/quantitykind/TemperatureVariance_NEON)"""
    return QUDT_QUANTITY_KIND["TEMPERATUREVARIANCE_NEON"]


def get_qudt_quantity_kind_temporal_summation_function() -> URIRef:
    """Returns the URI for QUDT quantity kind: Temporal Summation Function (http://qudt.org/vocab/quantitykind/TemporalSummationFunction)"""
    return QUDT_QUANTITY_KIND["TEMPORALSUMMATIONFUNCTION"]


def get_qudt_quantity_kind_tension() -> URIRef:
    """Returns the URI for QUDT quantity kind: Tension (http://qudt.org/vocab/quantitykind/Tension)"""
    return QUDT_QUANTITY_KIND["TENSION"]


def get_qudt_quantity_kind_thermal_admittance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Thermal Admittance (http://qudt.org/vocab/quantitykind/ThermalAdmittance)"""
    return QUDT_QUANTITY_KIND["THERMALADMITTANCE"]


def get_qudt_quantity_kind_thermal_capacitance() -> URIRef:
    """Returns the URI for QUDT quantity kind: thermal capacitance (http://qudt.org/vocab/quantitykind/ThermalCapacitance)"""
    return QUDT_QUANTITY_KIND["THERMALCAPACITANCE"]


def get_qudt_quantity_kind_thermal_conductance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Thermal Conductance (http://qudt.org/vocab/quantitykind/ThermalConductance)"""
    return QUDT_QUANTITY_KIND["THERMALCONDUCTANCE"]


def get_qudt_quantity_kind_thermal_diffusion_factor() -> URIRef:
    """Returns the URI for QUDT quantity kind: Thermal Diffusion Factor (http://qudt.org/vocab/quantitykind/ThermalDiffusionFactor)"""
    return QUDT_QUANTITY_KIND["THERMALDIFFUSIONFACTOR"]


def get_qudt_quantity_kind_thermal_diffusion_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Thermal Diffusion Ratio (http://qudt.org/vocab/quantitykind/ThermalDiffusionRatio)"""
    return QUDT_QUANTITY_KIND["THERMALDIFFUSIONRATIO"]


def get_qudt_quantity_kind_thermal_diffusion_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Thermal Diffusion Coefficient (http://qudt.org/vocab/quantitykind/ThermalDiffusionRatioCoefficient)"""
    return QUDT_QUANTITY_KIND["THERMALDIFFUSIONRATIOCOEFFICIENT"]


def get_qudt_quantity_kind_thermal_diffusivity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Thermal Diffusivity (http://qudt.org/vocab/quantitykind/ThermalDiffusivity)"""
    return QUDT_QUANTITY_KIND["THERMALDIFFUSIVITY"]


def get_qudt_quantity_kind_thermal_efficiency() -> URIRef:
    """Returns the URI for QUDT quantity kind: Thermal Efficiency (http://qudt.org/vocab/quantitykind/ThermalEfficiency)"""
    return QUDT_QUANTITY_KIND["THERMALEFFICIENCY"]


def get_qudt_quantity_kind_thermal_expansion_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Thermal Expansion Coefficient (http://qudt.org/vocab/quantitykind/ThermalExpansionCoefficient)"""
    return QUDT_QUANTITY_KIND["THERMALEXPANSIONCOEFFICIENT"]


def get_qudt_quantity_kind_thermal_transmittance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Thermal Transmittance (http://qudt.org/vocab/quantitykind/ThermalTransmittance)"""
    return QUDT_QUANTITY_KIND["THERMALTRANSMITTANCE"]


def get_qudt_quantity_kind_thermal_utilization_factor() -> URIRef:
    """Returns the URI for QUDT quantity kind: Thermal Utilization Factor (http://qudt.org/vocab/quantitykind/ThermalUtilizationFactor)"""
    return QUDT_QUANTITY_KIND["THERMALUTILIZATIONFACTOR"]


def get_qudt_quantity_kind_thermal_utilization_factor_for_fission() -> URIRef:
    """Returns the URI for QUDT quantity kind: Thermal Utilization Factor For Fission (http://qudt.org/vocab/quantitykind/ThermalUtilizationFactorForFission)"""
    return QUDT_QUANTITY_KIND["THERMALUTILIZATIONFACTORFORFISSION"]


def get_qudt_quantity_kind_thermodynamic_critical_magnetic_flux_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Thermodynamic Critical Magnetic Flux Density (http://qudt.org/vocab/quantitykind/ThermodynamicCriticalMagneticFluxDensity)"""
    return QUDT_QUANTITY_KIND["THERMODYNAMICCRITICALMAGNETICFLUXDENSITY"]


def get_qudt_quantity_kind_thermodynamic_entropy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Thermodynamic Entropy (http://qudt.org/vocab/quantitykind/ThermodynamicEntropy)"""
    return QUDT_QUANTITY_KIND["THERMODYNAMICENTROPY"]


def get_qudt_quantity_kind_thickness() -> URIRef:
    """Returns the URI for QUDT quantity kind: Thickness (http://qudt.org/vocab/quantitykind/Thickness)"""
    return QUDT_QUANTITY_KIND["THICKNESS"]


def get_qudt_quantity_kind_thomson_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Thomson Coefficient (http://qudt.org/vocab/quantitykind/ThomsonCoefficient)"""
    return QUDT_QUANTITY_KIND["THOMSONCOEFFICIENT"]


def get_qudt_quantity_kind_thrust_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Thrust Coefficient (http://qudt.org/vocab/quantitykind/ThrustCoefficient)"""
    return QUDT_QUANTITY_KIND["THRUSTCOEFFICIENT"]


def get_qudt_quantity_kind_thrust_to_weight_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Thrust To Weight Ratio (http://qudt.org/vocab/quantitykind/ThrustToWeightRatio)"""
    return QUDT_QUANTITY_KIND["THRUSTTOWEIGHTRATIO"]


def get_qudt_quantity_kind_thruster_power_to_thrust_efficiency() -> URIRef:
    """Returns the URI for QUDT quantity kind: Thruster Power To Thrust Efficiency (http://qudt.org/vocab/quantitykind/ThrusterPowerToThrustEfficiency)"""
    return QUDT_QUANTITY_KIND["THRUSTERPOWERTOTHRUSTEFFICIENCY"]


def get_qudt_quantity_kind_tilt() -> URIRef:
    """Returns the URI for QUDT quantity kind: Tilt (http://qudt.org/vocab/quantitykind/Tilt)"""
    return QUDT_QUANTITY_KIND["TILT"]


def get_qudt_quantity_kind_time_averaged_sound_intensity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Time averaged sound intensity (http://qudt.org/vocab/quantitykind/TimeAveragedSoundIntensity)"""
    return QUDT_QUANTITY_KIND["TIMEAVERAGEDSOUNDINTENSITY"]


def get_qudt_quantity_kind_time_constant_inductance_based() -> URIRef:
    """Returns the URI for QUDT quantity kind: time constant (inductance based) (http://qudt.org/vocab/quantitykind/TimeConstant_Inductance)"""
    return QUDT_QUANTITY_KIND["TIMECONSTANT_INDUCTANCE"]


def get_qudt_quantity_kind_time_per_count() -> URIRef:
    """Returns the URI for QUDT quantity kind: Time per Count (http://qudt.org/vocab/quantitykind/TimePerCount)"""
    return QUDT_QUANTITY_KIND["TIMEPERCOUNT"]


def get_qudt_quantity_kind_time_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Time Ratio (http://qudt.org/vocab/quantitykind/TimeRatio)"""
    return QUDT_QUANTITY_KIND["TIMERATIO"]


def get_qudt_quantity_kind_time_squared() -> URIRef:
    """Returns the URI for QUDT quantity kind: Time Squared (http://qudt.org/vocab/quantitykind/Time_Squared)"""
    return QUDT_QUANTITY_KIND["TIME_SQUARED"]


def get_qudt_quantity_kind_torque_constant() -> URIRef:
    """Returns the URI for QUDT quantity kind: torque constant (http://qudt.org/vocab/quantitykind/TorqueConstant)"""
    return QUDT_QUANTITY_KIND["TORQUECONSTANT"]


def get_qudt_quantity_kind_torque_per_length() -> URIRef:
    """Returns the URI for QUDT quantity kind: Torque per Length (http://qudt.org/vocab/quantitykind/TorquePerLength)"""
    return QUDT_QUANTITY_KIND["TORQUEPERLENGTH"]


def get_qudt_quantity_kind_torsional_rigidity() -> URIRef:
    """Returns the URI for QUDT quantity kind: torsional rigidity (http://qudt.org/vocab/quantitykind/TorsionalRigidity)"""
    return QUDT_QUANTITY_KIND["TORSIONALRIGIDITY"]


def get_qudt_quantity_kind_torsional_spring_constant() -> URIRef:
    """Returns the URI for QUDT quantity kind: torsional spring constant (http://qudt.org/vocab/quantitykind/TorsionalSpringConstant)"""
    return QUDT_QUANTITY_KIND["TORSIONALSPRINGCONSTANT"]


def get_qudt_quantity_kind_total_angular_momentum() -> URIRef:
    """Returns the URI for QUDT quantity kind: Total Angular Momentum (http://qudt.org/vocab/quantitykind/TotalAngularMomentum)"""
    return QUDT_QUANTITY_KIND["TOTALANGULARMOMENTUM"]


def get_qudt_quantity_kind_total_angular_momentum_quantum_number() -> URIRef:
    """Returns the URI for QUDT quantity kind: Total Angular Momentum Quantum Number (http://qudt.org/vocab/quantitykind/TotalAngularMomentumQuantumNumber)"""
    return QUDT_QUANTITY_KIND["TOTALANGULARMOMENTUMQUANTUMNUMBER"]


def get_qudt_quantity_kind_total_atomic_stopping_power() -> URIRef:
    """Returns the URI for QUDT quantity kind: Total Atomic Stopping Power (http://qudt.org/vocab/quantitykind/TotalAtomicStoppingPower)"""
    return QUDT_QUANTITY_KIND["TOTALATOMICSTOPPINGPOWER"]


def get_qudt_quantity_kind_total_cross_section() -> URIRef:
    """Returns the URI for QUDT quantity kind: Total Cross-section (http://qudt.org/vocab/quantitykind/TotalCrossSection)"""
    return QUDT_QUANTITY_KIND["TOTALCROSSSECTION"]


def get_qudt_quantity_kind_total_current() -> URIRef:
    """Returns the URI for QUDT quantity kind: Total Current (http://qudt.org/vocab/quantitykind/TotalCurrent)"""
    return QUDT_QUANTITY_KIND["TOTALCURRENT"]


def get_qudt_quantity_kind_total_current_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Total Current Density (http://qudt.org/vocab/quantitykind/TotalCurrentDensity)"""
    return QUDT_QUANTITY_KIND["TOTALCURRENTDENSITY"]


def get_qudt_quantity_kind_total_ionization() -> URIRef:
    """Returns the URI for QUDT quantity kind: Total Ionization (http://qudt.org/vocab/quantitykind/TotalIonization)"""
    return QUDT_QUANTITY_KIND["TOTALIONIZATION"]


def get_qudt_quantity_kind_total_linear_stopping_power() -> URIRef:
    """Returns the URI for QUDT quantity kind: Total Linear Stopping Power (http://qudt.org/vocab/quantitykind/TotalLinearStoppingPower)"""
    return QUDT_QUANTITY_KIND["TOTALLINEARSTOPPINGPOWER"]


def get_qudt_quantity_kind_total_mass_stopping_power() -> URIRef:
    """Returns the URI for QUDT quantity kind: Total Mass Stopping Power (http://qudt.org/vocab/quantitykind/TotalMassStoppingPower)"""
    return QUDT_QUANTITY_KIND["TOTALMASSSTOPPINGPOWER"]


def get_qudt_quantity_kind_total_pressure() -> URIRef:
    """Returns the URI for QUDT quantity kind: Total Pressure (http://qudt.org/vocab/quantitykind/TotalPressure)"""
    return QUDT_QUANTITY_KIND["TOTALPRESSURE"]


def get_qudt_quantity_kind_touch_thresholds() -> URIRef:
    """Returns the URI for QUDT quantity kind: Touch Thresholds (http://qudt.org/vocab/quantitykind/TouchThresholds)"""
    return QUDT_QUANTITY_KIND["TOUCHTHRESHOLDS"]


def get_qudt_quantity_kind_traffic_intensity() -> URIRef:
    """Returns the URI for QUDT quantity kind: traffic intensity (http://qudt.org/vocab/quantitykind/TrafficIntensity)"""
    return QUDT_QUANTITY_KIND["TRAFFICINTENSITY"]


def get_qudt_quantity_kind_transmittance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Transmittance (http://qudt.org/vocab/quantitykind/Transmittance)"""
    return QUDT_QUANTITY_KIND["TRANSMITTANCE"]


def get_qudt_quantity_kind_transmittance_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: Transmittance Density (http://qudt.org/vocab/quantitykind/TransmittanceDensity)"""
    return QUDT_QUANTITY_KIND["TRANSMITTANCEDENSITY"]


def get_qudt_quantity_kind_true_exhaust_velocity() -> URIRef:
    """Returns the URI for QUDT quantity kind: True Exhaust Velocity (http://qudt.org/vocab/quantitykind/TrueExhaustVelocity)"""
    return QUDT_QUANTITY_KIND["TRUEEXHAUSTVELOCITY"]


def get_qudt_quantity_kind_turbidity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Turbidity (http://qudt.org/vocab/quantitykind/Turbidity)"""
    return QUDT_QUANTITY_KIND["TURBIDITY"]


def get_qudt_quantity_kind_turns() -> URIRef:
    """Returns the URI for QUDT quantity kind: Turns (http://qudt.org/vocab/quantitykind/Turns)"""
    return QUDT_QUANTITY_KIND["TURNS"]


def get_qudt_quantity_kind_unbalance() -> URIRef:
    """Returns the URI for QUDT quantity kind: unbalance (http://qudt.org/vocab/quantitykind/Unbalance)"""
    return QUDT_QUANTITY_KIND["UNBALANCE"]


def get_qudt_quantity_kind_unknown() -> URIRef:
    """Returns the URI for QUDT quantity kind: Unknown (http://qudt.org/vocab/quantitykind/Unknown)"""
    return QUDT_QUANTITY_KIND["UNKNOWN"]


def get_qudt_quantity_kind_vapor_permeability() -> URIRef:
    """Returns the URI for QUDT quantity kind: Vapor Permeability (http://qudt.org/vocab/quantitykind/VaporPermeability)"""
    return QUDT_QUANTITY_KIND["VAPORPERMEABILITY"]


def get_qudt_quantity_kind_vapour_permeability() -> URIRef:
    """Returns the URI for QUDT quantity kind: Vapour Permeability (http://qudt.org/vocab/quantitykind/VapourPermeability)"""
    return QUDT_QUANTITY_KIND["VAPOURPERMEABILITY"]


def get_qudt_quantity_kind_vapor_permeance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Vapor Permeance (http://qudt.org/vocab/quantitykind/VaporPermeance)"""
    return QUDT_QUANTITY_KIND["VAPORPERMEANCE"]


def get_qudt_quantity_kind_vapour_permeance() -> URIRef:
    """Returns the URI for QUDT quantity kind: Vapour Permeance (http://qudt.org/vocab/quantitykind/VapourPermeance)"""
    return QUDT_QUANTITY_KIND["VAPOURPERMEANCE"]


def get_qudt_quantity_kind_vapor_pressure() -> URIRef:
    """Returns the URI for QUDT quantity kind: Vapor Pressure (http://qudt.org/vocab/quantitykind/VaporPressure)"""
    return QUDT_QUANTITY_KIND["VAPORPRESSURE"]


def get_qudt_quantity_kind_ventilation_rate_per_floor_area() -> URIRef:
    """Returns the URI for QUDT quantity kind: Ventilation Rate per Floor Area (http://qudt.org/vocab/quantitykind/VentilationRatePerFloorArea)"""
    return QUDT_QUANTITY_KIND["VENTILATIONRATEPERFLOORAREA"]


def get_qudt_quantity_kind_vertical_velocity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Vertical Velocity (http://qudt.org/vocab/quantitykind/VerticalVelocity)"""
    return QUDT_QUANTITY_KIND["VERTICALVELOCITY"]


def get_qudt_quantity_kind_video_frame_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: Video Frame Rate (http://qudt.org/vocab/quantitykind/VideoFrameRate)"""
    return QUDT_QUANTITY_KIND["VIDEOFRAMERATE"]


def get_qudt_quantity_kind_visible_radiant_energy() -> URIRef:
    """Returns the URI for QUDT quantity kind: Visible Radiant Energy (http://qudt.org/vocab/quantitykind/VisibleRadiantEnergy)"""
    return QUDT_QUANTITY_KIND["VISIBLERADIANTENERGY"]


def get_qudt_quantity_kind_vision_thresholds() -> URIRef:
    """Returns the URI for QUDT quantity kind: Vision Thresholds (http://qudt.org/vocab/quantitykind/VisionThresholds)"""
    return QUDT_QUANTITY_KIND["VISIONTHRESHOLDS"]


def get_qudt_quantity_kind_voltage_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Voltage Ratio (http://qudt.org/vocab/quantitykind/VoltageRatio)"""
    return QUDT_QUANTITY_KIND["VOLTAGERATIO"]


def get_qudt_quantity_kind_volume_per_time() -> URIRef:
    """Returns the URI for QUDT quantity kind: Volume per Time (http://qudt.org/vocab/quantitykind/VolumePerTime)"""
    return QUDT_QUANTITY_KIND["VOLUMEPERTIME"]


def get_qudt_quantity_kind_surface_related_volume_flow_rate() -> URIRef:
    """Returns the URI for QUDT quantity kind: surface‑related volume flow rate (http://qudt.org/vocab/quantitykind/VolumeFlowRate_SurfaceRelated)"""
    return QUDT_QUANTITY_KIND["VOLUMEFLOWRATE_SURFACERELATED"]


def get_qudt_quantity_kind_volume_flow_ratio() -> URIRef:
    """Returns the URI for QUDT quantity kind: Volume Flow Ratio (http://qudt.org/vocab/quantitykind/VolumeFlowRatio)"""
    return QUDT_QUANTITY_KIND["VOLUMEFLOWRATIO"]


def get_qudt_quantity_kind_volume_fraction() -> URIRef:
    """Returns the URI for QUDT quantity kind: Volume Fraction (http://qudt.org/vocab/quantitykind/VolumeFraction)"""
    return QUDT_QUANTITY_KIND["VOLUMEFRACTION"]


def get_qudt_quantity_kind_volume_per_unit_area() -> URIRef:
    """Returns the URI for QUDT quantity kind: Volume per Unit Area (http://qudt.org/vocab/quantitykind/VolumePerArea)"""
    return QUDT_QUANTITY_KIND["VOLUMEPERAREA"]


def get_qudt_quantity_kind_volume_strain() -> URIRef:
    """Returns the URI for QUDT quantity kind: Volume Strain (http://qudt.org/vocab/quantitykind/VolumeStrain)"""
    return QUDT_QUANTITY_KIND["VOLUMESTRAIN"]


def get_qudt_quantity_kind_volumic_bit_density() -> URIRef:
    """Returns the URI for QUDT quantity kind: volumic bit density (http://qudt.org/vocab/quantitykind/VolumetricBitDensity)"""
    return QUDT_QUANTITY_KIND["VOLUMETRICBITDENSITY"]


def get_qudt_quantity_kind_volumic_electric_charge() -> URIRef:
    """Returns the URI for QUDT quantity kind: volumic electric charge (http://qudt.org/vocab/quantitykind/VolumetricElectricCharge)"""
    return QUDT_QUANTITY_KIND["VOLUMETRICELECTRICCHARGE"]


def get_qudt_quantity_kind_volumetric_flux() -> URIRef:
    """Returns the URI for QUDT quantity kind: Volumetric Flux (http://qudt.org/vocab/quantitykind/VolumetricFlux)"""
    return QUDT_QUANTITY_KIND["VOLUMETRICFLUX"]


def get_qudt_quantity_kind_volumic_output_power() -> URIRef:
    """Returns the URI for QUDT quantity kind: volumic output power (http://qudt.org/vocab/quantitykind/VolumetricOutputPower)"""
    return QUDT_QUANTITY_KIND["VOLUMETRICOUTPUTPOWER"]


def get_qudt_quantity_kind_vorticity() -> URIRef:
    """Returns the URI for QUDT quantity kind: Vorticity (http://qudt.org/vocab/quantitykind/Vorticity)"""
    return QUDT_QUANTITY_KIND["VORTICITY"]


def get_qudt_quantity_kind_warm_receptor_threshold() -> URIRef:
    """Returns the URI for QUDT quantity kind: Warm Receptor Threshold (http://qudt.org/vocab/quantitykind/WarmReceptorThreshold)"""
    return QUDT_QUANTITY_KIND["WARMRECEPTORTHRESHOLD"]


def get_qudt_quantity_kind_warping_constant() -> URIRef:
    """Returns the URI for QUDT quantity kind: Warping Constant (http://qudt.org/vocab/quantitykind/WarpingConstant)"""
    return QUDT_QUANTITY_KIND["WARPINGCONSTANT"]


def get_qudt_quantity_kind_warping_moment() -> URIRef:
    """Returns the URI for QUDT quantity kind: Warping Moment (http://qudt.org/vocab/quantitykind/WarpingMoment)"""
    return QUDT_QUANTITY_KIND["WARPINGMOMENT"]


def get_qudt_quantity_kind_water_horsepower() -> URIRef:
    """Returns the URI for QUDT quantity kind: Water Horsepower (http://qudt.org/vocab/quantitykind/WaterHorsepower)"""
    return QUDT_QUANTITY_KIND["WATERHORSEPOWER"]


def get_qudt_quantity_kind_water_vapour_diffusion_coefficient() -> URIRef:
    """Returns the URI for QUDT quantity kind: Water vapour diffusion coefficient (http://qudt.org/vocab/quantitykind/WaterVaporDiffusionCoefficient)"""
    return QUDT_QUANTITY_KIND["WATERVAPORDIFFUSIONCOEFFICIENT"]


def get_qudt_quantity_kind_water_vapour_permeability() -> URIRef:
    """Returns the URI for QUDT quantity kind: water vapour permeability (http://qudt.org/vocab/quantitykind/WaterVapourPermeability)"""
    return QUDT_QUANTITY_KIND["WATERVAPOURPERMEABILITY"]


def get_qudt_quantity_kind_wavelength() -> URIRef:
    """Returns the URI for QUDT quantity kind: wavelength (http://qudt.org/vocab/quantitykind/Wavelength)"""
    return QUDT_QUANTITY_KIND["WAVELENGTH"]


def get_qudt_quantity_kind_wavenumber() -> URIRef:
    """Returns the URI for QUDT quantity kind: wavenumber (http://qudt.org/vocab/quantitykind/Wavenumber)"""
    return QUDT_QUANTITY_KIND["WAVENUMBER"]


def get_qudt_quantity_kind_web_time() -> URIRef:
    """Returns the URI for QUDT quantity kind: Web Time (http://qudt.org/vocab/quantitykind/WebTime)"""
    return QUDT_QUANTITY_KIND["WEBTIME"]


def get_qudt_quantity_kind_web_time_average_pressure() -> URIRef:
    """Returns the URI for QUDT quantity kind: Web Time Average Pressure (http://qudt.org/vocab/quantitykind/WebTimeAveragePressure)"""
    return QUDT_QUANTITY_KIND["WEBTIMEAVERAGEPRESSURE"]


def get_qudt_quantity_kind_web_time_average_thrust() -> URIRef:
    """Returns the URI for QUDT quantity kind: Web Time Average Thrust (http://qudt.org/vocab/quantitykind/WebTimeAverageThrust)"""
    return QUDT_QUANTITY_KIND["WEBTIMEAVERAGETHRUST"]


def get_qudt_quantity_kind_weight() -> URIRef:
    """Returns the URI for QUDT quantity kind: weight (http://qudt.org/vocab/quantitykind/Weight)"""
    return QUDT_QUANTITY_KIND["WEIGHT"]


def get_qudt_quantity_kind_wet_bulb_temperature() -> URIRef:
    """Returns the URI for QUDT quantity kind: Wet Bulb Temperature (http://qudt.org/vocab/quantitykind/WetBulbTemperature)"""
    return QUDT_QUANTITY_KIND["WETBULBTEMPERATURE"]


def get_qudt_quantity_kind_width() -> URIRef:
    """Returns the URI for QUDT quantity kind: Width (http://qudt.org/vocab/quantitykind/Width)"""
    return QUDT_QUANTITY_KIND["WIDTH"]


def get_qudt_quantity_kind_work_function() -> URIRef:
    """Returns the URI for QUDT quantity kind: Work Function (http://qudt.org/vocab/quantitykind/WorkFunction)"""
    return QUDT_QUANTITY_KIND["WORKFUNCTION"]
