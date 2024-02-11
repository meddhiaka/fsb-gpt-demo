import { useState } from "react";
import axios from "axios";

export default function App() {
  const [q, setQ] = useState('');

  async function fetchReply() {
    const r = await axios.post('http://localhost:1337/api/chat', { message: q });
    console.log(r.data[0]);
    setQ('');
  }

  const handleKeyDown = (e: { key: string; preventDefault: () => void; }) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      fetchReply();
    }
  };

  return (
    <div className="max-w-5xl container mx-auto bg-black h-screen flex flex-col place-content-end">
      <div className="w-full flex justify-center gap-x-2 my-3">
        <input
          placeholder="Ask me anything"
          className="placeholder:text-gray-600 px-2 py-3 w-9/12 outline-none rounded-sm border-red-500 border-[1px] bg-gray-500"
          type="text"
          name=""
          id=""
          value={q}
          onChange={(e) => setQ(e.target.value)}
          onKeyDown={handleKeyDown}
        />
        <button
          onClick={() => fetchReply()}
          className="w-2/10 bg-white border-[1px] border-red-500 rounded-md px-4 py-2"
        >
          Submit
        </button>
      </div>
    </div>
  );
}
