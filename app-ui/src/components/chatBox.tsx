import { TypeAnimation } from "react-type-animation";

export default function chatBox({ chat, setTypingStatus}) {
  return (
    <div className="flex-1 m-2 rounded-md p-2 bg-custom">
      {chat.map((e, index) => (
        <div
          key={index}
          className={`max-w-4xl mx-auto border-[1px] py-3 my-1 px-2 rounded-md ${e.role === "fsb-GPT-demo" ? "bg-red-500 text-white" : "bg-gray-300 text-gray-800"
            }`}
        >
          <p className="font-extrabold">{e.role}</p>
          {index % 2 === 1 ? (
            <p className="text-black">{e.message}</p>
          ) :
            (
              <TypeAnimation
                className={`text-black`}
                sequence={[200, () => {setTypingStatus(true)}, 3000, e.message, ()=> {setTypingStatus(false)}]}
                cursor={false}
                repeat={0}
              />
            )}
        </div>
      ))}
    </div>
  );
}


