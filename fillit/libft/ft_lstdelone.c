/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstdelone.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/11 17:57:35 by etexier           #+#    #+#             */
/*   Updated: 2019/11/18 14:24:22 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"

void	ft_lstdelone(t_list **alst, void (*del)(void *, size_t))
{
	t_list	*ptr;

	if (del != NULL)
	{
		ptr = *alst;
		if (ptr == NULL)
			return ;
		del(ptr->content, ptr->content_size);
		free(ptr);
		*alst = NULL;
	}
}
