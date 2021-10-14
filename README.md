# EASYSCRIPT 0.0.1

## DATA TYPES
    int - Integer
    float - Floating point numbers
    string - String
    arrays - Collection of items

## OPERANDS
    - Subtraction
    + Addition
    / Division
    * Multiplication
    % Modulus
    
## BOOLEAN OPERATIONS
    == Equals
    != Not Equals
    === Logically Equivalent *TODO - think about this more.
    !== Not Logically Equivalent
    < Less Than
    <= Less Than Equal To
    > Greater Than
    >= Greater Than Equal To
    ! Not

## BUILT INS
    if/else if/ else
    while
    for
    switch

## FUNCTION DEFINITION
    def functionName() {
        return x; // optional
    }

    def functionName(int arg1, string arg1, ...) {

    }

## CLASS DEFINITION
    class className() {

    }

    class className() {
        // fields
        className() {

        }
    }


##  CODE STRUCTURE
    function definitions
    class definitions
    main


# Grammar Specification
    file          : statements
    statements    : statement statements
    statement     : c_stmt | s_stmt | e_stmt
    c_stmt        : function_def | klass_def | main_def
    s_stmt        : assignment | return