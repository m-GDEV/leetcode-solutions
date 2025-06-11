/*
 * @lc app=leetcode id=232 lang=csharp
 *
 * [232] Implement Queue using Stacks
 */

// @lc code=start
public class MyQueue
{
    Stack<int> queue = new Stack<int>();
    Stack<int> temp_stack = new Stack<int>();

    public MyQueue()
    {
    }

    public void Push(int x)
    {
        temp_stack = new Stack<int>();
        // temp_stack.Push(x);

        // reverse stack order
        while (queue.Count != 0)
        {
            temp_stack.Push(queue.Pop());
        }

        queue = new Stack<int>();

        queue.Push(x);
        while (temp_stack.Count != 0)
        {
            queue.Push(temp_stack.Pop());
        }
    }

    public int Pop()
    {
        return queue.Pop();
    }

    public int Peek()
    {
        int val = queue.Pop();
        queue.Push(val);
        return val;
    }

    public bool Empty()
    {
        if (queue.Count == 0)
        {
            return true;
        }
        return false;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.Push(x);
 * int param_2 = obj.Pop();
 * int param_3 = obj.Peek();
 * bool param_4 = obj.Empty();
 */
// @lc code=end

