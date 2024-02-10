import { TypeAnimation } from "react-type-animation"

export default function App() {
  return (
    <div>
      <TypeAnimation
  sequence={[
    'One',
    700,
    'One Two',
    700,
    'One Two Three',
    700,
    'One Two Three four',
    700,
    'One Two Three four five',
    700,
    'One Two Three four five six',
    700
  ]}
  repeat={0}
/>
    </div>
  )
}