# import streamlit as st
# import tensorflow_text as tf_text
# import keras_nlp
# from tensorflow import keras

# # Load tokenizer and model
# @st.cache_resource
# def load_model():
#     tokenizer = keras_nlp.models.GPT2Tokenizer.from_preset("gpt2_base_en")
#     base_model = keras.models.load_model("fine_tuned_gpt2_qa.h5", compile=False)

#     gpt2 = keras_nlp.models.GPT2CausalLM(
#         vocabulary_size=base_model.vocabulary_size,
#         num_layers=base_model.num_layers,
#         num_heads=base_model.num_heads,
#         hidden_dim=base_model.hidden_dim,
#         intermediate_dim=base_model.intermediate_dim,
#         max_sequence_length=base_model.max_sequence_length,
#         name="gpt2_custom"
#     )
#     gpt2.set_weights(base_model.get_weights())
#     return tokenizer, gpt2

# tokenizer, gpt2_model = load_model()

# # Streamlit UI
# st.title("🩺 Medical Chatbot (Fine-tuned GPT-2)")
# st.write("Ask me anything related to health!")

# chat_history = st.session_state.get("chat", [])

# user_input = st.text_input("You:", "")

# if user_input:
#     prompt = f"Patient: {user_input}\nDoctor:"
#     response = gpt2_model.generate(prompt, max_length=100)
    
#     chat_history.append(("You", user_input))
#     chat_history.append(("Doctor", response))
#     st.session_state.chat = chat_history

# # Display chat history
# for sender, message in st.session_state.get("chat", []):
#     st.markdown(f"**{sender}:** {message}")

import tensorflow_text as tf_text

try:
    import tensorflow_text as tf_text
    print("tensorflow-text is properly installed.")
except ImportError as e:
    print("tensorflow-text not installed or failed to import:", e)
