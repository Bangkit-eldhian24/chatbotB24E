def get_response(message):
    message = message.lower()
    
    # Pilihan kata yang dikenali
    if "saya" in message:
        return "ada yg bs di bantu? saya cuman bot sederhana jgn berharap lebih!! T.T"
    elif "aku" in message:
        return "Ada yang mau di sampaikan?"
    elif "sayang" in message:
        return "Oh, baiklah sentuh lah rumput dan bersosialisasi lah :V "
    elif "halo" in message:
        return "Halo! Senang bertemu denganmu, sehat sehat ya :)"
    elif "terima kasih" in message:
        return "Sama-sama! Semoga hari kamu menyenankan!"
    elif "About me" in message:
        return "nama : Ardx (saya adalah pemula wajar pemula saya bukan sepuh eheheh)"
    elif "apakabar" in message:
        return "baik!, bagaimana dgn mu?"
    elif "kata kasar(opsional)" in message:
        return "minimal sopan santun le, aku cmn bot"

    else:
        return "Maaf, saya belum mengerti maksudmu. Coba pilih dari menu!"
