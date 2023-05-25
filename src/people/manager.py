from project01.models import Persona
from project01.serializer import AdminPersonasSerializer

class AdminPersonasManager():
    @staticmethod
    def get_all():
        personas = Persona.objects.all() # select * from Persona
        serializer = AdminPersonasSerializer(personas, many = True)
        return serializer.data

    @staticmethod
    def save_persona(serializer):
        try:
            persona = serializer.save()
        except Exception as error:
            raise

    @staticmethod
    def get_persona_by_id(pk):
        try:
            persona = Persona.objects.get(pk = pk)
            serializer = AdminPersonasSerializer(persona, many = False)
            return serializer.data

        except Exception as error:
            raise

    @staticmethod
    def update_persona(data, pk):
        try:
            persona_old = Persona.objects.get(pk = pk)
            serializer = AdminPersonasSerializer(persona_old, data = data)
            if serializer.is_valid(raise_exception = True):
                serializer.save()

        except Exception as error:
            raise

    @staticmethod
    def delete_persona(pk):
        try:
            persona = Persona.objects.get(pk = pk)
            persona.delete()

        except Exception as error:
            raise