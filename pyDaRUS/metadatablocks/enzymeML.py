# generated by datamodel-codegen:
#   filename:  enzymeML.json
#   timestamp: 2022-01-03T14:21:53+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from easyDataverse.core import DataverseBase
from pydantic import Field


class Unit(Enum):
    """
    Specifies the corresponding SI unit to the initial concentration value.
    """

    p_m = 'pM'
    n_m = 'nM'
    u_m = 'uM'
    m_m = 'mM'
    m = 'M'


class Constant(Enum):
    """
    Specifies if the proteins concentations was constant or not. If a protein serves as a substrate such as in protease reactions, concentrations are likely to change and this field should be set to 'Not constant'.
    """

    constant = 'Constant'
    not_constant = 'Not constant'


class Proteins(DataverseBase):
    identifier: Optional[str] = Field(
        None,
        description="Specifies the internal identifier of the protein. Please follow the convention of denote a protein entity by a 'p' followed by an integer. For instance, 'p1' is a valid ID.",
        multiple=False,
        typeClass='primitive',
        typeName='enzymeMLProteinID',
    )
    name: Optional[str] = Field(
        None,
        description='Specifies the convential name of the protein. Please note that this field on purpose can not be unique since protein/enzyme names vary in between fields. Use the amino acid sequence, UniProtID and/or EC number for a unique identification.',
        multiple=False,
        typeClass='primitive',
        typeName='enzymeMLProteinName',
    )
    vessel_reference: Optional[str] = Field(
        None,
        description="Specifies the name of the vessel in which the protein was given. If the protein was part of multiple reactions carried out in different vessel, please separated these via semicolon ';'.",
        multiple=False,
        typeClass='primitive',
        typeName='enzymeMLProteinVessel',
    )
    initial_concentration: Optional[float] = Field(
        None,
        description='Specifies the initial concentration value at the beginning of the experiment.',
        multiple=False,
        typeClass='primitive',
        typeName='enzymeMLProteinInitialConcentration',
    )
    unit: Optional[Unit] = Field(
        None,
        description='Specifies the corresponding SI unit to the initial concentration value.',
        multiple=False,
        typeClass='controlledVocabulary',
        typeName='enzymeMLProteinSubstanceUnits',
    )
    constant: Optional[Constant] = Field(
        None,
        description="Specifies if the proteins concentations was constant or not. If a protein serves as a substrate such as in protease reactions, concentrations are likely to change and this field should be set to 'Not constant'.",
        multiple=False,
        typeClass='controlledVocabulary',
        typeName='enzymeMLProteinConstant',
    )
    sequence: Optional[str] = Field(
        None,
        description="Specifies the aminoacid sequence of the protein. For instance 'MGHAGAHHAGÉ'.",
        multiple=False,
        typeClass='primitive',
        typeName='enzymeMLProteinSequence',
    )
    organism: Optional[str] = Field(
        None,
        description='Specifies the host organism that was used to express the protein.',
        multiple=False,
        typeClass='primitive',
        typeName='enzymeMLProteinOrganism',
    )
    uniprotid: Optional[str] = Field(
        None,
        description='Specifies the UniProt Identifier of the protein that is used to query the UniProt database.',
        multiple=False,
        typeClass='primitive',
        typeName='enzymeMLProteinUniProtID',
    )
    ecnumber: Optional[str] = Field(
        None,
        description='Specifies the EC-Number of the protein that denotes the hierarchical releation within the functional tree of protein-families. For instance EC: 1.1.1.1 belongs to the family of alcohol dehydrogenases.',
        multiple=False,
        typeClass='primitive',
        typeName='enzymeMLProteinECNumber',
    )
    sbo_term: Optional[str] = Field(
        None,
        description="Specifies the ID of the System Biology Ontology from branch 'material entity' to define a proteins role (e.g. SBO:0000240)",
        multiple=False,
        typeClass='primitive',
        typeName='enzymeMLProteinSBOTerm',
    )


