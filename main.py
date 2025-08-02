import getpass
import os
import sys
import json
import time
from datetime import datetime
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.schema import HumanMessage, AIMessage

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_banner():
    banner = """
    ╔══════════════════════════════════════╗
    ║           CHATTERBOX-CLI             ║
    ║        🔄 Streaming: 🟢 LIGADO       ║
    ║                                      ║
    ║  Comandos básicos:                   ║
    ║  - 'sair' ou 'quit': Sair            ║
    ║  - 'limpar': Limpar histórico        ║
    ║  - 'ajuda': Mostrar ajuda            ║
    ║  - 'historico': Ver histórico        ║
    ║  - 'contar': Contar mensagens        ║
    ║                                      ║
    ║  Comandos especiais:                 ║
    ║  - '/comandos': Ver comandos /       ║
    ║  - '/salvar': Salvar conversa        ║
    ║  - '/carregar': Carregar conversa    ║
    ║  - '/resumir': Resumir conversa      ║
    ║  - '/traduzir': Traduzir texto       ║
    ║  - '/stream': Liga/desliga streaming ║
    ╚══════════════════════════════════════╝
    """
    print(banner)

def show_history(messages):
    """Exibe o histórico de mensagens"""
    if not messages:
        print("📭 Histórico vazio!")
        return
    
    print("\n📜 Histórico da conversa:")
    print("=" * 50)
    for i, msg in enumerate(messages, 1):
        if isinstance(msg, HumanMessage):
            print(f"{i}. 🙋 Você: {msg.content}")
        elif isinstance(msg, AIMessage):
            print(f"{i}. 🤖 AI: {msg.content}")
    print("=" * 50)

def save_conversation(messages, filename=None):
    """Salva a conversa em um arquivo JSON"""
    if not messages:
        print("📭 Nenhuma conversa para salvar!")
        return
    
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"chat_history_{timestamp}.json"
    
    try:
        conversation_data = []
        for msg in messages:
            if isinstance(msg, HumanMessage):
                conversation_data.append({
                    "type": "human",
                    "content": msg.content,
                    "timestamp": datetime.now().isoformat()
                })
            elif isinstance(msg, AIMessage):
                conversation_data.append({
                    "type": "ai",
                    "content": msg.content,
                    "timestamp": datetime.now().isoformat()
                })
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(conversation_data, f, indent=2, ensure_ascii=False)
        
        print(f"💾 Conversa salva em: {filename}")
    except Exception as e:
        print(f"❌ Erro ao salvar conversa: {e}")

def load_conversation(filename):
    """Carrega uma conversa de um arquivo JSON"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            conversation_data = json.load(f)
        
        messages = []
        for item in conversation_data:
            if item["type"] == "human":
                messages.append(HumanMessage(content=item["content"]))
            elif item["type"] == "ai":
                messages.append(AIMessage(content=item["content"]))
        
        print(f"📂 Conversa carregada de: {filename}")
        return messages
    except FileNotFoundError:
        print(f"❌ Arquivo não encontrado: {filename}")
        return []
    except Exception as e:
        print(f"❌ Erro ao carregar conversa: {e}")
        return []

def handle_special_commands(command, messages, model):
    """Processa comandos especiais que começam com /"""
    if command.startswith('/summarize') or command.startswith('/resumir'):
        if not messages:
            print("📭 Nenhuma conversa para resumir!")
            return True
        
        summary_prompt = "Por favor, faça um resumo conciso da nossa conversa até agora."
        temp_messages = messages + [HumanMessage(content=summary_prompt)]
        
        try:
            print("📝 Gerando resumo...", end="", flush=True)
            response = model.invoke(temp_messages)
            print(f"\n📄 Resumo da conversa:\n{response.content}")
        except Exception as e:
            print(f"❌ Erro ao gerar resumo: {e}")
        return True
    
    elif command.startswith('/translate') or command.startswith('/traduzir'):
        parts = command.split(' ', 2)
        if len(parts) < 3:
            print("❌ Uso: /traduzir <idioma> <texto>")
            print("   Exemplo: /traduzir inglês Olá mundo")
            return True
        
        target_language = parts[1]
        text_to_translate = parts[2]
        
        translate_prompt = f"Traduza o seguinte texto para {target_language}: {text_to_translate}"
        
        try:
            print(f"🔄 Traduzindo para {target_language}...", end="", flush=True)
            response = model.invoke([HumanMessage(content=translate_prompt)])
            print(f"\n🌐 Tradução: {response.content}")
        except Exception as e:
            print(f"❌ Erro na tradução: {e}")
        return True
    
    elif command.startswith('/save') or command.startswith('/salvar'):
        parts = command.split(' ', 1)
        filename = parts[1] if len(parts) > 1 else None
        save_conversation(messages, filename)
        return True
    
    elif command.startswith('/load') or command.startswith('/carregar'):
        parts = command.split(' ', 1)
        if len(parts) < 2:
            print("❌ Uso: /carregar <nome_do_arquivo>")
            return True
        
        filename = parts[1]
        loaded_messages = load_conversation(filename)
        if loaded_messages:
            messages.clear()
            messages.extend(loaded_messages)
            print(f"✅ Conversa carregada! {len(loaded_messages)} mensagens.")
        return True
    
    elif command == '/stream':
        # Toggle streaming mode
        return 'toggle_streaming'
    
    elif command == '/commands' or command == '/comandos':
        print("""
