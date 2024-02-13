export default function chatInput({ q, setQ, handleKeyDown, fetchReply, typingStatus }: ChatInputProps) {
  return (
    <div className="w-full flex justify-center gap-x-2 my-3">
      <input
        placeholder="Aya 9oli haja"
        className="placeholder:text-white placeholder:opacity-30 px-4 py-3 w-9/12 outline-none rounded-md border-2 border-[#1F71BA] bg-gray-700 text-white"
        type="text"
        value={q}
        onChange={(e) => setQ(e.target.value)}
        onKeyDown={handleKeyDown}
        disabled={typingStatus}
      />
      <button
        onClick={() => fetchReply()}
        onTouchStart={() => fetchReply()}
        className="w-3/12 sm:w-2/12 bg-[#1F71BA] rounded-md px-2 hover:bg-[#1F71BA] transition duration-300 text-white font-semibold"
        disabled={typingStatus}
      >
        Ab3ath
      </button>
    </div>
  );
}
