import { useState } from "react";
import axios from "axios";
import toast, {toastConfig} from "react-simple-toasts";
import 'react-simple-toasts/dist/theme/dark.css';

import ChatBox from "./components/chatBox";
import ChatInput from "./components/chatInput";

toastConfig({
  theme: 'dark',
});



export default function App() {
  const [typingStatus, setTypingStatus] = useState<boolean>(true);
  const [q, setQ] = useState<String>("");
  const [chat, setChat] = useState<User[]>([
    {
      role: "fsb-GPT-demo",
      message: "Ahla bik, f chnowa najem n3awnek ?",
    },
  ]);

  async function fetchReply() {
    if (q === '') {
      toast('winou sou2elek ?')
    } else {
      const r = await axios.post("http://localhost:1338/api/chat", { message: q });
      setChat([
        ...chat,
        { role: "Foulen", message: q },
        { role: "fsb-GPT-demo", message: r.data[0] },
      ]);
      setQ("");
    }
  }

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      e.preventDefault();
      fetchReply();
    }
  };

  return (
    <div className="max-w-5xl container mx-auto bg-gray-900 h-screen flex flex-col place-content-end p-4">
      <ChatBox chat={chat} setTypingStatus={setTypingStatus} typingStatus={typingStatus} />
      <ChatInput q={q} setQ={setQ} handleKeyDown={handleKeyDown} fetchReply={fetchReply} typingStatus={typingStatus} />
    </div>
  );
}
