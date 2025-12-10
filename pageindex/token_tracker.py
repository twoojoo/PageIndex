"""
Token usage tracker for monitoring LLM API calls.
Tracks prompt tokens, completion tokens, and total tokens across all API calls.
"""

class TokenTracker:
    """Singleton-style token tracker to accumulate usage across all LLM calls."""
    
    def __init__(self):
        self.total_prompt_tokens = 0
        self.total_completion_tokens = 0
        self.total_tokens = 0
        self.call_count = 0
    def __init__(self):
        self.enabled = False
        self.total_prompt_tokens = 0
        self.total_completion_tokens = 0
        self.total_tokens = 0
        self.call_count = 0
        self.call_history = []
    
    def enable(self):
        """Enable token tracking."""
        self.enabled = True

    def disable(self):
        """Disable token tracking."""
        self.enabled = False
    
    def add_usage(self, prompt_tokens, completion_tokens, call_name="LLM Call"):
        """
        Add token usage from a single LLM call.
        
        Args:
            prompt_tokens: Number of tokens in the prompt
            completion_tokens: Number of tokens in the completion
            call_name: Name/description of the call for logging
        """
        if not self.enabled:
            return
            
        total = prompt_tokens + completion_tokens
        
        self.total_prompt_tokens += prompt_tokens
        self.total_completion_tokens += completion_tokens
        self.total_tokens += total
        self.call_count += 1
        
        # Store call history
        call_info = {
            'call_number': self.call_count,
            'call_name': call_name,
            'prompt_tokens': prompt_tokens,
            'completion_tokens': completion_tokens,
            'total_tokens': total
        }
        self.call_history.append(call_info)
        
        # Print to console
        # Print to console in greppable format
        print(f"TOKEN_USAGE: call_id={self.call_count} name={call_name} prompt={prompt_tokens} completion={completion_tokens} total={total}")
    
    def get_summary(self):
        """
        Get summary of total token usage.
        
        Returns:
            dict: Summary with total counts and call count
        """
        return {
            'total_calls': self.call_count,
            'total_prompt_tokens': self.total_prompt_tokens,
            'total_completion_tokens': self.total_completion_tokens,
            'total_tokens': self.total_tokens,
            'call_history': self.call_history
        }
    
    def print_summary(self):
        """Print a formatted summary of token usage."""
        print(f"TOKEN_SUMMARY: total_calls={self.call_count} prompt={self.total_prompt_tokens} completion={self.total_completion_tokens} total={self.total_tokens}")
    
    def reset(self):
        """Reset all counters to zero."""
        self.total_prompt_tokens = 0
        self.total_completion_tokens = 0
        self.total_tokens = 0
        self.call_count = 0
        self.call_history = []


# Global instance for easy access
_global_tracker = None

def get_global_tracker():
    """Get or create the global token tracker instance."""
    global _global_tracker
    if _global_tracker is None:
        _global_tracker = TokenTracker()
    return _global_tracker

def reset_global_tracker():
    """Reset the global token tracker."""
    global _global_tracker
    _global_tracker = TokenTracker()
