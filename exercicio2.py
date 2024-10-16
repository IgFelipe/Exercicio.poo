from botcity.web import WebBot

class MeuBot(WebBot):
    def action(self):
        
        self.go_to("")  

        
        self.fill("input[name='nome']", "Notebook")

       
        self.fill("input[name='preco']", "2500.00")

         
        self.fill("input[name='quantidade']", "10")

        
        self.click("button[type='submit']")

# Executar o bot
if __name__ == "__main__":
    bot = MeuBot()
    bot.start()
