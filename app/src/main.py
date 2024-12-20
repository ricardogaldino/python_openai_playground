from openai import OpenAI


class Main:
    def __init__(self):
        self.client = OpenAI(api_key="**********")

    def run(self):
        try:
            request = "Quem nasceu primeiro o ovo ou a galinha?"
            print(f"Pergunta: {request}")

            print("aguarde um momento...")
            completion = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "user",
                        "content": f"{request}"
                    }
                ]
            )

            response = completion.choices[0].message.content
            print(f"Resposta: {response}")

        except Exception as ex:
            print(f"Ocorreu um erro: {ex}")

        finally:
            print("Operação concluída.")


if __name__ == "__main__":
    Main().run()