🔧 Comandos especiais disponíveis:
  /resumir             - Gera um resumo da conversa
  /traduzir <idioma> <texto> - Traduz texto para o idioma especificado
  /salvar [arquivo]    - Salva a conversa (nome opcional)
  /carregar <arquivo>  - Carrega uma conversa salva
  /stream              - Liga/desliga modo streaming (respostas em tempo real)
  /comandos            - Mostra esta lista de comandos
        """)
        return True
    
    return False

def optimized_stream_response(model, messages, use_streaming=False):
    """Resposta com streaming opcional, baseada no simple_chat que funciona"""
    try:
        if use_streaming:
            print("🔄 Pensando...", end="", flush=True)
            
            try:
                response_stream = model.stream(messages)
                print(" ✅")
                print("🤖 AI: ", end="", flush=True)
                
                full_content = ""
                for chunk in response_stream:
                    if hasattr(chunk, 'content') and chunk.content:
                        print(chunk.content, end="", flush=True)
                        full_content += chunk.content
                        time.sleep(0.01)
                
                print()
                
                if full_content.strip():
                    from langchain.schema import AIMessage
                    return AIMessage(content=full_content.strip())
                else:
                    print("❌ Resposta vazia via streaming")
                    return None
                    
            except Exception as stream_error:
                print(f" ⚠️ Streaming falhou, usando modo normal: {stream_error}")
                use_streaming = False
        
        if not use_streaming:
            print("🔄 Pensando...", end="", flush=True)
            
            response = model.invoke(messages)
            print(" ✅ Resposta recebida!")
            
            if hasattr(response, 'content') and response.content and response.content.strip():
                content = response.content.strip()
                print(f"🤖 AI: {content}")
                return response
            else:
                print("❌ Resposta vazia ou inválida")
                print(f"❌ Response completo: {response}")
                return None
            
    except Exception as e:
        print(f"❌ Erro na chamada: {e}")
        import traceback
        traceback.print_exc()
        return None

def count_messages(messages):
    """Conta mensagens por tipo"""
    human_count = sum(1 for msg in messages if isinstance(msg, HumanMessage))
    ai_count = sum(1 for msg in messages if isinstance(msg, AIMessage))
    return human_count, ai_count

def main():
    load_dotenv()
    
    if not os.environ.get("GOOGLE_API_KEY"):
        os.environ["GOOGLE_API_KEY"] = getpass.getpass("Digite sua chave da API do Google Gemini: ")
    
    try:
        model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
        print("✅ Modelo carregado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao carregar modelo: {e}")
        sys.exit(1)
    
    messages = []
    streaming_enabled = True  # Streaming LIGADO por padrão
    
    clear_screen()
    print_banner()
    
    while True:
        try:
            user_input = input("\n🙋 Você: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'sair']:
                print("👋 Chat encerrado!")
                break
            
            if user_input.startswith('/'):
                result = handle_special_commands(user_input, messages, model)
                if result == 'toggle_streaming':
                    streaming_enabled = not streaming_enabled
                    status = "🟢 LIGADO" if streaming_enabled else "🔴 DESLIGADO"
                    mode = "Respostas em tempo real" if streaming_enabled else "Respostas completas"
                    print(f"🔄 Modo Streaming: {status}")
                    print(f"📝 {mode}")
                continue
            
            if user_input.lower() in ['clear', 'limpar']:
                messages.clear()
                clear_screen()
                print_banner()
                print("🗑️ Histórico limpo!")
                continue
            
            if user_input.lower() in ['help', 'ajuda']:
                print_banner()
                continue
            
            if user_input.lower() in ['history', 'historico', 'histórico']:
                show_history(messages)
                continue
            
            if user_input.lower() in ['count', 'contar']:
                human_count, ai_count = count_messages(messages)
                print(f"📊 Estatísticas: {human_count} suas mensagens, {ai_count} respostas da AI")
                continue
            
            if user_input == "":
                continue
            
            messages.append(HumanMessage(content=user_input))
            
            response = optimized_stream_response(model, messages, streaming_enabled)
            if response and hasattr(response, 'content') and response.content.strip():
                messages.append(response)
            elif response is None:
                print("⚠️ Não foi possível obter resposta do modelo. Tente novamente.")
                if messages and isinstance(messages[-1], HumanMessage):
                    messages.pop()
            else:
                print("⚠️ Resposta vazia recebida. Tente reformular sua pergunta.")
                if messages and isinstance(messages[-1], HumanMessage):
                    messages.pop()
            
        except KeyboardInterrupt:
            print("\n👋 Chat encerrado!")
            break
        except Exception as e:
            print(f"❌ Erro: {e}")

if __name__ == "__main__":
    main()