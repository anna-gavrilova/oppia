# coding: utf-8
#
# Copyright 2014 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, softwar
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from core.domain import widget_domain


class MultipleChoiceInput(widget_domain.BaseWidget):
    """Interaction for multiple choice input."""

    # The human-readable name of the interaction.
    name = 'Multiple Choice'

    # The category the interaction falls under in the repository.
    category = 'Basic Input'

    # A description of the interaction.
    description = (
        'Allows learners to select one of a list of multiple-choice options.')

    # Customization args and their descriptions, schemas and default
    # values.
    _customization_arg_specs = [{
        'name': 'choices',
        'description': 'The options that the learner can select from.',
        'schema': {
            'type': 'list',
            'validators': [{
                'id': 'has_length_at_least',
                'min_value': 1,
            }],
            'items': {
                'type': 'html',
                'ui_config': {
                    'size': 'small',
                }
            },
            'ui_config': {
                'add_element_text': 'Add multiple choice option',
            }
        },
        'default_value': ['Default choice'],
    }]

    # Actions that the learner can perform on this interaction which trigger a
    # feedback response, and the associated input types. Each interaction must
    # have at least one of these. This attribute name MUST be prefixed by '_'.
    _handlers = [{
        'name': 'submit', 'obj_type': 'NonnegativeInt'
    }]

    # Additional JS library dependencies that should be loaded in pages
    # containing this interaction. These should correspond to names of files in
    # feconf.DEPENDENCIES_TEMPLATES_DIR.
    _dependency_ids = []
