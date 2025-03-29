      N = len(postorder)
      post_val_to_idx = {} # val -> idx
      
      for i, n in enumerate(postorder):
        post_val_to_idx[n] = i
        
      def build(i1, i2, j1):
        if i1 > i2:
          return None

        root = TreeNode(preorder[i1])
        
        if i1 != i2:
          left_val = preorder[i1 +1]
          
          mid = post_val_to_idx[left_val] 
        
          left_size = mid -j1 +1
          
          root.left = build(i1 +1, i1 +left_size, j1)
          root.right = build(i1 +left_size +1, i2, mid +1)
        return root
        
      return build(0, N-1, 0)