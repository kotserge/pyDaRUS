# generated by datamodel-codegen:
#   filename:  process.json
#   timestamp: 2022-05-24T09:26:51+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from easyDataverse.base import DataverseBase
from pydantic import Field


class Type(Enum):
    """
    Specifies the position in the data life cycle.
    """

    generation = 'Generation'
    postprocessing = 'Postprocessing'
    analysis = 'Analysis'
    other = 'Other'


class ProcessingSteps(DataverseBase):
    id: Optional[int] = Field(
        None,
        description='Used to order the processing steps.',
        multiple=False,
        typeClass='primitive',
        typeName='processStepId',
    )
    type: Optional[Type] = Field(
        None,
        description='Specifies the position in the data life cycle.',
        multiple=False,
        typeClass='controlledVocabulary',
        typeName='processStepType',
    )
    date: Optional[str] = Field(
        None,
        description='Date this step has been performed.',
        multiple=False,
        typeClass='primitive',
        typeName='processStepDate',
    )
    methods: Optional[str] = Field(
        None,
        description='List of methods used in this processing step (detailed information about methods should be given under Processing Methods).',
        multiple=False,
        typeClass='primitive',
        typeName='processStepMethods',
    )
    error_method: Optional[str] = Field(
        None,
        description='Method used to measure the errors or uncertainties of this processing step.',
        multiple=False,
        typeClass='primitive',
        typeName='processStepErrorMethod',
    )
    software: Optional[str] = Field(
        None,
        description='List of software names used in this processing step (detailed information about software should be given under Software).',
        multiple=False,
        typeClass='primitive',
        typeName='processStepSoftware',
    )
    instruments: Optional[str] = Field(
        None,
        description='List of instrumental hardware used in this processing step (detailed information about instruments should be given under Instruments).',
        multiple=False,
        typeClass='primitive',
        typeName='processStepHardware',
    )
    environment: Optional[str] = Field(
        None,
        description='Name of the environment used for this processing step (detailed information about the environment should be given under Environments).',
        multiple=False,
        typeClass='primitive',
        typeName='processStepEnvironment',
    )
    input: Optional[List] = Field(
        None,
        description='Name of the file or object that was the input of this processing step',
        multiple=True,
        typeClass='primitive',
        typeName='processStepInput',
    )
    output: Optional[List] = Field(
        None,
        description='Name of the file or object that was the output of this processing step',
        multiple=True,
        typeClass='primitive',
        typeName='processStepOutput',
    )


class ProcessingMethods(DataverseBase):
    name: Optional[str] = Field(
        None,
        description='Name of the method as free text.',
        multiple=False,
        typeClass='primitive',
        typeName='processMethodsName',
    )
    description: Optional[str] = Field(
        None,
        description='Description of the method as free text',
        multiple=False,
        typeClass='primitive',
        typeName='processMethodsDescription',
    )
    parameters: Optional[str] = Field(
        None,
        description='List of all parameter names relevant for this method (detailed information about parameters should be given under Method Parameters).',
        multiple=False,
        typeClass='primitive',
        typeName='processMethodsPars',
    )


class IdType(Enum):
    """
    The type of digital identifier used for this software (e.g., Digital Object Identifier (DOI)).
    """

    ark = 'ark'
    ar_xiv = 'arXiv'
    bibcode = 'bibcode'
    doi = 'doi'
    ean13 = 'ean13'
    eissn = 'eissn'
    handle = 'handle'
    isbn = 'isbn'
    issn = 'issn'
    istc = 'istc'
    lissn = 'lissn'
    lsid = 'lsid'
    pmid = 'pmid'
    purl = 'purl'
    upc = 'upc'
    url = 'url'
    urn = 'urn'


class Software(DataverseBase):
    name: Optional[str] = Field(
        None,
        description='Name of the software.',
        multiple=False,
        typeClass='primitive',
        typeName='processSoftwareName',
    )
    version: Optional[str] = Field(
        None,
        description='Version of the software.',
        multiple=False,
        typeClass='primitive',
        typeName='processSoftwareVersion',
    )
    id_type: Optional[IdType] = Field(
        None,
        description='The type of digital identifier used for this software (e.g., Digital Object Identifier (DOI)).',
        multiple=False,
        typeClass='controlledVocabulary',
        typeName='processSoftwareIDType',
    )
    id_number: Optional[str] = Field(
        None,
        description='The identifier for the selected ID type.',
        multiple=False,
        typeClass='primitive',
        typeName='processSoftwareIDNumber',
    )
    citation: Optional[str] = Field(
        None,
        description='Assosicated text publication to the software.',
        multiple=False,
        typeClass='primitive',
        typeName='processSoftwareCitation',
    )
    url: Optional[str] = Field(
        None,
        description='Link to the software, code repository or application.',
        multiple=False,
        typeClass='primitive',
        typeName='processSoftwareURL',
    )
    license: Optional[str] = Field(
        None,
        description='The license type of the software.',
        multiple=False,
        typeClass='primitive',
        typeName='processSoftwareLicence',
    )


