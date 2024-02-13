interface User {
    role: string;
    message: string;
}

interface ChatInputProps {
    q: string;
    setQ: React.Dispatch<React.SetStateAction<string>>;
    handleKeyDown: (e: React.KeyboardEvent<HTMLInputElement>) => void;
    fetchReply: () => void;
    typingStatus: boolean;
}



interface ChatBoxProps {
    chat: User[];
    setTypingStatus: React.Dispatch<React.SetStateAction<boolean>>;
    typingStatus: boolean;
}