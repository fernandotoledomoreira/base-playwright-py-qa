import random
import string


class Common:

    # Método para geração de payload inválido
    @staticmethod
    def incorrect_payloads(incorrects_payloads):
        match incorrects_payloads:
            case "payload_vazio":
                return ""
            case "None":
                return None
            case "null":
                return "null"
            case "hash_vazio":
                return {}
            case "array_vazio":
                return []
            case "array_vazio_string":
                return "[]"
            case "hash_vazio_string":
                return "{}"
            case "payload_number":
                return 1
            case "payload_boolean_true":
                return True
            case "payload_boolean_false":
                return False


    # Método para gerar valores inválidos
    @staticmethod
    def values_change(value):
        if ".to_i" in value:
            return int(value.split('.')[0])
        elif ".to_f" in value:
            return float(value.split('.')[0])
        elif value == "None":
            return None
        elif value == "number_negative":
            return -1
        elif value == "boolean_true":
            return True
        elif value == "boolean_false":
            return False
        elif ".characters_type_string" in value:
            letters = string.ascii_lowercase
            number = int(value.split('.')[0])
            return ( ''.join(random.choice(letters) for i in range(number)) )
        elif ".characters_type_numbers" in value:
            number = int(value.split('.')[0])
            return int(( ''.join(random.choice("123456789") for i in range(number)) ))
        elif value == "Array":
            return []
        elif value == "Hash":
            return {}
        else:
            return value

    # Método para mudar valor de campo do payload
    @staticmethod
    def change_fields_payload(payload, field, value):
        count =  field.count(".")
        if count == 1:
            fields = field.split(".")
            if type(payload[fields[0]]) == list:
                payload[fields[0]][0][fields[1]] = Common.values_change(value)
            if type(payload[fields[0]]) == dict:
                payload[fields[0]][fields[1]] = Common.values_change(value)
        elif count == 2:
            fields = field.split(".")
            if type(payload[fields[0]]) == list:
                payload[fields[0]][0][fields[1]][fields[2]] = Common.values_change(value)
            if type(payload[fields[0]]) == dict:
                payload[fields[0]][fields[1]][fields[2]] = Common.values_change(value)
        else:
            payload[field] = Common.values_change(value)
        return payload

    # Método para remover campo do payload
    @staticmethod
    def remove_fields_payload(payload, field):
        count =  field.count(".")
        if count == 1:
            fields = field.split(".")
            if type(payload[fields[0]]) == list:
                del payload[fields[0]][0][fields[1]]
            if type(payload[fields[0]]) == dict:
                del payload[fields[0]][fields[1]]
        elif count == 2:
            fields = field.split(".")
            if type(payload[fields[0]]) == list:
                del payload[fields[0]][0][fields[1]][fields[2]]
            if type(payload[fields[0]]) == dict:
                del payload[fields[0]][fields[1]][fields[2]]
        else:
            del payload[field]
        return payload

    # Método para mudar valor de campo do header
    @staticmethod
    def change_headers(token, common_header, header, value):
        match header:
            case "all":
                common_header["Content-Type"] = str(Common.values_change(value))
                common_header["Authorization"] = str(Common.values_change(value))
            case "Content-Type":
                common_header["Content-Type"] = str(Common.values_change(value))
            case "Authorization":
                common_header["Authorization"] = str(Common.values_change(value))
        return common_header

    # Método para remover campo do header
    @staticmethod
    def delete_header(token, common_header, header):
        if header == "all":
            common_header = {}
            return common_header
        else:
            del common_header[header]
            return common_header