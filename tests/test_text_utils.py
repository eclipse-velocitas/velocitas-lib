# Copyright (c) 2024 Contributors to the Eclipse Foundation
#
# This program and the accompanying materials are made available under the
# terms of the Apache License, Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# SPDX-License-Identifier: Apache-2.0

from velocitas_lib.text_utils import (
    replace_item_in_list,
    replace_text_area,
)

test_text_literal = """
class SeatsServiceStub(seats_service_sdk.seats_pb2_grpc.SeatsServicer):
    # <auto-generated>
    '''
    @brief Seats service for getting and controlling the positions of the seats and their
    components in the vehicle.
    This definition corresponds to the COVESA Vehicle Service Catalog (VSC) comfort
    seats service definition (https://github.com/COVESA/vehicle_service_catalog)
    '''

    def Move(self, request, context):
        ''' Set the desired seat position

        Returns gRPC status codes:
        * OK - Seat movement started
        * OUT_OF_RANGE - The addressed seat is not present in this vehicle
        * INVALID_ARGUMENT - At least one of the requested component positions is invalid
        * INTERNAL - A seat service internal error happened - see error message for details
        '''
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

     # </auto-generated>
""".splitlines()

test_text: list[str] = [str(line) for line in test_text_literal]


def test_item_in_list():
    replaced_text = replace_item_in_list(
        test_text,
        "Seats",
        "ReplacedTestString",  # Case sensitive
    )
    matching_count = replaced_text.count("ReplacedTestString")

    assert matching_count == 2
    
    
def test_item_in_list_removes_empty_lines():
    replaced_text = replace_item_in_list(
        test_text,
        "'''",
        remove_empty=True,
    )

    assert len(replaced_text) == 20


def test_item_in_list_keep_empty_lines():
    replaced_text = replace_item_in_list(
        test_text,
        "'''",
    )

    assert len(replaced_text) == 24


def test_replace_text_area():
    replaced_text = replace_text_area(
        test_text,
        "# <auto-generated>",
        "# </auto-generated>",
        "ReplacedTestString",
    )
    matching_count = replaced_text.count("ReplacedTestString")

    assert matching_count == 1


def test_replace_text_area_remove_lines():
    replaced_text = replace_text_area(
        test_text,
        "'''",
        "'''",
    )
    
    assert len(replaced_text) == 10