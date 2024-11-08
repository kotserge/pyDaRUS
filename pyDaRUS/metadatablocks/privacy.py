# generated by datamodel-codegen:
#   filename:  privacy.json
#   timestamp: 2022-05-24T09:26:50+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from easyDataverse.base import DataverseBase
from pydantic import Field


class PersonalData(Enum):
    """
    Does the dataset contain personal data according to Art. 4 GDPR?
    """

    no = 'no'
    yes__but_anonymized = 'yes, but anonymized'
    yes__but_pseudonymized = 'yes, but pseudonymized'
    yes = 'yes'


class SpecialCategories(Enum):
    """
    Does the dataset contain special categories of personal data according to Art.9 GDPR?
    """

    no = 'no'
    yes = 'yes'


class Privacy(DataverseBase):
    personal_data: Optional[PersonalData] = Field(
        None,
        description='Does the dataset contain personal data according to Art. 4 GDPR?',
        multiple=False,
        typeClass='controlledVocabulary',
        typeName='privData',
    )
    special_categories: Optional[SpecialCategories] = Field(
        None,
        description='Does the dataset contain special categories of personal data according to Art.9 GDPR?',
        multiple=False,
        typeClass='controlledVocabulary',
        typeName='privSpecial',
    )
    explicit_consent: Optional[SpecialCategories] = Field(
        None,
        description='Did each person whose information appears in the data give explicit permission to share the data?',
        multiple=False,
        typeClass='controlledVocabulary',
        typeName='privConsent',
    )
    terms_of_consent: Optional[List] = Field(
        None,
        description='Did the content has any restrictions on sharing?',
        multiple=True,
        typeClass='primitive',
        typeName='privTermsOfConsent',
    )
    measures: Optional[List] = Field(
        None,
        description='Which technical and organisational measures are taken to secure the data (e.g. encryption of the data, rights management)?',
        multiple=True,
        typeClass='primitive',
        typeName='privMeasures',
    )
    _metadatablock_name: Optional[str] = 'privacy'