class MethodParameters(DataverseBase):
    name: Optional[str] = Field(
        None,
        description='Name of the parameter.',
        multiple=False,
        typeClass='primitive',
        typeName='processMethodsParName',
    )
    symbol: Optional[str] = Field(
        None,
        description='The symbol used to describe this parameter.',
        multiple=False,
        typeClass='primitive',
        typeName='processMethodsParSymbol',
    )
    unit: Optional[str] = Field(
        None,
        description='The unit or scale of this parameter.',
        multiple=False,
        typeClass='primitive',
        typeName='processMethodsParUnit',
    )
    value: Optional[float] = Field(
        None,
        description='The (numerical) value of this parameter.',
        multiple=False,
        typeClass='primitive',
        typeName='processMethodsParValue',
    )
    textual_value: Optional[str] = Field(
        None,
        description='The value of this method parameter. (for non numerical values)',
        multiple=False,
        typeClass='primitive',
        typeName='processMethodsParTextValue',
    )


class Instruments(DataverseBase):
    name: Optional[str] = Field(
        None,
        description='Name of this instrument.',
        multiple=False,
        typeClass='primitive',
        typeName='processInstruName',
    )
    description: Optional[str] = Field(
        None,
        description='Description of the instrument, e.g., what it is used for.',
        multiple=False,
        typeClass='primitive',
        typeName='processInstruDescr',
    )
    version: Optional[str] = Field(
        None,
        description='The type or version of this instrument.',
        multiple=False,
        typeClass='primitive',
        typeName='processInstruType',
    )
    part_number: Optional[List] = Field(
        None,
        description='A vendors part number for an instrument or a piece of equipment.',
        multiple=True,
        typeClass='primitive',
        typeName='processInstruPartnum',
    )
    serial_number: Optional[List] = Field(
        None,
        description='A vendors serial number for an instrument or a piece of equipment.',
        multiple=True,
        typeClass='primitive',
        typeName='processInstruSerialnum',
    )
    software: Optional[str] = Field(
        None,
        description='Required software for this instrument.',
        multiple=False,
        typeClass='primitive',
        typeName='processInstruSoftware',
    )
    location: Optional[str] = Field(
        None,
        description='Location of the instrument.',
        multiple=False,
        typeClass='primitive',
        typeName='processInstruLocation',
    )


class Environments(DataverseBase):
    name: Optional[str] = Field(
        None,
        description='Name of the environment.',
        multiple=False,
        typeClass='primitive',
        typeName='processEnvName',
    )
    compiler_names_and_flags: Optional[List] = Field(
        None,
        description='Name and flags of the used compilers.',
        multiple=True,
        typeClass='primitive',
        typeName='processEnvCompName',
    )
    number_of_nodes: Optional[int] = Field(
        None,
        description='Number of compute nodes inside a high performance cluster environment.',
        multiple=False,
        typeClass='primitive',
        typeName='processEnvNodes',
    )
    ppn: Optional[int] = Field(
        None,
        description='Processors per node',
        multiple=False,
        typeClass='primitive',
        typeName='processEnvPPN',
    )