class Unit1(Enum):
    """
    Specifies the corresponding SI unit to the initial concentration value.
    """

    n_m = 'nM'
    u_m = 'uM'
    m_m = 'mM'
    m = 'M'


class Reactants(DataverseBase):
    identifier: Optional[str] = Field(
        None,
        description="Specifies the internal identifier of the reactant. Please follow the convention of denote a reactant entity by an 's' followed by an integer. For instance, 's1' is a valid ID.",
        multiple=False,
        typeClass='primitive',
        typeName='enzymeMLReactantID',
    )
    name: Optional[str] = Field(
        None,
        description='Specifies the conventional or systematic name of the given reactant. Please note that this field on purpose can not be unique since molecule names vary in between fields. Please use either the InChI or SMILES code for a unique identification.',
        multiple=False,
        typeClass='primitive',
        typeName='enzymeMLReactantName',
    )
    vessel_reference: Optional[str] = Field(
        None,
        description="Specifies the vessel in which the reactant was given. If the reactant was part of multiple reactions carried out in different vessel, please separated these via semicolon ';'.",
        multiple=False,
        typeClass='primitive',
        typeName='enzymeMLReactantVessel',
    )
    initial_concentration: Optional[float] = Field(
        None,
        description='Specifies the initial concentration value at the beginning of the experiment.',
        multiple=False,
        typeClass='primitive',
        typeName='enzymeMLReactantInitialConcentration',
    )
    unit: Optional[Unit1] = Field(
        None,
        description='Specifies the corresponding SI unit to the initial concentration value.',
        multiple=False,
        typeClass='controlledVocabulary',
        typeName='enzymeMLReactantSubstanceUnits',
    )
    constant: Optional[Constant] = Field(
        None,
        description="Specifies if the reactants concentation was constant or not. If a reactant serves as a substrate/product, concentrations are likely to change and this field should be set to 'Not constant'.",
        multiple=False,
        typeClass='controlledVocabulary',
        typeName='enzymeMLReactantConstant',
    )
    inchicode: Optional[str] = Field(
        None,
        description='Specifies the IUPAC International Chemical Identifier, which is a unique identifier for a molecule',
        multiple=False,
        typeClass='primitive',
        typeName='enzymeMLReactantInchi',
    )
    smilescode: Optional[str] = Field(
        None,
        description='Specifies the Simplified Molecular Input Line Entry Specification, which is a unique identifier for a molecule',
        multiple=False,
        typeClass='primitive',
        typeName='enzymeMLReactantSmiles',
    )
    sbo_term: Optional[str] = Field(
        None,
        description="Specifies the ID of the System Biology Ontology from branch 'material entity' to define a reactants role (e.g. SBO:0000240)",
        multiple=False,
        typeClass='primitive',
        typeName='enzymeMLReactantSBOTerm',
    )


class TemperatureUnit(Enum):
    """
    Specifies the corresponding SI unit to the temperature value.
    """

    celsius = 'Celsius'
    kelvin = 'Kelvin'


