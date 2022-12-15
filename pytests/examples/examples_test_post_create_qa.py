# Variável para Data Driven Pytest
examples_post_create_qa_invalid_payload = [
    ("payload_vazio", 500),
    ("None", 500),
    ("null", 500),
    ("hash_vazio", 500),
    ("array_vazio", 500),
    ("array_vazio_string", 400),
    ("hash_vazio_string", 400),
    ("payload_number", 400),
    ("payload_boolean_true", 400),
    ("payload_boolean_false", 500),
]

# Variável para Data Driven Pytest
examples_post_create_qa_invalid_headers = [
    ("all", "0", 201),
    ("all", "", 401),
    ("all", "None", 201),
    ("all", "256.characters_type_string", 201),
    ("all", "256.characters_type_numbers", 201),
    ("all", "boolean_true", 201),
    ("all", "boolean_false", 201),
    ("Authorization", "0", 201),
    ("Authorization", "", 401),
    ("Authorization", "None", 201),
    ("Authorization", "256.characters_type_string", 201),
    ("Authorization", "256.characters_type_numbers", 201),
    ("Authorization", "boolean_true", 201),
    ("Authorization", "boolean_false", 201),
    ("Content-Type", "0", 201),
    ("Content-Type", "", 201),
    ("Content-Type", "None", 201),
    ("Content-Type", "256.characters_type_string", 201),
    ("Content-Type", "256.characters_type_numbers", 201),
    ("Content-Type", "boolean_true", 201),
    ("Content-Type", "boolean_false", 201),
    ("Content-Type", "application/javascript", 201),
    ("Content-Type", "application/x-www-form-urlencoded", 201),
]

# Variável para Data Driven Pytest
examples_post_create_qa_no_headers = [
    ("all", 401),
    ("Authorization", 401),
    ("Content-Type", 201),
]

# Variável para Data Driven Pytest
examples_post_create_qa = [
    ("name", "123", 400),
    ("name", "123.to_i", 400),
    ("name", "123.to_f", 400),
    ("name", "None", 400),
    ("name", "Null", 201),
    ("name", "number_negative", 400),
    ("name", "boolean_true", 400),
    ("name", "boolean_false", 400),
    ("name", "256.characters_type_string", 400),
    ("name", "256.characters_type_numbers", 400),
    ("name", "Array", 400),
    ("name", "Hash", 400),
    ("years", "123", 400),
    ("years", "123.to_i", 201),
    ("years", "123.to_f", 201),
    ("years", "None", 400),
    ("years", "Null", 400),
    ("years", "number_negative", 400),
    ("years", "boolean_true", 400),
    ("years", "boolean_false", 400),
    ("years", "256.characters_type_string", 400),
    ("years", "256.characters_type_numbers", 201),
    ("years", "Array", 400),
    ("years", "Hash", 400),
]

# Variável para Data Driven Pytest
examples_post_create_qa_no_fields = [
    ("name", 400),
    ("years", 400),
]