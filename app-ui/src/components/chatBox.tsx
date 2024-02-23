import { TypeAnimation } from "react-type-animation";

export default function chatBox({ chat, setTypingStatus }: ChatBoxProps) {
  return (
    <div className="flex-1 m-2 overflow-auto rounded-md p-2 bg-custom space-y-2">
      {chat.map((e, index) => (
        <div
          key={index}
          className={`max-w-4xl mx-auto border-[1px] py-3 my-1 px-2 rounded-md backdrop bg-white bg-opacity-10 text-white shadow-lg ${e.role === "fsb-GPT-demo" ? "border-[#1F71BA]" : "border-white"
            }`}
        >
          {index % 2 === 1 ? (
            <>
              <p className="font-extrabold  text-lg py-1">{e.role}</p>
              <p className="text-white">{e.message}</p>
            </>
          ) :
            (
              <>
                <p className=" font-extrabold text-[#91c5f3] text-lg py-1"><span className=" shadow-lg shadow-gray-500 text-xl mr-1">🤖</span>{e.role}</p>
                <TypeAnimation
                  className={`text-white`}
                  sequence={[200, () => { setTypingStatus(true) }, 3000, e.message, () => { setTypingStatus(false) }]}
                  cursor={false}
                  repeat={0}
                />
              </>
            )}
        </div>
      ))}
        {chat.length === 1 &&  (
          <div className="text-center pt-44  md:pt-44">
            <TypeAnimation
              className="text-white text-shadow text-3xl md:text-5xl font-black "
              sequence={[
                '#free_palestine 🇵🇸',
                1000,
                '#free_palestine 🇵🇸 🇹🇳 🇲🇷',
                3000,
                '#free_palestine 🇵🇸 ',
                100,
              ]}
              speed={10}
              repeat={Infinity}
            />
          </div>
        )}

    </div>
  );
}