class Reactions(DataverseBase):
    name: Optional[str] = Field(
        None,
        description="Specifies the conventional name of the reaction such as 'Alcohol dehydrogenation'. Please note, that this field on purpose can not be uniqe, since names vary in between fields and newly acquired reactions might not have a conventional name yet.",
        multiple=False,
        typeClass='primitive',
        typeName='enzymeMLReactionName',
    )
    temperature_value: Optional[float] = Field(
        None,
        description='Specifies the temperature value at which the experiment was executed.',
        multiple=False,
        typeClass='primitive',
        typeName='enzymeMLReactionTemperatureValue',
    )
    temperature_unit: Optional[TemperatureUnit] = Field(
        None,
        description='Specifies the corresponding SI unit to the temperature value.',
        multiple=False,
        typeClass='controlledVocabulary',
        typeName='enzymeMLReactionTemperatureUnit',
    )
    ph_value: Optional[float] = Field(
        None,
        description='Specifies the pH value at which the experiment was executed. Please note that pH values should fall in between the interval 0-14.',
        multiple=False,
        typeClass='primitive',
        typeName='enzymeMLReactionpH',
    )
    educts: Optional[str] = Field(
        None,
        description="Specifies the participating reactants/proteins which serve as educts. If multiple educts have been used, separate each of them via semicolon ';'.",
        multiple=False,
        typeClass='primitive',
        typeName='enzymeMLReactionEduct',
    )
    products: Optional[str] = Field(
        None,
        description="Specifies the participating reactants/proteins which serve as products. If multiple products have been used, separate each of them via semicolon ';'.",
        multiple=False,
        typeClass='primitive',
        typeName='enzymeMLReactionProduct',
    )
    modifiers: Optional[str] = Field(
        None,
        description="Specifies the participating reactants/proteins which serve as modifiers. For instance catalysing proteins should be entered as modifiers, which is the same for activators/inhibitors. If multiple modifiers have been used, separate each of them via semicolon ';'.",
        multiple=False,
        typeClass='primitive',
        typeName='enzymeMLReactionModifier',
    )
    equation: Optional[str] = Field(
        None,
        description="Specifies the reaction equation by separating educts and products via '->', while denoting multiple educts/products with a plusign and stoichiometries by 'Y Molecule'. For instance the following describes an alcohol dehydrogenation '1 Ethanol + 1 NAD+ -> 1 Acetaldehyde + 1 NADH + 1 H+'. ",
        multiple=False,
        typeClass='primitive',
        typeName='enzymeMLReactionEquation',
    )


class KineticParameters(DataverseBase):
    name: Optional[str] = Field(
        None,
        description="Specifies the conventional name of the kinetic paramter that has been estimated. For instance, 'vmax' is a valid name for a parameter. Please note, that for unique identification the SBO Term should be included.",
        multiple=False,
        typeClass='primitive',
        typeName='enzymeMLKineticParameterName',
    )
    value: Optional[float] = Field(
        None,
        description='Specifies the numerical value of the estimated kinetic parameter.',
        multiple=False,
        typeClass='primitive',
        typeName='enzymeMLKineticParameterValue',
    )
    unit: Optional[str] = Field(
        None,
        description='Specifies the SI unit of the estimated kinetic parameter.',
        multiple=False,
        typeClass='primitive',
        typeName='enzymeMLKineticParameterUnit',
    )
    sbo_term: Optional[str] = Field(
        None,
        description="Specifies the ID of the System Biology Ontology from branch 'systems description parameter' to define a kinetic parameter (e.g. SBO:0000545)",
        multiple=False,
        typeClass='primitive',
        typeName='enzymeMLKineticParameterSBOTerm',
    )


class KineticLaw(DataverseBase):
    name: Optional[str] = Field(
        None,
        description="Specifies the conventional name of the kinetic law that has been used. For instance 'Reversible Michaelis-Menten'.",
        multiple=False,
        typeClass='primitive',
        typeName='enzymeMLKineticLawName',
    )
    reaction_reference: Optional[str] = Field(
        None,
        description='Specifies the reaction that has beeen modeled by the given kinetic law.',
        multiple=False,
        typeClass='primitive',
        typeName='enzymeMLKineticLawReaction',
    )
    kinetic_model: Optional[str] = Field(
        None,
        description="Specifies the mathematical equation of the given kinetic law. For variables that reference entities that are part of this EnzymeML document, please use the given identifier. Parameters will be defined in another field and are referenced by their conventional names. For instance, the following equation denotes a valid kinetic model  'vmax  * s1 / ( km + s1 )'.",
        multiple=False,
        typeClass='primitive',
        typeName='enzymeMLKineticLawEquation',
    )


class Unit2(Enum):
    """
    Specifies the SI unit corresponding to the given vessel size value (e.g. 'mL')
    """

    ul = 'ul'
    ml = 'ml'
    l = 'l'


