post_create_qa_schema = {
    "type": "object",
    "properties": {
        "uuid": {
            "type": "string"
        },
        "createDate": {
            "type": "string"
        },
        "name": {
            "type": "string"
        },
        "years": {
            "type": "integer"
        }
    },
    "required": [
        "uuid",
        "createDate",
        "name",
        "years"
    ]
}