class Process(DataverseBase):
    processing_steps: List[ProcessingSteps] = Field(
        default_factory=list,
        description='Specification of the processing steps in the data life cycle.',
        multiple=True,
        typeClass='compound',
        typeName='processStep',
    )
    processing_methods: List[ProcessingMethods] = Field(
        default_factory=list,
        description='Information about used methods in the data life cycle.',
        multiple=True,
        typeClass='compound',
        typeName='processMethods',
    )
    software: List[Software] = Field(
        default_factory=list,
        description='Information about used software.',
        multiple=True,
        typeClass='compound',
        typeName='processSoftware',
    )
    method_parameters: List[MethodParameters] = Field(
        default_factory=list,
        description='Parameters relevant for processing methods.',
        multiple=True,
        typeClass='compound',
        typeName='processMethodsPar',
    )
    instruments: List[Instruments] = Field(
        default_factory=list,
        description='A representation of a piece of laboratory or field equipment, used in the execution of an experiment, that produces data.',
        multiple=True,
        typeClass='compound',
        typeName='processInstru',
    )
    environments: List[Environments] = Field(
        default_factory=list,
        description='(Computation) environments of the data generation. ',
        multiple=True,
        typeClass='compound',
        typeName='processEnv',
    )
    _metadatablock_name: Optional[str] = 'process'

    def add_environments(
        self,
        name: Optional[str] = None,
        compiler_names_and_flags: Optional[List] = None,
        number_of_nodes: Optional[int] = None,
        ppn: Optional[int] = None,
    ):
        """Function used to add an instance of Environments to the metadatablock.

        Args:

            name (string): Name of the environment.
            compiler_names_and_flags (array): Name and flags of the used compilers.
            number_of_nodes (integer): Number of compute nodes inside a high performance cluster environment.
            ppn (integer): Processors per node

        """

        self.environments.append(
            Environments(
                name=name,
                compiler_names_and_flags=compiler_names_and_flags,
                number_of_nodes=number_of_nodes,
                ppn=ppn,
            )
        )

    def add_instruments(
        self,
        name: Optional[str] = None,
        description: Optional[str] = None,
        version: Optional[str] = None,
        part_number: Optional[List] = None,
        serial_number: Optional[List] = None,
        software: Optional[str] = None,
        location: Optional[str] = None,
    ):
        """Function used to add an instance of Instruments to the metadatablock.

        Args:

            name (string): Name of this instrument.
            description (string): Description of the instrument, e.g., what it is used for.
            version (string): The type or version of this instrument.
            part_number (array): A vendors part number for an instrument or a piece of equipment.
            serial_number (array): A vendors serial number for an instrument or a piece of equipment.
            software (string): Required software for this instrument.
            location (string): Location of the instrument.

        """

        self.instruments.append(
            Instruments(
                name=name,
                description=description,
                version=version,
                part_number=part_number,
                serial_number=serial_number,
                software=software,
                location=location,
            )
        )

    def add_method_parameters(
        self,
        name: Optional[str] = None,
        symbol: Optional[str] = None,
        unit: Optional[str] = None,
        value: Optional[float] = None,
        textual_value: Optional[str] = None,
    ):
        """Function used to add an instance of MethodParameters to the metadatablock.

        Args:

            name (string): Name of the parameter.
            symbol (string): The symbol used to describe this parameter.
            unit (string): The unit or scale of this parameter.
            value (number): The (numerical) value of this parameter.
            textual_value (string): The value of this method parameter. (for non numerical values)

        """

        self.method_parameters.append(
            MethodParameters(
                name=name,
                symbol=symbol,
                unit=unit,
                value=value,
                textual_value=textual_value,
            )
        )

    def add_processing_methods(
        self,
        name: Optional[str] = None,
        description: Optional[str] = None,
        parameters: Optional[str] = None,
    ):
        """Function used to add an instance of ProcessingMethods to the metadatablock.

        Args:

            name (string): Name of the method as free text.
            description (string): Description of the method as free text
            parameters (string): List of all parameter names relevant for this method (detailed information about parameters should be given under Method Parameters).

        """

        self.processing_methods.append(
            ProcessingMethods(name=name, description=description, parameters=parameters)
        )

    def add_processing_steps(
        self,
        id: Optional[int] = None,
        type: Optional[Type] = None,
        date: Optional[str] = None,
        methods: Optional[str] = None,
        error_method: Optional[str] = None,
        software: Optional[str] = None,
        instruments: Optional[str] = None,
        environment: Optional[str] = None,
        input: Optional[List] = None,
        output: Optional[List] = None,
    ):
        """Function used to add an instance of ProcessingSteps to the metadatablock.

        Args:

            id (integer): Used to order the processing steps.
            type (Enum): Specifies the position in the data life cycle.
            date (string): Date this step has been performed.
            methods (string): List of methods used in this processing step (detailed information about methods should be given under Processing Methods).
            error_method (string): Method used to measure the errors or uncertainties of this processing step.
            software (string): List of software names used in this processing step (detailed information about software should be given under Software).
            instruments (string): List of instrumental hardware used in this processing step (detailed information about instruments should be given under Instruments).
            environment (string): Name of the environment used for this processing step (detailed information about the environment should be given under Environments).
            input (array): Name of the file or object that was the input of this processing step
            output (array): Name of the file or object that was the output of this processing step

        """

        self.processing_steps.append(
            ProcessingSteps(
                id=id,
                type=type,
                date=date,
                methods=methods,
                error_method=error_method,
                software=software,
                instruments=instruments,
                environment=environment,
                input=input,
                output=output,
            )
        )

    def add_software(
        self,
        name: Optional[str] = None,
        version: Optional[str] = None,
        id_type: Optional[IdType] = None,
        id_number: Optional[str] = None,
        citation: Optional[str] = None,
        url: Optional[str] = None,
        license: Optional[str] = None,
    ):
        """Function used to add an instance of Software to the metadatablock.

        Args:

            name (string): Name of the software.
            version (string): Version of the software.
            id_type (Enum): The type of digital identifier used for this software (e.g., Digital Object Identifier (DOI)).
            id_number (string): The identifier for the selected ID type.
            citation (string): Assosicated text publication to the software.
            url (string): Link to the software, code repository or application.
            license (string): The license type of the software.

        """

        self.software.append(
            Software(
                name=name,
                version=version,
                id_type=id_type,
                id_number=id_number,
                citation=citation,
                url=url,
                license=license,
            )
        )