class Vessels(DataverseBase):
    name: Optional[str] = Field(
        None,
        description='Specifies the exact production name of the vessel shoudl be given here (e.g. Eppendorf Tube)',
        multiple=False,
        typeClass='primitive',
        typeName='enzymeMLVesselName',
    )
    size: Optional[float] = Field(
        None,
        description="Specifies the volume value of the given vessel (e.g. '1')",
        multiple=False,
        typeClass='primitive',
        typeName='enzymeMLVesselSize',
    )
    unit: Optional[Unit2] = Field(
        None,
        description="Specifies the SI unit corresponding to the given vessel size value (e.g. 'mL')",
        multiple=False,
        typeClass='controlledVocabulary',
        typeName='enzymeMLVesselUnits',
    )
    constant: Optional[Constant] = Field(
        None,
        description="Specifies if the volume is constant or not. In some instances substances are added over the course of an experiment, where this field should be selected as 'Not constant'.",
        multiple=False,
        typeClass='controlledVocabulary',
        typeName='enzymeMLVesselConstant',
    )


class EnzymeMl(DataverseBase):
    proteins: list[Proteins] = Field(
        default_factory=list,
        description='This field describes the proteins that haven been used in the course of the experiment. These should include catalytic active enzymes as well as non-catalytic entities such as inhibitors.',
        multiple=True,
        typeClass='compound',
        typeName='enzymeMLProtein',
    )
    reactants: list[Reactants] = Field(
        default_factory=list,
        description='This field describes the reactants that have been used in the course of the experiment. This should be small molecules exclusively such as NADH, pyruvate or any other molecule that is not a protein.',
        multiple=True,
        typeClass='compound',
        typeName='enzymeMLReactant',
    )
    reactions: list[Reactions] = Field(
        default_factory=list,
        description='This field describes the reactions that have been executed in the course of the experiment. Here, every defined reactants/proteins will be combined towards a meaningful biochemical reaction equation.',
        multiple=True,
        typeClass='compound',
        typeName='enzymeMLReaction',
    )
    kinetic_parameters: list[KineticParameters] = Field(
        default_factory=list,
        description='This field describe the kinetic parameters that have been estimated using the given kinetic law.',
        multiple=True,
        typeClass='compound',
        typeName='enzymeMLKineticParameter',
    )
    kinetic_law: list[KineticLaw] = Field(
        default_factory=list,
        description='This field describes the kinetic law that has been used to model the reaction kinetics. It includes the conventional as well as the mathematic equation.',
        multiple=True,
        typeClass='compound',
        typeName='enzymeMLKineticLaw',
    )
    vessels: list[Vessels] = Field(
        default_factory=list,
        description="This field describes which vessels have been used to carry out the experiment. For example an 'Eppendorf tube' of size 1mL that held a constant volume.",
        multiple=True,
        typeClass='compound',
        typeName='enzymeMLVessel',
    )
    _metadatablock_name: Optional[str] = 'enzymeML'


    def add_kinetic_law(
        self,
        name: Optional[str] = None,
        reaction_reference: Optional[str] = None,
        kinetic_model: Optional[str] = None,
    ):
        """Function used to add an instance of KineticLaw to the metadatablock.

        Args:
        
            name (string): Specifies the conventional name of the kinetic law that has been used. For instance 'Reversible Michaelis-Menten'.
            reaction_reference (string): Specifies the reaction that has beeen modeled by the given kinetic law.
            kinetic_model (string): Specifies the mathematical equation of the given kinetic law. For variables that reference entities that are part of this EnzymeML document, please use the given identifier. Parameters will be defined in another field and are referenced by their conventional names. For instance, the following equation denotes a valid kinetic model  'vmax  * s1 / ( km + s1 )'.

        """

        self.kinetic_law.append(
            KineticLaw(
                name=name, reaction_reference=reaction_reference, kinetic_model=kinetic_model
            )
        )


    def add_kinetic_parameters(
        self,
        name: Optional[str] = None,
        value: Optional[float] = None,
        unit: Optional[str] = None,
        sbo_term: Optional[str] = None,
    ):
        """Function used to add an instance of KineticParameters to the metadatablock.

        Args:
        
            name (string): Specifies the conventional name of the kinetic paramter that has been estimated. For instance, 'vmax' is a valid name for a parameter. Please note, that for unique identification the SBO Term should be included.
            value (number): Specifies the numerical value of the estimated kinetic parameter.
            unit (string): Specifies the SI unit of the estimated kinetic parameter.
            sbo_term (string): Specifies the ID of the System Biology Ontology from branch 'systems description parameter' to define a kinetic parameter (e.g. SBO:0000545)

        """

        self.kinetic_parameters.append(
            KineticParameters(
                name=name, value=value, unit=unit, sbo_term=sbo_term
            )
        )


    def add_proteins(
        self,
        identifier: Optional[str] = None,
        name: Optional[str] = None,
        vessel_reference: Optional[str] = None,
        initial_concentration: Optional[float] = None,
        unit: Optional[Unit] = None,
        constant: Optional[Constant] = None,
        sequence: Optional[str] = None,
        organism: Optional[str] = None,
        uniprotid: Optional[str] = None,
        ecnumber: Optional[str] = None,
        sbo_term: Optional[str] = None,
    ):
        """Function used to add an instance of Proteins to the metadatablock.

        Args:
        
            identifier (string): Specifies the internal identifier of the protein. Please follow the convention of denote a protein entity by a 'p' followed by an integer. For instance, 'p1' is a valid ID.
            name (string): Specifies the convential name of the protein. Please note that this field on purpose can not be unique since protein/enzyme names vary in between fields. Use the amino acid sequence, UniProtID and/or EC number for a unique identification.
            vessel_reference (string): Specifies the name of the vessel in which the protein was given. If the protein was part of multiple reactions carried out in different vessel, please separated these via semicolon ';'.
            initial_concentration (number): Specifies the initial concentration value at the beginning of the experiment.
            unit (Enum): Specifies the corresponding SI unit to the initial concentration value.
            constant (Enum): Specifies if the proteins concentations was constant or not. If a protein serves as a substrate such as in protease reactions, concentrations are likely to change and this field should be set to 'Not constant'.
            sequence (string): Specifies the aminoacid sequence of the protein. For instance 'MGHAGAHHAGÉ'.
            organism (string): Specifies the host organism that was used to express the protein.
            uniprotid (string): Specifies the UniProt Identifier of the protein that is used to query the UniProt database.
            ecnumber (string): Specifies the EC-Number of the protein that denotes the hierarchical releation within the functional tree of protein-families. For instance EC: 1.1.1.1 belongs to the family of alcohol dehydrogenases.
            sbo_term (string): Specifies the ID of the System Biology Ontology from branch 'material entity' to define a proteins role (e.g. SBO:0000240)

        """

        self.proteins.append(
            Proteins(
                identifier=identifier, name=name, vessel_reference=vessel_reference, initial_concentration=initial_concentration, unit=unit, constant=constant, sequence=sequence, organism=organism, uniprotid=uniprotid, ecnumber=ecnumber, sbo_term=sbo_term
            )
        )


    def add_reactants(
        self,
        identifier: Optional[str] = None,
        name: Optional[str] = None,
        vessel_reference: Optional[str] = None,
        initial_concentration: Optional[float] = None,
        unit: Optional[Unit1] = None,
        constant: Optional[Constant] = None,
        inchicode: Optional[str] = None,
        smilescode: Optional[str] = None,
        sbo_term: Optional[str] = None,
    ):
        """Function used to add an instance of Reactants to the metadatablock.

        Args:
        
            identifier (string): Specifies the internal identifier of the reactant. Please follow the convention of denote a reactant entity by an 's' followed by an integer. For instance, 's1' is a valid ID.
            name (string): Specifies the conventional or systematic name of the given reactant. Please note that this field on purpose can not be unique since molecule names vary in between fields. Please use either the InChI or SMILES code for a unique identification.
            vessel_reference (string): Specifies the vessel in which the reactant was given. If the reactant was part of multiple reactions carried out in different vessel, please separated these via semicolon ';'.
            initial_concentration (number): Specifies the initial concentration value at the beginning of the experiment.
            unit (Enum): Specifies the corresponding SI unit to the initial concentration value.
            constant (Enum): Specifies if the reactants concentation was constant or not. If a reactant serves as a substrate/product, concentrations are likely to change and this field should be set to 'Not constant'.
            inchicode (string): Specifies the IUPAC International Chemical Identifier, which is a unique identifier for a molecule
            smilescode (string): Specifies the Simplified Molecular Input Line Entry Specification, which is a unique identifier for a molecule
            sbo_term (string): Specifies the ID of the System Biology Ontology from branch 'material entity' to define a reactants role (e.g. SBO:0000240)

        """

        self.reactants.append(
            Reactants(
                identifier=identifier, name=name, vessel_reference=vessel_reference, initial_concentration=initial_concentration, unit=unit, constant=constant, inchicode=inchicode, smilescode=smilescode, sbo_term=sbo_term
            )
        )


    def add_reactions(
        self,
        name: Optional[str] = None,
        temperature_value: Optional[float] = None,
        temperature_unit: Optional[TemperatureUnit] = None,
        ph_value: Optional[float] = None,
        educts: Optional[str] = None,
        products: Optional[str] = None,
        modifiers: Optional[str] = None,
        equation: Optional[str] = None,
    ):
        """Function used to add an instance of Reactions to the metadatablock.

        Args:
        
            name (string): Specifies the conventional name of the reaction such as 'Alcohol dehydrogenation'. Please note, that this field on purpose can not be uniqe, since names vary in between fields and newly acquired reactions might not have a conventional name yet.
            temperature_value (number): Specifies the temperature value at which the experiment was executed.
            temperature_unit (Enum): Specifies the corresponding SI unit to the temperature value.
            ph_value (number): Specifies the pH value at which the experiment was executed. Please note that pH values should fall in between the interval 0-14.
            educts (string): Specifies the participating reactants/proteins which serve as educts. If multiple educts have been used, separate each of them via semicolon ';'.
            products (string): Specifies the participating reactants/proteins which serve as products. If multiple products have been used, separate each of them via semicolon ';'.
            modifiers (string): Specifies the participating reactants/proteins which serve as modifiers. For instance catalysing proteins should be entered as modifiers, which is the same for activators/inhibitors. If multiple modifiers have been used, separate each of them via semicolon ';'.
            equation (string): Specifies the reaction equation by separating educts and products via '->', while denoting multiple educts/products with a plusign and stoichiometries by 'Y Molecule'. For instance the following describes an alcohol dehydrogenation '1 Ethanol + 1 NAD+ -> 1 Acetaldehyde + 1 NADH + 1 H+'. 

        """

        self.reactions.append(
            Reactions(
                name=name, temperature_value=temperature_value, temperature_unit=temperature_unit, ph_value=ph_value, educts=educts, products=products, modifiers=modifiers, equation=equation
            )
        )


    def add_vessels(
        self,
        name: Optional[str] = None,
        size: Optional[float] = None,
        unit: Optional[Unit2] = None,
        constant: Optional[Constant] = None,
    ):
        """Function used to add an instance of Vessels to the metadatablock.

        Args:
        
            name (string): Specifies the exact production name of the vessel shoudl be given here (e.g. Eppendorf Tube)
            size (number): Specifies the volume value of the given vessel (e.g. '1')
            unit (Enum): Specifies the SI unit corresponding to the given vessel size value (e.g. 'mL')
            constant (Enum): Specifies if the volume is constant or not. In some instances substances are added over the course of an experiment, where this field should be selected as 'Not constant'.

        """

        self.vessels.append(
            Vessels(
                name=name, size=size, unit=unit, constant=constant
            )
        )