import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.schema import HumanMessage

load_dotenv()

def test_direct_model():
    """Teste direto do modelo sem cache, histórico ou complexidades"""
    try:
        print("🔍 Testando modelo diretamente...")
        
        model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
        print("✅ Modelo inicializado com sucesso")
        
        # Teste simples
        message = [HumanMessage(content="Diga apenas 'olá'")]
        print("📤 Enviando mensagem simples...")
        
        response = model.invoke(message)
        
        print(f"✅ Resposta recebida: {response}")
        print(f"✅ Conteúdo: '{response.content}'")
        print(f"✅ Tipo: {type(response)}")
        print(f"✅ Tem conteúdo: {bool(response.content)}")
        print(f"✅ Conteúdo não vazio: {bool(response.content.strip()) if response.content else False}")
        
        # Teste com pergunta mais complexa
        print("\n🔍 Teste com pergunta mais complexa...")
        message2 = [HumanMessage(content="Como você está hoje?")]
        response2 = model.invoke(message2)
        
        print(f"✅ Resposta 2: '{response2.content}'")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        import traceback
        print("📋 Traceback completo:")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🚀 Iniciando teste direto do modelo...")
    success = test_direct_model()
    
    if success:
        print("\n✅ TESTE DIRETO PASSOU! O modelo funciona.")
        print("🔍 O problema está na lógica do ChatterBox-CLI.")
    else:
        print("\n❌ TESTE DIRETO FALHOU! Problema de configuração.")
