interface User {
    role: string;
    message: string;
}

interface ChatInputInt {
    q: string;
    setQ: React.Dispatch<React.SetStateAction<string>>;
    handleKeyDown: (e: any) => void;
    fetchReply(): Promise<void>;
}

