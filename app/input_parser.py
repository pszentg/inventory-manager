import re
import string
from typing import Dict, List

import logging

logger = logging.getLogger(__name__)


class InputParser:
    """
    Input parser class.
    Parses the input file that contains the original state of the inventory and
    the original instructions.
    """

    # Could return boolean, but we don't care about any return values.
    # Just throw an error if the input is invalid.
    def validate_state(input_string: string) -> None:
        # remove whitespaces and newlines from the input to check if the box labels are valid
        input_string_check = input_string.replace(" ", "")
        input_string_check = input_string_check.replace("\n", "")
        input_string_check = re.sub(r"\d+$", "", input_string_check)

        # check if there's only latin letters and the pipe in the segment that represents the boxes
        if re.findall(r"[^a-zA-Z|]", input_string_check):
            raise ValueError(
                "Only letters and the pipe character (|) are allowed to represent the boxes!"
            )

        # check if there's only one character for the box label
        labels = re.findall(r"|\w+|", input_string)
        for label in labels:
            if len(label) > 1:
                raise ValueError(
                    f"Only one character is allowed for the box label. {label} has {len(label)} characters."
                )

        # check if the labers are surrounded by the pipe character
        bounding_boxes = re.findall(r"\||\b[a-zA-Z]?\b|\|", input_string)
        if not bounding_boxes:
            raise ValueError(
                f"Box labels should be surrounded by the pipe ('|') character."
            )

    @staticmethod
    def parse_state(input_string: string) -> Dict:
        InputParser.validate_state(input_string)
        rows = input_string.split("\n")

        # last line is the number of the stacks
        stacks_string = rows[-1]

        stacks = re.findall(r"(\d+)+", stacks_string)
        try:
            max_stack = int(max(stacks))
        except ValueError:
            raise ValueError("Stack numbers cannot be empty!")

        if max_stack > 10:
            raise ValueError("Too many stacks. Maximum 10 stacks are allowed!")

        logger.debug(f"Max stacks: {max_stack}")

        # create a dictionary that stores the stack as a string. Storing it as such will make operations it O(1) complexity.
        # it can be also implemented in a way that it's O(1) with lists, because the stacks can be addressed directly.
        initial_state = {i: "" for i in range(1, max_stack + 1)}

        # The stack is rotated 90 degrees, but this will make managing easier, the last letter is the top box.
        boxes_string_as_list = input_string.split("\n")[0:-1]
        if len(boxes_string_as_list) == 0:
            raise ValueError("Initial state is empty!")

        for line in boxes_string_as_list:
            line = line.lstrip()
            for i in range(0, len(line), 4):
                box = line[i : i + 4]
                box_label = box[1]
                # Assuming that the box label is always at the second character of the 4
                # This has to be modified if in the future we allow multiple letter labels
                stack_number = i // 4 + 1
                try:
                    initial_state[stack_number] += box_label
                except KeyError:
                    logger.error(f"Stack {stack_number} is not valid!")
                    raise

        for stack in initial_state:
            initial_state[stack] = initial_state[stack][::-1].strip()

        return initial_state

    # instructions can be moved around, the numbers will be parsed out using the leading word,
    # so you can use the move x from y to z format or eg. from y move x to z.
    @staticmethod
    def parse_instructions(instructions: string) -> List:
        instructions = instructions.split("\n")
        parsed_instructions = []
        move_pattern = r"move\s*(\d+)"
        from_pattern = r"from\s*(\d+)"
        to_pattern = r"to\s*(\d+)"

        for instruction in instructions:
            try:
                move_ = re.findall(move_pattern, instruction.strip())[0]
                from_ = re.findall(from_pattern, instruction.strip())[0]
                to_ = re.findall(to_pattern, instruction.strip())[0]

                parsed_instructions.append((int(move_), int(from_), int(to_)))
            except IndexError:
                logger.error(f"Invalid instruction: {instruction}")
                raise ValueError(f"Invalid instruction: {instruction}")

        return parsed_instructions
