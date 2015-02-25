package romans
class Romans {
    def convert(romanChar:String):Int={
        def addOrSubtract(rest:String, head:Char):Int = 
            if (rest.isEmpty()) 
                changeToken(head)
            else
            {
                val nextVal = changeToken(rest.head)
                val currentVal = changeToken(head)
                if (nextVal > currentVal)
                    nextVal - currentVal + convert(rest.tail)
                else 
                    currentVal + convert(rest)
            }

        def changeToken(c:Char):Int = {
            c match {
                case 'I' => 1
                case 'V' => 5
                case 'X' => 10
                case 'L' => 50
                case 'C' => 100 
                case 'D' => 500 
                case 'M' => 1000 
                case _ => 0

            }
        }
        romanChar match {
            case "" => 0
            case _ => addOrSubtract(romanChar.tail, romanChar.head)

        }

    }

}
