#!/usr/bin/env python3
"""
Script to check whether inputs match prerequisites (has an even number of word/sentence pairs).
After checking, outputs those pairs with good format.
"""
import sys

def parse_input():
    """Parse input from stdin into front and back elements."""
    front_elements = []
    back_elements = []
    current_front = []
    current_back = []
    is_front = True
    
    while True:
        try:
            line = input()
            if not line.strip():
                if is_front and current_front:
                    front_elements.append("\n".join(current_front))
                    current_front = []
                    is_front = False
                elif not is_front and current_back:
                    back_elements.append("\n".join(current_back))
                    current_back = []
                    is_front = True
            else:
                if is_front:
                    current_front.append(line)
                else:
                    current_back.append(line)
        except EOFError:
            if current_front:
                front_elements.append("\n".join(current_front))
            if current_back:
                back_elements.append("\n".join(current_back))
            break
    
    return front_elements, back_elements


def check_prerequisites(front_elements, back_elements):
    """
    Check if inputs match prerequisites:
    - Must have an even number of total elements (equal front and back pairs)
    
    Returns:
        tuple: (is_valid, message, valid_pairs)
    """
    front_count = len(front_elements)
    back_count = len(back_elements)
    
    # Check if we have matching pairs
    if front_count != back_count:
        return False, f"Mismatch: {front_count} front elements but {back_count} back elements", []
    
    if front_count == 0:
        return False, "No card pairs found in input", []
    
    # Create valid pairs
    valid_pairs = list(zip(front_elements, back_elements))
    
    return True, f"Valid: {len(valid_pairs)} card pair(s) found", valid_pairs


def format_output(valid_pairs):
    """
    Format the valid pairs for output with good formatting.
    
    Args:
        valid_pairs: List of tuples containing (front, back) pairs
    """
    print("\n" + "=" * 60)
    print(f"VALIDATED CARD PAIRS: {len(valid_pairs)} pair(s)")
    print("=" * 60 + "\n")
    
    for i, (front, back) in enumerate(valid_pairs, 1):
        print(f"Card #{i}")
        print("-" * 60)
        print("FRONT:")
        print(front)
        print()
        print("BACK:")
        print(back)
        print("=" * 60 + "\n")


def main():
    """Main function to check inputs and output validated pairs."""
    # Parse input
    front_elements, back_elements = parse_input()
    
    # Check prerequisites
    is_valid, message, valid_pairs = check_prerequisites(front_elements, back_elements)
    
    # Output results
    print("\n" + "=" * 60)
    print("INPUT VALIDATION RESULT")
    print("=" * 60)
    print(f"Status: {'✓ PASSED' if is_valid else '✗ FAILED'}")
    print(f"Message: {message}")
    print("=" * 60)
    
    if is_valid:
        format_output(valid_pairs)
    else:
        print("\nPlease ensure your input has matching front/back pairs.")
        print("Each card should have:")
        print("  - Front content (one or more lines)")
        print("  - Empty line separator")
        print("  - Back content (one or more lines)")
        print("  - Empty line separator (before next card)")
    
    # Return exit code based on validation
    return 0 if is_valid else 1


if __name__ == "__main__":
    sys.exit(main())
