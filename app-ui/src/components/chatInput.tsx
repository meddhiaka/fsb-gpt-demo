export default function chatInput({ q, setQ, handleKeyDown, fetchReply }: ChatInputInt) {
  return (
    <div className="w-full flex justify-center gap-x-2 my-3">
      <input
        placeholder="Aya 9oli haja"
        className="placeholder:text-white placeholder:opacity-30 px-4 py-3 w-9/12 outline-none rounded-md border-2 border-red-500 bg-gray-700 text-white"
        type="text"
        value={q}
        onChange={(e) => setQ(e.target.value)}
        onKeyDown={handleKeyDown}
      />
      <button
        onClick={() => fetchReply()}
        className="w-3/12 sm:w-2/12 bg-red-500 rounded-md px-2 hover:bg-red-600 transition duration-300 text-white font-semibold"
      >
        Ab3ath
      </button>
    </div>
  );
}
