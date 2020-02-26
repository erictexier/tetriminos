/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memalloc.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/07 18:33:26 by etexier           #+#    #+#             */
/*   Updated: 2019/11/12 11:45:23 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"

void	*ft_memalloc(size_t size)
{
	void	*m;

	if (size == 0)
		return (NULL);
	m = (void *)malloc(size);
	if (m == 0)
		return (NULL);
	return (ft_bzero(m, size));
}
